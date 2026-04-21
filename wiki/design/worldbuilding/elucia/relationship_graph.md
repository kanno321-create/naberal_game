---
title: "relationship_graph — Elucia 세력 관계도"
type: relationship_graph
scope: continental_all_factions
created: 2026-04-22
updated: 2026-04-22
agent: Wave5-WorldIntegrator
wave: 5
qfix_version: Q-FIX 1~9 + X1·X2 반영
qcore_seal: v1.0
---

# Elucia 세력 관계도

> **Q-FIX 반영 인명 기준**:
> - Ilaris 왕: Aerric Maeran (X1 개명 · 구 Aldric Maeran)
> - Ceren 왕: Aedran Sellypha II (X2 개명 · 구 Aldren Sellypha II)
> - Thaloss 왕세자: Aldren (Q-FIX-5 · 구 Aldric)
> - Thaloss 공작: Edric Kaerv (Q-FIX-2 · 구 Edric Varn)
> - Aldric 왕국 House: Selyne (Q-FIX-4 · 구 House Seren)
> - Novas 수도: Duskgate (Q-FIX-9 · 구 Duskmoor)
> - 교황 위상: 황제와 동등한 최고 권위자 (Q-FIX-3 · 반신적 표현 삭제)

---

## 관계 범례

```
실선 녹색  ─── 동맹 / 협력
실선 적색  ─── 갈등 / 긴장 / 적대
실선 회색  ─── 중립 / 형식적 봉신
점선 회색  ─── 비밀 관계 / 은밀 접촉
굵은 화살표 →  권위 관계 (상위 → 하위)
```

---

## 전체 관계 다이어그램 (mermaid)

```mermaid
graph TD
    %% ── 핵심 노드 ──────────────────────────────
    SOL["🏛️ 성좌국 Choir of Elucia<br/>수도: Solaris<br/>교황 Pontifex Aurelius IV<br/>황제와 동등한 최고 권위"]

    %% ── 대왕국 ───────────────────────────────
    VAE["⚔️ Vaelin 바엘린<br/>수도: Vaelthorn<br/>왕: Aldric Vaen<br/>기마 대왕국"]
    MOR["🌊 Moran 모란<br/>수도: Mornheld<br/>해양 대왕국"]
    THA["⛏️ Thaloss 탈로스<br/>수도: Icehelm<br/>왕: Thormund<br/>왕세자: Aldren<br/>철 독점 대왕국"]

    %% ── 중왕국 ───────────────────────────────
    ILA["⚓ Ilaris 일라리스<br/>수도: Ilarien<br/>왕: Aerric Maeran ★X1<br/>해상 교역 중왕국"]
    MAE["🏔️ Maerith 마에리스<br/>수도: Maerholt<br/>북동 고지 중왕국"]
    ORY["🌿 Oryn 오린<br/>수도: Orynthil<br/>삼림 중왕국"]
    SYL["🌾 Sylren 실렌<br/>수도: Sylvenmere<br/>곡창 중왕국"]

    %% ── 소왕국 ───────────────────────────────
    CER["🧂 Ceren 세렌<br/>수도: Loravel<br/>왕: Aedran Sellypha II ★X2<br/>소금 독점 소왕국"]
    ALD["🦢 Aldric 알드릭<br/>수도: Lonwyn<br/>왕: Aldric IV<br/>House Selyne ★B4<br/>호수 소왕국"]
    NOV["🚪 Novas 노바스<br/>수도: Duskgate ★Q9<br/>Azim Pass 관문 소왕국"]

    %% ── 타종족 세력 ───────────────────────────
    ELF["🌲 타종족 세력<br/>엘프·용족 은신 공동체<br/>Deepsilvan·Orenwald 변경"]
    KAR["🏜️ Karzor 카르조르<br/>동쪽 대륙<br/>종교 해석 대립"]

    %% ══════════════════════════════════════════
    %% 성좌국 봉신 관계 (형식적 종주권)
    %% ══════════════════════════════════════════
    SOL -->|봉신 형식 종주권| VAE
    SOL -->|봉신 형식 종주권| MOR
    SOL -->|봉신 형식 종주권| THA
    SOL -->|봉신 형식 종주권| ILA
    SOL -->|봉신 형식 종주권| MAE
    SOL -->|봉신 형식 종주권| ORY
    SOL -->|봉신 형식 종주권| SYL
    SOL -->|봉신 형식 종주권| CER
    SOL -->|봉신 형식 종주권| ALD
    SOL -->|봉신 형식 종주권| NOV

    %% ══════════════════════════════════════════
    %% 동맹 (녹색 실선 — linkStyle 로 표현)
    %% ══════════════════════════════════════════
    VAE <-->|북부 3국 동맹| MOR
    VAE <-->|북부 3국 동맹| THA
    MOR <-->|북부 3국 동맹| THA
    ILA <-->|서해안 협약 Silvan Pact| CER
    MAE <-->|동부 고지 협력| ORY
    SYL <-->|남부 방어 협약| NOV

    %% ══════════════════════════════════════════
    %% 혼인 동맹 (진한 녹색)
    %% ══════════════════════════════════════════
    VAE <-.->|왕실 혼인 동맹| MOR
    ILA <-.->|왕비 Ceren 출신 혼인 관례| CER
    SYL <-.->|남부 소왕국 생존 혼인| ALD
    NOV <-.->|Azim 외교 완충 혼인| KAR

    %% ══════════════════════════════════════════
    %% 갈등·긴장 (적색)
    %% ══════════════════════════════════════════
    THA ---|Greygate 통행세 세대 원한| VAE
    THA -.-|철 공급 레버리지 긴장| SOL
    CER -.-|소금 독점 긴장| SOL
    CER ---|해염 vs 내륙 소금 분쟁 ★B3| ALD
    VAE ---|Eloryn 강 어업권| SOL
    ORY ---|Soranth 강 수운 분쟁| SYL
    ALD ---|Lonwyn 호수 소도 귀속 분쟁| CER
    NOV ---|Azim Pass 통행세 갈등| KAR
    SOL <-.-|종교 해석 냉전 적대| KAR

    %% ══════════════════════════════════════════
    %% 타종족 관계
    %% ══════════════════════════════════════════
    ELF <-.->|은신·비밀 접촉| ILA
    ELF <-.->|숲 경계 긴장| ORY
    SOL ----|타종족 몰살 이념 추구| ELF
```

---

## 주요 인물 노드 (Q-FIX 반영)

```mermaid
graph LR
    %% ── 성좌국 ───────────────────────────────
    AUR4["교황 Aurelius IV<br/>Pontifex · 세속+종교 최고 권위"]
    SOLUNDRA["추기경 Dravek Solundra<br/>이단심문 담당"]
    HALVENMOOR["추기경 Osbert Halvenmoor<br/>선임 추기경"]

    %% ── Vaelin ────────────────────────────────
    ALDRIC_VAEN["왕 Aldric Vaen<br/>Vaelin 현왕"]
    EDRIC_VAEN["왕세자 Edric Vaen<br/>※ 동명주의: Thaloss 공작 Edric Kaerv 와 구별"]

    %% ── Thaloss ───────────────────────────────
    THORMUND["왕 Thormund<br/>Thaloss 현왕"]
    ALDREN_THA["왕세자 Aldren ★Q5<br/>구: Aldric → Aldren 개명"]
    EDRIC_KAERV["공작 Edric Kaerv ★Q2<br/>Greygate 공작가<br/>구: Edric Varn → Edric Kaerv"]

    %% ── Ilaris ────────────────────────────────
    AERRIC["왕 Aerric Maeran ★X1<br/>구: Aldric Maeran → Aerric Maeran"]

    %% ── Ceren ─────────────────────────────────
    AEDRAN["왕 Aedran Sellypha II ★X2<br/>구: Aldren Sellypha II → Aedran Sellypha II"]

    %% ── Aldric 왕국 ────────────────────────────
    ALDRIC4["왕 Aldric IV<br/>Aldric 왕국 현왕"]
    COASTFEN_SELYNE["공작 House Selyne ★B4<br/>Coastfen 해염 담당<br/>구: House Seren"]

    %% 관계
    AUR4 --- HALVENMOOR
    AUR4 --- SOLUNDRA
    ALDRIC_VAEN --- EDRIC_VAEN
    THORMUND --- ALDREN_THA
    THORMUND --- EDRIC_KAERV
    EDRIC_KAERV ---|Greygate 고개 관할| ALDREN_THA
    AERRIC ---|Ilaris 왕국| AERRIC
    AEDRAN ---|소금 협상 담당| COASTFEN_SELYNE
    ALDRIC4 --- COASTFEN_SELYNE
```

---

## 핵심 관계 요약 표

| 관계 | 당사자 | 성격 | Q-FIX 관련 |
|------|--------|------|----------|
| **북부 3국 동맹** | Vaelin·Moran·Thaloss | 군사·경제 협력 | — |
| **서해안 협약** | Ilaris·Ceren | 해상+소금 공조 | — |
| **소금·해염 분쟁** | Ceren ↔ Aldric (Coastfen) | 실제 왕국 간 분쟁 | B-3 서사화 · House Selyne(B-4) |
| **Greygate 세대 원한** | Thaloss ↔ Vaelin | 15년 전쟁 잔재 | 왕세자 Aldren(Q5)·공작 Kaerv(Q2) |
| **철 공급 긴장** | Thaloss ↔ 성좌국 | 레버리지 경쟁 | — |
| **Azim Pass 갈등** | Novas ↔ Karzor | 통행세 + 대륙 간 냉전 | Duskgate(Q9) |
| **종교 냉전** | 성좌국 ↔ Karzor | 신 해석 대립 | — |
| **Ilaris 왕실 개명** | — | 동명 해소 | Aerric Maeran(X1) |
| **Ceren 왕실 개명** | — | 동명 해소 | Aedran Sellypha II(X2) |
| **교황 위상 재정의** | 성좌국 | 반신 → 황제와 동급 | Q-FIX-3 |
| **타종족 은신** | 엘프·용족 vs 성좌국 | 잠재 갈등 | B-2 연동 (몰살 이념) |

---

*관계도 생성: 2026-04-22 · Wave5-WorldIntegrator*
*Q-FIX 1~9 + X1·X2 전반 반영 완료*
*다음 갱신 기준: 서부 대륙 세력 추가 확정 시*
