---
name: 에이전트 spawning 시 설정 원전 필독 강제 + 인용 증명
description: 에이전트가 세계관 월드빌딩·집필 작업 시 반드시 brainstorm 원전·Rev.3 서사·CLAUDE·FAILURES 7종을 Read tool로 선독하고, 산출물 서두에 원문 인용 3줄+ 박제를 강제하는 규칙
type: feedback
originSessionId: a7033dcf-2d41-4bd0-950a-ba90de6fd9ad
---
# Rule
모든 서브에이전트 spawn 시 prompt 최상단에 **STEP 0 필독 블록** 을 박제한다. 7개 원전 파일을 Read tool로 선독하고, 산출물 서두에 각 파일로부터 3줄 이상 원문 인용 + 파일명:줄번호를 박제해야 한다. 인용 없는 산출물은 자동 반려.

**필독 7종 (고정 목록)**:
1. `wiki/design/brainstorm_2026-04-21_worldview_expansion.md` (3,146줄 · 50 발언 원전)
2. `wiki/design/brainstorm_2026-04-21.md` (903줄 · Rev.3 기준)
3. `wiki/design/game_setting_complete_2026-04-21.md` (630줄 · 통합 스냅샷)
4. `wiki/design/political_divisions.md` (150줄 · 26 정치단위 확정)
5. `wiki/design/story_full_narrative.md` (1,026줄 · Rev.3 서사)
6. `CLAUDE.md` (84줄 · 정체성·금기 9·필수 8)
7. `.claude/failures/FAILURES.md` (175줄 · FAIL-001~006 교훈)

**설정 불가침 영역** (briefing 공통 박제):
- Q-CORE 3건 (마왕↔할배·할배 동기·수정 2 기원) — 대표님+나베랄 결정, 에이전트 봉인
- 26 정치단위 (11 왕국 + 교황청 제국 + 동쪽 수도 + 14 자치구)
- 세계관 철학 3조 (불완전성·한결같음·영혼 평등)
- 50 발언 원전 인용 — 축약·요약·의역 금지
- 대표님 미확정 요소 (북쪽 얼음섬 내용물·수인족 외형·초고대문명 정체) 모호 보존

# Why
대표님 지시 (2026-04-22 세션 #4): *"에이전트가 작업할때 반드시 우리가 브레인스토밍으로 나눴던 정보들을 반드시 읽고 해라고해라, 안그럼 우리설정이랑 차이나버리면 곤란하다"* · *"핵심은 우리가 정한다"*

FAIL-002 / FAIL-004 / FAIL-006 재발 방지:
- FAIL-002: 대표님 발언 과해석 (Scene 2 동료 참살 → 한 문단 축약 이어야 할 것을 장문화 등 10건 집단 위반)
- FAIL-004: skill 수동 대기 (능동 호출 의무)
- FAIL-006: 원문 인용 축약·의역 (50 발언 원전 인용 시 반드시 원문 보존)

에이전트가 원전을 읽지 않고 기존 지식만으로 작업하면 설정 드리프트 발생 불가피. 인용 증명은 "읽었다" 자기 신고를 "읽은 증거" 물증으로 전환.

# How to apply
**Agent tool 호출 시**: prompt 필드 최상단에 다음 블록 박제:

```
═══════════════════════════════════════════════════
STEP 0 [우회 금지 · 위반 시 산출물 자동 반려]
═══════════════════════════════════════════════════

아래 7 파일을 Read tool 로 전부 읽은 후에만 작업 시작.

[필독 1] wiki/design/brainstorm_2026-04-21_worldview_expansion.md  (3,146줄)
[필독 2] wiki/design/brainstorm_2026-04-21.md                       (903줄)
[필독 3] wiki/design/game_setting_complete_2026-04-21.md            (630줄)
[필독 4] wiki/design/political_divisions.md                         (150줄)
[필독 5] wiki/design/story_full_narrative.md                        (1,026줄)
[필독 6] CLAUDE.md                                                  (84줄)
[필독 7] .claude/failures/FAILURES.md                               (175줄)

읽기 완료 증명: 산출물 서두 "## 원전 인용 증명" 섹션에
각 파일에서 네 작업 영역 관련 구간 3줄 이상 원문 인용 + 파일명:줄번호 박제.
═══════════════════════════════════════════════════

설정 불가침:
❌ Q-CORE 3건 건드리지 말 것 (마왕↔할배·할배 동기·수정 2 기원)
❌ 26 정치단위 추가·병합·삭제 금지
❌ 50 발언 원전 축약·요약·의역 금지
❌ 대표님 미확정 요소 채우지 말 것 (모호 보존)
✅ 왕국 내부 공작령·백작령·지명·도로·경제·문화 자율 재량
```

**모든 월드빌딩 에이전트 briefing 공통 적용**. 동쪽 대륙 Karzor 작업 시에도 재활용.
