---
name: 세션 #5 Q-FIX 10건 결정 박제
description: 2026-04-22 세션 #5 대표님 10건 일괄 결정 원문. Q-FIX 1~9 + 주인공 마을. Wave 5 진입 게이트 해소.
type: project
originSessionId: b65e7d30-e464-4e53-91f0-bb98ede1035e
---
세션 #5 착수 시 대표님이 일괄 결정한 10건 — 원문 그대로 박제.

## A 계열 (Ch.01 직결)

**A-1 주인공 마을**: `Ashenveil` 확정
- Silvan 서쪽 끝 안개 잦은 저지대 · 인구 150~200 · 마왕군 첫 출현 지점으로 안개 설정 직결
- 위치: `wiki/design/worldbuilding/elucia/toponymy/protagonist_village_candidates_2026-04-22.md`

**A-2 Aldric 동명 해소**: `Thaloss 왕세자 개명 Aldren`
- Aldric 왕(Vaelin) 유지 · Thaloss 왕세자 `Aldric → Aldren`
- 원문: "Thaloss 왕세자 개명 Aldren"

## B 계열 (구조 정합성)

**B-1 Edric 공작 동명 해소**: `Thaloss 공작 성 Kaerv`
- Vaelin 공작 `Edric Vaen` 유지 · Thaloss 공작 `Edric Varn → Edric Kaerv`
- 원문: "haloss 공작 성 Kaerv" (대표님 오타: Thaloss)

**B-2 교황 "반신적" 표현**: `완전 삭제 + 최고 권위자 황제와 동급`
- 원문: "a 삭제 그냥 최고의 권위자 황제와 동급"
- 의미: "반신" 같은 신격 표현 전부 삭제 · 교황은 **황제와 동등한 최고 권위자** 로 재정의
- Q-CORE 2 (할배 자기 정체 은닉) 원칙 준수 · 세계 내부에 "반신" 개념 자체가 존재 X
- 교황의 위상: 세속 제국 = 황제 · 종교 제국 = 교황 (두 권위가 제국 공동 통치 구조)

**B-3 소금 충돌 해결**: `c 분쟁 구조화`
- Coastfen(Aldric) 해염 생산 vs Ceren 소금 독점을 **실제 왕국 간 분쟁** 으로 서사화
- Aldric ↔ Ceren 외교 긴장 생성 · Wave 3 Diplomat 산출물과 통합 · Ch.05+ 정치 서브플롯 재료

**B-4 Seren/Ceren 동음**: `House Selyne`
- Aldric 가문 `House Seren → House Selyne`
- Aldric 왕국 음운 Set "Sel-" 계열 유지

## C 계열 (세부)

**C-1 Mirvane Port**: `전수 충돌 회피` (= 개별 파일 생성)
- `ports/00_overview` 에 언급된 Mirvane Port 의 실체 파일을 다른 10 항구와 동일 수준으로 생성

**C-2 Soranwatch/Soranth 접두 중복**: `유지`
- 개명 없음 · 실제 대륙 지명 중복 흔함

**C-3 Solaris 왕도 지구 수**: `12 구획`
- 성좌국 12 신 수와 상징 대응 · 의례 정합성

**C-4 Novas 수도**: `Duskgate`
- Wave 4 산출 `Duskmoor` → 원전 `Duskgate` 로 복원

## Why

- Wave 5 (Chronicler + World-Integrator) 진입 게이트 해소
- Ch.01 LN 본격 집필 사전 조건 확보 (주인공 마을 Ashenveil + 왕/왕세자 동명 해소)
- 868 파일 월드빌딩 산출물의 마지막 드리프트 정리

## How to apply

- Q-FIX 수정 에이전트 스폰 시 이 파일이 **권위 원전**. 다른 해석 금지.
- 기존 이름 → 새 이름 매핑:
  - `Aldric` (Thaloss 왕세자 컨텍스트) → `Aldren`
  - `Edric Varn` (Thaloss 공작) → `Edric Kaerv`
  - `House Seren` (Aldric 가문) → `House Selyne`
  - `Duskmoor` (Novas 수도) → `Duskgate`
  - 교황 관련 "반신적", "demi-god", "semi-divine" 류 표현 → "황제와 동급의 최고 권위자"
- 수정 후 드리프트 재검증: 옛 이름 grep = 0 건이어야 종료.

## Related

- `WORK_HANDOFF.md` 세션 #4 섹션 "대기 (Q-FIX 9건)"
- `wiki/design/worldbuilding/elucia/toponymy/protagonist_village_candidates_2026-04-22.md`
- FAIL-010 (병렬 fan-out 이름 공간 충돌) — 이번 10 결정이 정면 대응
