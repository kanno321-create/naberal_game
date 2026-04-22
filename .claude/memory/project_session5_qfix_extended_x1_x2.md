---
name: 세션 #5 드리프트 재검증 중 자체 해소 Q-FIX-X1 · X2
description: 세션 #5 Q-FIX-8 처리 중 발견한 추가 동명 충돌 2건. 대표님 욜로모드 위임 기반 자체 판단 수정. Aldric/Aldren 이름 공간 정리 완료.
type: project
originSessionId: b65e7d30-e464-4e53-91f0-bb98ede1035e
---
세션 #4 audit 에서 놓친 동명 충돌 2건을 세션 #5 드리프트 검증 중 발견 · 욜로모드 위임 기반으로 자체 해소.

## Q-FIX-X1: Ilaris 왕 `Aldric Maeran` vs Vaelin 왕 `Aldric Vaen`

- **충돌**: 두 왕국의 현 왕 이름이 동일 `Aldric`
- **우선 순위**: Vaelin 왕 `Aldric Vaen` = 세션 #4 핵심 권위 원전 · Ilaris 왕 `Aldric Maeran` = 하위 생성
- **해소**: Ilaris 왕 `Aldric Maeran → Aerric Maeran` (한글 `알드릭 마에란 → 에릭 마에란`)
- **파일명**: `king_aldric_maeran_2026-04-22.md → king_aerric_maeran_2026-04-22.md`
- **근거**: 
  - 음가 인접 (Al-dric ↔ Aer-ric) · 독자 기억 부담 최소
  - Ilaris 음운 Set (해양·상인 · 부드러운 rhotic) 와 조화
  - 세션 #5 Q-FIX-5 (Thaloss 왕세자 `Aldric→Aldren`) 논리 확장

## Q-FIX-X2: Ceren 왕 `Aldren Sellypha II` vs Thaloss 왕세자 `Aldren`

- **충돌**: 세션 #5 Q-FIX-5 로 Thaloss 왕세자를 `Aldren` 으로 개명했으나 Ceren 왕 이름도 이미 `Aldren Sellypha II`
- **우선 순위**: 대표님 세션 #5 직접 지정 (Thaloss 왕세자 Aldren) = 상위 권위 · Ceren 왕은 세션 #4 후속 생성
- **해소**: Ceren 왕 `Aldren Sellypha II → Aedran Sellypha II` (한글 `알드렌 셀리파 2세 → 에드란 셀리파 2세`)
- **파일명**: `king_aldren_sellypha_2026-04-22.md → king_aedran_sellypha_2026-04-22.md`
- **근거**:
  - 음가 인접 (Al-dren ↔ Aed-ran) · 독자 기억 부담 최소
  - Ceren 음운 Set (습지·부드러운 자음) 와 조화
  - 선왕 `Aldren 1세 → Aedran 1세` 도 연동 개명

## Why

- Ch.01 LN 본격 집필 이전 인명 충돌 완전 해소 필수
- FAIL-010 (병렬 fan-out 이름 공간 충돌) 의 후속 잔재 정리
- 세션 #4 audit 이 놓친 2건을 세션 #5 에서 전수 해소

## How to apply

- 이후 모든 에이전트는 이 두 인물을 새 이름으로만 호칭
- 기존 `Aldric Maeran`, `Aldren Sellypha` 참조는 전부 새 이름으로 업데이트
- 세션 #5 드리프트 재검증에 이 두 옛 이름도 포함

## 욜로모드 자체 판단 근거

- 대표님 원문 (세션 #5 취침 직전): "퍼미션 허락받는거 안물어보고 끝내기가능?" · "서부대륙은 너가 추천하는걸로 모두 정하면되는데"
- 이 두 충돌은 Ch.01 집필 게이트 차단 요인이므로 즉시 해소 필요
- 대표님 Q-FIX-5 결정 논리 (더 오래된 권위가 이름 유지 · 신규 생성 쪽이 양보) 를 기계적 확장 적용
- 기상 시 보고하여 이의 없으면 확정, 이의 있으면 재지정 가능

## Related

- `project_session5_qfix_decisions.md` — Q-FIX 1~9 원문
- `project_session5_yolo_mode_authorization.md` — 욜로모드 위임 범위
- FAIL-010 (병렬 fan-out 이름 공간 충돌)
