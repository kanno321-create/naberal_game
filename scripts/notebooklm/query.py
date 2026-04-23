"""NotebookLM subprocess wrapper per D-6 + D-7.

Contract
--------
- **D-6 (single-string query discipline)**: ``question`` MUST be a pre-composed
  single string. No newlines, no echo-to-stdin, no multi-question concatenation.
  The question flows through argv as a single list item — the Phase 6 CONTEXT
  D-6 anchor for the ``feedback_notebooklm_query.md`` memory rule.
- **D-7 (external skill reference, not copy)**: Call the external
  ``secondjob_naberal/.claude/skills/notebooklm`` skill via ``subprocess.run``.
  Never import its modules, never duplicate its Playwright venv, never copy
  browser_state. Path is resolved via (kwarg → env var → hardcoded fallback).
  Path anchor updated 2026-04-20 (session #24): migrated from the legacy
  ``shorts_naberal`` install to the active ``secondjob_naberal`` registry
  which holds the ``script-production-deep-research`` (대본제작용) notebook
  — the Phase 10 SCRIPT-gate RAG primary.

Encoding
--------
Per Phase 5 STATE decision #28, ``subprocess.run`` is invoked with
``encoding='utf-8'`` to survive the Windows cp949 default codec. Korean answers
and em-dashes in stderr would otherwise raise UnicodeDecodeError mid-pipeline.

Error propagation
-----------------
- Non-zero returncode -> ``RuntimeError`` carrying stderr (no silent swallow
  per Project Rule 3 — CLAUDE.md forbids silent fallback).
- Missing skill directory -> ``FileNotFoundError``.
- Subprocess hang beyond ``timeout_s + 30`` -> ``subprocess.TimeoutExpired``
  surfaces naturally.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

# D-7 skill path resolution — updated 2026-04-22 (집 PC 마스터 전략).
# Active registry: ``secondjob_naberal`` (5 notebooks, includes the 대본제작용
# / ``script-production-deep-research`` required for SCRIPT gate). Legacy
# ``shorts_naberal`` 은 3 notebooks 만 있어 migrated.
#
# Resolution order (`_resolve_skill_path` 참조):
#   1) kwarg `skill_path=`   — 테스트·CI 직접 주입
#   2) env ``NOTEBOOKLM_SKILL_PATH`` — 회사 PC 등 다른 환경용 명시 override
#   3) auto-detect           — parents[5] (Desktop 등) 형제 폴더 탐색
#   4) hardcoded fallback    — 집 PC 표준 경로 (최후안)
HARDCODED_FALLBACK = Path(r"C:/Users/PC/Desktop/secondjob_naberal/.claude/skills/notebooklm")
DEFAULT_SKILL_PATH = HARDCODED_FALLBACK  # backward-compat alias for older callers

# FOLLOW_UP_REMINDER marker emitted at the tail of every ``ask_question.py``
# answer. Wrapper strips it so downstream consumers see clean answer text.
# Literal per RESEARCH Area 3 line 595.
FOLLOW_UP_MARKER = "EXTREMELY IMPORTANT: Is that ALL you need"


def _auto_detect_skill_path() -> Path | None:
    """Try to locate ``secondjob_naberal`` as a sibling of ``naberal_group/``.

    parents layout (from this file ``scripts/notebooklm/query.py``):
        [0] notebooklm  [1] scripts  [2] game  [3] studios
        [4] naberal_group  [5] Desktop (or equivalent)

    Returns the skill path if the sibling ``secondjob_naberal`` tree exists,
    else ``None``. Uses ``Path.resolve()`` so OS display names (e.g. Korean
    ``바탕 화면``) do not matter — the real filesystem path is used.
    """
    try:
        desktop = Path(__file__).resolve().parents[5]
    except IndexError:
        return None
    candidate = desktop / "secondjob_naberal" / ".claude" / "skills" / "notebooklm"
    return candidate if candidate.exists() else None


def _resolve_skill_path(skill_path: Path | None) -> Path:
    """Resolve the skill path per D-7 precedence.

    Order: kwarg > env var > auto-detect > hardcoded fallback.
    Never silently falls through — if all four fail the caller will hit the
    ``FileNotFoundError`` in ``query_notebook`` per CLAUDE.md no-silent rule.
    """
    if skill_path is not None:
        return skill_path
    env = os.environ.get("NOTEBOOKLM_SKILL_PATH")
    if env:
        return Path(env)
    auto = _auto_detect_skill_path()
    if auto is not None:
        return auto
    return HARDCODED_FALLBACK


def _strip_follow_up(answer: str) -> str:
    """Remove the FOLLOW_UP_REMINDER marker and everything after it."""
    if FOLLOW_UP_MARKER in answer:
        return answer.split(FOLLOW_UP_MARKER)[0].rstrip()
    return answer


def query_notebook(
    question: str,
    notebook_id: str,
    timeout_s: int = 600,
    skill_path: Path | None = None,
) -> str:
    """Call the external NotebookLM skill's ``ask_question.py`` and return answer.

    Args:
        question: Pre-composed single string per D-6. No newlines, no
            multi-question bundling. Passed as a single argv item — Korean
            content survives because argv boundaries are not shell-parsed.
        notebook_id: Explicit notebook id per D-4 (no fallback to the skill's
            ``active_notebook_id``). Caller decides general vs channel-bible.
        timeout_s: Answer generation timeout in seconds. Subprocess timeout
            is ``timeout_s + 30`` to allow Playwright browser teardown.
        skill_path: Optional override. When ``None`` the resolver consults
            ``NOTEBOOKLM_SKILL_PATH`` env var, then falls back to
            ``DEFAULT_SKILL_PATH``.

    Returns:
        Answer text with the FOLLOW_UP_REMINDER marker and everything after
        it stripped. Trailing whitespace normalized.

    Raises:
        FileNotFoundError: Resolved skill directory does not exist.
        RuntimeError: Subprocess returned non-zero (auth expired, notebook
            missing, Playwright crash). Message carries stderr.
        subprocess.TimeoutExpired: Exceeded ``timeout_s + 30`` seconds.
    """
    sp = _resolve_skill_path(skill_path)
    if not sp.exists():
        raise FileNotFoundError(f"NotebookLM skill not found at {sp}")

    run_py = sp / "scripts" / "run.py"
    # ask_question.py 지원 인자: --question, --notebook-url, --notebook-id, --show-browser
    # library.json 은 Windows cp949 에서 한국어 로딩 실패 → --notebook-url 로 lookup 우회.
    # notebook_id 가 "xxxxxxxx-xxxx-..." UUID 형태면 full URL 로 변환하여 --notebook-url 사용.
    if "-" in notebook_id and len(notebook_id) >= 32 and "/" not in notebook_id:
        notebook_url = f"https://notebooklm.google.com/notebook/{notebook_id}"
        id_arg = ["--notebook-url", notebook_url]
    else:
        id_arg = ["--notebook-id", notebook_id]
    cmd = [
        sys.executable,
        "-X", "utf8",  # Windows cp949 → UTF-8 강제 (library.json 한국어 로딩 호환)
        str(run_py),
        "ask_question.py",
        "--question", question,
        *id_arg,
    ]
    # 환경변수로 UTF-8 고정 (subprocess 내부 open(file) 기본 codec 통제)
    env = {**os.environ, "PYTHONUTF8": "1", "PYTHONIOENCODING": "utf-8"}
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout_s + 30,
        env=env,
    )
    if result.returncode != 0:
        # 2026-04-24: stdout 도 오류 메시지에 포함 (ask_question.py 가 사용자용 메시지를
        # stdout 으로 print 하므로 stderr 만으로는 디버깅 불가).
        raise RuntimeError(
            f"NotebookLM query failed (rc={result.returncode}) "
            f"notebook_id={notebook_id}\n"
            f"--- STDOUT ---\n{result.stdout}\n"
            f"--- STDERR ---\n{result.stderr}"
        )
    return _strip_follow_up(result.stdout)
