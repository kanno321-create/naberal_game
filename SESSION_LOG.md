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
