---
title: "Elucia 지명 명명 규칙"
type: toponymy
subject: naming_conventions
created: 2026-04-22
updated: 2026-04-22
agent: Wave2-Toponymist
wave: 2
inputs:
  - wiki/design/political_divisions.md
  - wiki/design/brainstorm_2026-04-21_worldview_expansion.md
  - wiki/design/game_setting_complete_2026-04-21.md
  - wiki/design/worldbuilding/elucia/geography/00_overview.md
qcore_version: v1.0
---

# Elucia 지명 명명 규칙 (Naming Conventions)

## 원전 인용 증명

### [필독 1] political_divisions.md:140-146
> "FF7·Nier Automata·Disco Elysium 조어 톤: 추상·낯선·부드러움 / WoW 풍 회피: Ostvaria·Khaleqar·Auréllion 등 WoW 느낌 제거 / 고대·신비로움: Veilglass·Solaris·Zarahim 등 옛 언어 같은 울림 / 발음 가능: 모든 이름 한국어 표기 자연스러움 / 레퍼런스 직접 모사 금지"
— political_divisions.md:140-146

### [필독 2] political_divisions.md:50-62 (11 왕국 확정 이름)
> "엘루시아 성좌국 / Choir of Elucia ... 바엘린 / Vaelin ... 모란 / Moran ... 일라리스 / Ilaris ... 세렌 / Ceren ... 탈로스 / Thaloss ... 오린 / Oryn ... 마에리스 / Maerith ... 실렌 / Sylren ... 노바스 / Novas ... 알드릭 / Aldric"
— political_divisions.md:50-62

### [필독 3] brainstorm_2026-04-21_worldview_expansion.md:176 (발언 5)
> "이게 내가 그린맵, 내가 보는방향에서 좌측이 서구중세문명, 우측이 이슬람과비슷한 문명"
— 발언 5, brainstorm_2026-04-21_worldview_expansion.md:176

### [필독 4] game_setting_complete_2026-04-21.md:14-56 (세계관 철학 3조)
> "1. 불완전성 — 모든 것은 불완전하다 / 2. 한결같음 / 3. 영혼 평등 — 모든 종족의 영혼은 평등"
— game_setting_complete_2026-04-21.md

### [필독 5] .claude/failures/FAILURES.md:165-169 (FAIL-006)
> "비유·농담·메타 발언은 세계관 설정으로 승격 금지 / 대표님의 한국어 중의적 표현은 자의 해석 금지 / 이미지 프롬프트의 레퍼런스는 'inspired by tone of X' 수준으로만"
— FAILURES.md (FAIL-006 교훈)

---

## 요약

Elucia 지명은 **라틴어층·게르만어층·켈트어층·독자 조어층** 4개 층위를 혼합하여 생성한다. 각 왕국은 지리·문화 특성에 따라 우세 언어층을 달리한다. FF7·Nier Automata·Disco Elysium 의 조어 감각 — 추상적이되 발음 가능하고, 낯설되 기억 가능한 — 을 목표로 한다.

---

## 1. 4개 언어층 정의

| 층위 | 원천 | 어감 | 주 사용 왕국 |
|------|------|------|------------|
| **L1 라틴층** | 라틴어 어근 변형 | 질서·빛·공식·교회 | 성좌국 Choir·Solaris·중앙 |
| **L2 게르만층** | 고게르만·앵글로색슨 변형 | 강인·거칠·자연 | 북부 (Thaloss·Vaelin)·동부 (Oryn) |
| **L3 켈트층** | 웨일스·아일랜드 어근 변형 | 신비·부드럽·숲 | 서해안 (Ilaris·Ceren·Aldric) |
| **L4 독자 조어** | 위 3층 혼합 + 음운 규칙 독자 창작 | 고유·세계관 특수 | 모든 왕국 고유명사 |

---

## 2. 왕국별 우세 언어층 배정

| 왕국 | 권역 | 우세 층 | 이유 |
|------|------|--------|------|
| Choir of Elucia (성좌국) | Aurion | **L1 라틴** | 교황청·제국·공식 문서 문화 |
| Vaelin | Vaelin Plain | **L2 게르만** | 북부 기마 평원, 강인한 개척 문화 |
| Moran | Havren | **L2+L3** | 북서 해안, 바이킹+켈트 혼합 |
| Ilaris | Silvan | **L3 켈트** | 서해안 숲, 신비·해양·엘프 인접 |
| Ceren | Loravel | **L3 켈트** | 습지·수초·달 숭배 문화 |
| Thaloss | Norvend | **L2 게르만** | 산악 왕국, 광산·폐쇄·강인 |
| Oryn | Orenwald | **L2+L3** | 숲의 왕국, 신비로운 동부 |
| Maerith | Auryn | **L1+L2** | 고지대 귀족, 고풍스러운 어감 |
| Sylren | Soranth | **L1 라틴** | 남중앙 평원, 제국 영향권 |
| Novas | Duskmoor | **L2 게르만** | 남동 국경, 강건한 변경 문화 |
| Aldric | Lonwyn | **L3+L4** | 호수 왕국, 물·빛·신비 |

---

## 3. 지명 등급별 규칙

### 3-1. 대륙·섬·권역명 (Tier 0)
- **음절**: 2~3음절
- **구조**: 어근 + 접사 또는 순수 조어
- **규칙**: 모든 대륙·섬은 이미 확정 (세트 B). 신규 추가 없음

### 3-2. 수도·대도시 (Tier 1)
- **음절**: 2~3음절
- **규칙**: 라틴·게르만 혼합 / 끝모음 개방(-is, -us, -en, -heim)
- **예**: Solaris, Vaelthorn, Mornheld, Ilarien

### 3-3. 왕국 내 도시 (Tier 2)
- **음절**: 2~3음절
- **규칙**: 권역 우세 언어층 + 지형 어근
- **예**: Greymoor, Silverfen, Dawncliff

### 3-4. 마을·취락 (Tier 3)
- **음절**: 2음절 선호 (최대 3)
- **규칙**: 단순 어근 + 접미사 (-ton, -ford, -wick, -vale, -mere)
- **예**: Ashford, Grenwick, Elmvale

### 3-5. 지리 feature 이름 (산·강·숲)
- **음절**: 2~3음절 + 지형 유형어
- **규칙**: 특성 어근 + 지형 접미사
- **예**: Eloryn River, Norvend Range, Silvan Forest

---

## 4. 절대 금지 (FAIL-006 준수)

| 금지 유형 | 이유 | 대안 |
|---------|------|------|
| 실존 지명 직접 차용 | 레퍼런스 직접 모사 금지 | 어근만 차용·변형 |
| WoW 풍 이중자음 남발 | 조형 톤 회피 (Khaleqar 류) | 단순 자음 구조 |
| 아랍어·한자 직접 번역 | 실존 문화 직접 모사 | L4 독자 조어 |
| 3음절 초과 왕국명 | 발음 부담 | 2음절 단축형 병기 |
| 언더스코어·숫자 포함 | 세계관 몰입 저해 | 완전 알파벳 단어 |

---

## 5. 한국어 표기 원칙

모든 지명은 한국어 발음 자연스러움 우선:

| 영문 | 한국어 표기 | 검토 |
|------|-----------|------|
| Vaelthorn | 바엘손 | O |
| Mornheld | 모른헬드 | O |
| Ilarien | 일라리엔 | O |
| Eloryn | 엘로린 | O |
| Silvenmere | 실벤미어 | O |
| Dawncliff | 돈클리프 | O (도운클리프 지양) |

---

## 대표님 미확정 사항

- 왕국 내부 귀족 가문명 네이밍 스타일 — Wave 4 에서 확정 필요
- 타종족 (엘프·마족·드워프) 고유 언어층 추가 여부 — 대표님 결정 대기
- Karzor 지명 체계 (사막 문명권) — Wave 2 Toponymist 범위 외 · 별도 작업 필요

## 다음 Wave 의존 포인트

- **Kingdom-Detailer (Wave 4)**: 각 왕국 내 마을명은 해당 왕국 우세 언어층 규칙 준수
- **Historian (Wave 3)**: 고대 지명 (마족 시대·신 시대 유래 지명) 별도 어근 필요할 수 있음
- **Culturalist (Wave 2)**: 방언·지역 호칭이 공식 지명과 다를 때 대비표 필요
