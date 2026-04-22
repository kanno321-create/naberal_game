# FAILURES Index — naberal_game

> Category-tagging index across `FAILURES.md` (append-only).
>
> **D-11 invariant** (shorts 승계): 이 파일은 derivative index; Hook 은 이 파일 수정 허용 (FAILURES.md basename 만 append-only).

## Index by Category

### Planning / Structure (A-tier)
- (없음 — Phase 1+ 누적 예정)

### Design / Scope (B-tier)
- (없음)

### Engine / Unity (B-tier)
- (없음)

### Art / Audio (C-tier)
- (없음)

### Steam / Publishing (C-tier)
- (없음)

### Phase 0+ Entries
- See FAIL-001 in FAILURES.md — NotebookLM skill 호환 패치
- See FAIL-002 in FAILURES.md — AI 과해석 10건 집단 발생
- See FAIL-003 in FAILURES.md — Bash cd 로 작업 디렉토리 이동 (1차)
- See FAIL-004 in FAILURES.md — 설치한 창작 skill 미활용
- See FAIL-005 in FAILURES.md — Bash cd 재발 (2차)
- See FAIL-006 in FAILURES.md — FAIL-002 과해석 재발 4건
- See FAIL-007 in FAILURES.md — `hal_bae` 파일명 Q-CORE 2 봉인 위반
- See FAIL-008 in FAILURES.md — Q-CORE 원문 공개 산출물 박제 역설
- See FAIL-009 in FAILURES.md — 자기 정정 5회 연속 · 대표님 결정 전 예단
- See FAIL-010 in FAILURES.md — 병렬 fan-out 왕국 간 이름 공간 충돌
- See FAIL-011 in FAILURES.md — Bash cd 3회 재발
- See FAIL-012 in FAILURES.md — 세션 #4 audit 가 놓친 Aldric 동명 충돌
- See FAIL-013 in FAILURES.md — 세션 #5 POV 시점 충돌 Ch.01 직전 발견
- **See FAIL-014 in FAILURES.md — style_bible v2 §5-2 "~다 70%+" 하한 설계 미스 (세션 #6)**
- **See FAIL-015 in FAILURES.md — style_bible v1 Act 1 = 1인칭 규정 위반 3인칭 샘플 작성 (세션 #6)**
- **See FAIL-016 in FAILURES.md — 샘플링 독서로 나이트 Canon 반복 재질문 · 세션 간 영속성 실패 (세션 #7)**
- **See FAIL-017 in FAILURES.md — 세션 #7 영속 앵커 #3 자체가 이중 박제 미적용으로 구조적 무력화 (세션 #8)**

## Sources

- `FAILURES.md` — append-only log (Hook 강제)

## Update Protocol

1. 신규 FAIL 엔트리를 `FAILURES.md` 에 append (Hook 강제)
2. 엔트리에서 카테고리 키워드 추출
3. 이 파일의 해당 `### <Category>` heading 아래 bullet 추가
4. Bullet format: `- See FAIL-NNN in FAILURES.md`

---

*Scaffolded: 2026-04-20 (Phase 0 Bootstrap)*
