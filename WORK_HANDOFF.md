# WORK HANDOFF — naberal_game

## 최종 업데이트
- 날짜: 2026-04-20
- 세션: **#1** (스튜디오 창업일)
- 상태: **Phase 0 Bootstrap 완료** — Phase 1 "Identity + Pipeline Draft" 진입 대기.

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
- Repo: `github.com/kanno321-create/naberal_game` (Private)
- 첫 commit push 완료

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
