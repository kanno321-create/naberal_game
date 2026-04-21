---
category: design
status: active
tags: [moc, game, design]
updated: 2026-04-21
revision: 2
---

# Design — Map of Content

> Tier 2 도메인-특화 지식 노드 맵. 게임 디자인 영역.
> **2026-04-21 대표님 브레인스토밍 Revision 2 박제 완료** — 세계관 · 스토리 · 캐릭터 노드 (동료 8인 확장).

## 확정 장르·톤

| 항목 | 확정 |
|---|---|
| **장르** | HD-2D 다크 판타지 JRPG — 턴제 핵앤슬래시 with 패링 |
| **톤** | 오버로드 풍 잔혹한 현실 · 도덕적 복잡성 · 서사 중심 |
| **룩** | Octopath Traveler × Triangle Strategy (HD-2D) |
| **엔진** | Unity 6 LTS + URP |
| **개발 기간** | 24개월 목표 (1인 개발) |

## 설계 헌법 (3조항)

### 제1조 — 공격과 방어의 책임 분리
공격 = 주인공의 성장 + 컨트롤 / 방어 = 동료의 스킬트리 + 전략

### 제2조 — 플레이 스타일 다양성
모든 극단 빌드가 엔드게임을 클리어 가능해야 함

### 제3조 — 인간 비악(非惡) 원칙
인간은 악이 아니다. 모든 종족이 나태한 신 · 타락한 교회의 피해자

상세: [[world_lore#설계-헌법-design-constitution]]

---

## 문서 인덱스 (Active)

| 문서 | 내용 | 상태 |
|---|---|---|
| [[world_lore]] | 세계관 — 균형 수호자 체계 · 신앙 경제학 · 순환 구조 · 우주 포식자 · 첫 번째 신 | ✅ Rev.1 |
| [[story_outline]] | 스토리 3막 구조 + 일반 엔딩 + 진엔딩 (설계 문서) | ✅ Rev.1 |
| [[main_character]] | 주인공 나이트 + **동료 8인 (인간 4 + 타종족 4)** + 중요 NPC | ✅ Rev.2 |
| [[story_full_narrative]] | **작가 검증용 통합 서사본** — 프롤로그부터 진엔딩·에필로그까지 읽히는 이야기 | 📝 외부 공유용 |

## 게임플레이 문서 연계

| 문서 | 연계 내용 |
|---|---|
| [[../gameplay/combat_system]] | 웨이브 턴제 · 패링 · 콤보 · 극딜 |
| [[../gameplay/build_system]] | 5대 빌드 분기 · 6직업 · 상태이상 |
| [[../gameplay/endgame]] | 히든 보스 · 역대 신 무기 · 진엔딩 조건 |

---

## 핵심 서사 명제 요약

1. **메타 반전** — Phase 1 에서 믿었던 것이 Phase 2 에서 뒤집힘
2. **학살 쾌감 → 죄책감 전환** — 같은 시스템, 뒤집힌 감정 (Spec Ops: The Line 구조)
3. **일반 엔딩 = 표면적 희망 / 진엔딩 = 근본 해결의 비극**
4. **인간 비악** — 모두가 피해자인 비극
5. **순환 구조** — 일곱·여덟 번째 균형 반복, 진엔딩이 순환 파괴 시도

---

## 대표님 결정 대기 사항

### 캐릭터 미확정
- 주인공 나이트의 본명·외형·무기·성별
- **동료 8명** 각자 이름·성별·구체 배경 (특히 인간 4명의 과거가 Phase 2 반전 무게 결정)
- "악의 신" 최종 칭호 명칭

### 게임플레이 미확정
- **콤보 정의**: 공격 횟수 vs 처치 수 vs 하이브리드
- 빌드 리셋 방식 (페이즈 전환 자동 / 유료 / 고정)
- 인간 동료 합류 순서

### 스토리 미확정
- 챕터 수 (5? 7? 각각 보스 할당)
- 현재 신 (최종 보스) 의 타락 양상 구체 묘사
- 인간 마법사 동료 = 첫 번째 신 계승자 설정 수용 여부

---

## Revision 2 변경 내역 (2026-04-21 2차 박제)

### 캐릭터 변경
- **동료 5명 → 8명 확장** (인간 4 + 타종족 4)
- 인간 동료 상세 컨셉 추가 (기사·신관·마법사·도적)
- 인간 마법사 동료 = 첫 번째 신의 마법 체계 계승자 설정 제안

### 확정 사항
- 주인공 = 고유 직업 "균형의 수호자" 고정 + 스킬트리 다직업 느낌
- 동료 직업 = 고정 + 보조 직업

---

## Planned Nodes (Phase 2+ 확장)

> 현재 박제된 3개 노드 외, 아래는 추후 확장.

### Scaffold 상태 (기존 유지)
- [ ] `genre_choice.md` — 장르 선택 근거 (이제 확정됨 — 별도 문서 불필요할 수도)
- [ ] `core_loop.md` — 30초·3분·30분 3-tier 루프 (gameplay/combat_system 에 일부 반영됨)
- [ ] `concept_document.md` — 1-page 컨셉 (한 줄 피치)
- [ ] `scope_bloat_prevention.md` — MVP 체크리스트

### 신규 제안 (Phase 2+)
- [ ] `chapter_breakdown.md` — 챕터별 세부 플롯
- [ ] `antagonist_roster.md` — 적 세력 상세 (교회 · 왕국 · 우주 포식자)
- [ ] `dialogue_tone_guide.md` — 대사 톤 가이드 (첫 번째 신 · 동료 · 교회)
- [ ] `world_map.md` — 행성 지리 · 종족 영역 배치
- [ ] `cinematic_storyboard.md` — 주요 컷신 스토리보드 (프롤로그 · Phase 2 전환 · 진엔딩)

---

## Related

- **Root CLAUDE.md**: [[../../CLAUDE.md]] — 금기사항 §6 "MVP 없이 기능 블로트 금지"
- **기획 원본 세션**: 2026-04-21 나베랄 감마 브레인스토밍
- **Other Tier 2**: [[../gameplay/MOC]] · [[../engine/MOC]] · [[../art/MOC]] · [[../audio/MOC]] · [[../steam/MOC]]

---

## 이전 NotebookLM 리서치 (2026-04-20 · 유효)

> 이전 Phase 0 에서 수행한 1인 개발 MVP 리서치. 대표님 세계관·장르 확정으로 일부만 유효.

**원본**: [../../.planning/research/nlm_result_01_indie_mvp_design.md](../../.planning/research/nlm_result_01_indie_mvp_design.md)

### 지금도 유효한 항목
- **14-Tool Arsenal** (2026 1인 개발 프레임)
- **MVP 3-tier 루프**: 30초·3분·30분 ([[../gameplay/combat_system]] 반영)
- **성공 공식**: Balatro·Animal Well·Vampire Survivors의 "독창적 코어 메커니즘"
- **실패 패턴**: 튜토리얼 지옥 / AI Slop / Scope Bloat / Feature Creep
- **추천 학습 채널**: GMTK · Jonas Tyroller · Acerola

### 이제 무효 또는 재평가 필요
- ~~로그라이크 vs 시뮬 vs RPG 장르 비교~~ — **JRPG 확정**
- ~~Slay the Spire · Into the Breach 벤치마크~~ — Octopath · Chained Echoes · Clair Obscur 로 대체
- Hades의 "죽음 = 스토리" — 대표님 기억상실·봉인 해제 설계로 대체 구현됨

---

*Scaffolded: 2026-04-20 · Updated: 2026-04-21 (대표님 브레인스토밍 1차 박제 — 세계관·스토리·캐릭터 확정)*
