---
title: "게임 디자인 2차 브레인스토밍 (2026-04-22)"
layer: 1
canon_tier: derived
type: brainstorm_origin
category: design
round: 2 · 게임 구조·플레이 경험·MVP 범위
round_1_ref: "[[brainstorm_2026-04-21]]"
round_1_5_ref: "[[brainstorm_2026-04-21_worldview_expansion]]"
session: "#6 · workspace 브랜치 · 집 환경"
created: 2026-04-22
updated: 2026-04-22
author: 대표님 직접 결정 · 나베랄 감마 구조화
status: active
parent: "[[MOC]]"
moc: "[[MOC]]"
derived_from:
  - "[[story_full_narrative]]"
  - "[[brainstorm_2026-04-21]]"
  - "[[brainstorm_2026-04-21_worldview_expansion]]"
related:
  - "[[../gameplay/MOC]]"
  - "[[../gameplay/mvp_phase4_scope]]"
  - "[[../gameplay/combat_system]]"
  - "[[../gameplay/build_system]]"
agent_briefing_level: required
---

# 게임 디자인 2차 브레인스토밍 — 2026-04-22

## 배경

세션 #3~#5 에서 세계관·전투·빌드·엔드게임은 확정. 이번 라운드는 **상위 게임 구조 · 플레이 경험 · MVP 범위** 5 축 11 결정.

1차 (2026-04-21) → 전투·빌드·엔드게임·동료 8인·콤보×재료·히든보스·최강무기
1.5차 (2026-04-21) → 세계관 11축 · 네이밍 세트 B · 정치 단위 26 · 마법 5계층
2차 (2026-04-22 · 본 문서) → **게임 구조·플레이 경험·MVP**

---

## 확정 11건

### G-A 월드 구조 & 진행

- **A1 · 구조 모델** = **(b) 허브 마을 + 지역 챕터** (Octopath·Chrono Trigger 결)
  - 26 정치 단위 중 플레이어가 실제 방문할 허브 5~8개 선별 필요
  - Ch.01 Ashenveil → Ch.02 Misthollow/Fernhollow → Karzor Tilnar 축
  - 역주행 가능 · 탐험 + 선형 서사
- **A2 · 마을 기능** = **(b) NPC 호감도·사이드 퀘스트 허브**
  - 허브 = 저장·쇼핑·NPC·사이드 퀘스트·동료 이벤트 트리거

### G-B 데스 & 세이브

- **B1 · 사망 시** = **(b) 전투 시작점 복귀** (FF7·고전 JRPG)
  - Soulslike 긴장 아님 · 서사 진행 부담 낮춤
- **B2 · 세이브 시스템** = **(a) 수동 + 자동 혼합**
  - 마을 간이 UI = 수동 저장 가능
  - 필드 진입·전투 종료 자동 세이브

### G-C 서사 전달 & 첫 30분

- **C1 · 메인 전달 방식** = **(b) 2D 대화창 + 초상화 기본 + 애니메이션 컷신 혼용**
  - 대표님 원문: *"애니메이션 컷신을 담고싶어"*
  - 핵심 장면 **3~5컷**: 프롤로그 마왕 / Ashenveil 습격 / Act 2 동료 이탈 / Act 3 진입 / 진엔딩
  - AI 도구 체인: Kling AI · Veo 3.1 · Nano Banana Pro (`.env` 키 보유)
  - 1인 개발 경제성: 2D 대화창 기본 + 임팩트 포인트에만 애니컷
- **C2 · 튜토리얼** = **(c) 서사 + 튜토리얼 통합** (자연스러운 온보딩 · 현대 표준)
  - Ch.01 진행 = 기본 조작 학습 (나이트 각성 = AP 학습 · 첫 몹 조우 = 기술 슬롯 학습)

### G-D Phase 4 MVP 범위 (3~4개월)

- **D1 · 데모 배경** = **(a) Ashenveil 공격 재현** (서사 충격 + 전투 통합)
  - 감정 훅 강력 · 서사 부담 수용
  - 애니컷은 Phase 5 Vertical Slice 에서 추가 (MVP 는 2D CG + 이펙트)
- **D2 · MVP 포함 범위** = 제시 11 ✅ 그대로 OK (상세 → `mvp_phase4_scope.md`)
- **D3 · 검증 기준** = **(b) + (c) 복합**
  - (b) 대표님 본인 판단 = **Phase 4 직후 내부 검증**
  - (c) Steam Next Fest 데모 공개 = **Phase 7 직전 공식 데모**
  - 두 시점 병존

### G-E 사이드 컨텐츠 & 호감도

- **E1 · 사이드 비중** = **(b) 얕은 시드 퀘스트** (Octopath 결)
  - NPC 심부름·수집 수준 · Persona 급 깊이 X
  - 1인 개발 컨텐츠 부담 적정
- **E2 · 호감도 진행** = **(d) 특정 이벤트 트리거** (Chrono Trigger 결)
  - 선물·대화 반복 시스템 X → 1인 개발 부담 경감
  - 동료 8인 × 이벤트 8~12종/인
  - 엔드게임 동료 극딜 모드 해금 조건 = 호감도 MAX → 이벤트 트리거 완료

---

## 설계 영향 분석

### 월드 맵 필터링 (G-A1 영향)

- Elucia 11 왕국 + Karzor 15 자치구 = 26 정치 단위 중 **실제 방문 허브 5~8개** 선별 필요
- 후보 (서사 연동):
  1. **Ashenveil** (Ch.01 · 시작 · 공격받아 파괴 → Act 2 재건)
  2. **Misthollow or Fernhollow** (Ch.02 · 첫 외부 마을) ← 대표님 Ch.02 결정 대기
  3. **Solaris** (Ch.? · 성좌국 수도 · 교황청 대면)
  4. **Duskgate** (Novas 수도 · 서남 루트)
  5. **Nomen 섬** (대륙 간 환승 · Karzor 진입)
  6. **Sabin** (Azim Pass 마법 감지 통과 장면)
  7. **Zarahim** (Karzor 수도)
  8. **Tilnar** (Ch.16 마족 동굴 · Act 3 종착)
- 나머지 18~21 정치 단위 = **배경 세계관 깊이** (NPC 언급·문서·지도상 존재). 방문 불필요.

### 동료 호감도 시스템 (G-E2 영향)

- 8인 × 이벤트 8~12 종 = 총 64~96 이벤트
- 각 이벤트 구조: 특정 챕터·장소 도달 → 동료 선택 참여 → 선택지 대화 → 호감도 +1
- 호감도 MAX → 고유 궁극기 해금 → 동료 극딜 모드 (엔드게임) 사용 가능

### MVP 우선순위 재확인 (G-D 영향)

- Ashenveil 공격 재현 = 서사 훅 최상 (감정 강도 · Act 2 재건 씨앗)
- 애니컷 MVP 제외 → 2D CG + 화면 효과 · 스크린쉐이크 · BGM 으로 감정 전달
- Phase 5 에서 애니컷 1~2컷 추가 (Ashenveil 소멸 · 어머니 마지막 대사)

---

## 다음 세션 결정 필요

### ✅ 본 세션 후반 해소 (2026-04-22)
1. MVP 파티 = **주인공 + 기사 + 신관 = 3인** (1 → 2명 확장 · 콤보 맛 체감 목적)
2. 균형 빌드 기술 선별 = **콤보 트리거 다양화 우선** (상세 → `../gameplay/mvp_phase4_scope.md`)
3. Ashenveil 2D CG = **5컷** 확정
4. Ch.02 도착 마을 = **Misthollow** 확정 (세션 #5 대기 해소)
5. Unity 6 LTS = **Phase 1 종료 직후 조기 설치** (대표님 "미리미리")

### ✅ 2차 라운드 전량 해소 (2026-04-22 · 후반 결정)

6. **Sabin 마법 감지 기술 근거 = C Nomen 수정 2 파생** 확정
   - Veilglass 봉인지 → Nomen 섬 유입 → Karzor Sabin 장치 재료 경로
   - Karzor 성좌 왕조가 **수정 2 가 태초 마왕 유물임을 모르고 사용** (감시 장치로 오인) — 교황청이 할배=수호자 모르는 구조와 평행한 이중 아이러니
   - **Act 3 플롯 신설**: Sabin 통과 위해 Nomen 섬에서 수정 2 조각 회수 → Sabin 장치 무력화 → Tilnar 마족 동굴 진입
   - Ch.16 전 Nomen 섬 챕터 신설 가능성

7. **MVP 기간 = 3~4개월 유지 (대표님 결단)**
   - 3.5~4.5 확장 철회
   - 압축 수단: 마을 UI 간소화 · Ashenveil CG AI 병렬 · Unity 조기 연습 · 상점 Phase 5 이관

**2차 라운드 13건 전건 해소 완료. 3차 라운드 진입.**

---

## Related

- [[MOC]] — 디자인 MOC Rev.2 → Rev.3 갱신 대상
- [[../gameplay/MOC]] — Rev.3 반영
- [[../gameplay/mvp_phase4_scope]] — Phase 4 MVP 상세 (본 문서 G-D 결과)
- [[../gameplay/combat_system]]
- [[../gameplay/build_system]]
- [[../gameplay/endgame]]
- [[brainstorm_2026-04-21]] — 1차 원전
- [[brainstorm_2026-04-21_worldview_expansion]] — 1.5차 세계관
- [[novel/ch01]] — Ch.01 집필본 · MVP 데모 서사 기반
- [[worldbuilding/elucia/kingdoms/kingdom_ilaris/villages/village_ashenveil_2026-04-22]]
- [[../../.planning/research/nlm_result_01_indie_mvp_design]] — 3-tier 루프 원천

---

*박제: 2026-04-22 · 원안: 대표님 직접 · 구조화: 나베랄 감마 · workspace 브랜치*
