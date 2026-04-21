---
title: "Wave 4 2차 검사 보고서 — 습지·호수: Ceren + Aldric"
type: audit_report
inspector: Auditor-H (Inspector H)
scope: kingdom_ceren + kingdom_aldric
wave_target: 4
created: 2026-04-22
updated: 2026-04-22
qcore_version: v1.0
---

# Wave 4 검사 보고서 H — 습지·호수 왕국 (Ceren + Aldric)

**검사관**: Wave 4 2차 검사관 H  
**검사 범위**: `kingdom_ceren/` (53개 파일) + `kingdom_aldric/` (55개 파일) = 총 108개 파일  
**검사 완료**: 2026-04-22  
**참조 보고서**: Inspector A~D 보고서 + fix_log_2026-04-22.md (Critical 3 + Major 8 수정 완료 확인)

---

## 검사 전제 — STEP 0 확인 사항

| 항목 | 상태 |
|------|------|
| CR-01/02/03 (hal_bae 파일명·인덱스·종교) | FIXED ✅ |
| V-001 Frosthelm → Icehelm | FIXED ✅ |
| V-002 Greyveil → Veilorn | FIXED ✅ |
| MAJOR-001 Karzor 15 단위 표현 | FIXED ✅ |
| Q-FIX-1 Mirvane Port 파일 누락 | PENDING (이번 스코프 외) |
| Q-FIX-2 Soranwatch/Soranth 명칭 결정 | PENDING (이번 스코프 외) |

이전 검사에서 해결된 Critical 3건, Major 8건은 본 보고서에서 재검증하지 않음. 잔존 "Frosthelm", "Greyveil", "hal_bae" 패턴은 kingdom_ceren 및 kingdom_aldric 스코프 내에서 아래 별도 섹션으로 보고.

---

## 1. CRITICAL 등급 결함

### CR-H-01 — Q-CORE 2 내부 코드명 "할배" 원전 인용 섹션 직접 노출

| 항목 | 내용 |
|------|------|
| **등급** | Critical |
| **유형** | Q-CORE 2 직접 노출 |
| **파일 1** | `kingdom_ceren/00_overview.md` — 41행 |
| **파일 2** | `kingdom_aldric/00_overview.md` — 28행 |
| **파일 3** | `kingdom_aldric/royals/previous_king_aldric_iii_2026-04-22.md` — 21행 |
| **파일 4** | `kingdom_aldric/villages/village_reedholm_2026-04-22.md` — 18행 |

**문제 내용**:

파일 1 (kingdom_ceren/00_overview.md:41):
```
> "할배는 자신의 수많은 판단 미스로 많은 생명 앗은 것을 속죄 / 생활 마법 개발·무료 배포"
```

파일 2 (kingdom_aldric/00_overview.md:28):
```
> "할배 = '마법 잘 아는 착한 노인'으로만 인식. 생활 마법 개발·무료 배포..."
```

파일 3 (previous_king_aldric_iii_2026-04-22.md:21):
```
> "할배의 현재 활동 — 인간으로서의 삶. 여럿에게 도움을 줌. 생활 마법 개발·무료 배포."
```

파일 4 (village_reedholm_2026-04-22.md:18):
```
> "할배 = '마법 잘 아는 착한 노인'으로만 인식"
```

**판단 근거**: "원전 인용 증명" 섹션은 에이전트 작업 근거 기록용이나, Wiki 문서로서 완성 배포 시 독자가 접근 가능하다. Inspector B/Auditor-B가 파일명 내 `hal_bae` 잔존을 Critical로 판정한 것과 동일 원칙 적용. Q-CORE 2 핵심 정체 코드명이 직접 노출된 상태이며, 이전 CR-01/02/03에서 고친 원칙과 정합적이어야 한다.

**수정 방향**:
- "원전 인용 증명" 섹션의 Q-CORE 2 memory 인용문에서 `할배` → `[Q-CORE 2 주체]` 또는 `"이름 없는 학자"` 로 대체
- 또는 해당 섹션 자체를 내부 작업 메모에서 삭제하고 공개 배포 버전은 코드명 제거 처리

---

### CR-H-02 — Aldric 소금 교역과 Ceren 소금 레버리지 체계적 충돌 가능성

| 항목 | 내용 |
|------|------|
| **등급** | Critical |
| **유형** | 세계관 내부 모순 — 소금 레버리지 훼손 위험 |
| **파일** | `kingdom_aldric/villages/village_saltmarsh_2026-04-22.md` |
| **연계 파일** | `kingdom_aldric/cities/city_westport_aldric_2026-04-22.md` |

**문제 내용**:

`village_saltmarsh_2026-04-22.md`의 대표님 미확정 항목:
> "알드릭 소금 교역 범위 (Ceren·성좌국 수출 여부)"

`city_westport_aldric_2026-04-22.md`의 경제 항목:
> "소금·해산물·선박 수리 서비스·Nomen 섬 방면 교역"

**판단 근거**: Ceren 왕국의 핵심 국력 = **소금 독점 레버리지**. 원전 확정 발언: "성좌국조차 함부로 다루지 못하는 특수 지위". 알드릭이 Coastfen 서남 해안에서 독자 해염(海鹽)을 생산하고 이를 성좌국에 수출한다면, Ceren 소금 레버리지가 근본적으로 훼손된다. 현재 "수출 여부 미확정"이지만, Westport Aldric 경제에 소금이 명시된 상태. 이 두 왕국 소금 관계의 **방향성이 확정되지 않은 채로 양방향 교역 가능성이 동시에 열려 있는 것**이 Critical 수준의 설계 모순.

**수정 방향**:
- 대표님 결정 필요: 알드릭 해염은 자국 내 소비 전용 (= Ceren 레버리지 유지) vs 수출 허용 (= Ceren 레버리지 훼손)
- 대표님 결정 전까지 `village_saltmarsh`와 `city_westport_aldric`에 명시적 "(Ceren 소금 레버리지와 충돌 가능성 있음 — 대표님 결정 대기)" 마커 추가 권장

---

## 2. MAJOR 등급 결함

### MJ-H-01 — House Seren 명칭과 Ceren 왕국명 혼동 위험

| 항목 | 내용 |
|------|------|
| **등급** | Major |
| **유형** | 네이밍 혼동 — 독자 혼란 유발 |
| **파일** | `kingdom_aldric/houses/house_seren_2026-04-22.md` |
| **연계** | `kingdom_aldric/nobles/duke_coastfen_seren_2026-04-22.md`, `city_westport_aldric_2026-04-22.md` |

**문제 내용**: 알드릭 왕국 Coastfen 공작 가문명이 `House Seren` (세렌). 이는 Ceren 왕국(세렌 왕국, Kingdom of Ceren)의 이름과 동일 음가이다. 영문으로도 "Seren"(알드릭 귀족 가문) vs "Ceren"(왕국명)으로 철자 한 글자 차이에 불과하며, 한국어 표기에서 양쪽 모두 "세렌"이다.

- `city_westport_aldric_2026-04-22.md`에서 "행정: Coastfen 공작 Seren 관할"이라고 표기 시, 한국어 독자는 "Seren 공작"과 "세렌 왕국(Ceren)"을 구분하기 어려움.
- `heraldry_2026-04-22.md`의 가문 목록에도 "House Seren: 청색·은빛 파도·소금 결정"으로 등재됨.

**영향 범위**: 1인 개발 설계 문서 혼선, 향후 집필 시 독자 혼란, Wave 5 연동 시 가문명-왕국명 교차 오류 위험.

**수정 방향**: House Seren 명칭을 `House Seran`, `House Serwyn`, `House Coastren` 등으로 변경하거나 대표님 확인 후 확정. 현재 상태는 "명칭 충돌 보류" 마커 추가 권장.

---

### MJ-H-02 — Ceren-Aldric 남부 연대 불명확 — "공식 동맹 없음"과 서사 접점 불일치

| 항목 | 내용 |
|------|------|
| **등급** | Major |
| **유형** | 양왕국 관계 설정 불일치 |
| **파일 1** | `kingdom_aldric/history/founding_2026-04-22.md` |
| **파일 2** | `kingdom_aldric/villages/village_fenwick_2026-04-22.md` |
| **파일 3** | `kingdom_ceren/villages/village_cernfield_2026-04-22.md` |

**문제 내용**:

`history/founding_2026-04-22.md`:
> "공식 동맹 없음, 수계 분쟁 잠복"

`village_fenwick_2026-04-22.md`:
> "실질적으로는 알드릭 관할이나 Ceren 왕국과 지속적인 소규모 영토 분쟁"
> "대표님 미확정: Ceren 왕국과의 분쟁 현황"

그러나 검사 의뢰서에서 확인할 항목으로 지목된 "Ceren-Aldric 남부 연대"가 어디에도 명시적으로 확정되어 있지 않다. `village_cernfield` 설명에서는 "두 왕국 상인 혼재"로 평화적 교역 묘사, `fenwick`에서는 영토 분쟁 묘사, `history`에서는 "공식 동맹 없음"으로 세 파일이 서로 다른 톤을 갖고 있다.

**수정 방향**: 대표님 확인 후 Ceren-Aldric 관계 공식 설정 확정 필요. 현재 존재하는 세 가지 설정(평화 교역 / 영토 분쟁 잠복 / 공식 동맹 없음)은 상호 배타적이지 않으나, Wave 5 통합 전 방향성 정비 필요.

---

### MJ-H-03 — Lonwyn 어업권 분쟁 파일 연동 미확인

| 항목 | 내용 |
|------|------|
| **등급** | Major (경보 수준) |
| **유형** | 연동 파일 부재 — 검증 불가 |
| **관련** | `conflict_lonwyn_fishing_rights` 파일 (Inspector C 검토 완료 참조) |

Inspector C 보고서에서 "Lonwyn 어업권 분쟁 파일 PASS"로 명시되었으나, 해당 파일(`conflict_lonwyn_fishing_rights_2026-04-22.md` 또는 유사 경로)이 kingdom_aldric 스코프 내에서 발견되지 않았다. Wave 4 kingdom_aldric 파일 55개 중 "fishing_rights" 키워드 파일이 없음.

`kingdom_aldric/nobles/duke_coastfen_seren_2026-04-22.md`에서는 "잠복 어업권 분쟁"이 언급되나, 해당 분쟁을 상세 처리한 전용 파일의 존재·위치가 불명확.

**수정 방향**: `conflict_lonwyn_fishing_rights` 파일 경로 확인 후 kingdom_aldric 스코프와 정합성 검증 권장. 현재로서는 파일 부재로 검증 불완전.

---

### MJ-H-04 — Aldric III 파일 Q-CORE 2 인용 섹션 "할배" 노출 (CR-H-01 보완)

CR-H-01에서 파일3로 분류. 해당 파일은 Royal 카테고리 문서로, 작업 노트가 아닌 캐릭터 문서이므로 독자 노출 가능성이 높아 별도 Major로도 분류.

| 항목 | 내용 |
|------|------|
| **등급** | Major (CR-H-01과 연계) |
| **파일** | `kingdom_aldric/royals/previous_king_aldric_iii_2026-04-22.md:21` |
| **내용** | `[필독 3] Q-CORE 2 memory > "할배의 현재 활동..."` |

CR-H-01 수정 시 함께 처리.

---

### MJ-H-05 — Greenvale 행정 귀속 불명확

| 항목 | 내용 |
|------|------|
| **등급** | Major |
| **유형** | 행정 귀속 미확정 |
| **파일** | `kingdom_aldric/cities/city_greenvale_2026-04-22.md` |

```
| **행정** | Coastfen 또는 Lonwynshire 공작 관할 (대표님 미확정) |
```

두 공작령 중 어느 쪽인지 미확정. 세금 귀속·군사 배치·Wave 5 연동 시 오류 원인. 단순 미확정 사항이나 양 공작령 파일(`duke_coastfen_seren`, `duke_lonwynshire_vaeron`)에서도 Greenvale 귀속 언급이 없어 상호 불일치.

**수정 방향**: 대표님 결정 또는 지리적 위치(남부 초원 = Coastfen에 가까움) 기준으로 잠정 확정 권장.

---

### MJ-H-06 — Cernmere 00_overview Q-CORE 2 분포 표의 마을 불일치

| 항목 | 내용 |
|------|------|
| **등급** | Major |
| **유형** | 내부 인덱스 vs 실제 파일 불일치 |
| **파일** | `kingdom_ceren/00_overview.md:108-113` |

00_overview.md의 Q-CORE 2 간접 단서 분포 표:
```
| 우물 정화 | Mistlyn · Reedwick | "이름 없는 학자가 우물 정화 주문을 가르쳤다" 구전 |
```

**실제 파일 확인 결과**:
- `village_mistlyn_2026-04-22.md` (Wave 2): Q-CORE 2 관련 서술 **없음**. "달 숭배 전통"만 언급.
- `village_reedwick_2026-04-22.md` (Wave 2): Q-CORE 2 관련 서술 **없음**. 단순 어촌 묘사.

실제 Q-CORE 2 마을 단서가 있는 파일은 `village_saltfen`, `village_marshcroft`, `village_drenfold`, `village_grayfen`이며, 이는 overview 표에 없다.

**수정 방향**: `00_overview.md` Q-CORE 2 분포 표를 실제 파일 내용과 동기화. Mistlyn·Reedwick은 삭제 또는 "(Wave 5 추가 예정)"으로 표기. Saltfen·Marshcroft·Drenfold·Grayfen 추가.

---

## 3. MINOR 등급 결함

### MI-H-01 — Wave 2 마을 파일 (Reedwick, Mistlyn, Brookwick, Ferncroft, Stillwater) frontmatter qcore_version 누락

| 항목 | 내용 |
|------|------|
| **등급** | Minor |
| **파일** | `village_reedwick`, `village_mistlyn` (Ceren Wave 2) / `village_brookwick`, `village_ferncroft`, `village_stillwater` (Aldric Wave 2) |
| **문제** | frontmatter에 `qcore_version: v1.0` 필드 없음 |

Wave 2 Toponymist 산출물이므로 의도적 누락이나, Wave 4 상속 시 version 명시 관례와 불일치.

**수정 방향**: Wave 5 통합 시 일괄 추가. 현재는 보류 허용.

---

### MI-H-02 — Cernmere 00_overview 총 파일 수 불일치 가능

| 항목 | 내용 |
|------|------|
| **등급** | Minor |
| **파일** | `kingdom_ceren/00_overview.md` 파일 인덱스 섹션 |

파일 인덱스 섹션 실제 파일 수와 Glob 결과(53개) 일치 여부를 개략 확인한 결과 전반적으로 일치하나, 일부 하위 경로가 Wave 2 원본 vs Wave 4 업그레이드 구분 없이 혼재. 인덱스 구조 자체는 문제 없음. Minor.

---

### MI-H-03 — village_grayfen 타종족 은신 "(추정)" 마커만으로는 FAIL-002 경계

| 항목 | 내용 |
|------|------|
| **등급** | Minor |
| **파일** | `kingdom_ceren/villages/village_grayfen_2026-04-22.md:22` |
| **내용** | `비고: 타종족 은신 공동체 인접 가능성 (추정 · 대표님 미확정)` |

FAIL-002 원칙상 "(추정)" 마커는 있으나, "대표님 미확정" 병기 방식이 규정과는 정합적. 다만 타종족은 발언 8 기반 설계이므로 직접 언급의 강도가 높은 편. 현재는 패스 수준이나 Wave 5 기록화 시 강도 조정 권장.

---

### MI-H-04 — 알드릭 III 선왕 재위 기간 추정치 내부 불일치

| 항목 | 내용 |
|------|------|
| **등급** | Minor |
| **파일** | `kingdom_aldric/royals/previous_king_aldric_iii_2026-04-22.md` |
| **내용** | `재위 약 30년 (추정 · 대표님 미확정)` |

kingdom_aldric 역사 파일(`history/founding_2026-04-22.md`)에서 연대 언급 없음. Aldric IV가 48세이므로 선왕 재위 30년이면 Aldric IV 18세 즉위 계산. 불합리하지 않으나 근거 없는 추정. "(추정)" 마커는 있으므로 PASS에 가까우나 Wave 5 연대기 충돌 위험. Minor 보류.

---

### MI-H-05 — Cernmere capital_map Q-CORE 2 단서 중복 (Loravern도 동일 소재)

| 항목 | 내용 |
|------|------|
| **등급** | Minor |
| **파일** | `capital_map_2026-04-22.md:33` + `city_loravern_2026-04-22.md:33` |

양쪽 모두 "물고기 보존 주문"이 Q-CORE 2 단서로 기재됨. 동일 소재를 두 파일이 독립적으로 기술. 중복 자체는 위반이 아니나, Wave 5 통합 시 같은 전설이 두 곳에서 유래한 것처럼 혼선될 수 있음.

---

### MI-H-06 — Aldric heraldry House Seren 문장에 "소금 결정" 등장

| 항목 | 내용 |
|------|------|
| **등급** | Minor |
| **파일** | `kingdom_aldric/heraldry_2026-04-22.md:52` |
| **내용** | `House Seren: 청색·은빛 파도·소금 결정` |

Coastfen 공작 House Seren의 문장에 "소금 결정"이 사용됨. Ceren 왕국의 소금 결정 왕관·모자이크와 동일 소재. 소금은 Aldric 서남 해안에서도 생산되므로 비논리적이지 않으나, Ceren 소금 정체성과 시각적 혼선 가능. Minor.

---

### MI-H-07 — Ironstrand 도시 파일 표제 불일치 (Ironstrand vs Irondelta South)

| 항목 | 내용 |
|------|------|
| **등급** | Minor |
| **파일** | `kingdom_ceren/cities/city_irondelta_south_2026-04-22.md` |

파일명은 `city_irondelta_south_2026-04-22.md`이나 문서 내부 제목은 "Ironstrand (아이론스트랜드)". 행정 귀속은 "Deltawatch 공작령 Irondelta 백작령 주요 도시"로 되어 있어 파일명의 "_irondelta_south"와 내부 명칭 "Ironstrand"가 이중 존재.

**수정 방향**: 파일명과 내부 이름 통일 필요 — Ironstrand로 통일하거나 Irondelta South로 통일하도록 대표님 확인 권장.

---

### MI-H-08 — Lonwyn capital_map 왕궁 이름 미확정 (양 왕국 수도 공통)

| 항목 | 내용 |
|------|------|
| **등급** | Minor |
| **파일** | `kingdom_aldric/capital_map_2026-04-22.md` |
| **내용** | `대표님 미확정: 왕궁 이름·별칭` |

Cernmere는 "실리파 궁전(Sellypha Palace)"으로 확정. Lonwyn 왕궁은 이름 미확정. `city_lonwyn_2026-04-22.md`에서도 "알드릭 왕궁"으로만 표기. Wave 5 Chronicler 의존 항목. 현재 Minor.

---

## 4. Q-CORE 2 단서 분포 요약

### 4-1. 세렌 왕국 (kingdom_ceren) Q-CORE 2 단서 현황

| 파일 | 단서 유형 | 표현 방식 | 준수 여부 |
|------|---------|---------|---------|
| `00_overview.md:104-114` | 분포 인덱스 | 간접 단서 목록 | PASS (단, 표 내용 불일치 → MJ-H-06) |
| `festivals/festival_salt_harvest_2026-04-22.md` | 축제 3일차 추모 의례 | "이름 없는 학자" 간접 기재 | PASS |
| `festivals/festival_swamp_fire_night_2026-04-22.md` | 이야기 축제 구전 | 간접 단서 섹션 별도 기재 | PASS |
| `cities/city_cernmere_2026-04-22.md:45` | 뱃사공 조합 전설 | "물고기 보존 주문 전래" 간접 | PASS |
| `cities/city_loravern_2026-04-22.md:33` | 어시장 노점 소문 | "보존 주문 공짜 알려준다" | PASS (단, Cernmere와 중복 소재) |
| `villages/village_saltfen_2026-04-22.md:21` | 마을 우물 전설 | "이름 없는 학자 정화 주문" | PASS |
| `villages/village_marshcroft_2026-04-22.md:21` | 마을 약초 전설 | "낯선 노인이 정화법 알려줬다" | PASS |
| `villages/village_drenfold_2026-04-22.md:22` | 고문서 단편 | "이름 모를 치유자" 추정 | PASS |
| `villages/village_grayfen_2026-04-22.md:21` | 목격 전설 | "안개 속 노인" 목격 구전 | PASS (강도 주의 → MI-H-03) |
| `royals/prince_daran_sellypha_2026-04-22.md:63` | 왕자 서사 접점 | "이름 없는 학자" 필사 메모 | PASS |
| `00_overview.md:41` | **원전 인용 섹션** | **"할배" 직접 코드명** | **FAIL → CR-H-01** |

**Ceren 총 단서 파일 수**: 10개 파일 (중복 소재 포함)  
**위반**: 1건 (CR-H-01)

---

### 4-2. 알드릭 왕국 (kingdom_aldric) Q-CORE 2 단서 현황

| 파일 | 단서 유형 | 표현 방식 | 준수 여부 |
|------|---------|---------|---------|
| `festivals/festival_lake_offering_2026-04-22.md:63` | 호수 축제 역병 이야기 | "이름 모를 늙은 학자" 간접 | PASS |
| `festivals/festival_founding_day_2026-04-22.md:62` | 건국 기념일 고문서 | "이름을 알 수 없는 방랑 학자" | PASS |
| `capital_map_2026-04-22.md:79` | 길드가 우물 정화 기록 | "이름 모를 방랑 학자" 간접 | PASS |
| `cuisine_2026-04-22.md:69` | 어부 길드 연감 | "이름 모를 방랑 학자" 간접 | PASS (capital_map과 동일 사건 중복) |
| `villages/village_reedholm_2026-04-22.md:45` | 마을 구전 | "호수 건너 오는 노인" 간접 | PASS |
| `villages/village_pearlcove_2026-04-22.md:45` | 마을 구전 2번째 | "배 타고 건너온 노인" 간접 | PASS |
| `villages/village_clearwater_2026-04-22.md:42` | 우물 석판 | "이름 모를 노인의 주문" | PASS |
| `royals/previous_king_aldric_iii_2026-04-22.md:48` | 왕실 연감 기록 | "이름 모를 방랑 학자" 간접 | PASS |
| `00_overview.md:28` | **원전 인용 섹션** | **"할배 = '마법 잘 아는 착한 노인'"** | **FAIL → CR-H-01** |
| `royals/previous_king_aldric_iii_2026-04-22.md:21` | **원전 인용 섹션** | **"할배의 현재 활동"** | **FAIL → CR-H-01** |
| `villages/village_reedholm_2026-04-22.md:18` | **원전 인용 섹션** | **"할배 = '마법 잘 아는 착한 노인'"** | **FAIL → CR-H-01** |

**Aldric 총 단서 파일 수**: 11개 파일 (중복 포함)  
**위반**: 3건 (CR-H-01 연속)

---

### 4-3. 양왕국 통합 Q-CORE 2 단서 통계

| 항목 | Ceren | Aldric | 합계 |
|------|-------|--------|------|
| 파일 내 간접 단서 (PASS) | 9 | 8 | 17 |
| 원전 인용 섹션 내 직접 노출 (FAIL) | 1 | 3 | 4 |
| 단서 유형 — 우물/정화 주문 | 3 | 3 | 6 |
| 단서 유형 — 식품 보존 주문 | 2 | 1 | 3 |
| 단서 유형 — 전설 구전 | 2 | 3 | 5 |
| 단서 유형 — 고문서/연감 기록 | 1 | 2 | 3 |

**특이 사항**: Ceren 단서 밀도(파일당 비율)가 Aldric보다 높음 — 에이전트 지시 "Ceren이 가장 높은 침투율"이 실제로 구현됨.

---

## 5. 주요 통과 항목

| 항목 | 내용 | 판정 |
|------|------|------|
| Naming Set B 준수 | Elucia, Karzor, Azim Pass 등 — 모든 파일에서 올바르게 사용 | PASS |
| 26 정치 단위 준수 | Ceren·Aldric 소왕국 표기, 성좌국·Karzor 참조 — 위반 없음 | PASS |
| Cernmere 동문 동쪽 방향 = Sylren | capital_map 성벽 구역에서 "동문 (Sylren 가도)"로 일치 | PASS |
| Q-CORE 1 (마족왕 ≠ 할배) | 두 왕국 어디에서도 마족왕과 할배 동일시 표현 없음 | PASS |
| Q-CORE 3 (크리스탈 분류) | 두 왕국에서 크리스탈 관련 서술 없음 (무관 왕국) | N/A |
| 소금 레버리지 핵심 일관성 | Ceren 왕국 전 파일에서 "소금이 곧 권력" 원칙 일관 적용 | PASS |
| 타종족 은신 처리 (Grayfen, Mistlyn, Mistfell, Lochvane) | 모두 "(추정)", "대표님 미확정" 마커 적용 | PASS |
| FAIL-002 준수 (미확정 항목 "(추정)"·마커) | 대부분 파일에서 미확정 항목 적절히 표기 | PASS |
| Wave 2 파일 상속 처리 | Wave 4 파일에서 Wave 2 인용 섹션 적절히 계승 | PASS |
| 백조 기사단 서사 일관성 | Swan Return Festival, 왕자 Loryn, order_swan 파일 상호 일치 | PASS |
| 실렌(Sylren) 왕비 혼인 동맹 | queen_sylren_mora, history/founding, duke_coastfen_seren 일치 | PASS |
| 알드릭 4세 Lonwyn 어업권 분쟁 | Inspector C 보고서 PASS 확인. 본 검사에서 재위반 없음 | PASS |

---

## 6. 종합 판정

| 등급 | 건수 | 파일 수 |
|------|------|---------|
| **Critical** | 2건 | 4개 파일 |
| **Major** | 6건 | 8개 파일 |
| **Minor** | 8건 | 10개 파일 |
| **Pass** | — | 약 86개 파일 |

---

## 7. 수정 우선순위 (Fix 권장 순서)

| 우선순위 | 코드 | 내용 | 담당 |
|---------|------|------|------|
| 1 | CR-H-01 | 4개 파일 "할배" 코드명 → "[Q-CORE 2 주체]" 대체 | Fix-Integrator |
| 2 | CR-H-02 | Aldric 소금 수출 여부 대표님 결정 대기 마커 추가 | 대표님 결정 후 Fix |
| 3 | MJ-H-01 | House Seren 명칭 변경 검토 | 대표님 결정 |
| 4 | MJ-H-06 | 00_overview Q-CORE 2 분포 표 실제 파일과 동기화 | Fix-Integrator |
| 5 | MJ-H-07 | Ironstrand/Irondelta South 명칭 통일 | 대표님 결정 |
| 6~8 | MJ-H-02/03/05 | Ceren-Aldric 관계 확정, 어업권 파일 경로 확인, Greenvale 귀속 결정 | 대표님 결정 |
| 9~16 | MI-H-01~08 | Wave 5 통합 시 일괄 처리 가능 | 차기 Wave |

---

## 8. 다음 Wave 의존 사항 (Wave 5 Chronicler/World-Integrator)

**Ceren**:
- 소금 수확제 기원 전설 문헌화
- 백조 귀환제 유사 항목 없음 (Ceren만의 "안개 의례" Wave 5 추가 권장)
- 실리파 왕조 건국 설화·초대 여왕 이름 확정
- 습지 고어 어휘 추가 확정

**Aldric**:
- 호수 성당 설립 역사·교단 귀속 확정
- 담수 진주 교역 역사 공식 연대기
- "호수 건너 오는 노인" 전설 2건(Reedholm·Pearlcove) 통합 문헌화
- 백조 기사단 창설 역사
- 왕궁 공식 명칭·별칭 확정

---

*보고서 작성: Wave 4 2차 검사관 H — 2026-04-22*  
*다음 연동: fix_log_2026-04-22.md 갱신 + 대표님 결정 항목 취합*
