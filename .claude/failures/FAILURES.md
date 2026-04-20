# FAILURES — naberal_game

> **Append-only log**. 과거 실수·교훈·재발 방지 자산.
> `.claude/hooks/pre_tool_use.py` 의 `check_failures_append_only` 가 이 파일의 기존 content prefix 를
> 보존하지 않는 Write 를 거부한다. 엔트리는 시간순으로만 추가.

## 엔트리 규약

```
## FAIL-NNN — <짧은 제목> (YYYY-MM-DD, 세션 #N, Phase X)

**증상**: 관찰된 문제.
**원인**: 근본 원인 (증상이 아니라).
**교훈**: 재발 방지를 위한 구체적 규칙 (CLAUDE.md 금기사항·필수사항으로 승격 대상).
**참고**: 관련 커밋·문서·대화 링크.
```

## Sources

- 이 파일: Phase 0+ 축적 실패 저수지 (30일 패턴 집약 → SKILL.md.candidate)
- `FAILURES_INDEX.md`: 카테고리 태깅 (수정 가능, 이 파일만 append-only)

---

*Created: 2026-04-20 (Phase 0 Bootstrap — naberal_game studio 창업)*
*First entry: FAIL-001 (2026-04-21, 세션 #1 Part B)*

---

## FAIL-001 — NotebookLM skill 호환 패치 (3회 실패 후 복구, 2026-04-21, 세션 #1, Phase 0)

**증상**:
외부 `secondjob_naberal/.claude/skills/notebooklm` skill 을 shorts 의 `query.py` 로 호출 시 3회 연속 `rc=1` 실패. 첫 실패는 argparse 에러 메시지 명확 (`unrecognized arguments: --timeout 420`), 후속 실패는 stderr 비어있어 원인 불명. 직접 `run.py ask_question.py` 호출 시 `⚠️ Error loading library: 'cp949' codec can't decode byte 0xec` + `❌ Notebook 'a0bb9e88-...' not found` 동시 출력.

**원인**:
1. **skill 버전 차이** — shorts 의 `query.py` 가 전달하는 `--timeout` 인자를 secondjob_naberal 의 `ask_question.py` 는 지원하지 않음 (skill 자체가 Python `subprocess.run(timeout=...)` 로 관리).
2. **Windows cp949 기본 codec** — `library.json` 에 한국어 노트북 설명 포함되어 있는데 Python subprocess 가 cp949 로 read → UnicodeDecodeError. `PYTHONUTF8=1` 또는 `-X utf8` 플래그 없이는 실패.
3. **notebook_id lookup 의존성** — shorts query.py 가 `--notebook-id` 를 넘기면 skill 이 `library.json` 에서 ID → URL 매핑. 대표님이 새로 주신 노트북 ID `a0bb9e88-...` 는 library 에 등록 안 됨 → lookup 실패.
4. **Playwright 간헐적 rc=1** (2차 원인): Q4 1회 rc=1 + stderr 비어있음. 브라우저 세션 instability 추정, 재실행 시 즉시 복구됨. 원인 미상.

**교훈**:
- 외부 skill 호출 전 해당 skill 의 `argparse` 구조를 **소스 코드로 직접 확인** (내 가정은 자산의 현재 상태가 아닐 수 있다).
- Windows 환경에서 한국어 JSON 로딩 시 **반드시 `PYTHONUTF8=1` + `PYTHONIOENCODING=utf-8` + `-X utf8`** 세트로 subprocess 실행. env dict 에 명시.
- notebook ID 보다 **full URL 직접 전달** 이 더 robust (library lookup 완전 우회). UUID 형태 (`len >= 32, "-" in id, "/" not in id`) 감지되면 자동으로 URL 로 변환하는 adapter 로직 유지.
- Playwright 세션 간헐적 실패는 run 별 브라우저 독립 인스턴스로 복구됨. 3회 연속 실패 아니면 단순 재실행이 가장 경제적 대응.
- 이식한 외부 도구는 **한 번 성공시 내부 경로 고정 + 환경 차이 방어 주석** 작성 (query.py L103-105 주석 처리 완료).

**참고**:
- Commit: `70a4bf1 feat(research): NotebookLM deep research 6-query`
- 수정 파일: `scripts/notebooklm/query.py` L103-125 (UTF-8 env + URL 변환 로직)
- 실패 로그: `b4bwkouy3.output`, `b50c0e7gp.output`, `bpjezvezu.output` (임시 background task outputs)
- secondjob_naberal skill: `C:/Users/PC/Desktop/secondjob_naberal/.claude/skills/notebooklm/scripts/ask_question.py`
