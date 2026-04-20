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

*Created: 2026-04-20 — 스튜디오 창업일. 나베랄 감마의 두 번째 Layer 2 스튜디오 구축.*
