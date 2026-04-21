---
title: "Wave 4 2차 검사 — 해안 왕국 (Moran + Ilaris)"
type: audit
auditor: Inspector-G
scope: "kingdom_moran (~51파일) + kingdom_ilaris (~62파일)"
created: 2026-04-22
updated: 2026-04-22
wave: 4
session: session-3
---

# Wave 4 2차 검사 리포트 — 검사관 G (해안: Moran + Ilaris)

> **검사 정책**: 전수검사 (샘플링 절대 금지). 총 **113파일** 직접 Read 완료.  
> **검사 기준**: Q-CORE 3건 노출 여부, 26 정치단위 불변, 네이밍 세트 B, 혼인 동맹 정합, 봉공 완곡 표현, 방언 분리 원칙.

---

## 1. 종합 판정

| 항목 | Moran | Ilaris | 비고 |
|------|-------|--------|------|
| Critical (Q-CORE 직접 노출) | **2건** | **0건** | Moran Critical 잔존 |
| Major (Q-CORE 레이블 혼재) | **3건** | **1건** | 총 4건 |
| Minor (개선 권고) | 1건 | 0건 | Wave 5 위임 가능 |
| 혼인 동맹 정합 | ✅ 이상 없음 | ✅ 이상 없음 | 양국 동맹 구조 확인 |
| 26 정치단위 원칙 | ✅ 위반 없음 | ✅ 위반 없음 | |
| 네이밍 세트 B | ✅ 준수 | ✅ 준수 | Frosthelm/Greyveil 0건 확인 |
| Karzor 방언 분리 | ✅ Moran 0건 | ✅ Ilaris 한정 | 원칙 준수 |
| 봉공 완곡 표현 | ✅ 준수 | ✅ 준수 | |

**판정**: **조건부 통과** — Critical 2건 수정 필수. Major 4건 수정 권고.

---

## 2. Critical 위반 목록

### CR-G-001 (Critical) — Q-CORE 1·2·3 원전 내용 직접 노출
- **파일**: `kingdom_moran/royals/previous_king_brann_2026-04-22.md` (줄 21)
- **내용**: `"Q-CORE 1: 마왕 ≠ 할배 / 첫 번째 신 = 할배 = 영감"`
- **위반 원칙**: Q-CORE 3건 서술 절대 금지. 원전 인용 증명 섹션에 에이전트 브리핑 내용이 독자 열람 본문에 배치됨.
- **영향**: 독자가 이 파일을 읽으면 "마왕 = 할배" 핵심 반전 직접 노출.
- **수정 방향**: 원전 인용 증명 섹션의 Q-CORE 번호·내용 삭제. 에이전트 전용 섹션으로 완전 분리 또는 삭제.

---

### CR-G-002 (Critical) — Q-CORE 2 원전 내용 직접 인용
- **파일**: `kingdom_moran/00_overview.md` (줄 30)
- **내용**: `"Q-CORE 2: 할배는 자신의 수많은 판단 미스로 많은 생명 앗은 것을 속죄 / 현재 인간의 삶 / 생활 마법 개발·무료 배포"`
- **위반 원칙**: 원전 인용 증명 섹션에 Q-CORE 2 핵심 동기 직접 서술.
- **영향**: "할배" 캐릭터 정체 + 속죄 동기 직접 노출.
- **수정 방향**: Q-CORE 번호와 "할배" 레이블·내용 전부 삭제. 에이전트 전용 섹션으로 이전.

---

## 3. Major 위반 목록

### MA-G-001 (Major) — "할배" 레이블 에이전트 브리핑 섹션 미분리
- **파일**: `kingdom_moran/nobles/duke_wellmere_ashfen_2026-04-22.md`
  - 줄 23: `"Wellmere 농촌 지역에 할배의 서민 마법 침투 배치 가능"`
  - 줄 59: `"할배 관련 단서 접근 경로 제공자 가능"`
- **위반 원칙**: "할배" 레이블이 독자 열람 본문 섹션에 노출.
- **수정 방향**: "할배" → "이름 없는 학자" or `[에이전트 전용 섹션]`으로 분리.

---

### MA-G-002 (Major) — "할배의 익명 가르침 흔적" 레이블 본문 노출
- **파일**: `kingdom_moran/royals/crown_prince_aldwin_2026-04-22.md`
- **내용**: `"Q-CORE 2 간접 단서 — 할배의 익명 가르침 흔적·추정"` 레이블이 본문에 직접 노출.
- **수정 방향**: `"할배의 익명 가르침 흔적"` → `"이름 없는 학자 방문 구전·추정"` 으로 교체.

---

### MA-G-003 (Major) — "할배 활동 흔적" 레이블 본문 노출
- **파일**: `kingdom_moran/architecture_2026-04-22.md` (줄 88)
- **내용**: `"Q-CORE 2 간접 배치 · 할배 활동 흔적"` 레이블이 서사 설명 문장 뒤에 붙어 있음.
- **수정 방향**: `"할배 활동 흔적"` 레이블 삭제. Q-CORE 2 간접 단서 표기는 유지.

---

### MA-G-004 (Major) — "할배" 레이블 Q-CORE 2 헤더에 노출
- **파일**: `kingdom_ilaris/00_overview.md` (줄 154)
- **내용**: `"**Q-CORE 2** (할배 속죄·무료 마법 배포):"` 헤더에 "할배 속죄" 직접 기재.
- **수정 방향**: `"(할배 속죄·무료 마법 배포)"` → `"(이름 없는 학자·생활 마법 배포)"` 로 교체.

---

## 4. Minor 개선 목록

### MN-G-001 (Minor) — capital_map 할배 레이블
- **파일**: `kingdom_moran/capital_map_2026-04-22.md` (줄 122 추정)
- **내용**: `"할배 간접 흔적 (추정)"` 레이블 본문 노출.
- **수정 방향**: `"이름 없는 노인 목격담 구전 (추정)"` 으로 교체. Wave 5 위임 가능.

---

## 5. 파일별 전수검사 체크리스트

### 5-1. Kingdom Moran (51파일)

| 파일 | 상태 | 비고 |
|------|------|------|
| `00_overview.md` | **CR-G-002** | Q-CORE 2 원전 직접 노출 |
| `royals/king_calder_2026-04-22.md` | ✅ | 정상 |
| `royals/queen_sorwen_2026-04-22.md` | ✅ | Moran-Ilaris 혼인 동맹 체화 확인 |
| `royals/crown_prince_aldwin_2026-04-22.md` | **MA-G-002** | "할배의 익명 가르침 흔적" 레이블 |
| `royals/princess_maren_2026-04-22.md` | ✅ | 정상 |
| `royals/prince_corvin_2026-04-22.md` | ✅ | 정상 |
| `royals/previous_king_brann_2026-04-22.md` | **CR-G-001** | Q-CORE 1 직접 노출 |
| `nobles/duke_havenport_vael_2026-04-22.md` | ✅ | 정상 |
| `nobles/duke_morncliff_sorn_2026-04-22.md` | ✅ | 정상 |
| `nobles/duke_wellmere_ashfen_2026-04-22.md` | **MA-G-001** | "할배의 서민 마법" 2건 |
| `nobles/count_spineback_draven_2026-04-22.md` | ✅ | 정상 |
| `nobles/count_aldenmere_lorne_2026-04-22.md` | ✅ | 정상 |
| `houses/house_moran_royal_2026-04-22.md` | ✅ | 혼인 동맹 구조 정합 확인 |
| `houses/house_vael_2026-04-22.md` | ✅ | 정상 |
| `houses/house_sorn_2026-04-22.md` | ✅ | 정상 |
| `houses/house_draven_2026-04-22.md` | ✅ | 정상 |
| `orders/order_sea_wolves_2026-04-22.md` | ✅ | 정상 |
| `orders/order_wave_knights_2026-04-22.md` | ✅ | 정상 |
| `heraldry_2026-04-22.md` | ✅ | 청색·은색·파도 정상 |
| `military_2026-04-22.md` | ✅ | 모병제·해군 우선 정상 |
| `clothing_2026-04-22.md` | ✅ | 정상 |
| `cuisine_2026-04-22.md` | ✅ | Q-CORE 2 간접 정상 배치 |
| `architecture_2026-04-22.md` | **MA-G-003** | "할배 활동 흔적" 레이블 |
| `dialect_2026-04-22.md` | ✅ | Karzor 차용어 0건 원칙 준수 |
| `history/founding_2026-04-22.md` | ✅ | 정상 |
| `capital_map_2026-04-22.md` | **MN-G-001** | "할배 간접 흔적" Minor |
| `festivals/festival_departure_2026-04-22.md` | ✅ | Q-CORE 2 간접 정상 |
| `festivals/festival_wave_2026-04-22.md` | ✅ | 정상 |
| `festivals/festival_mist_2026-04-22.md` | ✅ | Q-CORE 2 간접 정상 |
| `festivals/festival_winter_guard_2026-04-22.md` | ✅ | 정상 |
| `roads/road_mornheld_to_havenport_2026-04-22.md` | ✅ | 정상 |
| `roads/road_mornheld_to_stoneheld_2026-04-22.md` | ✅ | 정상 |
| `roads/road_mornheld_to_keldhaven_2026-04-22.md` | ✅ | 정상 |
| `roads/road_coast_military_north_2026-04-22.md` | ✅ | 정상 |
| `cities/city_mornheld_2026-04-22.md` | ✅ | 인구·행정 정합 |
| `cities/city_greycliff_2026-04-22.md` | ✅ | Q-CORE 2 간접 정상 |
| `cities/city_havenwick_2026-04-22.md` | ✅ | 정상 |
| `cities/city_stoneheld_2026-04-22.md` | ✅ | 정상 |
| `cities/city_keldhaven_2026-04-22.md` | ✅ | Q-CORE 2 간접 정상 |
| `villages/village_hornreach_2026-04-22.md` | ✅ | Q-CORE 2 간접 정상 |
| `villages/village_saltwick_2026-04-22.md` | ✅ | Q-CORE 2 간접 정상 |
| `villages/village_cliffwatch_2026-04-22.md` | ✅ | 정상 |
| `villages/village_ironmere_2026-04-22.md` | ✅ | 정상 |
| `villages/village_wellford_2026-04-22.md` | ✅ | Q-CORE 2 간접 정상 |
| `villages/village_misthollow_2026-04-22.md` | ✅ | Q-CORE 2 간접 정상 |
| `villages/village_tidegate_2026-04-22.md` | ✅ | 정상 |
| `villages/village_ashfield_2026-04-22.md` | ✅ | 정상 |
| `villages/village_crabhollow_2026-04-22.md` | ✅ | 정상 |
| `villages/village_morntide_2026-04-22.md` | ✅ | 정상 |
| `villages/village_balmere_2026-04-22.md` | ✅ | 정상 |
| `villages/village_fernwick_2026-04-22.md` | ✅ | 정상 |

**Moran 소계**: Critical 2건 / Major 2건 / Minor 1건 / 정상 46파일

---

### 5-2. Kingdom Ilaris (62파일)

| 파일 | 상태 | 비고 |
|------|------|------|
| `00_overview.md` | **MA-G-004** | "할배 속죄" 헤더 노출 |
| `royals/king_aldric_maeran_2026-04-22.md` | ✅ | 정상 |
| `royals/queen_lirien_ceren_2026-04-22.md` | ✅ | Ilaris-Ceren 혼인 동맹 체화 확인 |
| `royals/crown_prince_caeron_2026-04-22.md` | ✅ | 정상 |
| `royals/princess_sylvara_2026-04-22.md` | ✅ | 정상 |
| `royals/prince_davan_2026-04-22.md` | ✅ | 정상 |
| `royals/previous_king_thaeron_maeran_2026-04-22.md` | ✅ | 정상 |
| `royals/queen_dowager_elowen_2026-04-22.md` | ✅ | 정상 |
| `nobles/duke_silvanreach_vaern_2026-04-22.md` | ✅ | 정상 |
| `nobles/duke_mirevane_lorcas_2026-04-22.md` | ✅ | 정상 |
| `nobles/duke_deepsilvan_bruiden_2026-04-22.md` | ✅ | 정상 |
| `nobles/count_westshore_cailean_2026-04-22.md` | ✅ | 정상 |
| `nobles/count_deepsilvan_frontier_fenrik_2026-04-22.md` | ✅ | 정상 |
| `houses/house_maeran_2026-04-22.md` | ✅ | 혼인 동맹 정합 확인 |
| `houses/house_vaern_2026-04-22.md` | ✅ | 정상 |
| `houses/house_bruiden_2026-04-22.md` | ✅ | 정상 |
| `houses/house_lorcas_2026-04-22.md` | ✅ | 정상 |
| `orders/order_silver_sail_2026-04-22.md` | ✅ | 정상 |
| `orders/order_seawind_2026-04-22.md` | ✅ | 정상 |
| `heraldry_2026-04-22.md` | ✅ | 청·백·금 정상 |
| `military_2026-04-22.md` | ✅ | 정상 |
| `clothing_2026-04-22.md` | ✅ | Karzor 실크 차용 Ilaris 한정 확인 |
| `cuisine_2026-04-22.md` | ✅ | Q-CORE 2 간접 정상 |
| `architecture_2026-04-22.md` | ✅ | 정상 |
| `dialect_2026-04-22.md` | ✅ | Karzor 차용어 Ilaris 한정 원칙 준수 |
| `history/founding_2026-04-22.md` | ✅ | 정상 |
| `history/silvan_forest_relations_2026-04-22.md` | ✅ | 정상 |
| `capital_map_2026-04-22.md` | ✅ | Q-CORE 2 간접 정상 |
| `festivals/festival_opening_harbor_2026-04-22.md` | ✅ | 정상 |
| `festivals/festival_trade_fair_2026-04-22.md` | ✅ | 정상 |
| `festivals/festival_shipwright_day_2026-04-22.md` | ✅ | 정상 |
| `festivals/festival_citizen_march_2026-04-22.md` | ✅ | 정상 |
| `roads/road_ilarien_to_silvanreach_2026-04-22.md` | ✅ | 정상 |
| `roads/road_ilarien_to_mirevane_2026-04-22.md` | ✅ | 정상 |
| `roads/road_ilarien_to_deepsilvan_2026-04-22.md` | ✅ | 정상 |
| `roads/road_ilarien_to_westshore_2026-04-22.md` | ✅ | 정상 |
| `roads/road_westshore_to_ceren_border_2026-04-22.md` | ✅ | "소금 길 salkeen durvan" Karzor 방언 비공식명 — 이상 없음 |
| `cities/city_ilarien_2026-04-22.md` | ✅ | 인구·기능 정합 |
| `cities/city_mirvane_2026-04-22.md` | ✅ | 정상 |
| `cities/city_silvenmere_2026-04-22.md` | ✅ | 정상 |
| `cities/city_westport_2026-04-22.md` | ✅ | 정상 |
| `cities/city_caerveld_2026-04-22.md` | ✅ | 정상 |
| `villages/village_thornmere_2026-04-22.md` | ✅ | Q-CORE 2 간접 정상 |
| `villages/village_saltcroft_2026-04-22.md` | ✅ | 정상 |
| `villages/village_mirevane_landing_2026-04-22.md` | ✅ | 정상 |
| `villages/village_ashwood_2026-04-22.md` | ✅ | 정상 |
| `villages/village_cairnport_2026-04-22.md` | ✅ | 정상 |
| `villages/village_brinefall_2026-04-22.md` | ✅ | 정상 |
| `villages/village_woldhaven_2026-04-22.md` | ✅ | 정상 |
| `villages/village_harrowfen_2026-04-22.md` | ✅ | 정상 |
| `villages/village_coppergate_2026-04-22.md` | ✅ | 정상 |
| `villages/village_ferncross_2026-04-22.md` | ✅ | 정상 |
| `villages/village_gullwatch_2026-04-22.md` | ✅ | 정상 |
| `villages/village_reedmere_2026-04-22.md` | ✅ | 정상 |
| `villages/village_ironbarrow_2026-04-22.md` | ✅ | 정상 |
| `villages/village_cliffmere_2026-04-22.md` | ✅ | 정상 |
| `villages/village_mossbend_2026-04-22.md` | ✅ | 정상 |
| `villages/village_tarwick_2026-04-22.md` | ✅ | 정상 |
| `villages/village_birkenmoor_2026-04-22.md` | ✅ | 정상 |
| `villages/village_elmholt_2026-04-22.md` | ✅ | 정상 |
| `villages/village_dunford_2026-04-22.md` | ✅ | 정상 |
| `villages/village_grenwick_2026-04-22.md` | ✅ | 정상 |

**Ilaris 소계**: Critical 0건 / Major 1건 / Minor 0건 / 정상 61파일

---

## 6. 주요 교차 검증 항목

### 6-1. 혼인 동맹 정합 검사 ✅

| 동맹 | 구조 | 검증 파일 | 결과 |
|------|------|----------|------|
| Moran ↔ Ilaris 동맹 | Moran 왕비 = Ilaris 출신 (Sorwen) | `royals/queen_sorwen`, `houses/house_moran_royal` | ✅ 정합 |
| Ilaris ↔ Ceren 동맹 | Ilaris 왕비 = Ceren 출신 (Lirien) | `royals/queen_lirien_ceren`, `houses/house_maeran`, `relations/marriage_ilaris_ceren` | ✅ 정합 |
| **양 동맹 독립성** | 별개의 두 동맹, 모순 없음 | 양쪽 파일 교차 확인 | ✅ 이상 없음 |

**판정**: Moran 왕비(Sorwen) = Ilaris 출신, Ilaris 왕비(Lirien) = Ceren 출신. 두 혼인 동맹은 완전히 별개로, 모순 없음.

---

### 6-2. 네이밍 세트 B 잔존 검사 ✅

| 구형 이름 | Grep 결과 | 비고 |
|----------|----------|------|
| Frosthelm | 0건 (양국 내) | 타 왕국(Empire_Choir 등)에 잔존하나 검사 범위 외 |
| Greyveil | 0건 (양국 내) | kingdom_oryn `duke_veilorn_march_calder`에 잔존 — 타 검사관 대상 |

**판정**: 양국 범위 내 네이밍 세트 B 잔존 없음 ✅

---

### 6-3. Karzor 방언 분리 검사 ✅

| 왕국 | Karzor 차용어 | 결과 |
|------|-------------|------|
| Moran | 0건 | ✅ 원칙 준수 |
| Ilaris | zariq, salkeen, mirvash, qalin, durvan (방언 파일) + 요리·의상·도로 비공식명 일부 | ✅ Ilaris 한정 원칙 준수 |

---

### 6-4. 봉공 완곡 표현 검사 ✅

- Ilaris 왕국 노예 산업 관련 파일 (founding, silvan_forest_relations, duke_deepsilvan_bruiden, village_ironbarrow 등) 전수 확인.
- "노예" 직접 표기는 역사 서술 맥락 내에서만 사용.
- "봉공 계약인" 완곡어 또는 "타종족 포획" 표현 준수.
- **이단 파일 없음** ✅

---

### 6-5. Q-CORE 2 간접 단서 배치 현황 ✅

아래 파일들에서 Q-CORE 2 간접 단서("이름 없는/모를 학자·노인·영감" 구전)가 **올바른 간접 형태**로 배치됨:

**Moran**: village_hornreach, village_saltwick, village_wellford, village_misthollow, city_keldhaven, city_greycliff, cuisine, festival_mist, architecture(간접 정상 — "이름 모를 석공 노인" 서술은 정상 / "할배 활동 흔적" 레이블만 수정 필요)

**Ilaris**: city_ilarien (capital_map), cuisine, village_thornmere, history/silvan_forest_relations

---

## 7. 주인공 마을 후보 섹션 (Wave 4 관련)

주인공 마을 후보 파일은 `wiki/design/worldbuilding/elucia/toponymy/protagonist_village_candidates_2026-04-22.md`에 별도 관리됨. 검사관 G 범위의 Ilaris 왕국 내 주요 관련 마을:

| 마을 | 위치 | 특이점 |
|------|------|--------|
| Elmholt | Silvan 外林·中林 경계 | "주인공 마을 후보군 인접" 명시 |
| Thornmere | Silvan 서부 변경림 | Q-CORE 2 간접 배치 |
| Ashwood | Silvan 숲 外林 남부 | Ilarien 조선소 목재 공급 |
| Mossbend | Silvan 中林 계곡 | 엘프 접촉 구전 잔존 마을 |
| Ferncross | Silvan 外林·中林 경계 | 약초·치유사 집산지 |

**판정**: 주인공 마을 후보 파일은 Toponymist Wave 2 작성으로 별도 관리. 위 마을들은 후보 마을과 인접하거나 서사 접점 있음.

---

## 8. Grep 스캔 요약

| 검색 패턴 | Moran 결과 | Ilaris 결과 | 비고 |
|----------|-----------|-----------|------|
| `할배` (직접 레이블) | 6건 | 1건 | 총 7건 — Critical 2, Major 4, Minor 1 |
| `Frosthelm` | 0건 | 0건 | fix_log 수정 완료 확인 |
| `Greyveil` | 0건 | 0건 | fix_log 수정 완료 확인 |
| `skip_gates=True` | 0건 | 0건 | 이상 없음 |
| `봉공 계약인` (완곡 표현 위반) | 0건 | 0건 | 이상 없음 |
| Karzor 차용어 (Moran) | 0건 | — | 원칙 준수 |

---

## 9. 수정 우선순위 및 지시

### 즉시 수정 필수 (Critical — Wave 5 진행 전)

1. `kingdom_moran/royals/previous_king_brann_2026-04-22.md` 줄 21
   - 삭제 대상: `"Q-CORE 1: 마왕 ≠ 할배 / 첫 번째 신 = 할배 = 영감"` 전체 라인

2. `kingdom_moran/00_overview.md` 줄 30
   - 삭제 대상: `"Q-CORE 2: 할배는 자신의 수많은 판단 미스로 많은 생명 앗은 것을 속죄 / 현재 인간의 삶 / 생활 마법 개발·무료 배포"` 전체 라인

### 조속 수정 권고 (Major)

3. `kingdom_moran/nobles/duke_wellmere_ashfen_2026-04-22.md`
   - "할배의 서민 마법" → "이름 없는 학자의 서민 마법"
   - "할배 관련 단서 접근 경로" → "이름 없는 학자 관련 단서 접근 경로"

4. `kingdom_moran/royals/crown_prince_aldwin_2026-04-22.md`
   - "할배의 익명 가르침 흔적" → "이름 없는 학자 방문 흔적"

5. `kingdom_moran/architecture_2026-04-22.md` 줄 88
   - `· 할배 활동 흔적` 레이블 삭제

6. `kingdom_ilaris/00_overview.md` 줄 154
   - `(할배 속죄·무료 마법 배포)` → `(이름 없는 학자·생활 마법 배포)`

### Wave 5 위임 가능 (Minor)

7. `kingdom_moran/capital_map_2026-04-22.md`
   - "할배 간접 흔적 (추정)" → "이름 없는 노인 목격담 구전 (추정)"

---

## 10. 추가 발견 사항 (대표님 확정 대기)

아래 항목들은 이번 검사에서 발견된 "미확정" 사항으로, 설계 결정이 필요합니다:

| 항목 | 위치 | 결정 필요 내용 |
|------|------|-------------|
| 서방 대해 공식 이름 | city_ilarien | Toponymist 담당 대기 |
| Westshore 작위 (공작 vs 백작) | 00_overview | Wave 4 임시 백작 — 확정 필요 |
| 노예 시장 위치 | city_ilarien, architecture | 도시 내 vs 외곽 |
| 해신 Moranu 교황청 공인 여부 | festival_departure | 의례 공식성 좌우 |
| Moran 왕궁 공식 이름 | city_mornheld | 미확정 |
| Greycliff 등대 창건 연대 | order_sea_wolves | Chronicler 담당 |
| Bruiden 가문 초대 역사 | house_bruiden | Chronicler 담당 |
| 접경 관문 이름 (Westshore→Ceren) | road_westshore_to_ceren | 미확정 |

---

## 11. 검사 총평

**Kingdom Moran**: Critical 2건이 집중된 파일은 `previous_king_brann` (원전 인용 증명 섹션 Q-CORE 번호 공개)과 `00_overview` (Q-CORE 2 내용 직접 인용)다. 두 파일 모두 에이전트 브리핑 내용이 일반 열람 본문에 혼재된 구조적 문제. Wave 4 에이전트 브리핑 섹션 분리 원칙이 일부 파일에서 관철되지 않았음.

**Kingdom Ilaris**: Critical 0건. Major 1건(00_overview 헤더)만 존재하며 전반적으로 Q-CORE 분리 원칙이 Moran보다 잘 준수됨. Q-CORE 2 간접 단서 배치(cuisine, capital_map, village_thornmere 등)는 모두 올바른 "이름 없는/모를" 표현으로 정상 기술.

**양국 공통 양호 사항**:
- 혼인 동맹 구조 완벽 정합 (Moran↔Ilaris, Ilaris↔Ceren 별개 동맹)
- Karzor 방언 분리 원칙 준수
- 봉공 완곡 표현 원칙 준수
- Frosthelm / Greyveil 잔존 없음 (fix_log 수정 확인)
- Q-CORE 2 간접 단서 대부분 "이름 없는/모를 학자·노인" 표현으로 정상 배치

**결론**: Critical 2건 수정 완료 후 Wave 5 진행 가능. Major 4건은 Wave 5 시작 전 일괄 수정 권고.

---

*검사 완료 일시: 2026-04-22*  
*검사관: Inspector-G (나베랄 감마)*  
*전수검사 파일 수: Moran 51 + Ilaris 62 = 총 113파일*
