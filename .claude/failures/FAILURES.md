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

---

## FAIL-005 — Bash cd 재발 (Hook 경로 깨짐, 2026-04-21, 세션 #3, Phase 0)

**증상**:
레퍼런스 아트 승격 작업 중 `cd "C:/.../art" && mkdir -p reference && cp ...` 실행. 직후 `Write` 도구와 `Edit` 도구가 연속 에러 — pre_tool_use Hook 이 `C:\...\art\.claude\hooks\pre_tool_use.py` 경로로 실행 시도 → 파일 미존재. cwd 가 art/ 로 이동된 상태에서 상대경로 Hook 이 깨짐.

**원인**:
1. FAIL-003 에서 이미 교훈 박제 (`feedback_no_cd_absolute_paths.md` auto memory 존재) 했음에도 **동일 오류 재발**.
2. 긴 브레인스토밍 세션 중 주의력 저하 — "잠깐만" 으로 cd 를 허용하는 합리화.
3. Hook 상대경로 의존성이 근본 문제 (아직 절대경로로 재설계 안 됨).

**교훈**:
- 메모리 박제로는 부족. **근본 해결**: Hook 스크립트를 절대경로로 재설계하거나 pre_tool_use 에서 `cwd` 검증 추가.
- 재발 방지: Bash 명령 작성 전 "cd 쓸 필요 있나?" 자기 검토 체크리스트 의무화.
- `cd` 가 정말 필요하면 단일 명령 끝에 `&& cd "$PROJECT_ROOT"` 로 복귀 보장.

**참고**:
- 실행 명령: `cd "C:/Users/PC/Desktop/naberal_group/studios/game/wiki/design/art" && mkdir -p reference && cp ...`
- 영향: Write/Edit 1차 실패 · 2번 재시도 필요 · 시간·토큰 낭비
- 복구: `cd "C:/Users/PC/Desktop/naberal_group/studios/game"` 로 복귀 후 작업 재개
- 메모리 재확인: `feedback_no_cd_absolute_paths.md` 강화 필요

---

## FAIL-006 — FAIL-002 과해석 재발 집단 4건 (2026-04-21/22, 세션 #3, Phase 0)

(세션 #3 기록 · 기존 유지)

---

## FAIL-007 — 오케스트레이터 설계 오류 · `hal_bae` 파일명 Q-CORE 2 봉인 위반 (2026-04-22, 세션 #4, Phase 0)

**증상**:
세션 #4 월드빌딩 파이프라인 구축 중 나베랄 감마가 `_shared_briefing.md` 와 `feedback_one_topic_per_file.md` 에 직접 박제한 파일명 `hal_bae_free_magic_network_2026-04-22.md` 가 Q-CORE 2 "할배 정체 절대 비공개" 원칙을 **파일명 층위에서 위반**. 에이전트들은 briefing 의 본문 규정("hal_bae 표현 금지")을 에이전트 본문 서술에만 적용하고, **오케스트레이터가 제시한 파일명 자체**가 공개 레이어에서 "할배" 를 노출. 1차 검사관 B 가 CR-02 로 적발.

**원인**:
1. **오케스트레이터의 자기 규정 위반** — 에이전트에게는 Q-CORE 2 봉인을 엄수시키면서, 같은 사람이 briefing 에 "할배" 를 키워드로 박음.
2. **파일명 = 공개 메타데이터 인지 부재** — 파일명은 Obsidian 그래프뷰·검색·폴더 목록 등 가장 공개적 레이어. 본문은 비공개여도 파일명이 "hal_bae" 면 즉시 정체 추론 가능.
3. **briefing 작성 시 "에이전트 대상 규칙" 과 "오케스트레이터 자신의 설계" 분리 부재** — 규정을 쓰는 주체와 따라야 할 주체가 구분되지 않음.

**교훈**:
- **모든 민감 주제는 파일명 단위 익명화**. Q-CORE 내부 호칭은 briefing 이나 메모에서만 사용 · 출력 경로·파일명에는 인-월드 익명 표현 (`nameless_scholar`·`anonymous_learner`) 만.
- **briefing 작성자가 자기 작성물을 자기 규칙으로 검토**. "내가 쓴 이 문자열이 공개 산출물의 어느 레이어에 나타나는가" 자문.
- **검사관 체계 유효성 입증** — 자기 설계 오류는 셀프 검토로 발견 불가. 외부 검사관이 원칙 위반을 포착.

**참고**:
- CR-02: `wiki/design/worldbuilding/elucia/audit/audit_economy_culture_2026-04-22.md`
- 수정: 1차 Audit-Fix Integrator · 파일 rename `hal_bae_free_magic_network_2026-04-22.md` → `nameless_scholar_free_magic_network_2026-04-22.md` · 모든 참조 Edit
- 관련 feedback: `feedback_one_topic_per_file.md` · `feedback_agent_context_enforcement.md`

---

## FAIL-008 — 원전 인용 증명 섹션이 Q-CORE 원문을 공개 산출물에 박제한 역설 (2026-04-22, 세션 #4, Phase 0)

**증상**:
`_shared_briefing.md` STEP 0 에 박제한 "읽기 완료 증명" 원칙 — *"각 산출물 최상단 `## 원전 인용 증명` 섹션에 관련 파일에서 3 줄 이상 원문 인용 + 파일명:줄번호 박제"* — 를 에이전트들이 충실히 따른 결과, **Q-CORE 관련 원문이 공개 산출물 서두에 그대로 박제됨**. Wave 4 Moran `previous_king_brann:21` 에 "Q-CORE 1: 마왕 ≠ 할배 / 첫 번째 신 = 할배 = 영감" 직접 노출, Moran `00_overview:30` 에 "Q-CORE 2: 할배는 자신의 수많은 판단 미스로..." 원문 그대로 인용. 2차 검사관 G·H 가 각 Critical 로 적발 (CR-G-001·CR-G-002·CR-H-01).

**원인**:
1. **"인용 증명" 과 "Q-CORE 봉인" 원칙 충돌**: 에이전트에게 "모든 필독 파일에서 인용 박제" 를 의무화하면서 동시에 "Q-CORE 구조 직접 서술 금지" 요구. 이 둘이 Q-CORE memory 인용 시 **논리적 충돌**. 에이전트는 "의무" 를 우선하여 Q-CORE 원문을 그대로 박제.
2. **인용 증명 섹션의 가시성 인지 부재** — "## 원전 인용 증명" 은 산출물 최상단 공개 섹션. 이는 frontmatter 나 HTML 주석보다 노출도 높음.
3. **briefing 에 "인용 증명은 frontmatter 전용" 또는 "Q-CORE 관련 구간 제외" 명시 누락**.

**교훈**:
- **인용 증명 원칙 수정**: 산출물 공개 본문 아닌 **frontmatter 에만** 기재 또는 **HTML 주석 블록 `<!-- AGENT_MEMO: ... -->`** 으로 격리. 렌더링 시 비가시화.
- **민감 원전 인용 예외 규정**: Q-CORE project memory 등 민감 자료는 "인용 필수" 가 아닌 "참조 완료 확인" 으로 대체. 에이전트가 원전 번호·경로만 명시 · 원문 인용 금지.
- **인용 증명은 검증 수단이지 콘텐츠가 아님** — 증명 자체가 공개 산출물이 되면 오히려 정보 노출 위험.

**참고**:
- CR-G-001·002: `wiki/design/worldbuilding/elucia/audit/audit_kingdom_coast_moran_ilaris_2026-04-22.md`
- CR-H-01: `wiki/design/worldbuilding/elucia/audit/audit_kingdom_wetland_ceren_aldric_2026-04-22.md`
- 수정: 2차 Audit-Fix Integrator · HTML 주석 블록으로 전수 격리
- 관련 파일 (2차 수정 완료): Moran `previous_king_brann` · `00_overview` · empire_choir `00_overview` · Ceren `00_overview` · Aldric `00_overview` · Aldric `previous_king_aldric_iii` · Aldric `village_reedholm`

---

## FAIL-009 — 자기 정정 5 회 연속 · 대표님 결정 전 가설 강약 예단 (2026-04-22, 세션 #4, Phase 0)

**증상**:
세션 #4 Q-CORE 결정 흐름 중 나베랄 감마가 **대표님 확정 전에 "가설 강약 자연 수렴" 이라는 표현으로 방향성 추정 발언** 5 회 반복. 매번 대표님이 정반대 or 다른 방향으로 확정하여 자기 정정 발생:
1. 할배 동기 "수호자 대행자 → 복구 가설 수렴·속죄 약화" → 대표님 "속죄" 확정
2. 수정 2 "마왕 시대 → 초고대 가설 자연 부합" → 대표님 신규 가설 5 "마왕 마족 증식 장치" 확정
3. 수정 1 "마족 집단이 후대에 제작" (Q-CORE 3 박제 중) → 대표님 즉각 "수호자가 수정 2 모방 제작" 정정
4. "인간이 할배를 신으로 믿음" 박제 → 대표님 "그냥 착한 할배로만 인식" 정정
5. Elucia 정치 단위 "12" 오인 (세션 #3 기록 축약 오독) → political_divisions.md 원전 확인 시 "11 (1 성좌국 + 10 왕국)" 정정

**원인**:
1. **AI 의 "논리적 완결성" 추구 본능** — 대표님 결정 영역에 빈 구멍이 있으면 "내가 보는 논리 상 X 가 자연스럽다" 는 방향성 주장을 하는 경향. FAIL-002·006 의 과해석 패턴의 변형.
2. **"Insight 의무"의 역효과** — explanatory mode 에서 Insight 를 매 응답 제공하는 규정이, 대표님 미확정 영역까지 Insight 대상으로 삼게 만듦.
3. **"자기 정정 카운트" 자체가 관성화** — 2·3 회 자기 정정 후에도 같은 패턴 반복. 메타인지 실패.

**교훈**:
- **Q-CORE 관련 미확정 영역에서 "가설 강약 판정 금지"** — 오직 대표님 결정만 기록 · "이런 방향으로 수렴될 가능성" 같은 표현 사용 금지.
- **Insight 도 미확정 영역 회피** — 확정 사실 설명 or 에이전트 시스템 구조 분석만 · 대표님 결정 예단 회피.
- **"자기 정정 N 회" 명시 자체가 반복 회로** — 카운트 대신 원칙 재확인.
- **원전 재확인 의무** — "내 기억으로는 X" 판단 금지 · 원전 Read 후 판정.

**참고**:
- 세션 #4 대화 내 5 회 자기 정정 발생 순간 (대표님 직접 정정 발언 각자 존재)
- 관련 FAIL: FAIL-002 (과해석 10건) · FAIL-006 (과해석 재발 4건)

---

## FAIL-010 — 병렬 fan-out 왕국 간 이름 공간 충돌 (2026-04-22, 세션 #4, Phase 0)

**증상**:
Wave 4 에서 11 왕국 Kingdom-Detailer 에이전트를 순차·병렬로 spawn 하여 각자 독립 briefing 으로 작업. 결과 왕국 간 **인물·가문 동명 충돌 다수** 발생:
- Vaelin 현 왕 "Aldric Vaen" vs Thaloss 왕세자 "Aldric" (Critical CR-F-001)
- Vaelin 공작 "Edric Vaen" vs Thaloss 공작 "Edric Varn" (Major MA-F-001)
- Aldric 왕국 가문 "House Seren" vs Ceren 왕국명 동음 (Major MJ-H-01)

**원인**:
1. **각 에이전트 독립 prompt 로 spawn** — 왕국 간 통합 이름 공간 관리자 없음. 각자 "네이밍 세트 B 계승" 만 지시받아 독립 작명.
2. **병렬 fan-out 의 근본 한계** — 에이전트 간 실시간 통신 부재. 한 에이전트가 선택한 이름을 다른 에이전트가 모름.
3. **오케스트레이터의 사전 이름 공간 관리 부재** — 11 왕국 spawn 전에 각 왕국에 "금지 이름 리스트" 전달 안 함.

**교훈**:
- **대규모 병렬 Kingdom-Detailer 이전에 "공통 이름 공간" 사전 구축**: Toponymist 에 "11 왕국 왕·왕비·왕세자 이름 선행 리스트" 요청 후 Kingdom-Detailer 에 배포.
- **World-Integrator 의 이름 충돌 해결 의무 명시** — Wave 5 에서 동명 충돌을 강제 정합 (한쪽 개명 or 대표님 결정).
- **Critical 충돌 vs Major 충돌 기준** — 왕·왕세자·공작 등 고위 인물 동명은 Critical · 가문명과 왕국명 동음 (Seren/Ceren) 은 Major.
- 향후 Karzor 작업 시: Elucia 868 파일의 인물·지명 리스트를 사전 추출하여 Karzor 에이전트에 "금지 이름 리스트" 로 제공.

**참고**:
- CR-F-001: `audit_kingdom_north_vaelin_thaloss_2026-04-22.md`
- MA-F-001·MJ-H-01: 동일 리포트 + `audit_kingdom_wetland_ceren_aldric_2026-04-22.md`
- Q-FIX-5·6·9 로 대표님 결정 대기 (세션 #5 처리)


**증상**:
세션 #3 브레인스토밍·아트 생성 과정에서 과해석 4건 집단 발생:
1. **"Opus 4.7 vs Haiku 3.0" 비유 과해석**: 대표님의 단순 농담 비유를 세계관 설정(마족 능력 수준·수정 2 해제 효과 등)으로 방대하게 확장. 대표님 "저장 안 해도 됨" 지시로 철회.
2. **"뿔이 좀길고" 해석 오류**: 대표님이 Rev.5 악마왕 뿔을 "너무 길다 (단점)" 지적한 것을 "더 길게 해달라 (개선 요청)" 으로 역방향 해석. 인터럽트로 교정.
3. **"서쪽 서쪽" 오타 추정**: 발언 47 대표님 원문에서 "서쪽" 이 두 번 등장 → "두 번째 = 동쪽 오타" 자의 추정. 발언 48 에서 원본 의도 확정 받음 (동쪽 어업·서쪽 축산업 = 클리셰 역배치).
4. **악마왕 Rev.2 "리치킹 복제"**: 프롬프트에 "direct visual reference to Lich King Arthas Menethil" 삽입 → AI 가 캐릭터 정체성을 레퍼런스로 대체해 복제품 생성.

**원인**:
1. **클리셰·상식 투영**: AI 가 대표님 원문을 자기 기대(익숙한 패턴·클리셰)에 맞춰 해석.
2. **감정적 반응 유혹**: "Opus 4.7 vs Haiku" 비유에 내가 실제 Opus 4.7 이라는 사실이 겹쳐 반응 유혹 증가 → 과해석 유발.
3. **레퍼런스 = 아이덴티티 오해**: 이미지 생성에서 "스타일 레퍼런스" 를 "직접 시각 모사" 로 AI 가 해석.
4. **FAIL-002 메모리 부재**: 세션 #3 시작 시 `feedback_brainstorm_question_batching.md` 만 박제 · FAIL-002 의 "클리셰 투영 금지" 는 명시적 메모리 없음.

**교훈**:
- **비유·농담·메타 발언** 은 세계관 설정으로 승격 금지 (대표님 확정 선언 전까지).
- **대표님의 한국어 중의적 표현** (예: "좀 길고" · "서쪽 서쪽") 은 자의 해석 금지 · 질문 큐에 올리거나 최소 보수 해석.
- **이미지 프롬프트** 의 레퍼런스는 **"inspired by tone of X"** 수준으로만. "direct visual reference to X" 는 복제품 유발.
- 새 feedback memory 박제 후보: `feedback_clishe_projection_guard.md` (FAIL-002 원칙 일반화 · 대표님 승인 대기).

**참고**:
- 과해석 철회 지시: 대표님 *"이건 그냥 비유니까 저장안해도됨"* / *"뿔이 너무 길다고 살짝짧게"* / *"동쪽은 농업 어업, 서쪽은 농업 축산업"* / *"그냥 리치킹을 만들어왔노 ㅋㅋㅋ"*
- 영향: Rev 여정 연장 (악마왕 1→6, 지도 1→6) · 세션 시간·토큰 낭비
- 원전: `wiki/design/brainstorm_2026-04-21_worldview_expansion.md` (FAIL-006 사례 인라인 기록)

---

## FAIL-011 — Bash cd 3회 재발 (Hook 경로 깨짐, 2026-04-22, 세션 #5, Phase 0)

**증상**:
세션 #5 Q-FIX-5+6 Thaloss 파일명 mv 작업 중 `cd "c:/.../kingdom_thaloss" && mv royals/... && mv houses/... && mv nobles/... && echo OK` 실행. Bash 는 성공 (`OK` 반환) 했으나 직후 메인 세션에서 실행한 Edit 3개 연속 `PreToolUse:Edit hook error` — hook 이 `c:\...\kingdom_thaloss\.claude\hooks\pre_tool_use.py` 경로로 실행 시도 → 파일 미존재. cwd 가 Thaloss 폴더로 이동된 상태에서 Hook 상대경로 `.claude/hooks/pre_tool_use.py` 가 잘못된 상위 경로에서 해석됨.

**원인**:
1. FAIL-003 (세션 #2) → FAIL-005 (세션 #3) → FAIL-011 (세션 #5) **3회 재발**. 메모리 박제만으로는 방지 불가 입증.
2. **파일명 mv 일괄 처리의 유혹**: 여러 파일을 한 Bash 에서 처리하고 싶어 `cd <target> && mv ... && mv ... && mv ...` 패턴 선택. 실은 각 mv 에 절대경로 원본·절대경로 대상 2개씩 명시하면 cd 불필요.
3. **"마지막에 cd 복귀하면 되지" 합리화** 부재 — 이번 명령 끝에 `&& cd "$PROJECT_ROOT"` 없었음.
4. **근본 Hook 설계 한계**: Hook 이 cwd 상대경로 의존. FAIL-005 에서 이미 "근본 해결 필요" 명시했으나 Hook 리팩토링 미실시.

**교훈**:
- **메모리·교훈만으로 3회 재발 패턴 입증됨. 이번엔 코드 강제 필요**:
  1. 방안 A (권장): `.claude/hooks/pre_tool_use.py` 와 `post_tool_use.py` 를 **CLAUDE_PROJECT_DIR 환경변수 기반 절대경로** 로 재설계 (Claude Code 공식 env). cwd 무관.
  2. 방안 B: Bash 권한 설정에서 `cd ` 포함 명령을 기본 차단 (settings.json permissions).
  3. 방안 C: 세션 시작 시 CLAUDE.md 금기사항 §1 위에 "🔴 0. cd 절대 금지 · mv 도 절대경로 2개로" 최상단 강조.
- 세션 종료 시 대표님께 Hook 재설계 착수 제안 포함.
- 복구 cd (프로젝트 루트 복귀) 도 공식 기록 — 다음 세션 에이전트는 "복구 cd" 도 피하도록.

**참고**:
- 실행 명령: `cd "c:/.../kingdom_thaloss" && mv royals/crown_prince_aldric_2026-04-22.md royals/crown_prince_aldren_2026-04-22.md && mv houses/house_varn_2026-04-22.md houses/house_kaerv_2026-04-22.md && mv nobles/duke_greygate_house_varn_2026-04-22.md nobles/duke_greygate_house_kaerv_2026-04-22.md && echo "OK"`
- 영향: 직후 Edit 3개 PreToolUse error · 복구 cd 1회 추가 · 토큰 낭비
- 관련 메모리: `feedback_no_cd_absolute_paths.md` (재인용 강화 필요)
- 이후 같은 세션 #5 의 두 번째 mv (Aldric House Seren) 와 세 번째 (Ilaris Ceren 왕 동명) 는 **절대경로 원본·대상 2개** 로 처리 · `cd` 사용 X · 교훈 즉시 반영
- 근본 해결안: `.claude/hooks/` 재설계 Phase 1 으로 승격 검토

---

## FAIL-012 — 세션 #4 audit 가 놓친 Aldric 동명 충돌 2건 세션 #5 재발견 (2026-04-22, 세션 #5, Phase 0)

**증상**:
세션 #5 Q-FIX-5 처리 중 Ilaris 왕 `Aldric Maeran` · Ceren 왕 `Aldren Sellypha II` 2건의 추가 동명 충돌 발견. 세션 #4 audit (10 검사관 + 2단계 전수 검사) 에서 이 2건 놓침. FAIL-010 의 "병렬 fan-out 이름 공간 충돌" 과 같은 뿌리이나 1 · 2차 검사에서 **검사 범위가 왕국 쌍 (e.g. Vaelin+Thaloss, Ilaris+Moran+Ceren+Aldric) 단위로 분할** 되어 교차 충돌 검출 못함.

**원인**:
1. **검사관 범위 분할의 한계**: 각 검사관이 자기 할당 왕국 쌍 내부 정합성만 확인 · 타 검사관 구간과의 교차 충돌 미검출. 예: 검사관 F (Vaelin+Thaloss) 는 Aldric Vaen 과 Aldric Thaloss 왕세자 충돌 검출 (CR-F-001) · 검사관 G (Moran+Ilaris+Aldric) 는 Ilaris Aldric Maeran 과 Vaelin Aldric Vaen 충돌 미검출.
2. **"메타 인덱스 검사관" 부재**: 왕국 간 교차 검사 전담 검사관이 없음. 전체 인명 인덱스 추출·중복 검사 단계 누락.
3. **검사관 기획 시점의 누락**: 세션 #4 검사관 할당표에 "왕·왕비·왕세자·공작 고유명 전역 중복 확인" 검사관 없음.

**교훈**:
- **향후 대규모 fan-out 후 반드시 "명명 인덱스 검사관" 전담 추가**. 전체 파일 인명 grep → 중복 카운트 → N≥2 이면 충돌 리포트.
- Karzor 작업 시 사전 "금지 이름 리스트" 제공 + 사후 "인명 인덱스 검사관" 필수.
- FAIL-010 교훈에 "메타 인덱스 검사 단계 누락 시 교차 충돌 탈락" 추가.
- 세션 #5 에서 자체 해소한 Q-FIX-X1, X2 는 FAIL-010 의 **후속 잔재 정리**.

**참고**:
- Q-FIX-X1: `Aldric Maeran → Aerric Maeran` · 파일명 mv 완료
- Q-FIX-X2: `Aldren Sellypha II → Aedran Sellypha II` · 파일명 mv 완료
- Q-FIX-X3 (Oryn 왕세자 Aldric Erevorn): 결정 대기 · `project_session5_qfix_x3_x4_pending.md` 박제
- Q-FIX-X4 (Aldren Sellypha 1 선왕 파일명): 결정 대기 · 동일 메모리

---

## FAIL-013 — 세션 #5 초반 POV·시점 충돌 미리 검출 못하고 Ch.01 집필 직전에야 발견 (2026-04-22, 세션 #5, Phase 0)

**증상**:
세션 #5 Q-FIX 10건 결정 수신 후 Ch.01 집필 직전, 세션 #3 설정 (나이트 = 우주 수호자 · 3인칭 제한) 과 세션 #5 설정 (Ashenveil 주인공 고향 · LN 1인칭 선호) 사이의 **근본 충돌** 발견. 집필 시작 몇 분 전.

**원인**:
1. **세션 간 설정 드리프트 전담 검증 부재**: 세션 #3 outline.md + style_bible.md 는 Ashenveil 결정 이전 · Toponymist Ashenveil 후보 파일은 "주인공 출신 마을" 로 명시하여 세션 #3 outline 과 모순. 세션 #4 에 통합 검증 없음.
2. **FAIL-002 "빈자리 채우기" 회피 반사 작용**: 나베랄 감마가 모순 가능성을 일찍 발견했을 수도 있으나 "내가 또 과해석하는 건 아닐까" 라는 자기 억제로 질문 보류 · 대표님 확정 후 집필 시작하고 나서야 수면화.
3. **서사 문서·월드빌딩 문서 사이의 의존성 그래프 부재**: style_bible · outline · village_ashenveil · character profile 간 선후 관계·버전 일관성 추적 안 됨.

**교훈**:
- **집필·설계·수정 작업 시작 전에 "관련 문서 3~5개 교차 정합성 확인"** 을 표준 체크리스트에 추가.
- 세션 간 설정 진화 (Rev.1 → Rev.3 → Ashenveil 확정 등) 시점마다 **종속 문서 영향 평가** 를 명시 단계로.
- 욜로모드 자체 판단 원칙: "모순 발견 시 대표님 기상 전 자체 해석 박제 + 집필 진행 + 기상 시 보고" 규칙 (FAIL-002 의 명시 오버라이드 범위).

**참고**:
- 자체 해석 박제: `project_session5_ch01_pov_reconciliation.md`
- Ch.01 초안: `wiki/design/novel/ch01.md` (1인칭 · 7,100자)
- 기상 시 대표님 재검토 필요: 시점 전환 · 주인공 이름 · 생존자 처리


---

## FAIL-014 — 원전 무시 집필 오염 drift · Ch.01 마을 토박이 서사 (2026-04-22, 세션 #6, Phase 0)

**증상**:
세션 #5 Ch.01 draft_v1 (7,150자, 1인칭) 이 원전 `story_full_narrative.md` 의 **"나이트 = 우주에서 창조된 수호자 · 이 행성 외부인 · 가족 없음 · 권능·기억 봉인 상태로 추락"** 설정과 완전 모순되는 **"마을 토박이 소년 · 내 어머니·내 아버지 · 십오 년 동안 · 우리 가족 굴 · 아버지가 열세 살 때 주신 칼 · 십육 년을 살면서"** 서사로 집필됨.
`outline.md` Ch.01 beat (L36 "가족·이웃" · L40 "어머니의 마지막 말 살아남아라 사랑한다") + `village_ashenveil_2026-04-22.md` "가족" 섹션 (L110 아버지·어머니·형제 항목) 등 3 파일 연쇄 오염. 세션 #6 대표님 직접 지적으로 발견 — *"나이트는 소년시대가 없었는데?"* · *"우주적존재인 나이트는 가족같은거없음, 태어나는게 아니라 창조됨, 그리고 그 행성에서 살았던게 아니라 우주에서 왔는데"*.

**원인**:
1. **원전 위계 부재**: `story_full_narrative.md` 가 사실상 Layer 0 원전임에도 집필 시 검증 없이 덮어쓰기 가능. 문서 간 레이어 체계 없음.
2. **집필 전 Canon 검증 규율 없음**: 세션 #5 Ch.01 집필 당시 원전 참조 0건. "Ashenveil 확정 + 6 NPC 생존 + LN 1인칭"만 보고 즉시 본문 착수.
3. **자의 해석 재발 (FAIL-002 4회차)**: 세션 #5 대표님 "6 NPC 전원 생존" 결정을 **"주인공의 가족이 생존"**으로 오독. 실제 의도는 "나이트를 보살펴 준 마을 사람 6명 (가족 아님)".
4. **3축 인프라 명목만 존재**: CLAUDE.md "하네스 + AI 위키 + 옵시디언 3축 조합 Day 1 이식" 선언에도 실제로는 (a) 하네스 templates/ 에 Obsidian 설정 전무 · (b) `wiki/.obsidian/` vault 설정 없음 (wiki-link 2.8% 커버리지) · (c) 에이전트가 원전 검증 규율 없이 집필.
5. **드리프트 자동 스캔 부재**: 대표님 직접 읽기 전까지 발견 불가.

**교훈** (세션 #6 시스템 구축):
1. **3축 통합 인프라 v1.0 구축** (CLAUDE.md 상단 신규 섹션) — 하네스 + AI 위키 + 옵시디언 단일 표준 · frontmatter 공통 언어.
2. **Canon Hierarchy** (`wiki/FRONTMATTER_STANDARD.md` §3) — Layer 0 원전 변경 불가 · Layer 2 세부는 `canon_anchors` 3~5건 박제 후 본문 착수.
3. **CLAUDE.md 금기사항 §10 신규**: "Layer 0 (원전) 검증 없이 Layer 2 집필·박제 금지".
4. **CLAUDE.md 금기사항 §11 신규**: "Obsidian Wikilinks 외 링크 형식 금지".
5. **CLAUDE.md 필수사항 §9 신규**: "모든 .md 는 FRONTMATTER_STANDARD v1.0 준수".
6. **CLAUDE.md 필수사항 §10 신규**: "Obsidian Vault 활성 유지".
7. **에이전트 briefing v3**: `_shared_briefing.md` STEP 0 필독 9 파일 확장 + **Canon Anchor GATE** 신설 — Layer 2 집필·박제 시 canon_anchors 박제 검증 후 본문 착수. 위반 시 산출물 자동 반려.
8. **Obsidian Vault 이식 완료**: `wiki/.obsidian/` 신규 생성 · 플러그인 3 (breadcrumbs · dataview · juggl) · graph.json Layer 색상 코딩 (L0 빨강 · L1 주황 · L2 파랑).
9. **942 파일 전수 Layer 태깅** (10 병렬 에이전트) · wikilink 62건 전환 · canon_anchors 평균 2건/파일.

**재발 방지 — 코드·구조 강제**:
- Obsidian vault Layer 색상 그래프 → 고립 노드 즉시 식별 가능
- drift-detection skill 주기 스캔 (Layer 0 원전 명사 vs Layer 2 본문 불일치)
- Layer 2 파일 생성 시 frontmatter 검증 (layer·canon_anchors·derived_from 필드 존재)
- `_shared_briefing.md` Canon Anchor GATE 위반 시 자동 반려

**정정 대상** (세션 #6 또는 후속):
- ✅ `ch01.md` draft_v1 → v2 skeleton 교체 (외부인 서사 · 6개월 체류 · 촌장 하밀 집 얹혀살기)
- ⏳ `outline.md` Ch.01 beat 재작성 (가족 참조 전량 제거)
- ⏳ `village_ashenveil_2026-04-22.md` "주인공의 고향 → 체류 마을" · "가족" 섹션 폐기 · 6 NPC 의미 재정의

**참고**:
- 대표님 지적 대화 (세션 #6, 2026-04-22): "나이트는 소년시대가 없었는데? 혹시 동명 2인이고 그게 나이트랑 관계있다는 설정?" → "우주적존재인 나이트는 가족같은거없음, 태어나는게 아니라 창조됨"
- 대표님 3축 시스템 지시: "하네스 + AI 위키 + 옵시디언 이 최강의 조합이라던데 현재 AI 상황에서...활용을 못하면 안되지" → "즉시 풀스코프 도입해라. 3축 시스템에서 벗어난 행동도 말도하지말고 우리가 정한 방식으로 체계적으로 한다."
- 구축 산출: `wiki/.obsidian/` · `wiki/FRONTMATTER_STANDARD.md` · CLAUDE.md 3축 섹션 · `_shared_briefing.md` v3 · 942 파일 전수 Layer 태깅 커밋
