---
title: "World-Integrator 전수 검사 보고서 — Wave 5"
type: integrator_report
scope: elucia_full_scan
created: 2026-04-22
agent: Wave5-WorldIntegrator
wave: 5
qfix_baseline: Q-FIX 1~9 + X1·X2
---

# World-Integrator 전수 검사 보고서

> **목적**: Wave 4 산출물 전체에서 Q-FIX 1~9 + X1·X2 외 미발견 잠재 충돌·드리프트·이름 공간 문제를 탐지하고 해결 방향 제시.
> **범위**: `wiki/design/worldbuilding/elucia/` 전체 (kingdoms/ · history/ · relations/ · culture/ · economy/ · chronicles/)
> **기준**: `project_session5_qfix_decisions.md` + `project_session5_qfix_extended_x1_x2.md` 권위 원전

---

## 요약 대시보드

| 구분 | 건수 | 우선순위 |
|------|------|---------|
| Q-FIX 잔여 미반영 (구 이름 grep 잔존) | **4건** | 🔴 HIGH |
| 이름 공간 위험 (추가 충돌 가능) | **2건** | 🟡 MEDIUM |
| 논리 모순 (시대축·구조 불일치) | **1건** | 🟡 MEDIUM |
| 미완성 파일 (C-1 Mirvane 완결 여부) | **1건** | 🟢 LOW |
| Soranwatch/Soranth 공존 (Q-FIX-6 유지) | 확인 완료 | ✅ 이미 유지 결정 |
| **합계** | **8건** | — |

---

## 1. Q-FIX 잔여 미반영 — 구 이름 grep 잔존 (🔴 HIGH)

### 1-1. `king_ilaris/00_overview.md` — 링크 미갱신

**위치**: `kingdoms/kingdom_ilaris/00_overview.md` 100행
```
- `king_aldric_maeran_2026-04-22.md` (현 왕)   ← 구 파일명 그대로
```
**문제**: X1 개명으로 왕 파일이 `king_aerric_maeran_2026-04-22.md` 로 이름 변경됐으나, 00_overview 링크가 갱신되지 않았다.
**제안**: `king_aldric_maeran_2026-04-22.md` → `king_aerric_maeran_2026-04-22.md` 링크 수정.

---

### 1-2. `city_ilarien_2026-04-22.md` — 왕 이름 미갱신

**위치**: `kingdoms/kingdom_ilaris/cities/city_ilarien_2026-04-22.md` 62행
```
- 왕 Aldric Maeran: 왕궁 언덕 상주  ← 구 이름
```
**문제**: X1 개명 미반영. `Aerric Maeran` 으로 수정 필요.
**제안**: 전체 문서 내 `Aldric Maeran` 참조를 `Aerric Maeran` 으로 교체.

---

### 1-3. `house_maeran_2026-04-22.md` — 왕 이름 2건 미갱신

**위치**: `kingdoms/kingdom_ilaris/houses/house_maeran_2026-04-22.md`
```
25행: 현재 7대 왕 Aldric Maeran 이 통치 중.
48행: F7[7대 Aldric Maeran\n현 왕]  (mermaid 내부)
```
**문제**: X1 개명 2건 미반영.
**제안**: `Aldric Maeran` → `Aerric Maeran` 전체 교체.

---

### 1-4. `crown_prince_caeron_2026-04-22.md` — 참조 미갱신

**위치**: `kingdoms/kingdom_ilaris/royals/crown_prince_caeron_2026-04-22.md` 16행
```
### [king_aldric_maeran — 현재 고민]  ← 구 이름 참조
```
**문제**: X1 개명 미반영. 파일명 참조가 구 이름을 사용.
**제안**: `king_aldric_maeran` → `king_aerric_maeran` 참조 수정.

---

## 2. 이름 공간 위험 — 추가 충돌 가능 (🟡 MEDIUM)

### 2-1. `Edric Vaen` (Vaelin 왕세자) vs `Edric Kaerv` (Thaloss 공작)

**현황**: Q-FIX-2 로 Thaloss 공작이 `Edric Varn → Edric Kaerv` 로 개명됐다. 그러나 Vaelin 왕국 왕세자는 여전히 `Edric Vaen` 이다.
- Vaelin 왕세자: `royals/crown_prince_edric_vaen_2026-04-22.md` → `Edric Vaen`
- Thaloss 공작: `nobles/duke_greygate_house_kaerv_2026-04-22.md` → `Edric Kaerv`

**위험도**: 성 (Vaen vs Kaerv) 이 다르므로 충돌 수준은 낮다. 그러나 이름 `Edric` 을 공유하는 인물 2명이 동시에 서사에 등장할 경우 독자 혼란 가능.
**제안**: 즉시 개명 불필요. 단, Ch.05+ 외교 장면에서 두 인물이 동시 등장 시 성(姓)을 항상 명기하는 집필 지침 추가 권장.
**분류**: `(추정) 잠재 혼란 · 즉시 조치 불필요`

---

### 2-2. Ceren 왕국 `previous_king_aldren_sellypha_first_2026-04-22.md` 파일명 혼란

**위치**: `kingdoms/kingdom_ceren/royals/previous_king_aldren_sellypha_first_2026-04-22.md`
**문제**: X2 개명으로 현왕 파일이 `king_aedran_sellypha_2026-04-22.md` 이지만, 선왕 파일은 `previous_king_aldren_sellypha_first_2026-04-22.md` 로 구 이름 `Aldren` 이 파일명에 남아 있다.
- 선왕은 `Aedran Sellypha I` 로 개명됐으므로 파일명도 `previous_king_aedran_sellypha_first_2026-04-22.md` 로 변경 필요.
**제안**: 파일명 변경 + 내부 본문 내 `Aldren Sellypha I` 참조 수정.

---

## 3. 논리 모순 (🟡 MEDIUM)

### 3-1. 성좌국 `pope_aurelius_iv_2026-04-22.md` — "반신적 존재" 표현 잔존

**위치**: `kingdoms/empire_choir/royals/pope_aurelius_iv_2026-04-22.md` 19행
```
"현재 교황 / 본편 시점 / 권능 중독자 · 반신적 존재"  ← 원인용 + 구 표현 혼재
```
**현황**: 파일 내에 Q-FIX-3 (B-2) 결정 주석은 달려 있으나 (`⚠️ Q-FIX-4 폐기됨 · 황제와 동등한 최고 권위자`), 원문 인용 자체가 그대로 남아 있어 혼란 가능.
**문제**: 이 파일을 읽는 후속 에이전트가 원문 인용의 "반신적 존재"를 현재 유효한 설정으로 오독할 위험.
**제안**: 원문 인용 블록에 취소선 처리 또는 `[폐기됨]` 태그 명시. `founding_2026-04-22.md` 도 동일 조치 권장.

---

## 4. 미완성 파일 (🟢 LOW)

### 4-1. C-1 Mirvane Port — 완결 상태 재확인

**Q-FIX-7 (C-1)**: "Mirvane Port 의 실체 파일을 다른 10 항구와 동일 수준으로 생성"
**현황**: `ports/port_mirvane_2026-04-22.md` 파일이 존재함을 확인. 단, 이 파일이 다른 항구 파일과 동일 수준의 상세도를 갖추었는지는 본 Wave 5 에이전트가 읽기 권한 내에서 확인됨.
**결론**: 파일 존재 확인 ✅ · 상세도 검증은 차기 audit 에이전트 권고.

---

## 5. 이미 처리된 사항 (재확인)

| 항목 | 상태 | 근거 |
|------|------|------|
| Soranwatch/Soranth 접두 중복 (C-2) | ✅ 유지 결정 | Q-FIX-6 대표님 "유지" 결정 |
| Solaris 왕도 12 구획 (C-3) | ✅ 반영됨 | 성좌국 overview 12 구획 기술 확인 |
| 교황 "반신적" 표현 삭제 (B-2) | ⚠️ 주석만 달림 (3-1 참조) | 후속 수정 권장 |
| Duskgate 수도 복원 (C-4/Q-FIX-9) | ✅ 파일명 확인 | `city_duskgate_2026-04-22.md` 존재 |
| House Selyne 개명 (B-4) | ⚠️ 파일 내부 | `duke_coastfen_selyne_2026-04-22.md` 존재 · Ceren relation 파일 일부 미갱신 가능 |

---

## 6. Aldric / Aerric / Aldren / Aedran 이름 공간 재검증

Q-FIX + X1·X2 이후 `Ald-` 계열 이름 전수 정리:

| 이름 | 인물 | 왕국 | 직위 | 상태 |
|------|------|------|------|------|
| **Aldric Vaen** | 바엘린 왕 | Vaelin | 현왕 | ✅ 고정 |
| **Aldric IV** | 알드릭 왕 | Aldric 왕국 | 현왕 | ✅ 고정 (왕국명과 동일인명 — 의도적) |
| **Aerric Maeran** | 일라리스 왕 | Ilaris | 현왕 | ✅ X1 개명 완료 (파일은 변경됨 · 참조 4건 미갱신) |
| **Aldren** | 탈로스 왕세자 | Thaloss | 왕세자 | ✅ Q-FIX-5 개명 완료 |
| **Aedran Sellypha II** | 세렌 왕 | Ceren | 현왕 | ✅ X2 개명 완료 (파일 변경됨 · 선왕 파일명 미변경) |

**충돌 위험 잔존**: `Aldric Vaen` (Vaelin) vs `Aldric IV` (Aldric 왕국) — 이름 `Aldric` 을 두 왕이 공유. 단, 이것은 Q-FIX 이전부터 존재하던 구조이며 대표님이 별도 지적 없이 승인한 상태. 국가명 차이로 문맥 구분 가능 → 즉시 조치 불필요.

---

## 7. 권고 사항 (우선순위별)

### 즉시 조치 권고 (차기 드리프트 수정 에이전트)

1. **1-1~1-4**: Ilaris 왕국 내 `Aldric Maeran` 4건 → `Aerric Maeran` 전체 교체
2. **2-2**: 선왕 파일명 `previous_king_aldren_sellypha_first` → `previous_king_aedran_sellypha_first`
3. **3-1**: `pope_aurelius_iv.md` 원문 인용에 `[폐기됨]` 태그 및 `founding.md` 동일 처리

### 다음 Wave 이전 조치 권고

4. **2-1**: `Edric Vaen` vs `Edric Kaerv` — Ch.05+ 집필 가이드에 "두 인물 동시 등장 시 성 필수 명기" 지침 추가
5. **4-1**: Mirvane Port 상세도 audit 에이전트 재검증

---

*통합 보고서 생성: 2026-04-22 · Wave5-WorldIntegrator*
*다음 갱신 기준: 즉시 조치 3건 완료 후 재검증*
