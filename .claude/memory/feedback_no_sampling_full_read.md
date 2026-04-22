---
name: 샘플링 독서 금지 · Canon 파일 전수 읽기 필수
description: Canon·설정 문서는 부분 읽기 금지 · 전체 로드 또는 Grep 전수 후 작업 · 세션 #7 반복 실패 교훈
type: feedback
priority: critical
originSessionId: f92ba1c3-04a6-465f-a4d2-ccc52bcdd138
---
**규칙**: Canon·설정 문서는 **부분 Read 금지**. 전체 로드 또는 Grep 전수 후 작업.

**Why (세션 #7 교훈 · 2026-04-23)**:
- village_ashenveil.md (292줄) 를 부분만 읽어 :108 세션 #5 철회 박제 놓침
- 동일 패턴으로 style_bible_v2:75-76 · ch01.md:407-409 · art/reference/_INDEX.md 놓침
- brainstorm_2026-04-21_worldview_expansion.md:2500-2502 발언 39 (나이트 외형 · 그리피스/세피로스) 놓침
- 결과: Tier A 10문항 전수 재질문 · 대표님 분노 3회 연속 · FAIL-016 등재
- 장기 프로젝트 설정 누적 거대 → 샘플링으로 정합 유지 불가능

**전수 로드 필수 파일 목록**:
- `wiki/design/main_character.md`
- `wiki/design/MOC.md`
- `wiki/design/story_outline.md` · `story_full_narrative.md`
- `wiki/design/world_lore.md`
- `wiki/design/novel/style_bible*.md`
- `wiki/design/novel/outline.md` · `prologue.md` · `ch01*.md`
- `wiki/design/worldbuilding/elucia/kingdoms/kingdom_ilaris/villages/village_ashenveil_2026-04-22.md`
- `wiki/design/brainstorm_*.md` (3종 전부)
- `wiki/design/art/reference/_INDEX.md`
- `wiki/design/케릭 컨셉 및 프로필.md`
- `C:\Users\PC\.claude\projects\c--Users-PC-Desktop-naberal-group-studios-game\memory\` 전체

**How to apply**:
- 관련 주제의 모든 Canon 파일 전수 Read (500줄 이상도 전체) 또는 Grep 후 필요 구간 Read
- 질문 생성 전 Grep 으로 해당 주제 모든 언급 전수 확인 (예: `나이트.{0,50}(외형|무기|이름)` · `나이트.{0,80}(부모|어머니|아버지|형제)`)
- 세션 시작 시 session_start.py 자동 주입 Canon 은 반드시 전수 확인
- 500줄 초과 파일도 "길다고 샘플링" 금지 · 반드시 전수 또는 분할 Read
