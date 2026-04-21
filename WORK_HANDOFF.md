# WORK HANDOFF — naberal_game

## 최종 업데이트
- 날짜: 2026-04-21
- 세션: **#2** (세계관 확정 + 창작 skill 설치 + 소설 프로젝트 시작)
- 상태: **Phase 0 Bootstrap 연장** — 세계관 Rev.3 확정 · 창작 도구 파이프라인 완비 · 소설 프롤로그 Rev.1. Phase 1 "Identity + Pipeline Draft" 진입 대기 유지 (실질 Phase 0 확장).

---

## 세션 #2 완료 항목 (2026-04-21 후반)

### ✅ 세계관 철학 3조 조문화 (최상위 원칙 신설)
- 가. 불완전성 · 나. 나이트 인격체 (한결같음) · 다. 영혼 평등
- 설계 헌법 3조와 병립 구조
- `wiki/design/brainstorm_2026-04-21.md` 제0부에 박제 (대표님 원문 인용 22건 앵커)

### ✅ 엔딩 체계 5구조 확정
- 2분기 (인간 vs 화합) × 2회차 (1회차/다회차) + 진엔딩 E
- 각 엔딩의 Phase 별 최종 보스 · 전투 구조 상세

### ✅ 과해석 10건 집단 정정 (FAIL-002)
1. Scene 2 동료 참살 상세 → 한 문단 축약
2. 히든 엔딩 트리거 → 자동 발동
3. 엔딩 E → 진엔딩 재정의
4. 7대 신 지위 → 엔드게임 무기 획득 장치
5. "신이 번식 본능 심음" → 자연 번식력
6. 우주 포식자 → 숨겨진 보스
7. Phase 1 동료 = 인간 4만 (타종족은 이별 후)
8. 첫 번째 신 = 후발주자 (용족·엘프가 최초)
9. 성간 혼천의 (NotebookLM drift) 폐기 → 의지결 × 성인식 장비
10. "뒤틀림" = 사회 억압 구조 (공간 왜곡 아님)

### ✅ 동료 구조 전면 재편
- Act 1 = 인간 4 (기사·신관·마법사·도적)
- Act 2 중반 = 인간 전원 이탈
- Act 2 후반 = 타종족 4 (엘프·마족·오크·용족)
- Act 3 선택 분기점 (인간 vs 화합)

### ✅ 의지결 × 성인식 장비 시스템 확정 (4층 스킬)
- 3종 (스킬형·스탯형·특수형)
- 성인식 목걸이 1개 (별도 슬롯) · 등급별 증폭 +0%~+30%
- 링크 2/3/4 시너지 (페어링 차별화)
- 종족별 성인식 문화 (엘프 30세 · 마족·용족 내재 장착)
- 주인공 성인식 편입 에피소드 (마을 16세 성인식, 촌장 눈감아줌)

### ✅ 종족 생태학·신앙 경제학
- 행성 시간축: 용족+엘프 → 마족 → 수호자 개입 → 첫 신 → 인간·기타
- 6종 각자 번식·신앙·성인식 메커니즘
- 신앙 경제학 쌍방 공모 구조

### ✅ 하네스 경로 원복
- `fdf41b1` 의 `../../harness/` → `../harness/` 복원 (8 파일 byte-exact)
- commit `54ca1af`

### ✅ 설계 원전 · 종합 스냅샷 · Rev.3 서사
- `wiki/design/brainstorm_2026-04-21.md` (1,050줄) — Rev.3 인용 기준
- `wiki/design/game_setting_complete_2026-04-21.md` (630줄) — NLM 공유용
- `wiki/design/story_full_narrative.md` Rev.3 (1,026줄) — 과해석 반영 재작성
- `wiki/design/MOC.md` 갱신

### ✅ 창작 skill 라이브러리 설치 (전역)
- 3개 레포 clone 완료 (`~/.claude/skills/`):
  - `haowjy/creative-writing-skills` (Apache 2.0) — 13 skills + 17 agents
  - `danjdewhurst/story-skills` (MIT) — 5 skills
  - `Bobby-Gray/claude-dnd-skill` (MIT) — 1 skill
- **총 22개 skill + 17 agent 자동 등록** (system-reminder 확인)
- 제외: `forsonny/Claude-Code-Novel-Writer` (금기 §1 충돌)
- 보류: `nicmarti/skills-weaver` (Go 1.25 미설치)

### ✅ 딥 리서치 2건 + Phase 2 대기 명세
- `.planning/research/nlm_result_07_claude_creative_skills.md`
- `.planning/research/nlm_result_08_game_dev_libraries.md` (80+ URL 교차검증)
- `.planning/research/phase_2_deferred_tools.md` (unity-mcp · Yarn Spinner 3.1 · skills-weaver)

### ✅ 소설 프로젝트 시작
- `wiki/design/novel/outline.md` (25-30 챕터 지도, 30-40만자 목표)
- `wiki/design/novel/style_bible.md` (문체·시점·톤 헌법)
- `wiki/design/novel/prologue.md` Rev.1 (6,200자, 9 섹션)
- 단 skill 미활용 집필 — FAIL-004

### ✅ 핸드오프 3종
- 이 `WORK_HANDOFF.md` 업데이트
- `SESSION_LOG.md` 세션 #2 섹션 append
- `.claude/failures/FAILURES.md` FAIL-002 ~ FAIL-004 append

### ✅ auto memory 박제
- `reference_brainstorm_original_2026-04-21.md` — 향후 세션 필독 원전 위치
- `feedback_no_cd_absolute_paths.md` — cd 금지 원칙
- `MEMORY.md` 갱신 (총 4 엔트리)

### ✅ Git commits (세션 #2 진행분)
```
54ca1af fix(paths): 하네스 상대경로 원복
04e50e2 docs(design): 2026-04-21 브레인스토밍 설계 원전 박제 (Rev.3 기준)
```
(세션 #2 마무리 커밋 3-5개는 세션 종료 시 실행 예정)

---

## 대표님 결정 (세션 #2)

### 확정
1. **세계관 철학 3조** — 불완전성 · 한결같음 · 영혼 평등
2. **엔딩 체계** — 2분기 × 2회차 + 진엔딩 E
3. **동료 구조** — Act 1 인간 4만 · Act 2 전원 이탈 · 타종족 4명 합류
4. **의지결 × 성인식 장비** 시스템 · 링크 시너지
5. **"악의 신" 칭호 유예** — 시대가 이름을 정한다
6. **창작 skill 4개 (prose-writing, chapter-writing + 지원 7개)** 전부 활용 예정
7. **소설 집필 우선순위** — 화합 선택 분기 (정사 루트) 먼저

### 대기 중 (대표님 고민 중)
- [ ] 초반 주인공 동기 세부 연출
- [ ] 진엔딩 생존·사망 동료 명단
- [ ] 진엔딩 생존자 = 인간 도적 유지 여부
- [ ] Go 1.25 설치 여부 (skills-weaver 활성화)
- [ ] 피드백 메모리 `feedback_over_interpretation_guard.md` 박제 승인

### 추후 박제 대기
- 오크·드워프 세부 설정
- 오크 성인식 (전투 통과 의례 ↔ 목걸이 조화)
- 드워프 성인식 나이
- 마족·용족의 "태어날 때 의지결 내재 장착" 구체 메커니즘
- 마왕의 현재 상태
- 우주 포식자 vs 균형 수호자 선행 역사

---

## 다음 세션 (세션 #3) 할 일

### 🎯 1순위 — Skill 활용 집필 전환 (FAIL-004 교훈)
- [ ] Ch.01 집필 전 `Skill(skill="prose-writing")` + `Skill(skill="writing-principles")` + `Skill(skill="chapter-writing")` 호출
- [ ] Ch.01 숲의 그림자 집필 (~8,000자)
- [ ] 완성 후 `Skill(skill="prose-critique")` 로 사후 검수
- [ ] 필요시 `Skill(skill="prose-analysis")` 로 정량 지표 확인

### 2순위 — 세션 #2 미커밋 정리
- [ ] 원자 커밋 3-5개:
  1. Creative writing skills 메타 설치 기록 (`.planning/research/phase_2_deferred_tools.md` 등)
  2. Rev.3 서사 · 종합 스냅샷 (`story_full_narrative.md` · `game_setting_complete_*`)
  3. 딥 리서치 보고서 2종 (`nlm_result_07~08`)
  4. 소설 프로젝트 (`wiki/design/novel/`)
  5. 핸드오프 3종 (`WORK_HANDOFF.md` · `SESSION_LOG.md` · `FAILURES.md`)

### 3순위 — 후속 챕터
- [ ] Ch.02 마을의 저녁 (늙은 학자 첫 만남)
- [ ] Ch.03 성인식의 외부인 (목걸이 획득 · 의지결 시스템 서사 도입)

### 4순위 — 대표님 대기 결정 중 시급한 건 결정 요청
- 초반 주인공 동기 세부 (Ch.01~03 집필 전 필요할 수도)

---

## 병행 작업 상태

- **studios/shorts**: Phase 10 "Sustained Operations" 진입 대기 (세션 #26 Entry Gate PASSED)
- **studios/estimator**: (별도 스튜디오, 본 작업 범위 외)
- **창작 skill 전역 설치**: shorts 도 활용 가능 (나베랄 그룹 전체 자산)

---

## 참고

- **AI 도구 체인**: shorts 검증 + 오늘 창작 skill 확장 + Phase 2 예정 unity-mcp · Yarn Spinner
- **솔로 인디 레퍼런스**: Balatro · Animal Well · Vampire Survivors + Clair Obscur: Expedition 33 (턴제 패링)
- **서사 레퍼런스**: Overlord · Nier Automata · Drakengard · Warcraft 3 · Berserk · Spec Ops · Disco Elysium · Undertale

---

## (세션 #1 완료 내역 — 아래 유지)

---

## 세션 #1 완료 항목

### ✅ 하네스 스캐폴드
- `new_domain.py game` 실행 — 하네스 템플릿 5종 + Hook 3종 + 공용 스킬 5개 복사
- git init (독립 저장소)

### ✅ AI 위키 + Obsidian 확장 (shorts Perfect Navigator 패턴 Day 1 이식)
- `wiki/` + 6 카테고리 (design/engine/gameplay/art/audio/steam) + MOC.md × 6 + README.md
- `.obsidian/.gitkeep` — Obsidian vault anchor

### ✅ Memory + Failures + Deprecated Patterns
- `.claude/memory/MEMORY.md` + `project_game_stack.md` (Unity 6 + Steam + C# 박제)
- `.claude/failures/{FAILURES,FAILURES_INDEX}.md` (append-only 초기)
- `.claude/deprecated_patterns.json` (하네스 공용 5 regex 승계)

### ✅ Navigator 인프라 (shorts 2026-04-20 검증본 이식)
- `.claude/hooks/session_start.py` — Step 6b Navigator Coverage 포함
- `scripts/validate/navigator_coverage.py` — Navigator drift 자동 검증

### ✅ CLAUDE.md + ARCHITECTURE.md (Day 1 Perfect Navigator)
- `CLAUDE.md` — 96줄 목표, Identity + 금기 9 + 필수 8 + Navigator 매트릭스
- `docs/ARCHITECTURE.md` — Phase 0 Bootstrap + 10-phase 로드맵 초안

### ✅ Unity `.gitignore` 확장
- Library/, Temp/, Logs/, UserSettings/, Build/ 등 Unity 표준 패턴 추가

### ✅ GitHub 원격
- Repo: `github.com/kanno321-create/naberal_game` (Private, main 브랜치 — master deleted on origin)
- 첫 commit `02da275` push 완료

### ✅ Part B: NotebookLM Deep Research 6-쿼리 (57,609자 수집)
대표님 노트북 `a0bb9e88-b8cc-4a8d-a55a-75ffa01996eb` 소스 자료 기반 전 영역 지식 획득:
- Q1 인디 현실 + MVP + 게임 디자인 (7,152자)
- Q2 Unity 6 LTS 전부 (9,301자)
- Q3 게임 아트 2D/3D + AI 2026 (12,265자)
- Q4 게임 오디오 (9,665자)
- Q5 Steam + 마케팅 + 한국 인디 (12,182자)
- Q6 관리/멘털 + 법률(한국) + AI 2026 (7,044자)

**박제 완료**:
- `.planning/research/nlm_result_0{1..6}_*.md` — 6 원본 답변 보존
- `.planning/research/nlm_summary.md` — 상황 → 원본 1-hop 네비게이션
- `.claude/memory/reference_beginner_gamedev_knowledge.md` — 나베랄 감마 즉시 회수용
- `wiki/{design,engine,art,audio,gameplay,steam}/MOC.md` — 6 카테고리 전수 반영
- `scripts/notebooklm/{query.py,run_deep_research.py}` — UTF-8 패치 포함 runner

**실패 박제 (FAIL-001)**:
- `--timeout` 인자 미지원 (secondjob_naberal skill 버전 차이)
- library.json cp949 디코딩 실패 → PYTHONUTF8=1 강제 필요
- 미등록 notebook ID → `--notebook-url` full URL 우회
- Playwright 간헐적 rc=1 (Q4 1회) → 재실행으로 복구

**핵심 발견**:
- 14-Tool Arsenal (2026 1인 개발 프레임)
- MVP 이중 의미: Model-View-Presenter(코드) + Minimum Viable Product(제품)
- 30초·3분·30분 3-tier 핵심 루프
- Balatro/Animal Well/Vampire Survivors 공식: "독창적·직관적 코어 메커니즘 + 극대화된 게임성"
- AI Slop 방지: CLAUDE.md 로 AI 스코프·스타일 통제 (현재 CLAUDE.md 가 이 역할 수행)
- 한국 특수: W-8BEN 원천세 30%→10%, 홈택스 간이과세, BIC/PlayX4

**Git commit**:
```
70a4bf1 feat(research): NotebookLM deep research 6-query — 초보 1인 인디 게임 개발 전 영역 지식
```

---

## 대표님 결정 (세션 #1)

1. **장르 방향**: 복합 게임플레이 (로그라이크/시뮬/RPG) — 장기 창작 12~24개월
2. **플랫폼**: Steam PC
3. **엔진**: Unity 6 LTS (C#)
4. **시간 배분**: 미정 (Phase 2 에서 확정)

---

## 다음 세션 (Phase 1) 할 일

- [ ] `.planning/ROADMAP.md` 초안 작성 (10-phase 게임 개발 lifecycle)
- [ ] 장르 3 후보 비교 분석 → MVP 방향 확정 (`wiki/design/genre_choice.md`)
- [ ] 핵심 루프 30초·3분·30분 3-tier 초안 (`wiki/gameplay/core_loop_30s_3m_30m.md`)
- [ ] 시간 배분 결정 → Phase 2 일정 역산
- [ ] Unity 6 LTS 설치 + Steamworks 파트너 등록 계획

## 병행 작업 상태

- **studios/shorts**: Phase 10 "Sustained Operations" 진입 대기 (세션 #26 Entry Gate PASSED)
- **studios/estimator**: (별도 스튜디오, 본 작업 범위 외)

---

## 참고

- AI 도구 체인은 shorts 에서 검증됨 — `studios/shorts/docs/ARCHITECTURE.md §4` 재활용 가능
- 솔로 인디 성공 레퍼런스: Balatro (LocalThunk) · Animal Well (Billy Basso) · Vampire Survivors (poncle) — 모두 1인 Steam 히트
