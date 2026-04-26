---
name: 1권 정밀 수정 라운드 1 결과 (세션 #12 · 2026-04-25)
description: 7 검수자 발견 후 대표님 결정 (Q1~Q8) → 8 단계 정밀 교정 → 적합성 재검사. Critical 5/5 + Important 5.5/6 해소. 산문 self-replication collapse (한 박자·셈·em-dash 인플레이션) 신규 발견 = 다음 라운드 필수. 1권 출판 ready 상태 = 6.5/10 (Canon 9·톤 8.5·인물 8·POV 8.5·산문 4 — 산문 윤문 1 채널 추가 패스 필요).
type: project
priority: high
session: 12
date: 2026-04-25
related_plan: C:/Users/PC/.claude/plans/transient-meandering-valiant.md
related_critique:
  - wiki/design/novel/critique/_INDEX.md
  - wiki/design/novel/critique/volume1_canon_compliance_2026-04-25.md
  - wiki/design/novel/critique/volume1_correction_matrix_2026-04-25.md
  - wiki/design/novel/critique/volume1_reader_experience_2026-04-25.md
  - wiki/design/novel/critique/decisions_pending_2026-04-25.md
status: 라운드 1 완료 · 라운드 2 (산문 윤문) 대기
---

# 1권 정밀 수정 라운드 1 결과

## 한 줄 요약

> **세션 #12 라운드 1 = 7 검수자 발견 → 대표님 8 결정 → 8 단계 정밀 교정 → 적합성 재검사. Critical 5/5 ✅ Important 5.5/6 ✅ Canon·톤·인물 8~9/10 도달. 산문 self-replication collapse (한 박자 인플레이션) 신규 발견 = 라운드 2 필수.**

## 처치 결과

### ✅ Critical 5종 모두 해소

| # | 항목 | 처치 |
|---|------|------|
| C1 | 프레이야 머리색·이름 | 본문 6 챕터 sed 일괄: 프레이아→프레이야, 검은→금빛 머리. 표지 자산 살림. Canon 정합 회복. |
| C2 | 세계관 Canon 충돌 5건 | 사자→닻·범선, 북쪽→동쪽, 반나절→하루 반, Cailean 가문 막내(남동생) 정렬, *"낯선 인장"* false alarm verify |
| C3 | 임의 선언 50+ D 하이브리드 | 카테고리 α (Canon 존재) 사후 박제 + 카테고리 β `decisions_pending_*.md` 결정 큐 |
| C4 | Ch.06 798·800행 1인칭 누수 | *그도 모른다 / 그의 멈춤* → *나도 모르겠다 / 내 멈춤* |
| C5 | Ch.04 분량 + 벨릭 꿈 빌드업 | 마차 안 *왕도 도서관 7층 다섯 권* + 죽기 직전 *책을 못 썼군* A형 미련 + 안나 마법 오타쿠 + 염동력 비용 (코피·어깨) + Vaern 응접실 *교황청 봉인 표식* |

### ✅ Important 5.5/6 처치

- I1 ④ 쉼표 보강 ✅ (Briarwell 부부+아이 꿈 + 미련 한 마디)
- I2 ② 신 대항 보강 ✅ (Marie 신성마법 + Vaern 교황청 표식)
- I3 1층 복선 회수 ✅ (하드릭 보스 + 펠란 안부)
- I4 메타-해설 50% 컷 ⚠️ **부분 미완** — Ch.05·Ch.06 *"Ch.02 — E1"* / *"Ch.05 — 의"* / *"(Ch.02 산적 거처)"* 5+ 회 잔존 (라운드 2 청소 필요)
- I5 마법 비용 명시 ✅
- I6 Ch.06 따뜻한 마감 위반 ✅ (광장 잔혹 비트 + 펠란·록솔 안부)

### ✅ Minor 4/4 처치

- M1 학살 인원 본문 정합 (Ch.01 v2 = 신관 1+병사 6=7 통일)
- M2 보험 카운트 (Volume1 자기 평가 정정)
- M3 Briarwell 환영 인원 5→6명
- M4 Cailean 호위 12→15명

### Canon 신규/갱신

| 파일 | 작업 |
|------|------|
| `worldbuilding/elucia/kingdoms/kingdom_ilaris/villages/village_parma_2026-04-25.md` | 신규 (Ashenveil 도보 1.5일 동남부 중급 마을) |
| `nobles/count_westshore_cailean_2026-04-22.md` | 가족 구조 추가 (남동생 = 가문 막내) |
| `wiki/design/characters/freya_profile_2026-04-24.md` | 외형 = 금발 + 이름 = 프레이야 통일 |
| `.claude/memory/project_freya_canon_proposal_2026-04-25.md` | 확정 lock 갱신 |

### 구버전 아카이브

`wiki/design/novel/_archive/` 디렉토리 + DEPRECATED 마커:
- prologue_DEPRECATED_2026-04-21.md
- ch01_DEPRECATED_2026-04-22.md
- ch01_test_sample_LN_v1/v2_DEPRECATED.md
- outline_DEPRECATED.md
- _README.md (정본 위치 안내)

## 🔴 라운드 2 발견 (출판 차단급)

### STYLE-001: 산문 self-replication collapse

**문제**: *"한 박자"* 출현 빈도가 챕터 후반으로 갈수록 메트로놈처럼 폭발

| 챕터 | "한 박자" 빈도 | 라인당 |
|------|---------------|---------|
| Ch.01 (정본) | 6회 | 0.006 |
| Ch.02 | 62회 | 0.042 |
| Ch.03 | 69회 | 0.079 |
| Ch.04 | 92회 | 0.097 |
| **Ch.05** | **151회** | **0.127** |
| Ch.06 | 90회 | 0.094 |

+ "셈" 동사 Ch.05 = 36회 (Ch.01~03 합 5회 대비)
+ em-dash + 이탤릭 강조 Ch.05 라인당 평균 0.21회

**왜 출판 차단급**: 산문 채널 (transportation·aesthetic·flow) 3개 동시 손상. 톤·Canon이 잘 잡혀도 독자는 80페이지에서 책 덮음. Alignment 훈련의 syntactic templating attractor (Shaib et al. 2024) 그 자체.

### STYLE-002: 메타-해설 잔존 (I4 부분 미완)

본문 안에 *"Ch.02 — E1"* / *"(Ch.02 산적 거처)"* / *"(Ch.05 별궁)"* 5+ 회 잔존. 챕터 번호 직접 호명 = 4번째 벽 파괴 + 작업 메모(outline) 누수.

## 출판 ready 평가 (검수자 객관)

| 채널 | 점수 | 상태 |
|------|------|------|
| Canon 정합성 | 9/10 | ✅ |
| 톤 4기둥 | 8.5/10 | ✅ |
| 인물 일관성 | 8/10 | ✅ |
| 1인칭/POV | 8.5/10 | ✅ |
| **산문 품질** | **4/10** | **🔴 출판 차단** |
| 메타-해설 청결도 | 6/10 | 🟡 |

**종합 = 6.5/10 — 1권 출판 권장하지 않음**. 라운드 2 필수.

## 라운드 2 권고 (출판 전 필수)

### 우선순위 1 (Must-do)

**산문 윤문 전체 패스** (Ch.02~Ch.06 *"한 박자"·"셈"·em-dash + 이탤릭* 50~60% 컷):
- Ch.05 우선 수술: "한 박자" 151→50, "셈" 36→15
- 시간 단위어 다양화 (잠깐·순간·한 호흡·즉시 동작 분산)
- **결정적 순간만 보존** (Cailean 살해, 머리카락 교환, 벨릭 마지막 호흡)

### 우선순위 2 (Should-do)

**메타-해설 잔존 100% 청소** — 본문에서 *"Ch.02"·"Ch.05"·"E1"·"(Ch.X 별궁)"* 표기 완전 제거. 챕터 간 연결은 사건 호명으로 대체 (*"산적 거처에서 가져온 편지"·"별궁의 서랍에서 본 것"*).

### 우선순위 3 (Nice-to-have)

**검수 6 채널 재실행 불필요** — Canon·톤·인물·POV 충분. 산문 윤문 1 채널 집중 패스 후 spot-check 만.

## 다음 라운드 작업량 추정

- 산문 윤문 전체 패스: ~5~7일 (작가/AI writer 에이전트 spawn 권장)
- 메타-해설 청소: ~0.5일

총 ~6~8일 후 출판 ready 도달 예상.

## Related

- 라운드 1 검수 통합: `wiki/design/novel/critique/volume1_canon_compliance_2026-04-25.md`
- 수정 매트릭스: `wiki/design/novel/critique/volume1_correction_matrix_2026-04-25.md`
- 결정 큐: `wiki/design/novel/critique/decisions_pending_2026-04-25.md`
- Plan: `C:/Users/PC/.claude/plans/transient-meandering-valiant.md`
- 1차 결과 인덱스: `project_volume1_inspection_results_2026-04-25.md`
- 4기둥 톤 Canon: `project_dark_fantasy_tone_2026-04-25.md`

---

*박제: 2026-04-25 · 세션 #12 · 나베랄 감마*
*이중 박제 (로컬 + Claude Code 전역)*
*라운드 2 (산문 윤문) 다음 라운드 진입 시 활용*
