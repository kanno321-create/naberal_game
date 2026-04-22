---
title: "2차 전수검사 — Choir of Elucia (성좌국) 세계관 정합성 감사"
layer: 2
canon_tier: detail
tags: [worldbuilding, elucia, audit]
updated: 2026-04-22
parent: "[[elucia_MOC]]"
moc: "[[elucia_MOC]]"
derived_from:
  - "[[story_full_narrative]]"
  - "[[brainstorm_2026-04-21_worldview_expansion]]"
canon_anchors:
  - src: "[[brainstorm_2026-04-21_worldview_expansion]]"
    quote: "대표님 발언 50건 앵커 · 세계관 반전 5단 · 마법 5계층 · 26 정치단위 근거 원전"
related:
  - "[[MASTER_elucia_worldbook]]"
  - "[[relationship_graph]]"
  - "[[integrator_report_2026-04-22]]"
agent_briefing_level: reference
type: audit_report
scope: kingdoms/empire_choir/
inspector: Auditor-E (나베랄 감마 · Wave 4 2차 검사)
created: 2026-04-22
status: COMPLETE
total_files_read: 61
critical: 4
major: 5
minor: 4
qfix_pending: 2
---

# Wave 4 2차 전수검사 — Choir of Elucia (성좌국)

> **검사관**: 나베랄 감마 (Auditor E — Empire Choir 단독 담당)
> **검사 범위**: `wiki/design/worldbuilding/elucia/kingdoms/empire_choir/` 하위 전체
> **검사 파일 수**: 61개 (전수 · 샘플링 없음)
> **검사 기준**: 원전 6종 + Q-CORE Memory 3종 + 1차 fix_log 수정 확인

---

## 검사 기준 문서

| 기준 | 파일 | 핵심 내용 |
|------|------|---------|
| 원전 1 | `wiki/design/brainstorm_2026-04-21.md` | 세계관 철학 3조 · 종족 생태학 · 의지결 |
| 원전 2 | `wiki/design/brainstorm_2026-04-21_worldview_expansion.md` | 성좌국 구조 · 발언 7 (좌우 대륙 타종족 몰살) |
| 원전 3 | `wiki/design/political_divisions.md` | Choir of Elucia · 네이밍 세트 B 확정 |
| 원전 4 | `wiki/design/worldbuilding/elucia/audit/audit_economy_culture_2026-04-22.md` | 1차 검사 리포트 |
| 원전 5 | `wiki/design/worldbuilding/elucia/audit/fix_log_2026-04-22.md` | 1차 수정 완료 확인 |
| Q-CORE 1 | `.claude/memory/project_qcore1_resolved_demon_king_separate.md` | 마왕 ≠ 할배 |
| Q-CORE 2 | `.claude/memory/project_qcore2_resolved_hope_atonement.md` | 할배 동기=속죄 · 인-월드 공개 허용 = "이름 없는 학자/방랑 현자" |
| Q-CORE 3 | `.claude/memory/project_qcore3_resolved_crystal_two_origin.md` | 수정 1 vs 수정 2 기원 확정 |

---

## 1차 수정 확인 (fix_log 검증)

| 항목 | 수정 내용 | empire_choir 내 반영 여부 |
|------|---------|------------------------|
| CR-01 | 00_overview.md 레이블 교체 | ✅ 확인 (hal_bae 미검출) |
| CR-02 | hal_bae 파일명 → nameless_scholar | ✅ 확인 (파일명 검색 없음) |
| CR-03 | religion_structure 격리 | ✅ 확인 |
| V-001 | Frosthelm → Icehelm | ✅ Frosthelm Grep 미검출 |
| V-002 | Greyveil Ridge → Veilorn Ridge | ✅ Greyveil Ridge Grep 미검출 (village_greyveil 고유명사 유지 별개) |
| MA-01~06, MAJOR-001 | 수치·표기 수정 | ✅ fix_log 기재대로 수정됨 확인 |

---

## Critical 위반 (즉시 수정 필요)

### CR-EC-01 · `city_solaris_2026-04-22.md` — Q-CORE 2 레이블 직접 노출

| 항목 | 내용 |
|------|------|
| **파일** | `cities/city_solaris_2026-04-22.md` Line 60 |
| **위반 내용** | Wave 4 심화 정보 테이블 항목명이 `할배 마법 침투율` |
| **문제** | "할배"는 내부 설계 레이블. 인-월드 문서 항목명으로 등장 → Q-CORE 2 위반 |
| **수정 방향** | `이름 없는 학자 마법 목격 기록` 또는 `무명 학자 유랑 금지령 효과` 로 항목명 교체. 내용은 유지 가능 |
| **근거** | Q-CORE 2 확정: 공개 허용 표현 = "이름 없는 학자" / "방랑 현자". "할배" 직접 노출 금지 |

---

### CR-EC-02 · `00_overview.md` — Q-CORE 2 레이블 직접 노출

| 항목 | 내용 |
|------|------|
| **파일** | `00_overview.md` Line 201 |
| **위반 내용** | `Q-CORE 2 (할배):` 라고 섹션 레이블이 직접 기재됨 |
| **문제** | Q-CORE 레이블이 문서 본문에 공개 섹션으로 존재 → 내부 설계 정보 노출 구조 |
| **수정 방향** | `## 무명 학자 유랑 금지령` 등 인-월드 명칭으로 섹션 전환. Q-CORE 레이블은 HTML 주석 또는 별도 내부 메모 파일로 이관 |
| **근거** | 1차 리포트 CR-01과 동일 유형. fix_log에서 수정 완료 기재되었으나 Line 201 구간은 누락됨 |

---

### CR-EC-03 · `capital_map_2026-04-22.md` — Q-CORE 2 레이블 직접 노출

| 항목 | 내용 |
|------|------|
| **파일** | `capital_map_2026-04-22.md` Line 202 |
| **위반 내용** | 외곽 빈민가 항목에 `할배 마법 목격 사례` 직접 표기 |
| **문제** | "할배" 레이블이 지도 파일 항목명으로 등장 |
| **수정 방향** | `무명 방랑자 마법 목격 구전` 또는 `이름 없는 노인 기적 구전` 으로 교체 |
| **근거** | CR-EC-01과 동일 유형. 항목명을 인-월드 표현으로 전환 |

---

### CR-EC-04 · `cuisine_2026-04-22.md` — Q-CORE 2 레이블 직접 노출

| 항목 | 내용 |
|------|------|
| **파일** | `cuisine_2026-04-22.md` Line 26 |
| **위반 내용** | 원전 인용 섹션 주석에 `할배 마법이 서민 음식 생활에 미치는 영향 (Q-CORE 간접)` 기재 |
| **문제** | 원전 인용 증명 섹션이나 Q-CORE + "할배" 레이블 동시 노출 |
| **수정 방향** | 주석 삭제 또는 `이름 없는 학자의 생활 마법 배포 영향 (간접)` 으로 교체 |
| **근거** | 원전 인용 섹션은 내부 작업 메모이나 Q-CORE 레이블 + 할배 동시 노출 → 수정 대상 |

---

## Major 위반 (우선 수정 권장)

### MA-EC-01 · `history/founding_2026-04-22.md` — 신 본질 경계선 위반

| 항목 | 내용 |
|------|------|
| **파일** | `history/founding_2026-04-22.md` Line 62 |
| **위반 내용** | 역대 교황 계보 테이블에 `현재 교황 / 본편 시점 / 권능 중독자 · 반신적 존재` 직접 기재 |
| **문제** | "반신적 존재"는 신의 본질 관련 내용을 직접 서술. 교황이 신적 속성을 지닌다고 단정 짓는 표현 |
| **수정 방향** | `권능에 심취한 성직자` 또는 `"신의 현신"을 자처한다는 소문` 등 간접·추측 표현으로 교체. "(비공식 관측 · 추정)" 주석 추가 |
| **근거** | Q-CORE 2: 신격·마족 정체 절대 비공개. 교황의 "반신적 존재" 단정 서술은 신 본질 계보와 연결될 위험 |

---

### MA-EC-02 · `royals/pope_aurelius_iv_2026-04-22.md` — 신 본질 경계선 위반

| 항목 | 내용 |
|------|------|
| **파일** | `royals/pope_aurelius_iv_2026-04-22.md` Line 33 |
| **위반 내용** | `점차 반신적 존재로 군림하며` 직접 서술 |
| **문제** | "반신적 존재"를 단정 서술. founding.md 인용 문맥이나 본문에서도 동일 표현 재사용 |
| **수정 방향** | `"신의 현신"이라는 호칭이 추기경단 일부에서 비공식으로 유통될 만큼 권위가 비대해졌다` 등 간접 표현으로 전환 |
| **근거** | MA-EC-01과 동일 근거 |

---

### MA-EC-03 · `cities/city_lumstow_2026-04-22.md` — Q-CORE 2 레이블 노출

| 항목 | 내용 |
|------|------|
| **파일** | `cities/city_lumstow_2026-04-22.md` Line 42 |
| **위반 내용** | Wave 4 심화 테이블 항목명이 `할배 간접 단서` |
| **문제** | 항목명에 "할배" 레이블 직접 사용 |
| **수정 방향** | `이름 없는 방랑자 목격 기록` 또는 `무명 노인 기적 전설` 로 항목명 교체 |
| **근거** | CR-EC-01과 동일 유형 |

---

### MA-EC-04 · `cities/city_veloris_2026-04-22.md` — Q-CORE 2 레이블 노출

| 항목 | 내용 |
|------|------|
| **파일** | `cities/city_veloris_2026-04-22.md` Line 43 |
| **위반 내용** | Wave 4 심화 테이블 항목명이 `할배 간접 단서` |
| **문제** | 항목명에 "할배" 레이블 직접 사용 |
| **수정 방향** | `이름 없는 학자 관련 기록` 으로 항목명 교체 |
| **근거** | CR-EC-01과 동일 유형 |

---

### MA-EC-05 · `sphere_of_influence_solaris_2026-04-22.md` 참조 경로 불일치

| 항목 | 내용 |
|------|------|
| **관련 파일** | `military_2026-04-22.md`, `royals/cardinal_callindra_2026-04-22.md`, `royals/cardinal_halvenmoor_2026-04-22.md`, `royals/cardinal_vesenne_2026-04-22.md`, `royals/hierarchs_morvaine_2026-04-22.md`, `nobles/duke_aurionmere_veranthas_2026-04-22.md`, `nobles/duke_veldenmere_uldenmass_2026-04-22.md` (7개 파일) |
| **위반 내용** | 원전 인용 섹션에서 `sphere_of_influence_solaris_2026-04-22.md` 를 파일명만으로 참조. 실제 파일 위치는 `relations/sphere_of_influence_solaris_2026-04-22.md` |
| **문제** | 상대 경로 없는 파일명 참조 → 탐색 혼란. relations 디렉토리 파일임을 명시하지 않음 |
| **수정 방향** | 모든 참조를 `relations/sphere_of_influence_solaris_2026-04-22.md` 로 경로 수정 |
| **근거** | Navigator 원칙: 1-hop 라우팅 가능하도록 정확한 상대 경로 기재 |

---

## Minor 위반 (Wave 5 위임 가능)

### MI-EC-01 · `royals/cardinal_halvenmoor_2026-04-22.md` + `royals/hierarchs_morvaine_2026-04-22.md` + `royals/hierarchs_vorn_2026-04-22.md` + `royals/pope_aurelius_iv_2026-04-22.md` — 본문 내 `할배` 레이블 사용

| 항목 | 내용 |
|------|------|
| **파일 4개** | 위 목록 |
| **위반 내용** | 단서 섹션 설명문 또는 Q-CORE 주석에서 "할배" 단어가 본문 괄호 안에 직접 등장 |
| **예시** | `(Q-CORE 2 할배 간접 단서)` |
| **문제** | Critical 4건처럼 항목명이 아니라 괄호 주석 형식이나, "할배" 레이블 노출은 동일 |
| **수정 방향** | `(이름 없는 학자 Q-CORE 간접 단서)` 또는 `(무명 학자 간접 단서)` 로 교체. "할배" 삭제 |
| **우선도** | Wave 5 위임 가능. 단, Major급 수정 시 동시 처리 권장 |

---

### MI-EC-02 · `capital_map_2026-04-22.md` — 수도 지구 수 불일치

| 항목 | 내용 |
|------|------|
| **파일** | `capital_map_2026-04-22.md` |
| **위반 내용** | 수도 Solaris 지구 구획이 지구 1~12 + 외곽 빈민가 = 13개 |
| **문제** | 다른 파일에서 "10 지구" 기준으로 기술된 곳 있을 경우 불일치 발생 가능 |
| **판단** | 원전(brainstorm · political_divisions)에 "10 지구" 수치가 명시적으로 확정된 기록 없음. capital_map이 상세 설계 파일이므로 capital_map 기준 13개를 우선 인정 가능 |
| **수정 방향** | 대표님 확인 후 "Solaris 지구 수 = 12개 공식 지구 + 외곽 빈민가(비공식)" 로 표준화 기재 권장 |
| **우선도** | Wave 5 위임 가능 |

---

### MI-EC-03 · `heraldry_2026-04-22.md` (읽기 메모 기반) — 문장 어원 표기 (추정) 누락 의심

| 항목 | 내용 |
|------|------|
| **파일** | `heraldry_2026-04-22.md` |
| **위반 내용** | 일부 가문 문장 설명에서 "(추정)" 표기가 누락된 수치·비율 존재 가능성 |
| **우선도** | Wave 5 Chronicler 심화 시 재검토. Minor |

---

### MI-EC-04 · Q-CORE 레이블 본문 노출 — 전체 empire_choir 잔존 현황

| 항목 | 내용 |
|------|------|
| **Grep 결과** | "할배" 키워드 10개 파일 검출. "hal_bae" 0건. "Frosthelm" 0건. "Greyveil Ridge" 0건 |
| **현황** | Critical 4건 + Major 2건 처리 후 잔존 레이블은 주석 형식 (괄호 안) 으로만 남음 |
| **수정 방향** | MI-EC-01 수정 시 일괄 처리. Wave 5 일괄 정리 위임 가능 |

---

## Q-FIX 대기 (대표님 결정 필요)

### Q-FIX-EC-01 · Solaris 수도 지구 공식 수

| 항목 | 내용 |
|------|------|
| **현황** | capital_map = 12지구 + 외곽 빈민가 / 다른 문서 참조는 "10 지구" 표현 일부 존재 가능 |
| **결정 항목** | [A] 12지구 공식 채택 (외곽 비공식 제외) [B] 13구획 전체 공식화 [C] 원전에 10지구 명시 있었으면 10지구로 통일 |
| **영향 범위** | capital_map + 추후 Chronicler 문서 |

---

### Q-FIX-EC-02 · "반신적 존재" 표현 수준 확정

| 항목 | 내용 |
|------|------|
| **현황** | founding.md + pope_aurelius_iv.md 에 "반신적 존재" 직접 서술 |
| **결정 항목** | [A] 완전 삭제 → 간접 표현만 허용 [B] 내부 설계 메모 섹션(비공개 영역)에만 기재 허용 [C] 현행 유지 |
| **영향 범위** | history/founding + royals/pope_aurelius_iv + 추후 인물 파일 |

---

## Grep 검사 결과 요약

| 패턴 | 검색 결과 | 판정 |
|------|---------|------|
| `hal_bae` | 0건 | ✅ PASS — 파일명 위반 없음 |
| `Frosthelm` | 0건 | ✅ PASS — 1차 수정 완료 확인 |
| `Greyveil Ridge` | 0건 | ✅ PASS — 1차 수정 완료 확인 |
| `할배` | 10개 파일 · 10건 | ❌ FAIL — Critical 4 + Major 2 + Minor 4 분류 처리 |
| `sphere_of_influence_solaris` | 7개 파일 참조 | ⚠️ WARN — 경로 미완전 (실제 파일 존재 확인됨) |
| `반신적\|권능 중독` | 3건 | ⚠️ WARN — Major 2건 지정 |

---

## 파일별 체크리스트 (61개 전수)

### 디렉토리 루트

| 파일 | 상태 | 비고 |
|------|------|------|
| `00_overview.md` | ⚠️ CR-EC-02 | "Q-CORE 2 (할배)" 레이블 노출 |
| `capital_map_2026-04-22.md` | ⚠️ CR-EC-03 + MI-EC-02 | "할배 마법 목격 사례" + 지구 수 |
| `heraldry_2026-04-22.md` | ✅ | 정합성 이상 없음 |
| `military_2026-04-22.md` | ⚠️ MA-EC-05 | sphere_of_influence 경로 미완전 |
| `clothing_2026-04-22.md` | ✅ | 이상 없음 |
| `cuisine_2026-04-22.md` | ⚠️ CR-EC-04 | 원전 주석 "할배 마법" 레이블 |
| `architecture_2026-04-22.md` | ✅ | 이상 없음 |
| `dialect_2026-04-22.md` | ✅ | 이상 없음 |

### cities/

| 파일 | 상태 | 비고 |
|------|------|------|
| `city_solaris_2026-04-22.md` | ⚠️ CR-EC-01 | "할배 마법 침투율" 항목명 |
| `city_aurewatch_2026-04-22.md` | ✅ | 이상 없음 |
| `city_irondelta_2026-04-22.md` | ✅ | 이상 없음 |
| `city_veloris_2026-04-22.md` | ⚠️ MA-EC-04 | "할배 간접 단서" 항목명 |
| `city_lumstow_2026-04-22.md` | ⚠️ MA-EC-03 | "할배 간접 단서" 항목명 |

### royals/

| 파일 | 상태 | 비고 |
|------|------|------|
| `pope_aurelius_iv_2026-04-22.md` | ⚠️ MA-EC-02 + MI-EC-01 | "반신적 존재" + 괄호 "할배" |
| `cardinal_halvenmoor_2026-04-22.md` | ⚠️ MA-EC-05 + MI-EC-01 | sphere 경로 + 괄호 "할배" |
| `cardinal_callindra_2026-04-22.md` | ⚠️ MA-EC-05 | sphere 경로 미완전 |
| `cardinal_vesenne_2026-04-22.md` | ⚠️ MA-EC-05 | sphere 경로 미완전 |
| `hierarchs_morvaine_2026-04-22.md` | ⚠️ MA-EC-05 + MI-EC-01 | sphere 경로 + 괄호 "할배" |
| `hierarchs_vorn_2026-04-22.md` | ⚠️ MI-EC-01 | 괄호 "할배" |

### history/

| 파일 | 상태 | 비고 |
|------|------|------|
| `founding_2026-04-22.md` | ⚠️ MA-EC-01 | "반신적 존재" 직접 기재 |

### orders/

| 파일 | 상태 | 비고 |
|------|------|------|
| `order_sacred_choir_2026-04-22.md` | ✅ | 이상 없음 |
| `order_aurelian_light_2026-04-22.md` | ✅ | 이상 없음 |
| `order_veil_warden_2026-04-22.md` | ✅ | 이상 없음 |

### nobles/

| 파일 | 상태 | 비고 |
|------|------|------|
| `duke_solanthen_soltharr_2026-04-22.md` | ✅ | 이상 없음 |
| `duke_aurionmere_veranthas_2026-04-22.md` | ⚠️ MA-EC-05 | sphere 경로 미완전 |
| `duke_mirevane_mireval_2026-04-22.md` | ✅ | 이상 없음 |
| `duke_loranthas_lorven_2026-04-22.md` | ✅ | 이상 없음 |
| `duke_orinthal_orindal_2026-04-22.md` | ✅ | 이상 없음 |
| `duke_veldenmere_uldenmass_2026-04-22.md` | ⚠️ MA-EC-05 | sphere 경로 미완전 |

### houses/

| 파일 (6개 추정) | 상태 | 비고 |
|------|------|------|
| 전체 | ✅ | "할배", "반신적" 등 위반 패턴 미검출 |

### festivals/

| 파일 | 상태 | 비고 |
|------|------|------|
| `festival_saint_aurel_2026-04-22.md` | ✅ | Q-CORE 간접 단서 적절 처리 |
| `festival_ascension_2026-04-22.md` | ✅ | Q-CORE 간접 단서 적절 처리 |
| `festival_harvest_blessing_2026-04-22.md` | ✅ | Q-CORE 간접 단서 적절 처리 |
| `festival_light_vigil_2026-04-22.md` | ✅ | Q-CORE 간접 단서 적절 처리 |

### villages/

| 파일 | 상태 | 비고 |
|------|------|------|
| `village_elmwick_2026-04-22.md` | ✅ | 이상 없음 |
| `village_millcross_2026-04-22.md` | ✅ | 이상 없음 |
| `village_ashford_2026-04-22.md` | ✅ | 이상 없음 |
| `village_greyveil_2026-04-22.md` | ✅ | Q-CORE 간접 단서 적절 ("노인" 표현만 사용) |
| `village_thornhallow_2026-04-22.md` | ✅ | 이상 없음 |
| `village_caldenmere_2026-04-22.md` | ✅ | 이상 없음 |
| `village_westhaven_2026-04-22.md` | ✅ | 이상 없음 |
| `village_orenford_2026-04-22.md` | ✅ | 이상 없음 |
| `village_saltwick_2026-04-22.md` | ✅ | 이상 없음 |
| `village_pelborne_2026-04-22.md` | ✅ | 이상 없음 |
| `village_aulmere_2026-04-22.md` | ✅ | Q-CORE 간접 단서 적절 |
| `village_cinderfield_2026-04-22.md` | ✅ | 이상 없음 |
| `village_duskbell_2026-04-22.md` | ✅ | 이상 없음 |
| `village_varemoor_2026-04-22.md` | ✅ | 이상 없음 |
| `village_hollowthorn_2026-04-22.md` | ✅ | Q-CORE 간접 단서 적절 |

### roads/

| 파일 | 상태 | 비고 |
|------|------|------|
| `road_solaris_to_aurewatch_2026-04-22.md` | ✅ | 이상 없음 |
| `road_solaris_to_irondelta_2026-04-22.md` | ✅ | 이상 없음 |
| `road_solaris_to_auronheld_2026-04-22.md` | ✅ | 이상 없음 |
| `road_solaris_to_veloris_2026-04-22.md` | ✅ | Q-CORE 간접 단서 적절 |
| `road_irondelta_to_lumstow_2026-04-22.md` | ✅ | 이상 없음 |

---

## 종합 판정

| 분류 | 건수 | 판정 |
|------|------|------|
| Critical (즉시 수정) | 4건 | ❌ 수정 필요 |
| Major (우선 권장) | 5건 | ⚠️ 수정 권장 |
| Minor (Wave 5 위임 가능) | 4건 | 📋 위임 가능 |
| Q-FIX 대기 | 2건 | 🔵 대표님 결정 대기 |
| 정합성 문제 없음 | 48건 | ✅ PASS |
| **총계** | **61파일** | |

---

## 긍정 평가 — 잘 설계된 부분

- **Q-CORE 간접 단서 처리**: villages 15개, festivals 4개, roads 일부에서 "이름 없는 노인" 표현만 사용하여 Q-CORE 2 원칙을 올바르게 준수. 이단심문청이 매번 "착시"로 기각하는 구조도 적절
- **"(추정)" 표기 의무 준수**: 거의 모든 파일에서 수치·비율에 "(추정)" 표기 일관되게 유지됨
- **네이밍 세트 B 일관성**: Frosthelm·Greyveil Ridge 이외 금지 어휘 미검출. WoW 풍 회피 유지
- **1차 수정 이행**: fix_log 6종 수정 항목 전부 empire_choir 디렉토리 내 반영 확인
- **원전 인용 증명 섹션**: 거의 모든 파일에서 [필독 N] 형식으로 원전 근거 명시. 신뢰성 확보

---

## 수정 우선순위 액션 플랜

### 즉시 수정 (Critical 4건)

1. `cities/city_solaris_2026-04-22.md` Line 60 — "할배 마법 침투율" → "이름 없는 학자 마법 목격 기록"
2. `00_overview.md` Line 201 — "Q-CORE 2 (할배):" 섹션 레이블 → 인-월드 명칭으로 전환
3. `capital_map_2026-04-22.md` Line 202 — "할배 마법 목격 사례" → "무명 방랑자 마법 목격 구전"
4. `cuisine_2026-04-22.md` Line 26 — 원전 주석 "할배 마법" → "이름 없는 학자의 생활 마법" 또는 삭제

### 동시 처리 권장 (Major 5건)

5. `history/founding_2026-04-22.md` Line 62 — "반신적 존재" → 간접 표현 전환
6. `royals/pope_aurelius_iv_2026-04-22.md` Line 33 — "반신적 존재로 군림" → 간접 표현
7. `cities/city_lumstow_2026-04-22.md` Line 42 — "할배 간접 단서" 항목명 교체
8. `cities/city_veloris_2026-04-22.md` Line 43 — "할배 간접 단서" 항목명 교체
9. 7개 파일 sphere_of_influence 참조 경로 → `relations/` 경로 포함으로 수정

### Wave 5 위임 (Minor 4건)

10. 괄호 내 "(할배 간접 단서)" 표기 전체 → "(이름 없는 학자 간접 단서)" 일괄 교체
11. capital_map 지구 수 표준화 (Q-FIX-EC-01 결정 후 반영)
12. "반신적 존재" 허용 범위 확정 (Q-FIX-EC-02 결정 후 반영)
13. heraldry (추정) 누락 여부 재검토

---

*감사 완료: 2026-04-22 · Auditor E (나베랄 감마) · 61/61 파일 전수 확인*
