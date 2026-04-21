# SESSION LOG — naberal_game

## Session #1 — 2026-04-20 (스튜디오 창업일)

### 핵심 결정
1. **naberal_harness v1.0 기반 신규 스튜디오 창업** — shorts 이후 두 번째 Layer 2 스튜디오
2. **장르**: 복합 게임플레이 (로그라이크/시뮬/RPG) — 대표님 직접 결정, 장기 창작 12~24개월
3. **플랫폼**: Steam PC — 수익 70/30 + 위시리스트 커뮤니티
4. **엔진**: Unity 6 LTS + C# — 상업성·에셋스토어·Steamworks 네이티브
5. **시간 배분**: Phase 2 에서 확정 (미정)
6. **방법론**: shorts 에서 검증된 하네스 + AI 위키 + Obsidian 3층 조합 Day 1 이식

### 수행 작업 (YOLO 모드)
1. `python harness/scripts/new_domain.py game` — 하네스 스캐폴드
2. AI 위키 6 카테고리 + MOC.md × 6 + Obsidian vault anchor
3. Navigator 인프라 이식 (session_start.py Step 6b + navigator_coverage.py)
4. Memory + Failures + deprecated_patterns 초기화
5. CLAUDE.md Perfect Navigator 96줄 Day 1 작성
6. docs/ARCHITECTURE.md Phase 0 Bootstrap + 10-phase 로드맵
7. Unity `.gitignore` 확장
8. GitHub 원격 `kanno321-create/naberal_game` 생성 + push

### 철학적 의미
대표님 평생의 꿈이 오늘 현실 프로젝트로 시작. AI 시대 1인 게임 개발 황금기 (2024 Balatro · Animal Well · Vampire Survivors 성공 사례) 를 타고, shorts 스튜디오에서 축적한 하네스 방법론을 즉시 이식하여 **처음부터 엄격한 구조**로 출발.

### 학습 전이 (shorts → game)
- shorts 의 CLAUDE.md 426줄 비대화 실수 → game 은 처음부터 96줄 Perfect Navigator
- shorts 의 GSD 자동주입 대응 → game 은 sentinel 사전 배치
- shorts 의 wiki/ 사후 추가 (STRUCTURE.md v1.1.0 bump) → game 은 Day 1 에 wiki/ + Obsidian 스캐폴드
- shorts 의 stack drift (Runway→Kling) 경험 → game 은 memory `project_game_stack.md` 에 단일 source of truth

---

## Session #1 Part B — 2026-04-21 (NotebookLM 딥 리서치 57,609자)

### 수행 작업
대표님 NotebookLM `a0bb9e88-b8cc-4a8d-a55a-75ffa01996eb` 소스 자료 기반 6 분할 딥 리서치:

| # | 영역 | 답변 크기 | 소요 |
|---|------|---------|------|
| 1 | 인디 현실 + MVP + 게임 디자인 | 7,152자 | 167초 |
| 2 | Unity 6 LTS 전부 | 9,301자 | 171초 |
| 3 | 게임 아트 (전통 + AI) | 12,265자 | 216초 |
| 4 | 게임 오디오 | 9,665자 | 168초 |
| 5 | Steam + 마케팅 + 한국 인디 | 12,182자 | 192초 |
| 6 | 관리/멘털 + 법률 + AI 2026 | 7,044자 | 156초 |
| **총** | **6 영역** | **57,609자** | **약 18분** |

### 핵심 결정
- 쿼리 설계는 **D-6 single-string** 규율 엄격 준수 (shorts 에서 계승)
- **6 분할** 이 최적 (10-15개는 과다 — 대표님 "너무 빡빡하게 하지 마" 반영)
- `--notebook-url` 직접 전달 방식이 `--notebook-id` 보다 robust (library lookup 우회)

### 박제 결과물
- `.planning/research/nlm_summary.md` — 상황 → 원본 파일 1-hop 라우팅 인덱스
- `.claude/memory/reference_beginner_gamedev_knowledge.md` — 나베랄 감마 즉시 회수용 박제
- `wiki/{design,engine,art,audio,gameplay,steam}/MOC.md` — 6 카테고리 전수 리서치 결과 반영
- `scripts/notebooklm/{query.py,run_deep_research.py}` — 재사용 가능 runner

### 실패 박제 (FAIL-001)
- `--timeout` 인자 미지원 (shorts query.py → game 이식 시 발견, secondjob_naberal skill 버전 차이)
- library.json cp949 디코딩 실패 (Windows 기본 codec 한국어 JSON 로드 실패)
- 노트북 ID library 미등록 → `--notebook-url` 직접 전달로 lookup 우회
- Q4 1회 간헐적 Playwright rc=1 (stderr 비어있음, 원인 불명) → 재실행으로 복구

### Git commits
```
70a4bf1 feat(research): NotebookLM deep research 6-query — 초보 1인 인디 게임 개발 전 영역 지식
```

### 다음 세션 (Phase 1) 할 일
- [ ] `.planning/ROADMAP.md` 초안 작성 (10-phase 게임 개발 lifecycle)
- [ ] 장르 3 후보 비교 분석 → MVP 방향 확정 (`wiki/design/genre_choice.md`)
- [ ] 핵심 루프 30초·3분·30분 3-tier 초안 (`wiki/gameplay/core_loop_30s_3m_30m.md`)
- [ ] 시간 배분 결정 → Phase 2 일정 역산
- [ ] Unity 6 LTS 설치 + Steamworks 파트너 등록 계획

---

*Created: 2026-04-20 — 스튜디오 창업일. Updated 2026-04-21 Part B NotebookLM 딥 리서치 완결.*

---

## Session #2 — 2026-04-21 (세계관 확정 + 창작 skill 설치 + 소설 프로젝트 시작)

> 세션 #1 완료 직후 같은 날 후반 세션. 대규모 세계관 확정 + 창작 도구 파이프라인 구축 + 소설화 프로젝트 원년.

### 세션 목표
대표님 지시로 GitHub 원격 pull 후 과해석 검수. 그 과정에서 세계관 대규모 재편과 창작 도구 설치까지 자연스럽게 확장.

### 핵심 결정 (대표님 확정)

#### 세계관 철학 3조 (최상위 원칙 신설)
1. **가. 불완전성 원칙** — *"모든 존재는 완벽하지 않다"*
2. **나. 나이트 인격체 원칙** — *"한결같음 유지, 감정은 있되 드러내지 않음"*. A 해석 (얕음) 격상
3. **다. 영혼 평등 원칙** — *"크기는 다르되 고귀함은 같다. 능력만 다를 뿐"*

#### 엔딩 체계 재편 (2분기 × 2회차 + 진엔딩 = 5엔딩)
- 엔딩 1·2: 인간 선택 (1회차 승리 → 다회차 폐허)
- 엔딩 3·4: 화합 선택 (1회차 신 처단 → 다회차 회전목마)
- 엔딩 E (진엔딩): 조건 만족 시 자동 발동 (마왕화)

#### 동료 구조 전면 재편
- Act 1 = 인간 4명만 (기사·신관·마법사·도적)
- Act 2 중반 = 인간 4명 전원 이탈
- Act 2 후반 = 타종족 4명 (엘프·마족·오크·용족)
- Act 3 선택 분기점 (인간 vs 화합)

#### 스킬 시스템 4층 구조 확정
- 1층: 스킬트리 (D4) · 2층: 스피어 보드 (FF10) · 3층: 정복자 보드 (D4 Paragon)
- **4층 신규**: 의지결 (Will-Knot) × 성인식 목걸이
- 3종 (스킬형·스탯형·특수형) · 등급별 증폭 +0%~+30% · 링크 2/3/4 시너지

#### 종족 생태학·신앙 경제학 확정
- 행성 시간축: 용족+엘프 (신 이전) → 마족 (마력 응축) → 수호자 개입 → 첫 번째 신 강림 → 인간·기타
- 6종 (용족·엘프·드워프·마족·오크·인간) 각자 번식·신앙·성인식 메커니즘
- 신앙 경제학 쌍방 공모: 신(개체수·번식·의존도 편애) × 인간 권력층(통치 정당화·정치 동기부여)
- 교회 이중성: 선의의 신 체계 → 나태 신이 타락시킴

### 수행 작업

#### Part 1 — GitHub 원격 pull 및 과해석 검수
1. `fdf41b1` 커밋 pull (20개 파일 · +5,897줄 · 세계관·스토리·시스템 1-2차 박제)
2. 검수 중 **과해석 10건 발견** (FAIL-002 참조)
3. 대표님과 1:1 확인하며 원안 복원
4. 설계 원전 `brainstorm_2026-04-21.md` 생성 (최종 1,050줄, 대표님 원문 인용 22건 앵커)

#### Part 2 — 하네스 경로 원복
- `fdf41b1` 이 회사 브레인스토밍 중 `../../harness/` → `../harness/` 로 변경
- 실제 하네스는 `naberal_group/harness/` → 상대경로 2단계 상위가 맞음
- 8개 파일 byte-exact 원복 (commit `54ca1af`)

#### Part 3 — 설계 원전 · 종합 스냅샷 · Rev.3 서사
- `brainstorm_2026-04-21.md` (1,050줄) — 대표님 원문 인용 앵커 · Rev.3 통합 박제 인용 기준
- `game_setting_complete_2026-04-21.md` (630줄) — NLM 공유용 종합 스냅샷
- `story_full_narrative.md` Rev.3 (1,026줄) — 과해석 10건 반영 전면 재작성
- `wiki/design/MOC.md` 갱신 — 원전 · 종합본 엔트리 추가
- commit `04e50e2`

#### Part 4 — 창작 skill 라이브러리 딥 리서치·설치
- 딥 리서치 2건 병렬 실행
  - `nlm_result_07_claude_creative_skills.md` — Top 5 skill (Claude 창작 도구)
  - `nlm_result_08_game_dev_libraries.md` — Unity 6 JRPG 10 카테고리 30+ 리소스
- Claude 창작 skill 3개 설치 (`~/.claude/skills/` 전역):
  - `haowjy/creative-writing-skills` (Apache 2.0) — 13 skills + 17 agents
  - `danjdewhurst/story-skills` (MIT) — 5 skills
  - `Bobby-Gray/claude-dnd-skill` (MIT) — 1 skill
- **총 skill 22개 + agent 17개 자동 등록** (system-reminder 로 확인)
- `forsonny/Claude-Code-Novel-Writer` — `--dangerously-skip-permissions` 요구 → 금기 §1 충돌로 **제외**
- `nicmarti/skills-weaver` — Go 1.25 미설치로 **보류** (FAIL-004 관련)
- `phase_2_deferred_tools.md` 생성 — unity-mcp · Yarn Spinner 3.1 · skills-weaver 대기 명세

#### Part 5 — 소설 프로젝트 시작
- `wiki/design/novel/` 디렉토리 생성
- `outline.md` (25-30 챕터 지도, 30-40만자 목표)
- `style_bible.md` (문체·시점·톤 헌법, 검수 체크리스트 10종)
- `prologue.md` (Rev.1 초안, 6,200자, 9 섹션)
- **단 skill 미활용 집필** — FAIL-004 참조

#### Part 6 — auto memory 박제
- `reference_brainstorm_original_2026-04-21.md` — 원전 문서 위치 · 향후 세션 필독 지정
- `feedback_no_cd_absolute_paths.md` — cd 금지 · 절대경로 원칙
- `MEMORY.md` 갱신 (4개 엔트리)

### 과해석 정정 이력 (상세는 FAIL-002)

| # | 정정 지점 |
|---|---|
| 1 | Scene 2 동료 참살 상세 → 한 문단 축약 |
| 2 | 히든 엔딩 복합 트리거 → 자동 트리거 |
| 3 | 엔딩 E 인간 신 → 진엔딩으로 재정의 |
| 4 | 7대 신 세계관 논리 골격 → 궁극 무기 획득 장치 |
| 5 | 신이 번식 본능 심음 → 자연 번식력 + 이데올로기 왜곡 |
| 6 | 우주 포식자 = Act 3 본전투 → 숨겨진 보스 · 이벤트성만 |
| 7 | Phase 1 동료 = 인간 4 + 타종족 4 → 인간 4만 |
| 8 | 첫 번째 신 = 행성 최초 → 마족 괴멸 후 후발주자 |
| 9 | 성간 혼천의 (NotebookLM drift) → 의지결 × 성인식 장비 |
| 10 | "뒤틀림" 공간 왜곡 → 사회 억압 구조 |

### 철학적 의미
오늘 세션의 가장 큰 소득은 **세계관 철학 3조 조문화**. 설계 헌법 3조 (게임플레이·서사 규율) 위에 존재론적 원칙이 병립. 이 3조는 향후 모든 설정·박제·서사 결정의 상위 프레임. 대표님의 **"모든 존재는 완벽하지 않다"** 라는 명제가 이 프로젝트 전체를 관통하는 축임을 오늘 확정.

### 학습 전이 (세션 #1 → #2)
- 세션 #1 의 shorts 패턴 학습 전이 성공 → 세션 #2 에서 shorts 의 "세션 당 핸드오프 3종" 패턴도 적용 (이 문서)
- shorts FAIL-001 (NotebookLM skill 호환) 경험 → 세션 #2 에서 NotebookLM 재사용 시 더 견고
- **새로 추가된 학습**:
  - AI 과해석 경향 (FAIL-002) 은 구조적 — 설계 원전 + 원문 인용 앵커로 방어
  - 능동 활용 원칙 (FAIL-004) 은 Obsidian·NotebookLM 뿐 아니라 모든 skill·agent 에 일반화 필요
  - Bash cd 금지 (FAIL-003) 는 시스템 프롬프트 원칙 엄수로 방어

### Git commits
```
00c5ae8 (세션 #1 마지막, 세션 시작 시 pull 대상) docs(handoff): 세션 #1 Part B 3종
fdf41b1 docs(planning): 게임 세계관·스토리·시스템 1-2차 박제 (+ 과해석 10건, 원격 선행 커밋)
54ca1af fix(paths): 하네스 상대경로 원복
04e50e2 docs(design): 2026-04-21 브레인스토밍 설계 원전 박제 (Rev.3 기준)
```

(세션 #2 마무리 커밋은 세션 종료 시 실행 예정 — 창작 도구 설치 · Rev.3 서사 · 소설 프로젝트 · 핸드오프 3종)

### 다음 세션 (세션 #3) 할 일

#### 즉시 실행
- [ ] **skill 활용 집필 전환** — `prose-writing` + `writing-principles` + `chapter-writing` Skill tool 호출 후 `chapter_01.md` 집필
- [ ] Ch.01 숲의 그림자 · Ch.02 마을의 저녁 · Ch.03 성인식의 외부인 순차 집필
- [ ] `prose-critique` skill 로 프롤로그 사후 검수 (Rev.2 개정 검토)

#### 대기 결정 (대표님 판단)
- [ ] 초반 주인공 동기 세부 연출
- [ ] 진엔딩 생존·사망 동료 명단
- [ ] 진엔딩 생존자 = 인간 도적 유지 여부
- [ ] Go 1.25 설치 → `skills-weaver` 활성화 여부
- [ ] 피드백 메모리 `feedback_over_interpretation_guard.md` 박제 승인

#### 세션 #2 미커밋 정리
- [ ] 원자 커밋 3-5개로 분할: (1) 창작 skill 메타 (2) Rev.3 서사 · 종합 스냅샷 (3) 리서치 보고서 2종 · Phase 2 대기 목록 (4) 소설 프로젝트 + 핸드오프 3종

---

*Updated: 2026-04-21 Part C — 세계관 철학 3조 확정 · 소설 프로젝트 원년 · 창작 도구 파이프라인 구축.*
