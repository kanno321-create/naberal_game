---
name: 세션 #5 Q-FIX-X3·X4 대표님 결정 대기
description: 드리프트 재검증 중 추가 발견 2건. 욜로모드 자체 판단 보류. 대표님 기상 시 결정 요청.
type: project
originSessionId: b65e7d30-e464-4e53-91f0-bb98ede1035e
---
## 배경

세션 #5 Q-FIX 9 + 자체 해소 X1·X2 후 드리프트 재검증 중 추가 잠재 충돌 2건 발견. FAIL-002 빈자리 채우기 방지 원칙에 따라 욜로모드 범위 내이지만 **보수적으로 보류** · 대표님 기상 시 결정 요청.

## Q-FIX-X3: Oryn 왕세자 `Aldric Erevorn` 동명 충돌 [결정 대기]

- **파일**: `wiki/design/worldbuilding/elucia/kingdoms/kingdom_oryn/royals/crown_prince_aldric_erevorn_2026-04-22.md`
- **충돌**:
  - Vaelin 왕 `Aldric Vaen` (세션 #4 권위 원전)
  - Aldric 왕국 왕조 `King Aldric IV` (왕국·왕조명이라 무관)
  - Oryn 왕세자 `Aldric Erevorn` (이 이름이 새 충돌)
- **영향**: Ch.05+ 기사단·외교 서브플롯에서 Aldric 왕조의 Aldric IV 와 구분 혼란
- **추천안 (나베랄 감마)**: `Aldric Erevorn → Aldryk Erevorn` 또는 `Aldar Erevorn`
  - `Aldryk` = 음가 거의 일치 · Oryn 숲족 음운 Set (어두운 모음 + k 자음) 유지
- **왜 보류**: Q-FIX-X1, X2 는 대표님 결정 논리 (Q-FIX-5) 의 직접 연장이나, Oryn 왕세자는 세션 #4 당시 별도 생성물이라 대표님 시각 확인 필요

## Q-FIX-X4: 옛 Aldren Sellypha 1세 파일명 정리 [결정 대기]

- **파일**: `wiki/design/worldbuilding/elucia/kingdoms/kingdom_ceren/royals/previous_king_aldren_sellypha_first_2026-04-22.md`
- **상태**: 내용은 Q-FIX-X2 에 따라 `Aldren → Aedran` 치환된 것으로 추정 · **파일명만 구 Aldren 유지**
- **충돌**: 파일명 `aldren` 이 Thaloss 왕세자 Aldren 과 네임스페이스 공유
- **추천안**: 파일명 `previous_king_aldren_sellypha_first_2026-04-22.md → previous_king_aedran_sellypha_first_2026-04-22.md`
- **왜 보류**: 단순 mv 건이므로 대표님 기상 시 즉시 처리 가능. 지금 처리 시 다른 에이전트 (Wave 5) 가 이 파일을 참조 중일 수 있어 안전 우선.

## Drift 재검증 상태 (세션 #5, 2026-04-22)

| 대상 | 처리 결과 |
|------|---------|
| **Aldric 왕국명** | 유지 · 왕조·국가명 (정상) |
| **Aldric 왕조 `King Aldric IV`** | 유지 · 왕조명 동일 혈통 자연 (정상) |
| **Vaelin 왕 `Aldric Vaen`** | 유지 · Q-FIX-5 권위 원전 |
| **Thaloss 왕세자 `Aldric`** | ✅ Aldren 으로 개명 완료 |
| **Ilaris 왕 `Aldric Maeran`** | ✅ Aerric Maeran 으로 개명 완료 (X1) |
| **Oryn 왕세자 `Aldric Erevorn`** | ⏸ **Q-FIX-X3 결정 대기** |
| **Ceren 왕 `Aldren Sellypha II`** | ✅ Aedran Sellypha II 로 개명 완료 (X2) |
| **Ceren 선왕 `Aldren Sellypha I` 파일명** | ⏸ **Q-FIX-X4 결정 대기** |
| **Thaloss 공작 `Edric Varn`** | ✅ Edric Kaerv · House Kaerv 로 개명 완료 |
| **Aldric 공작 `House Seren`** | ✅ House Selyne 로 개명 완료 |
| **Novas 수도 `Duskmoor`** | ✅ Duskgate 로 치환 완료 |
| **교황 "반신적 존재"** | ✅ 공개 서술 제거 · 인용 주석화 완료 |

## Why

- Ch.01 LN 초안 완성 (Ashenveil 오프닝) — 이어지는 Ch.05+ 에서 Oryn 왕세자 본격 등장 전 X3 필수 해소
- X4 는 단순 파일명 정리 · 위험도 낮음

## How to apply

기상 시 대표님께 다음 3 선택지 제시:
- X3: 추천 `Aldryk Erevorn` 또는 다른 안 또는 유지
- X4: mv 실행 확인

## Related

- `project_session5_qfix_decisions.md`
- `project_session5_qfix_extended_x1_x2.md`
- FAIL-010 (병렬 fan-out 이름 공간 충돌 · 이 세 번째 잔재)
