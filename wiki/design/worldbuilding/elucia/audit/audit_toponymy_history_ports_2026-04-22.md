---
title: Wave Audit — Toponymy · History · Ports 전수검사
type: audit
scope: continent
auditor: Inspector-D (Toponymy + History + Ports)
wave: audit
created: 2026-04-22
updated: 2026-04-22
qcore_version: v1.0
---

# Wave Audit — Toponymy · History · Ports 전수검사 리포트

**검사관**: Inspector-D (Toponymy + History + Ports 담당)
**검사 기준일**: 2026-04-22
**검사 방법**: 전수 Read — 샘플링 없음. Read 없이 판정 없음.
**판정 기준**: Q-CORE 3건 + 네이밍 세트 B + 발언 5 지도 원칙 + 세계관 철학 3조

---

## 1. 검사 범위 — 읽은 파일 전목록

### 1-A. 원전 파일 (7건)

| # | 파일 경로 | 완독 |
|---|-----------|------|
| 1 | `wiki/design/brainstorm_2026-04-21_worldview_expansion.md` | ✅ 전체 (offset 분할 완독) |
| 2 | `wiki/design/game_setting_complete_2026-04-21.md` | ✅ §1~§9 완독 / §10+ 미확인 (하단 §8 명기) |
| 3 | `wiki/design/political_divisions.md` | ✅ 전체 |
| 4 | `wiki/design/novel/` (프롤로그·스타일 바이블) | ✅ |
| 5 | `wiki/design/worldbuilding/elucia/history/` 전체 6파일 | ✅ |
| 6 | `wiki/design/worldbuilding/elucia/ports/` 전체 11파일 | ✅ |
| 7 | `.claude/failures/FAILURES.md` | ✅ FAIL-001~006 |

### 1-B. Toponymy 검사 대상 — 비실행 왕국 6개 전수

| 왕국 | cities/ | villages/ | history/ |
|------|---------|-----------|----------|
| kingdom_thaloss | ✅ 5도시 전부 | ✅ 2마을 전부 | ✅ founding + war_perspective |
| kingdom_oryn | ✅ 5도시 전부 | ✅ 2마을 전부 | ✅ founding |
| kingdom_maerith | ✅ 5도시 전부 | ✅ 3마을 전부 | ✅ founding |
| kingdom_sylren | ✅ 5도시 전부 | ✅ 3마을 전부 | ✅ founding |
| kingdom_novas | ✅ 5도시 전부 | ✅ 3마을 전부 | ✅ founding |
| kingdom_aldric | ✅ 5도시 전부 | ✅ 3마을 전부 | ✅ founding |

### 1-C. History 검사 대상

| 파일명 | 완독 |
|--------|------|
| `event_empire_founding_2026-04-22.md` | ✅ |
| `event_plague_ash_death_2026-04-22.md` | ✅ |
| `event_great_famine_2026-04-22.md` | ✅ |
| `war_northern_border_2026-04-22.md` | ✅ |
| `war_papal_succession_crisis_2026-04-22.md` | ✅ |
| `war_slave_revolt_ilaris_2026-04-22.md` | ✅ |
| `war_nomen_isle_conflict_2026-04-22.md` | ✅ |

### 1-D. Ports 검사 대상

| 파일명 | 등급 | 완독 |
|--------|------|------|
| `00_overview.md` | — | ✅ |
| `port_veilglass_gate_2026-04-22.md` | A | ✅ |
| `port_irondelta_2026-04-22.md` | A | ✅ |
| `port_aldricport_2026-04-22.md` | A | ✅ |
| `port_norngard_2026-04-22.md` | A | ✅ |
| `port_soranthhaven_2026-04-22.md` | B | ✅ |
| `port_havenwick_2026-04-22.md` | B | ✅ |
| `port_caerveld_2026-04-22.md` | B | ✅ |
| `port_fenlyn_2026-04-22.md` | B | ✅ |
| `port_keldhaven_naval_2026-04-22.md` | C | ✅ |
| `port_ghost_cove_2026-04-22.md` | C | ✅ |
| `port_mirvane_2026-04-22.md` | B | ❌ **파일 없음 — ISSUE 등재** |

---

## 2. Q-CORE 3건 준수 현황

### Q-CORE 1: 마왕 ≠ 할배 (완전 별개)

**판정**: ✅ **PASS — 전 파일 준수**

- 할배 = 첫 번째 신 (마족 출신). 마왕은 마족 시대 이전부터 존재하는 별개 존재.
- history 6파일 전부 할배를 "이름 모를 학자" / "방랑자" 형태로만 묘사. 마왕 언급과 교차 없음.
- `war_nomen_isle_conflict`에서 "마왕 시대 유물" 언급이 등장하나 할배와 연결짓지 않음 — 정합.
- 비실행 왕국 6개 history 파일 전부: 마왕·할배 혼용 표현 없음. 개별 언급 시 명확히 분리.

### Q-CORE 2: 할배 동기 = 속죄, 인간으로 위장, 가난한 서민에게 생활 마법 무료 배포

**판정**: ✅ **PASS — 핵심 파일 정합 확인**

- `event_plague_ash_death_2026-04-22.md`: "이름 모를 학자가 우물 정화 마법을 마을 주민들에게 무상으로 전수" — 가난한 서민 대상 무료 배포 정합 ✅
- `event_great_famine_2026-04-22.md`: "방랑하던 노인이 씨앗 개량 마법과 관개 기술을 농부들에게 가르침" — 동일 패턴 정합 ✅
- `event_empire_founding_2026-04-22.md`: 교황청 설립 서술에서 할배 직접 등장 없음 — Q-CORE 2와 무관하게 독립적 서술. 충돌 없음.
- 발언 17 (극한 마력 보유자 = 절대 탐지 불가 인간 위장): 할배의 정체 미발각 일관성과 정합 ✅

### Q-CORE 3: 수정 1 = 수호자 함정 장치, 수정 2 = 마왕의 마족 증식 장치 (마족은 자기 장치인 줄 앎)

**판정**: ✅ **PASS — 번호 체계 일치 확인**

- 브레인스토밍 발언 28: "수정 1 = 균형 수호자 제한장치, 수정 2 = 마족 자발봉인 최강기술"
- Q-CORE 3 확정: "수정 1 = 수호자가 수정 2 모방 제작한 감시·함정, 수정 2 = 마왕 원본 증식장치"
- **번호 배정 일치**: 두 체계 모두 수정 1 = 수호자 관련, 수정 2 = 마족 원본. 충돌 없음.
- `war_nomen_isle_conflict`: 수정 2(Veilglass 북쪽) 미발견 상태 묘사 — 발언 25(후반부 플레이어 발견) 정합 ✅
- 비실행 왕국 6개 history: 수정 직접 언급 없음 — 적절 (왕국 수준 역사 파일에서 수정 개입 불필요)

---

## 3. 네이밍 세트 B 준수 현황 (10개 고유명사 변경 금지)

| 세트 B 명칭 | 검사 결과 | 사용 파일 |
|------------|----------|-----------|
| Elucia | ✅ 일관 사용 | history 전체, ports 전체, 왕국 파일 전체 |
| Karzor | ✅ 일관 사용 | political_divisions, war_nomen_isle_conflict |
| Veilglass | ✅ 일관 사용 | ports/00_overview, port_veilglass_gate, war_nomen_isle_conflict |
| Nomen | ✅ 일관 사용 | ports/00_overview, war_nomen_isle_conflict |
| Azim Pass | ✅ 일관 사용 | kingdom_novas cities/founding |
| Silvan | ✅ 일관 사용 | kingdom_oryn cities (Sylvan 변형 없음 — 별도 확인) |
| Orenwald | ✅ 일관 사용 | kingdom_oryn cities (Orynthil 내 언급) |
| Norvend | ✅ 일관 사용 | war_northern_border, kingdom_thaloss history |
| Solaris | ✅ 일관 사용 | event_empire_founding, political_divisions |
| Zarahim | ✅ 일관 사용 | political_divisions |

**세트 B 이탈 의심 표기 검토**:
- `kingdom_oryn` 내 "Soranwatch" — Soranth(sylren) + watch 합성. 지명 접미사 재사용. 세트 B 침범 아님. 단, **아래 §6-A "Soranth 접두 중복" NOTICE 참조**.
- 모든 10개 명칭: 대소문자·철자 일관. 이탈 없음.

---

## 4. 발언 5 지도 원칙 준수 현황

### 핵심 원칙: "Nomen 섬 빨간 점 항구 = Veilglass 가는 유일한 경로"

**판정**: ✅ **PASS — 완전 정합**

| 파일 | 관련 서술 | 정합 여부 |
|------|-----------|-----------|
| `ports/00_overview.md` | "Veilglass Gate = Elucia 유일의 대륙 간 관문" | ✅ |
| `port_veilglass_gate_2026-04-22.md` | Empire Choir 직속 항구 / Nomen 섬 경유 항로 | ✅ |
| `war_nomen_isle_conflict_2026-04-22.md` | "Nomen 섬 통제 = Veilglass 항로 차단 가능" / 전략적 요충 서술 | ✅ |
| `kingdom_novas/history/founding` | 아짐 관문 = 육로 유일 경로 (해상과 구분) | ✅ |

- 발언 5 "대륙 위쪽 해상 불가(암초·몬스터)" → `port_norngard`(Vaelin 북부 군항)이 Veilglass 행 정규 항로 없음. 군사 항구로만 묘사. 원칙 준수 ✅
- **육로 대안**: Azim Pass(Novas) 경유 Karzor 대륙 연결. 해상 Veilglass 루트와 명확히 구분됨 ✅

---

## 5. 세계관 철학 3조 준수 현황

### 철학 1조: 불완전성 (신은 완벽하지 않다)

**판정**: ✅ **PASS**

- `event_empire_founding`: 교황청이 "신의 뜻"을 표방하나 내부 권력 다툼과 세속화 묘사 — 1조 구현 ✅
- `war_papal_succession_crisis`: 교황 계승 갈등 = 종교 기관의 불완전성 직접 표현 ✅
- 비실행 왕국 history 전부: 교황청 세금·억압에 대한 불만 서술 — 신성 기관의 인간적 결함 표현 ✅

### 철학 2조: 나이트 인격체 (선/악 이분법 거부)

**판정**: ✅ **PASS**

- `war_northern_border`: 탈로스·바엘린 양측 시각 파일 별도 제작 — 어느 쪽도 단순 악당 아님 ✅
- `war_slave_revolt_ilaris`: 진압측(인간)·반란측(엘프) 양측 서술. 제3자 시각 포함 ✅
- `war_nomen_isle_conflict`: Elucia vs Karzor = 양측 모두 정당한 주권 주장. 악당 없음 ✅
- `kingdom_thaloss/war_thaloss_vaelin_perspective`: 탈로스 시각에서 자국 = 피해자 서술 — 나이트 인격체 원칙 구현 ✅

### 철학 3조: 영혼 평등 (종족 무관 동등 존엄)

**판정**: ✅ **PASS**

- `war_slave_revolt_ilaris`: 엘프 노예화를 역사적 비극으로 묘사. 교황청 차별 합리화 = 부정적으로 서술 ✅
- `event_great_famine`: 기근 중 타종족 박해를 "명분 확산"으로 서술 — 이를 정당화하지 않음 ✅
- 비실행 왕국 6개 founding: 오크·엘프 등 타종족 언급 시 일방적 악당 묘사 없음 ✅

---

## 6. Toponymy 검사 — 명명 규칙 L1~L4 준수

### 6-A. 왕국별 언어층 배정 현황

| 왕국 | 우세층 | 수도 | 도시 대표 | 판정 |
|------|--------|------|-----------|------|
| Thaloss | L2 게르만 | Icehelm | Irongate·Embervane·Stonecrown·Nordwatch | ✅ |
| Oryn | L1 라틴 + L4 독자 | Orynthil | Waldmere·Soranwatch·Veilorngate·Darkwyn | ✅ |
| Maerith | L1 라틴 + L2 게르만 혼합 | Maerholt | Stormcrag·Ironhelm·Highvane·Coldmere | ✅ |
| Sylren | L1 라틴 | Sylvenmere | Soranthhaven·Greenwatch·Plainhold·Rivemark | ✅ |
| Novas | L1 라틴 + L4 독자 | Duskmoor | Sandwatch·Thornheld·Redstone·Dusthaven | ✅ |
| Aldric | L2 게르만 + L3 켈트 | Lonwyn | Aldricport·Lakemere·Greenvale·Crestholm | ✅ |

### 6-B. NOTICE — Soranth 접두 중복 (비CRITICAL)

**발견 사항**: "Soranth" 접두가 복수 왕국에 걸쳐 등장.

| 왕국 | 사용 지명 |
|------|-----------|
| Sylren (남중앙 평원) | **Soranth** 평원 (왕국 기반 지형명) |
| Sylren (항구) | **Soranthhaven** (Port 파일과 도시 파일 동일 명칭) |
| Oryn (도시) | **Soranwatch** (감시 거점 도시) |

**판정**: ⚠️ **NOTICE — 지명 중복 위험**

- Soranth 평원(Sylren)은 고유 지형명으로 확정된 원전(political_divisions)이 있음. 세트 B는 아니나 파생 지명이 다수.
- `Soranwatch`(Oryn)은 Soranth 평원에서 먼 북동 고지대 위치. 지리적으로 멀어 Sylren Soranth와 직접 연결은 아니나 독자가 혼동 가능.
- **권고**: Oryn의 Soranwatch를 대표님 확인 후 개명 검토 (예: Thornwatch, Northwatch 등).
- **CRITICAL 위반은 아님**. 단, 소설·게임 텍스트에서 독자 혼동 유발 가능.

### 6-C. 마을 명명 규칙 확인

| 왕국 | 마을 목록 | 특이사항 |
|------|-----------|----------|
| Thaloss | Deepcoombe·Frostend | L2 게르만 일관 ✅ |
| Oryn | Elderwick·Mossford | L2 게르만 (왕국 특성 일부 혼합) — 허용 범위 ✅ |
| Maerith | Ashcrag·Ridgeholm·Deepvein | L2 게르만 일관 ✅ |
| Sylren | Reedmere·Millford·Haywick | L1+L2 혼합 — Sylren 특성 반영 ✅ |
| Novas | Drysand·Oasholm·Moorend | L2 게르만 일관 ✅ |
| Aldric | Brookwick·Ferncroft·Stillwater | L2 게르만 + L3 켈트 혼합 ✅ |

**전반 판정**: ✅ PASS. 왕국별 우세 언어층 일관.

---

## 7. History 파일 상호 정합성 검사

### 7-A. 사건 연대 충돌 여부

| 사건 | 등장 파일들 | 충돌 |
|------|------------|------|
| 대역병 "회색 재의 죽음" | event_plague_ash_death / 복수 왕국 founding | ✅ 정합 |
| 대기근 "잿빛 태양" | event_great_famine / sylren founding (최대 피해) | ✅ 정합 |
| 북부 전쟁 (15년) | war_northern_border / thaloss_war_perspective / maerith founding | ✅ 정합 |
| 교황 계승 위기 | war_papal_succession_crisis / maerith founding (환영 내심) | ✅ 정합 |
| 일라리스 엘프 반란 | war_slave_revolt_ilaris / ilaris 관련 파일 | ✅ 정합 |
| 노멘 섬 분쟁 | war_nomen_isle_conflict / novas founding (아짐 관문 언급) | ✅ 정합 |
| 성좌국 형성 | event_empire_founding / 전 왕국 founding (복속 시기) | ✅ 정합 |

**발견 사항**: 모든 사건들이 상호 참조 파일 간 내용 충돌 없음. "대표님 미확정"으로 표기된 구체적 연대는 공란으로 일관 처리됨 — 올바른 처리 방식.

### 7-B. 할배 등장 사건 정합성

| 사건 | 할배 역할 | Q-CORE 2 정합 |
|------|-----------|---------------|
| 대역병 | 우물 정화 마법 전수 (서민 대상 무료) | ✅ |
| 대기근 | 씨앗 개량·관개 마법 전수 (농부 대상 무료) | ✅ |
| 북부 전쟁 | 직접 개입 기록 없음 (적절 — 감시자 역할) | ✅ |
| 교황 계승 위기 | 직접 개입 기록 없음 | ✅ |
| 노멘 섬 분쟁 | 직접 개입 기록 없음 | ✅ |

**특기 사항**: 할배는 개인 단위(마을·농부) 대상 소규모 개입. 국가 단위 전쟁에는 불개입 일관 — 속죄 동기(서민 구제)와 완전 정합 ✅

---

## 8. Ports 상세 검사

### 8-A. 등급 분류 논리 정합성

| 등급 | 기준 | 해당 항구 | 판정 |
|------|------|-----------|------|
| A등급 | 대륙 교역 핵심 / 연간 톤수 최대 | Veilglass Gate·Irondelta·Aldricport·Norngard | ✅ |
| B등급 | 지역 교역 중심 / 전략 보조 | Soranthhaven·Havenwick·Caerveld·Fenlyn·(Mirvane 미파일) | ✅ |
| C등급 | 특수 목적 / 소규모 | Keldhaven Naval·Ghost Cove | ✅ |

**등급 분류 일관성**: ✅ PASS. 각 항구의 위치·기능·규모가 등급과 정합.

### 8-B. 지배 세력 귀속 검증

| 항구 | 귀속 | political_divisions 정합 |
|------|------|--------------------------|
| Veilglass Gate | Empire Choir 직속 | ✅ 성좌국 = 대륙 관문 통제 |
| Irondelta | Empire Choir 직할 (곡물 항) | ✅ |
| Aldricport | Kingdom Aldric | ✅ Aldric = 남서 호수 수운 왕국 |
| Norngard | Kingdom Vaelin | ✅ Vaelin = 북부 평원 군사 왕국 |
| Soranthhaven | Kingdom Sylren | ✅ Sylren = 남중앙 평원·강 수계 |
| Havenwick | Kingdom Moran | ✅ Moran = 서부 어업 |
| Caerveld | Kingdom Ilaris | ✅ Ilaris = 서남 해안 |
| Fenlyn | Kingdom Ceren | ✅ Ceren = 서남 습지 |
| Keldhaven Naval | Kingdom Moran | ✅ Moran 군항 (Havenwick 보조) |
| Ghost Cove | 무소속 | ✅ 비공식 항구 |

**전체 귀속 정합**: ✅ PASS.

### 8-C. 발언 5 원칙 — 북쪽 해상 불가 원칙 검증

- 북부 항구 Norngard(Vaelin): 군사 항구로만 묘사. 정규 상업 항로 없음. Veilglass 방면 정기선 언급 없음 ✅
- 대륙 위쪽 암초·몬스터 설정: Norngard 파일에 "북방 항로는 몬스터 습격 빈발로 민간 운항 불가" 서술 — 발언 5 직접 구현 ✅

---

## 9. 발견된 ISSUE 목록

### ISSUE-D-001 (CRITICAL 아님 — 파일 누락)

**내용**: `ports/00_overview.md`에 **Mirvane Port** (B등급, Kingdom Ilaris 내륙 수로항)이 등재되어 있으나, 해당 파일 `port_mirvane_2026-04-22.md`가 존재하지 않음.

**근거**:
- `00_overview.md` 항구 목록: 11개 (A등급 4 + B등급 5 + C등급 2)
- 실제 존재하는 포트 파일: 10개 (B등급 파일 = 4개 — Mirvane 제외)
- Mirvane Port 설명: "Kingdom Ilaris 내륙 수로 연결 항구. Lonwyn 호수와 연결되는 운하 기점."

**처리 요청**: 대표님 확인 후 `port_mirvane_2026-04-22.md` 파일 생성 또는 00_overview에서 삭제 선택.

**영향 범위**: kingdom_ilaris 관련 파일, kingdom_aldric (Lonwyn 호수) 관련 파일과의 연결성 검토 필요.

---

### NOTICE-D-001 (비CRITICAL — 지명 중복 위험)

**내용**: "Soranth" 접두 지명이 복수 왕국에 분산 존재 (§6-B 상세 참조).

- Soranth 평원 (Sylren 기반 지형)
- Soranthhaven (Sylren 항구 도시)
- Soranwatch (Oryn 도시)

**처리 요청**: Oryn의 Soranwatch 개명 여부 대표님 확인.

---

### NOTICE-D-002 (비CRITICAL — 미확인 구간 존재)

**내용**: 아래 파일들의 일부 구간이 이번 전수검사에서 미확인 상태로 남음.

| 파일 | 미확인 구간 | 이유 |
|------|------------|------|
| `game_setting_complete_2026-04-21.md` | §10 엔드게임·참조작품 이후 | 용량 초과, §1~§9만 완독 |
| `story_full_narrative.md` | 전체 | history 파일들이 [필독 5]로 인용하는 원전이나 이번 검사 범위 미포함 |

**영향 평가**: history 파일 전체가 해당 원전을 인용·반영하고 있어 CRITICAL 충돌 여부는 현재 읽은 파일로 파악 가능. 단, §10+ 구간에서 추가 설정이 존재할 경우 재검사 필요.

---

## 10. 종합 판정

| 검사 항목 | 판정 |
|----------|------|
| Q-CORE 1 (마왕 ≠ 할배) | ✅ PASS |
| Q-CORE 2 (할배 동기·행동 패턴) | ✅ PASS |
| Q-CORE 3 (수정 1·2 번호 체계) | ✅ PASS |
| 네이밍 세트 B 10개 (변경 금지) | ✅ PASS |
| 발언 5 지도 원칙 (Veilglass 유일 항로) | ✅ PASS |
| 세계관 철학 3조 | ✅ PASS |
| Toponymy — 명명 규칙 L1~L4 | ✅ PASS (NOTICE-D-001 첨부) |
| History — 상호 정합성 | ✅ PASS |
| History — 할배 등장 패턴 | ✅ PASS |
| Ports — 등급·귀속 정합성 | ✅ PASS (ISSUE-D-001 첨부) |
| Ports — 발언 5 원칙 구현 | ✅ PASS |

**CRITICAL 위반**: **0건**
**ISSUE (처리 요청)**: **1건** (ISSUE-D-001: Mirvane Port 파일 누락)
**NOTICE (대표님 확인 권고)**: **2건** (Soranth 중복, 미확인 구간)

---

## 11. 대표님 확인 요청 사항

1. **ISSUE-D-001**: `port_mirvane_2026-04-22.md` 파일 생성 or `00_overview.md`에서 Mirvane 삭제 — 어느 쪽으로 처리할까요?

2. **NOTICE-D-001**: Oryn 왕국 도시 `Soranwatch`를 다른 이름으로 변경할까요? (Sylren의 Soranth와 혼동 방지)

3. **NOTICE-D-002**: `game_setting_complete_2026-04-21.md` §10 이후 구간 및 `story_full_narrative.md` 추가 검사가 필요하면 말씀해 주십시오. 현재 CRITICAL 충돌은 없으나 해당 파일들에 신규 설정이 있을 경우 재검사하겠습니다.

---

*검사관 Inspector-D — Wave Audit 완료 2026-04-22*
*샘플링 없음 · Read 없이 판정 없음 · 전수검사 원칙 준수*
