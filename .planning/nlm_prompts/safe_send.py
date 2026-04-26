"""Safe NotebookLM sender with duplicate response detection + auto retry.

세션 #14 race condition 우회 (2026-04-26):
- ask_question.py polling 이 *직전 답변을 stable 로 인식* 하는 race
- 새 답변 element 가 추가되기 전에 7초만에 *이전 답변* 을 stable 로 잡음
- 결과: 매 호출 후 *직전 답변 그대로 반환* 되는 복제 응답

해결:
- 응답 받은 후 직전 응답들과 hash 비교
- 복제면 자동 재시도 (최대 4회 · 매번 90초 대기)
- 환경변수 NLM_NOTEBOOK_ID 로 노트북 ID 지정

사용법:
    NLM_NOTEBOOK_ID=<uuid> python safe_send.py <prompt.txt> <response.md> [timeout_s]
"""
from __future__ import annotations
import hashlib
import os
import subprocess
import sys
import time
from pathlib import Path

if len(sys.argv) < 3:
    print("Usage: safe_send.py <prompt.txt> <response.md> [timeout_s]", file=sys.stderr)
    sys.exit(2)

prompt_path = Path(sys.argv[1]).resolve()
response_path = Path(sys.argv[2]).resolve()
timeout_s = int(sys.argv[3]) if len(sys.argv) > 3 else 2400

responses_dir = response_path.parent
RUN_PY = prompt_path.parent / "run.py"
SEPARATOR = "=" * 60
MAX_RETRIES = 5
WAIT_BETWEEN = 150  # seconds between retries (대표님 2026-04-26: "시간 넉넉히 줘라")


def extract_answer(body: str) -> str:
    """프롬프트와 답변 사이의 ===... 구분선 이후 본문만 추출."""
    if SEPARATOR in body:
        parts = body.split(SEPARATOR)
        if len(parts) >= 3:
            return parts[-1].strip()
    return body.strip()


def collect_prev_hashes() -> set[str]:
    """현재 response_path 제외한 모든 이전 응답의 답변 hash 수집."""
    hashes = set()
    for f in responses_dir.glob("*.md"):
        if f.resolve() == response_path:
            continue
        try:
            body = f.read_text(encoding="utf-8")
            ans = extract_answer(body)
            if ans and len(ans) > 100:  # 의미 있는 길이만
                hashes.add(hashlib.sha256(ans.encode()).hexdigest())
        except Exception:
            pass
    return hashes


for attempt in range(1, MAX_RETRIES + 1):
    print(f"\n=== ATTEMPT {attempt}/{MAX_RETRIES} ===", flush=True)
    if response_path.exists():
        response_path.unlink()

    prev_hashes = collect_prev_hashes()
    print(f"  cached {len(prev_hashes)} prev response hashes", flush=True)

    cmd = [sys.executable, str(RUN_PY), str(prompt_path), str(response_path), str(timeout_s)]
    result = subprocess.run(cmd, env=os.environ.copy())

    if result.returncode != 0:
        print(f"  run.py failed (rc={result.returncode})", flush=True)
        sys.exit(result.returncode)

    if not response_path.exists():
        print(f"  response file not created", flush=True)
        sys.exit(1)

    body = response_path.read_text(encoding="utf-8")
    ans = extract_answer(body)
    h = hashlib.sha256(ans.encode()).hexdigest()

    if h not in prev_hashes:
        print(f"  OK UNIQUE answer (attempt {attempt}, {len(ans)} chars)", flush=True)
        sys.exit(0)

    print(f"  FAIL DUPLICATE detected (attempt {attempt})", flush=True)
    if attempt < MAX_RETRIES:
        print(f"  waiting {WAIT_BETWEEN}s before retry...", flush=True)
        time.sleep(WAIT_BETWEEN)

print(f"FAILED after {MAX_RETRIES} attempts — duplicate response persists", file=sys.stderr)
sys.exit(1)
