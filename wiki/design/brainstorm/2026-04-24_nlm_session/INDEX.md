---
category: design/brainstorm
tags: [brainstorm, nlm, session, 2026-04-24]
created: 2026-04-24
status: active
notebook_id: 672ad9c5-ec56-45a2-a5f7-17c5fa023b5c
notebook_url: https://notebooklm.google.com/notebook/672ad9c5-ec56-45a2-a5f7-17c5fa023b5c
prompts_dir: .planning/nlm_prompts/
responses_dir: .planning/nlm_responses/
---

# 2026-04-24 NotebookLM 브레인스토밍 세션

> 대표님 지시 (2026-04-24): NotebookLM 을 스토리 브레인스토밍 공동 저자로 공식 지정 · 라이트노벨·다크판타지 기술 자료 + kanno321-create/naberal_game 레포 결합 · 질문은 파일에 완성 후 붙여넣기로 전송.

## 세션 개요

- **목적**: Act 1~3 각 챕터·씬·동료 합류·카르조르·진엔딩·엔딩 5종까지 Canon 공백 채우기
- **방식**: 프롬프트를 `.txt` 로 작성 → `to_single_line()` 변환 → `page.keyboard.insert_text()` atomic 주입 → Enter · 한 쿼리 = 한 메시지
- **Canon 원칙 5건 강제**: 나이트 우주 창조 · 모두 비악 · Q-CORE 4 이중 자아 · 진엔딩 동료 명단 락업 · 할배 속죄 은닉
- **프롬프트 길이**: NotebookLM 한도 ~3000자. 각 프롬프트 1400~1900자로 축소 + Canon 핵심 embedding
- **응답 평균**: 70~100초 · 5500~7700자

## 쿼리 목록

### Tier 1 — Act 1 집필 직결·카타르시스 정점

| # | 주제 | 프롬프트 | 응답 | 상태 |
|---|------|---------|------|-----|
| 01 | Ch.02~03 마을 도달·성인식 목걸이 | [01_ch02_coming_of_age.txt](../../../.planning/nlm_prompts/01_ch02_coming_of_age.txt) | [01_ch02_coming_of_age.md](../../../.planning/nlm_responses/01_ch02_coming_of_age.md) | ✅ |
| 02 | Ch.14~16 삼각 관계 감정 곡선 | [02_ch14_16_triangle_emotion.txt](../../../.planning/nlm_prompts/02_ch14_16_triangle_emotion.txt) | [02_ch14_16_triangle_emotion.md](../../../.planning/nlm_responses/02_ch14_16_triangle_emotion.md) | ✅ |
| 04 | Ch.16 진엔딩 Scene 2 학살 | [04_ch16_ending_massacre_order.txt](../../../.planning/nlm_prompts/04_ch16_ending_massacre_order.txt) | [04_ch16_ending_massacre_order.md](../../../.planning/nlm_responses/04_ch16_ending_massacre_order.md) | ✅ |
| 06 | Ch.04~06 숲 악마·영웅 칭호·루시안 | [06_ch04_06_forest_boss_and_lucian.txt](../../../.planning/nlm_prompts/06_ch04_06_forest_boss_and_lucian.txt) | [06_ch04_06_forest_boss_and_lucian.md](../../../.planning/nlm_responses/06_ch04_06_forest_boss_and_lucian.md) | ✅ |
| 07 | Ch.11 기억 회복 · Act 전환 | [07_ch11_memory_recovery_transition.txt](../../../.planning/nlm_prompts/07_ch11_memory_recovery_transition.txt) | [07_ch11_memory_recovery_transition.md](../../../.planning/nlm_responses/07_ch11_memory_recovery_transition.md) | ✅ |
| 08 | Ch.15 마왕 봉인 대면·세리스 | [08_ch15_demon_king_encounter.txt](../../../.planning/nlm_prompts/08_ch15_demon_king_encounter.txt) | [08_ch15_demon_king_encounter.md](../../../.planning/nlm_responses/08_ch15_demon_king_encounter.md) | ✅ |

### Tier 2 — 세계관 심화·동료 합류·엔딩 차별화

| # | 주제 | 프롬프트 | 응답 | 상태 |
|---|------|---------|------|-----|
| 03 | 여섯 번의 균형 역사·할배 시점 | [03_six_cycles_history.txt](../../../.planning/nlm_prompts/03_six_cycles_history.txt) | [03_six_cycles_history.md](../../../.planning/nlm_responses/03_six_cycles_history.md) | ✅ |
| 05 | 카르조르 저항군 내부 구조 | [05_karzor_rebel_structure.txt](../../../.planning/nlm_prompts/05_karzor_rebel_structure.txt) | [05_karzor_rebel_structure.md](../../../.planning/nlm_responses/05_karzor_rebel_structure.md) | ✅ |
| 09 | Ch.07~10 도적·마법사·신관·할배 2차 | [09_ch07_10_companions_join.txt](../../../.planning/nlm_prompts/09_ch07_10_companions_join.txt) | [09_ch07_10_companions_join.md](../../../.planning/nlm_responses/09_ch07_10_companions_join.md) | ✅ |
| 10 | Ch.12~13 세 자아의 밤·인간 이탈 | [10_ch12_13_human_departure.txt](../../../.planning/nlm_prompts/10_ch12_13_human_departure.txt) | [10_ch12_13_human_departure.md](../../../.planning/nlm_responses/10_ch12_13_human_departure.md) | ✅ |
| 11 | 진엔딩 Scene 3~6 왕좌 시퀀스 | [11_true_ending_scene3_6_throne.txt](../../../.planning/nlm_prompts/11_true_ending_scene3_6_throne.txt) | [11_true_ending_scene3_6_throne.md](../../../.planning/nlm_responses/11_true_ending_scene3_6_throne.md) | ✅ |
| 12 | 엔딩 5종 차별화 설계 | [12_endings_five_differentiation.txt](../../../.planning/nlm_prompts/12_endings_five_differentiation.txt) | [12_endings_five_differentiation.md](../../../.planning/nlm_responses/12_endings_five_differentiation.md) | ✅ |

## 설계 시놉시스 (synthesis 정제본)

집필 직전 Canon 후보로 정제한 시놉시스. 응답 원본에서 핵심 대사·장면·복선만 추출.

### Act 1 (Ch.02~Ch.11)
- [[synthesis_ch02_03_fernhollow]] — Ch.02~03 마을 도달·성인식 (Fernhollow 추천·할배 대사·의식 3단계·괄호 B 3 후보)
- [[synthesis_ch04_06_forest_boss_lucian]] — Ch.04~06 숲 악마·영웅·루시안 (의지결 드롭·"둥지가 있었소"·루시안 길치 첫 폭발·타종족 진압 3조 맥락)
- [[synthesis_ch07_10_companions]] — Ch.07~10 카일·엘라라·미리암 합류·할배 2차 (뒷골목·금서 서고·학살 현장·모닥불 재회·할배 대사 3 후보)
- [[synthesis_ch11_memory_recovery]] — Ch.11 기억 회복·Act 1→2 전환 (거대 고룡·용의 확장 대사·재맥락 5 대사·1인칭→3인칭 문장 후보)

### Act 2 (Ch.12~Ch.16)
- [[synthesis_ch12_13_departure]] — Ch.12~13 세 자아의 밤·진실의 식탁·인간 4 이탈 (C안 3 반사·이탈 순서·미리암 연모 발현·카르조르 첫발)
- [[synthesis_ch14_16_triangle]] — Ch.14~16 삼각 관계 (세리스 3단계·미리암 C안·첫 직면 대사·갭모에 5 씬)
- [[synthesis_ch15_demon_king]] — Ch.15 마왕 봉인 대면 (수정 2·마왕 의식 폭풍·세리스 시조이신가·나이트 가해자 자각·오르토무스 용족)
- [[synthesis_ch16_massacre]] — Ch.16 진엔딩 Scene 2 학살 (사망 순서 A안·보르단·세리스 대사·플래시백 매칭·3 생존자)

### 엔딩
- [[synthesis_endings_five]] — 엔딩 5종 차별화 (E1~E4 각 연출·E5 발동 시점 C안·5 엔딩 메시지 테이블)

### 세계관 심화·Act 2 무대
- [[synthesis_six_cycles]] — 여섯 번의 균형 역사 (6 순환 표·할배 독백 3 회고·이전 세대 수호자 Template 관계·마족 대학살 진실·우주 포식자 C안)
- [[synthesis_karzor_rebel]] — 카르조르 저항군 (4 핵심 인물·이념 분열·나일라 주방 갭모에·3 사막 전투 문화·C안 거점·할배 흔적)

### 진엔딩 왕좌 시퀀스
- [[synthesis_true_ending_scene3_6]] — 진엔딩 Scene 3~6·에필로그 (카일+엘라라 서술·108 흑요석 계단·이전 수호자 유적 A안·왕관형 풀페이스 투구·D안 혼합 군세·파란→보라 광채 Cut 3)

### Act 2 내부 역학 (보강자료 정제)
- [[synthesis_phase4_5_internal_conflict]] — 페이즈 4.5 인간 4인 vs 세리스 갈등 3막 (모닥불 살기·은/음 속성 상극·미냐 계열 룬어·혐오 역설 전투력)

### 작법 헌법 (보강자료 정제)
- [[synthesis_dark_fantasy_4principles]] — 다크판타지 묘사 4원칙 (오감 날것·상식 반전+코스믹 호러·템포 조절·병적 비유+잔혹한 비용)

### ✅ 모든 synthesis 완료 (12/12)
세션 오염으로 1차 실패했던 11 Scene 3~6 은 **"맥락 리셋 명시 프롬프트"** 로 2차 시도 성공 (76.1초 · 6902자). 프롬프트 상단에 *"[주제 · 오해 금지] 이번 질문은 ... 입니다. 이전 질문과 별개로 신선하게 응답해 주십시오."* 명시가 NotebookLM 세션 과포화 우회 기법으로 확인됨.

## 핵심 수확 요약 (각 쿼리별 Canon 편입 재료)

### 01. Ch.02~03 마을·성인식 (완료 · 5519자)
- **마을명 확정 추천**: **Fernhollow** (양치식물+오목한 계곡 · Ashenveil 잿빛 안개와 대비 · "따뜻한 은신처")
- **할배 2차 대사 후보 3개** + 복선 대사 1개
- **성인식 3단계 절차**: 청수 세례 → 결속의 끈 → 목걸이 수여
- **첫 의지결 감응 괄호 B 발화 3개 예시**

### 02. Ch.14~16 삼각 관계 (완료 · 7555자)
- **세리스 감정 3단계**: 유혹(Ch.16) → 룬어 전수(Ch.17~20) → 파멸 예감(Ch.21)
- **갭모에 3 씬**: 머리 쓰다듬기 · 손잡기 · 상처 치료
- **미리암 연모 발현 = Ch.13 이탈 시 마지막 주저** (C안 확정)
- **미리암-세리스 첫 직면** 대사 4개 + 나이트 괄호 B + 여운 문장

### 04. Ch.16 진엔딩 학살 순서 (완료 · 7592자)
- 5인 사망 순서 옵션 A/B/C 비교 + 추천
- 보르단·세리스 마지막 대사 후보
- 플래시백 일상 씬 매칭
- 3 생존자 연출 상세
- Scene 2 → Scene 3 연결

### 06. Ch.04~06 숲 악마·루시안 (완료 · 7677자)
- Ch.04 숲 악마 본체 전투 · 첫 기억 파편 · 첫 의지결 "둥지가 있었소" 드롭
- Ch.05 영웅 칭호 + 불안 복선 1개
- Ch.06 루시안 첫 등장 · 5~7교환 대사
- 타종족 진압 목격 · 루시안 첫 균열

### 07. Ch.11 기억 회복·Act 2 전환 (완료 · 6832자)
- 마지막 수호신 거대 용 전투 3페이즈
- 기억 회복 시점 연출 4안
- 이전 10화 기억 파편 재맥락 5개
- 기억 ≠ 힘 분리 연출
- 1인칭 → 3인칭 전환 마지막·첫 문장

### 08. Ch.15 마왕 봉인 대면 (완료 · 8750자)
- 수정 2 봉인 접근 Tilnar 동굴 최심부
- 마왕 형상·인지 방식
- 세리스 "시조이신가" 대사 씬 상세
- 나이트 "가해자 소속" 자각 · 침묵 원칙
- 이벤트 용족 1명 설계

### 03. 여섯 순환 역사 (🔄 전송 중)
### 05. 카르조르 저항군 (⏳ 대기)
### 09. Ch.07~10 동료 합류 (⏳ 대기)
### 10. Ch.12~13 인간 이탈 (⏳ 대기)
### 11. 진엔딩 Scene 3~6 (⏳ 대기)
### 12. 엔딩 5종 차별화 (⏳ 대기)

## 기술 메모

### 쪼개짐 버그 해결 과정 (FAIL-018 후보)
1. **v1 실패**: `ask_question.py` 가 `StealthUtils.human_type()` 사용 → 한 글자씩 keystroke → NotebookLM UI 가 중간에 엔터 감지하여 프롬프트를 여러 메시지로 분리 전송 (대표님 스크린샷 직접 증명)
2. **v2 실패**: `to_single_line()` 로 `\n` 제거했으나 여전히 쪼개짐 — human_type() 자체가 delay 있어서 중간 submit 트리거
3. **v3 실패**: `.fill()` 교체 시도했으나 Angular 상태 업데이트 미트리거로 Enter 시 빈 값 인식
4. **v4 성공**: `page.keyboard.insert_text()` 로 IME composition 이벤트 atomic 삽입 + 300ms sleep + Enter. 쪼개짐 물리적 불가

### 프롬프트 길이 제한
- NotebookLM 한도: **약 3000자** (대표님 확인)
- 실측: 4440자 → rc=1 실패 / 1413자~1900자 → 정상 (71~100초)

### 실제 전송 내용 박제
- 원본 `.txt` 는 사람이 편집 가능한 구조적 포맷 유지
- runner 가 `to_single_line()` 으로 변환 후 `.sent.txt` 에 저장
- 대표님 검수 가능한 "실제 NotebookLM 에 들어간 문자열" 영구 박제

## Related

- [[../../main_character]] — 주인공 나이트 Canon
- [[../../케릭 컨셉 및 프로필]] — 대표님 직접 작성 동료 8인 Canon 최상위
- [[../../novel/style_bible_v2_2026-04-22]] — 문체 헌법
- [[../../novel/outline]] — 소설 구조
- [[../brainstorm_2026-04-21]] — 원전
- [[../brainstorm_2026-04-22_karzor_act2_revelation]] — Act 2 Karzor 서사
