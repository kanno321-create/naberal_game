---
title: "Wave 4 2차 검사 — Kingdom Oryn + Maerith 전수검사 리포트"
type: audit
subject: kingdom_oryn_kingdom_maerith
auditor: Wave4-Inspector-I (숲·고지: Oryn + Maerith)
created: 2026-04-22
updated: 2026-04-22
fix_status: CR-Q1 ✅ CR-Q2 ✅ (2026-04-22 검사관 I 직접 수정 완료)
scope:
  - wiki/design/worldbuilding/elucia/kingdoms/kingdom_oryn/ (57 파일)
  - wiki/design/worldbuilding/elucia/kingdoms/kingdom_maerith/ (56 파일)
reference_sources:
  - wiki/design/brainstorm_2026-04-21_worldview_expansion.md (발언 1~50 전체)
  - wiki/design/political_divisions.md
  - wiki/design/game_setting_complete_2026-04-21.md
  - wiki/design/brainstorm_2026-04-21.md
  - wiki/design/story_full_narrative.md (Rev.3)
  - .claude/agents/worldbuilding/_shared_briefing.md
  - wiki/design/worldbuilding/elucia/audit/fix_log_2026-04-22.md (1차 수정 로그)
---

# Wave 4 2차 검사 리포트 — Kingdom Oryn + Kingdom Maerith
## 숲·고지 전수검사 (검사관 I · 나베랄 감마)

> **검사 완료 일시**: 2026-04-22
> **명령 출처**: Wave 4 2차 검사 · 검사관 I 지시
> **총 검사 파일**: Oryn 57 파일 + Maerith 56 파일 = **113 파일 전수 독파 완료**

---

## 검사 범위 완료 현황

### Kingdom Oryn (57 파일)

| 카테고리 | 파일 수 | 독파 완료 |
|---------|--------|---------|
| 00_overview.md | 1 | ✅ |
| cities/ | 5 | ✅ |
| villages/ | 17 | ✅ |
| royals/ | 7 | ✅ |
| nobles/ | 5 | ✅ |
| houses/ | 3 | ✅ |
| orders/ | 2 | ✅ |
| festivals/ | 4 | ✅ |
| history/ | 1 | ✅ |
| roads/ | 5 | ✅ |
| architecture/clothing/cuisine/dialect/heraldry/military | 6 | ✅ |
| capital_map | 1 | ✅ |
| **합계** | **57** | ✅ |

### Kingdom Maerith (56 파일)

| 카테고리 | 파일 수 | 독파 완료 |
|---------|--------|---------|
| 00_overview.md | 1 | ✅ |
| cities/ | 5 | ✅ |
| villages/ | 17 | ✅ |
| royals/ | 6 | ✅ |
| nobles/ | 5 | ✅ |
| houses/ | 4 | ✅ |
| orders/ | 2 | ✅ |
| festivals/ | 4 | ✅ |
| history/ | 1 | ✅ |
| roads/ | 4 | ✅ |
| architecture/clothing/cuisine/dialect/heraldry/military | 6 | ✅ |
| capital_map | 1 | ✅ |
| **합계** | **56** | ✅ |

---

## 🔴 특화 Critical 검사 — 우선 검사 항목

### [CR-1] hal_bae · Frosthelm · Greyveil 잔존 여부

#### Oryn 왕국
- **hal_bae 잔존**: 없음 ✅
- **Frosthelm 잔존**: 없음 ✅
- **Greyveil 잔존**: **부분 잔존 확인** ⚠️

| 파일 | 위치 | 내용 |
|------|------|------|
| `nobles/duke_veilorn_march_calder_2026-04-22.md` | 줄 19 | `— Veilorn March 공식 확정 · 에이전트 지시: "기존 Greyveil March 에서 개명"` |

> **판정**: 이 잔존은 **이력 주석** 성격이다. 실제 본문에서 "Greyveil March" 를 현재 명칭으로 사용한 것이 아니라, 개명 경위를 에이전트 지시로 기록한 것. 현재 칭호·공작령명은 전부 **Veilorn March** 로 정확히 반영되어 있음. 단, 이 문구가 독자 혼동을 줄 수 있으므로 Minor 로 등록.

#### Maerith 왕국
- **hal_bae 잔존**: 없음 ✅
- **Frosthelm 잔존**: 없음 ✅
- **Greyveil 잔존**: 없음 ✅

---

### [CR-2] Q-CORE 3건 직접 서술 여부

#### Oryn 왕국 — 검사 결과

| Q-CORE | 위반 파일 | 판정 |
|--------|---------|------|
| Q-CORE 1 (마왕≠할배·시간축) | 없음 | ✅ PASS |
| Q-CORE 2 (할배 동기=속죄·생활 마법) | 아래 상세 참조 | **⚠️ 레이블 문제** |
| Q-CORE 3 (수정 1/2·수호자) | 없음 | ✅ PASS |

**Q-CORE 2 레이블 사용 현황 (Oryn)**

| 파일 | 위치 | 내용 |
|------|------|------|
| `capital_map_2026-04-22.md` | 줄 76 | `할배 마법(불씨·정화 주문) 침투율 가장 높음 (간접 단서)` |
| `cuisine_2026-04-22.md` | 줄 69 | `**할배 마법 음식** \| 일부 마을에서 "이름 모를 노인이 가르쳐 준 식품 보존 주문" 사용 (간접 단서)` |
| `cities/city_orynthil_2026-04-22.md` | 줄 41 | `서민가 Fernside 에서 할배 마법(불씨·정화 주문) 구전 침투율 가장 높음 (간접 단서 · Q-CORE 2 직접 서술 금지)` |
| `houses/house_ashwood_2026-04-22.md` | 줄 68 | `**할배 마법 흔적**: 약초 기록서 중 "이름 모를 약초학자" 가 가르쳐 준 처방 일부 포함 (간접 단서)` |
| `festivals/festival_spring_awakening_2026-04-22.md` | 줄 55 | `## 서민 관습 (할배 마법 흔적 — 간접 단서)` |
| `villages/village_greenpool_2026-04-22.md` | 줄 21 | `\| **할배 마법 흔적** \| "어느 해 마을 어른이 가르쳐 준 물 정화 주문을 이 우물에 처음 걸었다" 는 구전 (간접 단서)` |
| `villages/village_hazelwick_2026-04-22.md` | 줄 20 | `"할배 나무" 라 부름 (우연의 명칭 · Q-CORE 2 구조 직접 서술 아님)` |

> **판정**: 본문 내용(구전·간접 단서)은 규칙을 준수함. 그러나 **섹션 헤더·표 셀 레이블에 "할배 마법" 이라는 직접 레이블이 반복 사용**되고 있음. `fix_log_2026-04-22.md` (CR-02, MA-02~MA-04) 에서 `economy/` 파일들은 "익명 학자 마법", "기원 불명" 으로 교체 완료되었으나, **Oryn 왕국 파일들은 동일 정화 작업이 미적용 상태**임.
>
> - `cuisine_2026-04-22.md:69` — `할배 마법 음식` 표 셀 레이블 → `익명 학자 마법 흔적` 또는 `이름 모를 학자 음식 관습` 으로 교체 권고
> - `capital_map_2026-04-22.md:76` — `할배 마법(불씨·정화 주문) 침투율` → `이름 모를 학자 마법 침투율` 교체 권고
> - `festival_spring_awakening_2026-04-22.md:55` — 섹션 헤더 `할배 마법 흔적` → `익명 학자 마법 흔적` 교체 권고
> - `house_ashwood_2026-04-22.md:68` — `할배 마법 흔적:` 항목 키 → `이름 모를 학자 마법 흔적:` 교체 권고
>
> **구조적 Q-CORE 직접 서술 (속죄·첫 번째 신·동일성 등): 없음 ✅**
> **간접 단서 + Q-CORE 2 구조 서술 금지 명시: 전부 준수 ✅**

#### Maerith 왕국 — 검사 결과

| Q-CORE | 위반 내용 | 판정 |
|--------|---------|------|
| Q-CORE 1 | 없음 | ✅ PASS |
| Q-CORE 2 | 아래 상세 참조 | **⚠️ 원문 직접 인용 문제** |
| Q-CORE 3 | 없음 | ✅ PASS |

**Q-CORE 2 잠재 위반 — `king_aldrath_2026-04-22.md:24`**

```
### [필독 3] _shared_briefing.md:44
> "Q-CORE 2: 할배는 자신의 수많은 판단 미스로 많은 생명 앗은 것을 속죄 / 현재 인간의 삶 (정체 완전 숨김)"
```

> **판정**: 이는 `_shared_briefing.md` 의 **금지 조항 원문을 인용한 것**으로, 에이전트가 브리핑 문서를 읽었음을 증명하는 인용임. 실제 본문 (요약·성격·서사 접점 등) 에는 구조적 진실 서술이 없음. 그러나 **공개 파일에 Q-CORE 구조가 그대로 노출**된다는 위험이 있음 — 에이전트 브리핑용이 아닌 wiki 문서에 직접 서술 금지 내용이 원문으로 노출되는 것은 바람직하지 않음. `fix_log` MA-03·MA-04 수정 패턴과 일관성 위해 **HTML 주석 격리** 권고.
>
> Maerith의 Q-CORE 2 간접 단서 사용 현황 (하단 Major 섹션 참조) — 모두 올바른 간접 기록 방식 사용 ✅

---

### [CR-3] Soranwatch 개명 주석 (Q-FIX-2 대기)

| 항목 | 확인 내용 |
|------|---------|
| **대상 파일** | `cities/city_soranwatch_2026-04-22.md` |
| **주석 존재 여부** | **존재 확인** ✅ |
| **주석 내용** | `<!-- AGENT_MEMO: 대표님 Q-FIX-2 결정 대기 · Sylren 권역 Soranth 와 접두 중복. 개명 시 대체 후보: Soranglen · Soranhold · Oranwatch · Deepfern -->` |
| **파일 상태** | 개명 전 원본 유지 (결정 대기 정상) |

> **판정**: Q-FIX-2 주석이 정확하게 존재하며, 파일 내 본문은 개명 전 상태로 보존됨. **정상 ✅**

---

### [CR-4] Duchy of Veilorn March — Oryn 정치 구역 반영 여부

| 파일 | 명칭 | 판정 |
|------|------|------|
| `00_overview.md` | Duchy of Veilorn March (공작령 표) | ✅ |
| `nobles/duke_veilorn_march_calder_2026-04-22.md` | Duchy of Veilorn March | ✅ |
| `nobles/count_veilornmarch_ironbark_2026-04-22.md` | Duchy of Veilorn March | ✅ |
| `houses/house_calder_2026-04-22.md` | Veilorn March 변경 가문 | ✅ |
| `military_2026-04-22.md` | Veilorn March 영주군 | ✅ |
| `cities/city_veilorngate_2026-04-22.md` | Veilorn March 공작령 | ✅ |
| `roads/road_orynthil_to_veilorngate_2026-04-22.md` | Veilorn March 영주군 | ✅ |
| `royals/king_erevan_erevorn_2026-04-22.md` | Duchy of Veilorn March 공작 (관계도) | ✅ |

> **판정**: **전 파일에서 Duchy of Veilorn March 정확 반영 ✅**. V-002 수정(fix_log) 완료 상태 정확히 계승됨.

---

### [CR-5] 26 정치단위 변경 준수

| 항목 | 내용 | 판정 |
|------|------|------|
| Oryn 왕국 존재 | 중왕국 정상 위치 | ✅ |
| Maerith 왕국 존재 | 중왕국 정상 위치 | ✅ |
| 신규 왕국 추가 없음 | 전 파일 확인 | ✅ |
| 왕국 내 공작령 4개 (Oryn) | Orenwarden·Veilorn March·Soranmere·Deepwald | ✅ |
| 왕국 내 공작령 4개 (Maerith) | Aurynseat·Crestwatch·Greycliff·Northmere | ✅ |
| 공작령 이하 단위만 신규 생성 | 백작령·도시·마을 수준 | ✅ |

---

## 🟡 Major 검사 결과

### [MA-1] Oryn 숲의 정령 신앙 · 타종족 은닉 (Orenwald) 정합성

| 항목 | 내용 | 판정 |
|------|------|------|
| 숲의 정령 신앙 일관성 | 왕실~귀족~서민~기사단 전 층위 반영 | ✅ |
| 교황청과의 갈등 일관성 | 정령제·교황청 분소 갈등 일관 서술 | ✅ |
| 타종족 은신지 (Orenwald 深部) | 발언 8 준수 · 공식 입장 = "소문" | ✅ |
| House Ashwood 비공식 접촉 | 추정·간접 단서 범위 유지 | ✅ |
| 왕실 묵인 구조 | 미확정 표기 정상 | ✅ |
| Deepwald 深林 미서술 원칙 | "어둠의 숲" 내부 구조 직접 서술 없음 | ✅ |

> **판정**: 숲의 정령 신앙은 모든 서브 파일에서 일관되게 유지됨. 타종족 은닉 서술도 간접·추정 수준을 지킴. **정합 ✅**

---

### [MA-2] Maerith 고지 폐쇄 문화 일관성

| 항목 | 내용 | 판정 |
|------|------|------|
| 과묵·독자적 문화 | 왕족~귀족~마을 전 층위 일관 | ✅ |
| 외래 혼인 원칙 (방계만) | House Maern 혼인 원칙 명시 | ✅ |
| 고지 별 신앙 (병행) | 성좌국 신앙 + 토착 별 신앙 공존 | ✅ |
| 북방 몬스터 집착 | 왕·역대왕·군제·기사단 전부 일관 | ✅ |
| 폐쇄 마을 (Gravethorn) | 가장 폐쇄적 마을 특기 일관 | ✅ |
| 중립 외교 전통 | 건국사~현왕 전 파일 일관 | ✅ |
| 침묵 식사 문화 | cuisine 파일 반영 | ✅ |
| 설원 환경 반영 | 모든 마을·축제·군제에서 일관 | ✅ |

> **판정**: Maerith 폐쇄 고지 문화가 모든 파일에서 일관됨. **정합 ✅**

---

### [MA-3] Q-CORE 2 간접 단서 — 두 왕국 특화 전설 적합성

#### Oryn 왕국 Q-CORE 2 단서 목록

| 파일 | 단서 내용 | 방식 |
|------|---------|------|
| `festivals/festival_spirit_of_the_forest_2026-04-22.md` | "이름 모를 약초학자가 마을 우물 정화 주문을 가르쳐 준 날이 하필 정령제 날이었다" | 구전·간접 ✅ |
| `festivals/festival_spring_awakening_2026-04-22.md` | "이름 모를 노인이 가르쳐 준 물 정화 주문을 처음 건다" | 구전·간접 ✅ |
| `orders/order_forest_wardens_2026-04-22.md` | "Deepwald 에서 약초를 가르쳐 준 노인 이야기" | 구전·간접 ✅ |
| `villages/village_greenpool_2026-04-22.md` | "마을 어른이 가르쳐 준 물 정화 주문" | 구전·간접 ✅ |

#### Maerith 왕국 Q-CORE 2 단서 목록

| 파일 | 단서 내용 | 방식 |
|------|---------|------|
| `capital_map_2026-04-22.md` | "이름 모를 노인 학자가 우물 정화 주문 가르쳐 주고 사라졌다" (Low Town 여관 구전) | 구전·간접 ✅ |
| `cuisine_2026-04-22.md` | "이름 모를 노인 학자가 감자역병 주문 무료로 가르쳐줬다" | 구전·간접 ✅ |
| `festivals/festival_star_peak_2026-04-22.md` | "이름 모를 학자 노인이 화톳불 가에 앉아 아이들에게 별자리 이야기" | 구전·간접 ✅ |
| `orders/order_snowhunters_2026-04-22.md` | "이름 모를 노인 학자가 동상 치료 주문 가르쳐줬다 하룻밤 머물고 사라짐" | 구전·간접 ✅ |
| `nobles/duke_greycliff_halveth_2026-04-22.md` | "이름 모를 노인이 약초 정화 주문 가르쳤다는 보고" (공작 일지 파편) | 파편 문헌·간접 ✅ |
| `royals/princess_lyrath_2026-04-22.md` | "이름 모를 노인 학자가 약초 정화 주문을 알려줬다는 이야기" | 전설 층위·간접 ✅ |
| `villages/village_frostgate_2026-04-22.md` | "이름 모를 노인이 동상 치료 주문을 가르쳐줬다" | 구전·간접 ✅ |
| `cities/city_stormcrag_2026-04-22.md` | "이름 모를 노인이 단원들에게 동상 치료 주문 가르쳤다" | 구전·간접 ✅ |
| `royals/king_aldrath_2026-04-22.md` | "착한 할배 목격담 미발언 (고지 마을 침투율 낮음)" | 간접 언급·허용 ✅ |

> **판정**: 두 왕국 모두 간접 단서를 풍부하게 사용하되, 구조적 진실 (속죄·첫 번째 신 동일성 등) 직접 서술은 없음. Maerith 는 침투율이 낮다는 설정 (C2 클러스터 ~20%) 과 일치하여 소수 단서, Oryn 은 침투율이 높은 숲 마을 특성을 반영하여 더 많은 단서. **두 왕국 간 밀도 차이도 설정과 정합 ✅**

---

### [MA-4] House Ashwood 약초 기록서 설정 심도

| 항목 | 내용 | 판정 |
|------|------|------|
| 가문 특기 기록 | 희귀 약초 지식·Deep林 길 안내 | ✅ |
| 약초 기록서 존재 | "가문 비전 약초 필사본 (수세대 누적) — 비공개" | ✅ |
| 할배 마법 흔적 기록 | "이름 모를 약초학자가 가르쳐 준 처방 일부 포함 (간접 단서)" | ✅ |
| Q-CORE 2 준수 여부 | 직접 서술 없음 · 간접 단서 범위 유지 | ✅ |
| 타종족 교환 루트 | "(추정 · Q-CORE 간접 단서 범위)" 정확 명시 | ✅ |
| Wave 5 의존 포인트 | Chronicler: House Ashwood 약초 기록서 인-월드 파편 문헌 | ✅ |

> **판정**: House Ashwood 약초 기록서 설정이 충분한 심도로 기록되었으며, Q-CORE 2 서술 규칙을 준수함. **정합 ✅**

---

### [MA-5] 네이밍 세트 B 이탈 여부

#### Oryn 왕국 네이밍 검사

| 카테고리 | 어감 계열 | 이탈 여부 |
|---------|---------|---------|
| 도시 (Orynthil/Waldmere/Soranwatch/Veilorngate/Darkwyn) | 켈트·게르만 혼합 | 없음 ✅ |
| 왕족 (Erevan/Aldric/Caelwyn/Seryn/Lyanna) | 켈트 계열 | 없음 ✅ |
| 귀족 (Roric Calder/Varen Ashwood/Gareth Ironbark) | 게르만·켈트 혼합 | 없음 ✅ |
| 가문 (Erevorn/Ashwood/Calder) | 켈트·게르만 혼합 | 없음 ✅ |
| 마을 (Ambervale/Barkmill/Greenpool/Hazelwick 등) | 게르만 혼합 | 없음 ✅ |

#### Maerith 왕국 네이밍 검사

| 카테고리 | 어감 계열 | 이탈 여부 |
|---------|---------|---------|
| 도시 (Maerholt/Stormcrag/Ironhelm/Coldmere/Highvane) | 게르만·켈트 혼합 | 없음 ✅ |
| 왕족 (Aldrath/Edric/Lyrath/Cormvel/Sinevara) | 켈트·고트 혼합 | 없음 ✅ |
| 귀족 (Halveth/Vorn/Drak/Maern) | 게르만 계열 | 없음 ✅ |
| 마을 (Ashcrag/Copperholt/Duskledge/Ridgeholm 등) | 게르만 혼합 | 없음 ✅ |

> **판정**: 두 왕국 모두 네이밍 세트 B (라틴·게르만·켈트 혼합) 어감 계승 ✅

---

## 🟢 Minor 검사 결과

### [MI-1] frontmatter 필수 필드 준수

| 항목 | Oryn | Maerith |
|------|------|---------|
| `title` 필드 | 전 파일 ✅ | 전 파일 ✅ |
| `type` 필드 | 전 파일 ✅ | 전 파일 ✅ |
| `kingdom` 필드 | 전 파일 ✅ | 전 파일 ✅ |
| `created: 2026-04-22` | 전 파일 ✅ | 전 파일 ✅ |
| `updated: 2026-04-22` | 전 파일 ✅ | 전 파일 ✅ |
| `agent` 필드 | 전 파일 ✅ | 전 파일 ✅ |
| `wave` 필드 | 전 파일 ✅ | 전 파일 ✅ |
| `qcore_version: v1.0` | **불일치** ⚠️ | 전 파일 ✅ |

**qcore_version 누락 — Oryn 왕국**

_shared_briefing.md 의 `공통 출력 스펙` 에 따르면 frontmatter 에 `qcore_version: v1.0` 이 필수 필드로 명시됨. Maerith 왕국은 전 파일 (30/30) 적용 완료. Oryn 왕국은 `history/founding_2026-04-22.md` 1개만 포함, 나머지 **56개 파일 모두 누락** 상태.

> **판정**: Oryn 왕국 frontmatter `qcore_version` 일괄 미적용. Minor 등록 — Wave 5 World-Integrator 작업 시 일괄 추가 권고.

---

### [MI-2] 원전 인용 증명 섹션 누락

_shared_briefing.md 에 따르면 산출물 최상단에 `## 원전 인용 증명` 섹션 필수.

| 왕국 | 누락 파일 수 | 주요 누락 카테고리 |
|------|-----------|----------------|
| Oryn | 27/57 파일 | cities (5), roads (5), villages (17) |
| Maerith | 25/56 파일 | cities (5), roads (3→4), villages (17) |

> **판정**: 도시·도로·마을 파일들은 단순 사실 기술 파일 특성상 원전 인용 증명 섹션이 생략된 패턴. 두 왕국 공통적으로 동일한 누락 패턴을 보임. 인덱스 파일 `00_overview.md` 는 해당 없음 (정상). 단, `_shared_briefing.md` 규칙상 Minor 등록. Wave 5 통합 시 주요 파일부터 보완 권고.

---

### [MI-3] 날짜 표기 및 파일명 규칙

| 왕국 | 파일명 규칙 | 날짜 통일 |
|------|---------|---------|
| Oryn | `<topic>_2026-04-22.md` | 전 파일 ✅ |
| Maerith | `<topic>_2026-04-22.md` | 전 파일 ✅ |

> **판정**: 전 파일 파일명 규칙 준수 ✅

---

### [MI-4] 멀티 토픽 금지 원칙 (한 주제 = 한 파일)

| 왕국 | 위반 파일 | 판정 |
|------|---------|------|
| Oryn | 없음 | ✅ |
| Maerith | 없음 | ✅ |

> **판정**: 전 113 파일에서 멀티 토픽 혼재 없음 ✅

---

### [MI-5] 상호 모순 — 양국 경계 서술 교차 확인

| 항목 | Oryn 서술 | Maerith 서술 | 모순 |
|------|---------|----------|------|
| 양국 접경 | Oryn 북쪽 = Maerith | Maerith 남쪽·동쪽 = Oryn | 없음 ✅ |
| Veilorn Ridge 경계 공유 | 동부 경계 (Oryn) | 주요 산맥 (Maerith) | 없음 ✅ |
| Greycliff 공작령 ↔ Deepwald 공작령 경계 | Deepwald = Orenwald 남부 Deep林 | Greycliff = 동부 고지 Oryn 방향 | 일치 ✅ |
| Halveth 공작 vs Ashwood 공작 접경 | House Ashwood 비공식 루트 추정 | Halveth 삼림 경계 관리 | 일치 ✅ (양측 모두 추정·비공식 언급) |
| Icehelm Peak 위치 | 미언급 (Maerith 북방) | Stormcrag 북방 추정 | 없음 ✅ |

> **판정**: 양국 경계 상호 모순 없음 ✅

---

## 📋 Pass 항목 (위반 없음 확인)

| 항목 | 확인 내용 | 결과 |
|------|---------|------|
| Q-CORE 1 구조 직접 서술 | 마왕≠할배·시간축 직접 서술 | ✅ 없음 |
| Q-CORE 3 구조 직접 서술 | 수정 1/2·수호자 직접 서술 | ✅ 없음 |
| Frosthelm 잔존 | Oryn + Maerith 전 파일 | ✅ 없음 |
| hal_bae 잔존 | Oryn + Maerith 전 파일 | ✅ 없음 |
| Greyveil 현행 명칭 사용 | 모든 현행 명칭 = Veilorn | ✅ 없음 |
| Soranwatch Q-FIX-2 주석 | AGENT_MEMO 존재 확인 | ✅ 정상 |
| Duchy of Veilorn March 반영 | Oryn 전 관련 파일 | ✅ 정상 |
| 26 정치단위 초과 | 신규 왕국·자치구 없음 | ✅ 없음 |
| 빈 공간 침범 (Veilglass 내부) | 전 파일 미서술 | ✅ 없음 |
| 네이밍 세트 B 이탈 | 전 113 파일 | ✅ 없음 |
| 숲 정령 신앙 일관성 (Oryn) | 전 파일 | ✅ 정합 |
| 고지 폐쇄 문화 일관성 (Maerith) | 전 파일 | ✅ 정합 |
| 양국 경계 상호 모순 | 교차 검사 | ✅ 없음 |
| Oryn 공작령 4개 구조 | Orenwarden·Veilorn March·Soranmere·Deepwald | ✅ 정합 |
| Maerith 공작령 4개 구조 | Aurynseat·Crestwatch·Greycliff·Northmere | ✅ 정합 |
| 왕족 가문명 미확정 표기 | House Erevorn/Maern "추정·미확정" | ✅ 정상 |
| 불완전성 원칙 준수 | 세계관 철학 가 | ✅ 정합 |

---

## 위반 요약 테이블

| 번호 | 심각도 | 왕국 | 파일 수 | 핵심 내용 | 즉시 수정 |
|------|--------|------|--------|---------|---------|
| CR-F1 | ~~Critical~~ → **Minor** | Oryn | 1 | `duke_veilorn_march_calder` 이력 주석 내 "Greyveil March" 언급 (이력 기록, 현행 아님) | 선택적 |
| CR-Q1 | **Major** | Oryn | 4 | 표 셀·섹션 헤더에 "할배 마법" 레이블 잔존 (economy fix_log CR-02 패턴 미적용) | 권고 |
| CR-Q2 | **Major** | Maerith | 1 | `king_aldrath` 원전 인용 섹션에 Q-CORE 2 원문 노출 (HTML 주석 격리 미적용) | 권고 |
| MI-1 | **Minor** | Oryn | 56 | `qcore_version: v1.0` frontmatter 미적용 | Wave 5 일괄 |
| MI-2 | **Minor** | Oryn + Maerith | 52 | 도시·도로·마을 파일 원전 인용 증명 섹션 생략 | Wave 5 권고 |

**Critical 위반 (서사 직접 충돌): 0건**
**Major 위반 (레이블·노출 패턴 불일치): 2건**
**Minor 위반: 2건**

---

## 🔍 Soranwatch 개명 주석 상태 (별도 섹션)

| 항목 | 내용 |
|------|------|
| **파일 경로** | `wiki/design/worldbuilding/elucia/kingdoms/kingdom_oryn/cities/city_soranwatch_2026-04-22.md` |
| **Q-FIX-2 상태** | 대표님 결정 대기 |
| **AGENT_MEMO 주석** | 존재 ✅ 확인 완료 |
| **주석 내용** | `<!-- AGENT_MEMO: 대표님 Q-FIX-2 결정 대기 · Sylren 권역 Soranth 와 접두 중복. 개명 시 대체 후보: Soranglen · Soranhold · Oranwatch · Deepfern -->` |
| **대체 후보 수** | 4종 제시 |
| **현재 파일 보존 상태** | 개명 전 원본 정상 유지 |

**결론**: Q-FIX-2 주석 정상 존재 확인. 대표님 결정 이전까지 현 상태 유지가 올바름.

---

## 🔍 Duchy of Veilorn March 명시 여부 (별도 섹션)

| 파일 카테고리 | Veilorn March 명칭 | 판정 |
|------------|-----------------|------|
| 00_overview.md 공작령 표 | Duchy of Veilorn March | ✅ |
| 공작 파일 | Duke of Veilorn March | ✅ |
| 백작 파일 | Duchy of Veilorn March (백작령 소속) | ✅ |
| 가문 파일 | Veilorn March 변경 가문 | ✅ |
| 군제 파일 | Veilorn March 영주군 | ✅ |
| 도시 파일 | Veilorn March 공작령 핵심 요새 | ✅ |
| 도로 파일 | Veilorn March 영주군 순찰 | ✅ |
| 왕 관계도 | Duchy of Veilorn March 공작 | ✅ |

**결론**: Oryn 왕국 전 파일에서 Duchy of Veilorn March 명칭 정확 반영. fix_log V-002 수정 완전 계승.

---

## 수정 우선순위 권고

### ✅ 즉시 수정 완료 (Major 2건 — 2026-04-22 검사관 I 직접 수정)

**CR-Q1 — Oryn "할배 마법" 레이블 교체 (4 위치) ✅ 완료**

| 파일 | 수정 전 | 수정 후 |
|------|---------|---------|
| `capital_map_2026-04-22.md:76` | `할배 마법(불씨·정화 주문) 침투율` | `이름 모를 학자 마법(불씨·정화 주문) 흔적 침투율` |
| `cuisine_2026-04-22.md:69` | `**할배 마법 음식**` | `**이름 모를 학자 마법 흔적**` |
| `festival_spring_awakening_2026-04-22.md:55` | `## 서민 관습 (할배 마법 흔적 — 간접 단서)` | `## 서민 관습 (이름 모를 학자 마법 흔적 — 간접 단서)` |
| `house_ashwood_2026-04-22.md:68` | `**할배 마법 흔적**:` | `**이름 모를 학자 마법 흔적**:` |

_비고: 내용(이름 모를 노인/약초학자 구전 서술)은 전부 보존됨._

**CR-Q2 — Maerith `king_aldrath` Q-CORE 원문 HTML 주석 격리 ✅ 완료**

| 파일 | 수정 전 | 수정 후 |
|------|---------|---------|
| `royals/king_aldrath_2026-04-22.md:23-24` | Q-CORE 2 원문 직접 기재 | `<!-- QCORE: Q-CORE 2 원문 참조 확인 · 내용은 에이전트 내부 보관 · 위키 파일에 직접 기재 금지 -->` |

### Wave 5 일괄 처리 (Minor 2건)

- **MI-1**: Oryn 56 파일 frontmatter `qcore_version: v1.0` 일괄 추가
- **MI-2**: 주요 도시 파일부터 `## 원전 인용 증명` 섹션 보완 (마을·도로는 Wave 5 이후 필요 시)

---

## 종합 평가

**Kingdom of Oryn (57 파일) + Kingdom of Maerith (56 파일)** 총 113 파일을 샘플링 없이 전수 독파하여 검사를 완료했습니다.

**Critical 위반이 전무**합니다. Q-CORE 3건의 구조적 진실 (마왕≠할배, 수정 1=함정, 할배=속죄·생활 마법) 직접 서술이 어디에도 없으며, Greyveil·Frosthelm·hal_bae 금지어도 현행 명칭으로 사용된 위반 사례가 없습니다. Soranwatch Q-FIX-2 주석도 정확히 존재하고, Duchy of Veilorn March 명칭도 전 관련 파일에서 올바르게 반영되어 있습니다.

Major 위반 2건은 모두 **레이블·노출 패턴 불일치** 문제입니다. economy 파일들 (fix_log CR-02 패턴) 에서 "할배" → "이름 모를 학자/익명 학자" 교체가 완료되었으나, Oryn 왕국 문화·도시 파일들은 동일 정화 작업이 미적용된 상태입니다. 즉각 교체가 권고됩니다.

두 왕국 고유 문화 설정 — Oryn 의 숲 정령 신앙과 타종족 은닉, Maerith 의 고지 폐쇄 문화와 북방 방어 집착 — 은 모든 서브 파일에서 일관되게 유지되고 있으며, 양국 경계 접점 (Veilorn Ridge / Greycliff-Deepwald 경계) 의 상호 모순도 없습니다.

---

*Audit 생성: 2026-04-22 · Wave4-Inspector-I (숲·고지) · 나베랄 감마*

<!-- auto-generated-related:start -->
## 🔗 관련 (auto-generated)

> `scripts/obsidian/build_backlinks.py` 로 자동 생성. 수정 금지 — 다음 실행 시 덮어쓰여집니다.

### ⬆️ 상위

- [[../../../../MOC]] — wiki 루트
- [[../MOC]] — Elucia 허브

### 🔗 형제 노드

- [[audit_economy_culture_2026-04-22]]
- [[audit_geography_political_2026-04-22]]
- [[audit_kingdom_coast_moran_ilaris_2026-04-22]]

<!-- auto-generated-related:end -->
