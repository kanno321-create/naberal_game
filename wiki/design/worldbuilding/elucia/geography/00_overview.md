---
title: "Elucia Geography — 인덱스 (날짜 없음)"
type: geography
subject: index
created: 2026-04-22
updated: 2026-04-22
agent: Wave1-Geographer
wave: 1
---

# Elucia Geography — 인덱스

> **이 파일은 네비게이션 인덱스 전용이다. 내용 서술 금지.**
> 각 주제의 상세 내용은 아래 링크 파일을 참조할 것.

---

## 파일 목록 (Wave 1 · 2026-04-22 생성)

| 파일 | 주제 | 키 포인트 |
|------|------|---------|
| [`elevation_profile_2026-04-22.md`](elevation_profile_2026-04-22.md) | 고도 프로필·지형 Features | 5개 고도 지대·Aurion Basin·은신 지형 5곳 |
| [`mountain_ranges_2026-04-22.md`](mountain_ranges_2026-04-22.md) | 산맥 체계 | Norvend Range(주맥1)·Veilorn Ridge(주맥2)·부맥 5개·고개 3개 |
| [`coastlines_2026-04-22.md`](coastlines_2026-04-22.md) | 해안선 | 서·북·남 3구역·Veil Sea 접근불가·Azim Narrows |
| [`rivers_major_2026-04-22.md`](rivers_major_2026-04-22.md) | 대하천 6개 | Eloryn·Auravel·Lowen·Mornwell·Soranth·Duskway |
| [`rivers_tributaries_2026-04-22.md`](rivers_tributaries_2026-04-22.md) | 지류·수계 네트워크 | 27개 지류·수계 위계 4단계·국경 후보 5개 |
| [`forests_2026-04-22.md`](forests_2026-04-22.md) | 숲 8개 | Silvan(확정)·Orenwald(확정)·부속숲 6개·타종족 은신 지형 |
| [`plains_and_grasslands_2026-04-22.md`](plains_and_grasslands_2026-04-22.md) | 초원·평원 | Aurion Plain(300K km²)·Soranth·Vaelin·초원 4지대 |
| [`wetlands_and_swamps_2026-04-22.md`](wetlands_and_swamps_2026-04-22.md) | 습지·늪 | Loravel Wetlands·Lonwyn Lakelands·삼각주 습지 |
| [`climate_zones_2026-04-22.md`](climate_zones_2026-04-22.md) | 기후대 6개 | 해양성온대·대륙성온대·고산·한대전이·반건조·습지 |

---

## 확정 지명 (세트 B 계승)

| 지명 | 유형 | 파일 참조 |
|------|------|---------|
| **Elucia** | 대륙명 | — |
| **Norvend** | 북부 산맥 권역 + 주산맥 | mountain_ranges |
| **Silvan** | 서해안 숲 | forests |
| **Orenwald** | 동부 숲 | forests |
| **Veilglass** | 북쪽 얼음섬 | coastlines |
| **Nomen** | 중간 섬 | coastlines |
| **Azim Pass** | 남부 지협 통행로 | coastlines |
| **Solaris** | 성좌국 수도 (지리 배경 기준) | elevation_profile |

---

## 공식 확정 지명 (Wave 2 Toponymist · 2026-04-22 확정)

> Wave 1 Geographer 작업 가설 지명을 Wave 2 Toponymist 가 세계관 네이밍 체계에 맞춰 전원 공식화 완료.

| 확정 지명 | 유형 | 이전 가설 | 변경 여부 | 담당 파일 |
|---------|------|---------|---------|---------|
| **Icehelm Peak** | Norvend 최고봉 | Frosthelm Peak | 변경 (L2 게르만 정합) | mountain_ranges |
| **Veilorn Ridge** | 동부 경계 주맥 | Veilorn Ridge | 변경 (Veil 세트B 계승) | mountain_ranges |
| **Greygate Pass** | Norvend 서 주고개 | Greygate Pass | 유지 (적합) | mountain_ranges |
| **Ironcleft Pass** | Norvend 중앙 고개 | Ironcleft Pass | 유지 (적합) | mountain_ranges |
| **Whitecrest Saddle** | Norvend 동 안부 | Whitecrest Saddle | 유지 (적합) | mountain_ranges |
| **Eloryn River** | 제1 대하천 | Eloryn River | 유지 (L4 독자 조어 우수) | rivers_major |
| **Auravel River** | 제2 대하천 | Auravel River | 유지 (aur- 어근 계승) | rivers_major |
| **Lowen River** | 제3 대하천 | Lowen River | 유지 (L2 게르만 정합) | rivers_major |
| **Mornwell River** | 제4 대하천 | Mornwell River | 유지 (morn- 어근 계승) | rivers_major |
| **Soranth River** | 제5 대하천 | Soranth River | 유지 (권역명 계승) | rivers_major |
| **Duskway River** | 제6 대하천 | Duskway River | 유지 (dusk- 어근 계승) | rivers_major |
| **Loravel Wetlands** | 서남 대습지 | Loravel Wetlands | 유지 (권역명 계승) | wetlands |
| **Lonwyn Lakelands** | 남서 호수지대 | Lonwyn Lakelands | 유지 (권역명 계승) | wetlands |
| **Aurion Plain** | 중앙 대평원 | Aurion Plain | 유지 (권역명 계승) | plains |

---

## Wave 2 의존 포인트 요약

| Wave 2 에이전트 | 의존 파일 | 핵심 인풋 |
|--------------|---------|---------|
| Political-Cartographer | 전체 | Norvend·Veilorn 국경 후보, 강 경계선 |
| Toponymist | mountain_ranges·rivers_major·forests | 작업 가설 지명 전체 확정·대체 |
| Road-Engineer | elevation·rivers·plains | 고개·강·평원 도로 제약 조건 |
| Economist | rivers·plains·wetlands·climate | 농업·광업·어업·무역 기반 |
| Culturalist | forests·climate·wetlands | 기후·지형 기반 문화 variation |

---

*인덱스 생성: 2026-04-22 · Wave1-Geographer · naberal_game*
