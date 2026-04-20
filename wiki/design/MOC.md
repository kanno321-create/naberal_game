---
category: design
status: scaffold
tags: [moc, game, design]
updated: 2026-04-20
---

# Design — Map of Content

> Tier 2 도메인-특화 지식 노드 맵. 게임 디자인 영역.
> 실제 노드 내용은 Phase 2 Domain Definition 이후 채워짐.

## Scope

장르 선택 근거, 핵심 메카닉 설계, 컨셉 문서, 게임 디자인 원칙 (Juice, Flow, Meaningful Choice, Risk/Reward), 레벨 디자인 패턴.

## Planned Nodes

> Phase 2 에서 채워질 노드 placeholder. 현재는 scaffold.

- [ ] `genre_choice.md` — 로그라이크 vs 시뮬 vs RPG 비교 + 솔로 인디 적합도
- [ ] `core_loop.md` — 핵심 게임플레이 루프 정의 (30초·3분·30분 3-tier)
- [ ] `concept_document.md` — 1-page 컨셉 (한 줄 pitch + USP + 레퍼런스)
- [ ] `solo_indie_success_patterns.md` — Balatro/Vampire Survivors/Animal Well 공통 패턴
- [ ] `scope_bloat_prevention.md` — MVP 정의 + 기능 블로트 방지 체크리스트

## Related

- **Tier 1**: (Phase 2 에서 링크)
- **Other Tier 2**: [[../gameplay/MOC]] (게임플레이 루프 연결), [[../engine/MOC]] (구현 제약)
- **Root CLAUDE.md**: [[../../CLAUDE.md]] — 금기사항 §6 "MVP 없이 기능 블로트 금지"

## NotebookLM 딥 리서치 (2026-04-20)

**원본 답변**: [../../.planning/research/nlm_result_01_indie_mvp_design.md](../../.planning/research/nlm_result_01_indie_mvp_design.md) (15.7KB, 7,152자)
**네비게이션**: [../../.planning/research/nlm_summary.md](../../.planning/research/nlm_summary.md)

### 이 카테고리 반영된 핵심
- **14-Tool Arsenal** (2026 1인 개발 프레임)
- **MVP 이중 의미**: Model-View-Presenter 코드 + Minimum Viable Product 제품
- **30초·3분·30분 3-tier 루프** (외부 지식)
- **성공 공식**: Balatro/Animal Well/Vampire Survivors 의 "독창적·직관적 코어 메커니즘 + 극대화된 게임성"
- **실패 패턴**: 튜토리얼 지옥 / AI Slop / Scope Bloat / Feature Creep
- **하이브리드 장르**: Slay the Spire (무작위 + 덱빌딩 통제감), Into the Breach (완전 정보 퍼즐), Hades (죽음 = 스토리)

### 추천 학습 채널
- 영어: **GMTK (Game Maker's Toolkit)** · Jonas Tyroller · Dev Enabled · Acerola
- 한국어: 레트로(retr0) · 골드메탈 · 케이디 · Unity Korea

### Planned Nodes 상태 (Phase 2+ 에서 개별 노드 생성 시 참조)
- [ ] `genre_choice.md` — 로그라이크/시뮬/RPG 비교 (nlm_result_01 §3 참조)
- [ ] `core_loop.md` — 3-tier 루프 설계 (nlm_result_01 §2-3, 외부 지식 보완)
- [ ] `concept_document.md` — 1-page 컨셉
- [ ] `solo_indie_success_patterns.md` — Balatro/Vampire Survivors (nlm_result_01 §1)
- [ ] `scope_bloat_prevention.md` — MVP 체크리스트 + CLAUDE.md AI 스코프 통제 (nlm_result_01 §2)

---

*Scaffolded: 2026-04-20 (Phase 0 Bootstrap) · Updated: 2026-04-21 (NotebookLM 딥 리서치 결과 반영)*
