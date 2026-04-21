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

---

## FAIL-002 — AI 과해석 10건 집단 발생 (빈 자리 채우기 경향, 2026-04-21, 세션 #2, Phase 0)

**증상**:
이전 세션 commit `fdf41b1` 에서 박제한 세계관·서사 설정 중 대표님 원안과 어긋난 **10건 과해석** 발견. 진엔딩 Scene 2 동료 참살 상세 연출 / 히든 엔딩 복합 트리거 / 엔딩 E 인간 신 정의 / 7대 신 = 세계관 논리 골격 / "신이 번식 본능 심음" / 우주 포식자 = Act 3 본전투 / Phase 1 동료 = 인간 4 + 타종족 4 / 첫 번째 신 = 행성 최초 존재 / "성간 혼천의" 서사 (NotebookLM drift) / "뒤틀림" 공간 왜곡 뉘앙스. 각 건이 대표님 원안과 구체적 충돌.

**원인**:
1. **AI 의 빈 자리 채우기 경향** — 대표님 원안이 짧거나 기술적 설정일 때 나베랄 감마·NotebookLM 둘 다 그 빈 자리를 "철학적 깊이 · 멋진 서사적 정당화 · 논리적 완결성" 으로 채우려는 체계적 경향. 5건 발생 후에도 동일 패턴 반복 후 10건 누적.
2. **원전·박제 분리 부재** — 대표님 원안 인용이 어디에도 박제되지 않아 에이전트가 기존 박제물만 읽고 재해석 반복. 과해석 위에 추가 과해석 누적.
3. **과해석이 표면적으로 매력적** — 원안보다 박제본이 더 정교·풍부해서 대표님도 긴 시간 읽어야 drift 발견 가능.

**교훈**:
- **CLAUDE.md 금기 §10 신규 후보**: "대표님 원문 인용 없이 세계관 핵심 설정 추가 금지. 원안 분량의 3배 이상 박제하려 할 때는 질문 먼저, 박제 나중."
- **빈 자리는 `[대표님 결정 대기]` 마커 유지**. AI 가 "합리적 추론" 으로 채우지 말 것. 이는 오늘 박제한 `feedback_over_interpretation_guard.md` (auto memory, 대표님 승인 대기) 와 같은 원칙.
- **설계 원전 문서 의무화**: `brainstorm_YYYY-MM-DD.md` 에 대표님 원문 인용을 **변경 불가 앵커** 로 박제. 향후 에이전트는 이 원전 기준으로 drift 검출. 이번 세션 `brainstorm_2026-04-21.md` 가 그 첫 적용.
- **AI 제안 설정 추적**: 나베랄 감마든 NotebookLM 이든, AI 가 생성한 "고유 설정" 은 대표님 승인 전엔 가설 취급.

**참고**:
- 원전: `wiki/design/brainstorm_2026-04-21.md` 제1부 (과해석 정정 10건 + 대표님 원문 인용 22건)
- 종합 스냅샷: `wiki/design/game_setting_complete_2026-04-21.md` §0 "NotebookLM 에게 알림" (같은 10건)
- NotebookLM drift 원본: `wiki/design/notebooklm_1.txt`
- auto memory 대기: `feedback_over_interpretation_guard.md` (대표님 승인 필요)

---

## FAIL-003 — Bash cd 로 작업 디렉토리 이동, Hook 경로 깨짐 (2026-04-21, 세션 #2, Phase 0)

**증상**:
Claude skill 설치 중 `cd ~/.claude && for s in ...; do cp -r ... ; done` 명령 실행. 직후 PostToolUse Hook (`post_tool_use.py`) 이 `C:\Users\PC\.claude\.claude\hooks\post_tool_use.py` 경로로 파일 열려 시도 — **이중 `.claude\.claude\`** 경로로 파일 미존재 에러. 복사 자체는 성공했으나 Hook 후속 처리 실패.

**원인**:
1. Hook 이 프로젝트 루트 cwd 를 전제로 **상대경로** `.claude/hooks/post_tool_use.py` 사용.
2. `cd` 로 작업 디렉토리를 `~/.claude` 로 이동 → 상대경로 해석 결과가 `~/.claude` + `.claude/hooks/...` = 이중 `.claude` 경로 조합.
3. 시스템 프롬프트에 명시된 원칙 *"Try to maintain your current working directory throughout the session by using absolute paths and avoiding usage of cd"* 위반.

**교훈**:
- **Bash 도구 안에서 `cd` 금지**. 모든 경로는 **절대경로**로.
- 여러 디렉토리 순회 시 `for d in /abs/path/*/; do ... "$d" ...; done` 형식.
- 사용자 명시 요청 시에만 `cd` 허용, 사후 cwd 복귀 필수.
- 이 교훈은 auto memory 박제 완료: `feedback_no_cd_absolute_paths.md`.

**참고**:
- 실행 명령: `cd ~/.claude && for s in story-init character-management worldbuilding plot-structure chapter-writing; do cp -rn "skills/story-skills/skills/$s" "skills/$s" && echo "OK: $s"; done`
- 영향: 설치는 완료, Hook 자동 감사 로그 1회 누락
- 복구: 이후 모든 명령을 절대경로로 변경 (`cd "c:/.../game" && ...` 대신 `ls ~/.claude/skills/`)

---

## FAIL-004 — 설치한 창작 skill 을 활용하지 않고 직접 집필 (2026-04-21, 세션 #2, Phase 0)

**증상**:
`~/.claude/skills/` 에 창작 skill 22개 + agent 17개 설치 완료 후, 소설 프롤로그 집필 시 **Skill tool 호출 없이** 나베랄 감마가 단독으로 집필 (`wiki/design/novel/prologue.md` Rev.1, 6,200자). 대표님 지적 *"간략한 내용을 가지고 소설쓰는 스킬 찾아봐바 라이브러리에 있을듯 ㅎㅎ"* 후 뒤늦게 `prose-writing`, `writing-principles`, `chapter-writing` 등이 설치됐음에도 활용 안 한 것 자각.

**원인**:
1. **설치 완료 = 활용 완료 착각**. 설치는 skill 파일을 디스크에 두는 것. 활용은 **Skill tool 로 명시적 호출** 해야 방법론이 내 컨텍스트에 주입됨.
2. **피드백 메모리의 부분 적용**. 오늘 박제한 `feedback_active_obsidian_notebooklm.md` 는 Obsidian·NotebookLM 능동 활용을 지시. 그런데 동일 원칙 (설치 도구의 능동 호출) 을 **설치한 skill** 에 확장 적용 못 함. 피드백이 원칙 수준으로 일반화되지 않고 고유명사에 묶임.
3. **창작 작업 시작 관성**. 집필은 "직접 쓰기" 가 가장 빠른 길이라는 암묵적 전제 — skill 방법론 로드는 귀찮은 우회로 느껴짐. 그러나 이 전제가 Rev.2 과해석 10건의 뿌리 (*"내가 그냥 쓰면 대표님 원안과 맞겠지"*) 와 같은 구조.

**교훈**:
- 창작·분석·검수 작업 시작 전 **관련 skill 을 먼저 `Skill(skill="name")` 로 호출** 하고, 방법론 로드 후 작업.
- 피드백 메모리 확장: **능동 활용 원칙은 모든 설치 도구 (Obsidian, NotebookLM, skill, agent) 에 동일 적용**.
- 집필 skill 우선순위: `prose-writing` (문장·문단) + `chapter-writing` (장 구조) + `writing-principles` (독자 심리) + `story-context` (컨텍스트 스코프) + `prose-critique` (사후 검수).
- 세션 #3 부터 Ch.01 집필 시 위 순서로 skill 호출 후 진행.

**참고**:
- 프롤로그 (skill 미활용): `wiki/design/novel/prologue.md` Rev.1, 6,200자
- 설치된 창작 skill 목록: 이번 세션 `SESSION_LOG.md` 의 "수행 작업 · 창작 skill 설치" 섹션
- 대표님 지적 시점: 오늘 세션 후반 ("ㅎㅎ" 포함)
- 해결: 세션 #3 브리핑에 "skill 호출 체크리스트" 포함 예정

