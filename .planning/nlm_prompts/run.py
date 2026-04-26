"""NotebookLM single-question runner.

대표님 지시 (2026-04-24): "질문할때는 먼저 질문문을 모두 만들어놓고 붙혀넣기로 질문해라"
→ 프롬프트는 별도 .txt 파일에 미리 작성 → 이 runner 가 읽어서 argv 로 전달
→ scripts/notebooklm/query.py 의 D-6 single-string 규율 준수

사용법:
    python .planning/nlm_prompts/run.py <prompt.txt> <response.md> [timeout_s]

timeout 기본 1200s (20분 · 대표님 "시간 빡빡하게 잡지마라")
"""
from __future__ import annotations

import os
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.notebooklm.query import query_notebook

# 환경변수 NLM_NOTEBOOK_ID 로 override 가능 (다른 노트북에 임시 질문 시).
# Default = 2026-04-24 소설 전용 노트북 (라노벨·다크판타지 기술 + kanno321-create/naberal_game 레포)
NOTEBOOK_ID = os.environ.get("NLM_NOTEBOOK_ID", "672ad9c5-ec56-45a2-a5f7-17c5fa023b5c")


def to_single_line(text: str) -> str:
    """NotebookLM UI 의 Enter 자동 전송 문제 방지.

    대표님 지적 (2026-04-24): 프롬프트 내 줄바꿈이 NotebookLM 채팅창에서
    엔터키로 해석돼 각 단락이 별개 메시지로 전송됨 → 쿼리 낭비 + Canon 오염.

    해결: 모든 줄바꿈을 단일 공백으로, 연속 공백·탭을 하나로 통합.
    한국어 문장 구조(마침표·【】·섹션 번호) 는 그대로 보존되므로 NotebookLM
    이 구조를 파악하는 데 지장 없음.
    """
    single = text.replace("\r\n", " ").replace("\n", " ").replace("\r", " ")
    single = re.sub(r"[ \t]+", " ", single).strip()
    return single

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except (AttributeError, OSError):
    pass

if len(sys.argv) < 3:
    print("Usage: run.py <prompt.txt> <response.md> [timeout_s]", file=sys.stderr)
    sys.exit(2)

prompt_path = Path(sys.argv[1])
response_path = Path(sys.argv[2])
timeout_s = int(sys.argv[3]) if len(sys.argv) > 3 else 1200

raw = prompt_path.read_text(encoding="utf-8").strip()
question = to_single_line(raw)

# .sent.txt 로 실제 전송 내용 박제 (대표님 검수 가능)
sent_path = prompt_path.with_suffix(".sent.txt")
sent_path.write_text(question, encoding="utf-8")

print(f"prompt raw: {prompt_path.name} ({len(raw)} chars, {raw.count(chr(10))} newlines)")
print(f"prompt sent: {sent_path.name} ({len(question)} chars, single-line)")
print(f"timeout: {timeout_s}s")
print(f"notebook: {NOTEBOOK_ID}")
print("querying NotebookLM... (browser startup ~30s, answer generation varies)")

t0 = time.time()
try:
    answer = query_notebook(
        question=question,
        notebook_id=NOTEBOOK_ID,
        timeout_s=timeout_s,
    )
except Exception as e:
    print(f"FAILED after {time.time() - t0:.1f}s: {e}", file=sys.stderr)
    sys.exit(1)

dt = time.time() - t0
print(f"DONE in {dt:.1f}s · answer: {len(answer)} chars")

response_path.parent.mkdir(parents=True, exist_ok=True)
response_path.write_text(
    f"---\n"
    f"prompt_file: {prompt_path.name}\n"
    f"notebook_id: {NOTEBOOK_ID}\n"
    f"question_chars: {len(question)}\n"
    f"answer_chars: {len(answer)}\n"
    f"duration_s: {dt:.1f}\n"
    f"date: 2026-04-24\n"
    f"---\n\n"
    f"# NotebookLM 응답 — {prompt_path.stem}\n\n"
    f"{answer}\n",
    encoding="utf-8",
)
print(f"saved: {response_path}")
