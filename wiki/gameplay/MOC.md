---
category: gameplay
status: scaffold
tags: [moc, game, gameplay]
updated: 2026-04-20
---

# Gameplay — Map of Content

> Tier 2 도메인-특화 지식 노드 맵. 게임플레이 시스템 영역.

## Scope

핵심 루프, 진행 시스템 (unlock·progression·meta), 경제 시스템 (리소스·통화·밸런스), 난이도 곡선, 플레이어 에이전시, 피드백 루프 (Juice).

## Planned Nodes

- [ ] `core_loop_30s_3m_30m.md` — 30초 (행동) · 3분 (목표) · 30분 (세션) 3-tier 루프 설계
- [ ] `progression_systems.md` — meta-progression vs per-run 언락 (로그라이크 기준)
- [ ] `economy_balancing.md` — 리소스 획득/소비 곡선, 통화 인플레이션 방지
- [ ] `difficulty_curve.md` — 난이도 곡선 + Dynamic Difficulty Adjustment
- [ ] `feedback_juice.md` — 스크린쉐이크, 파티클, 사운드 임팩트 (Game Feel 원칙)

## Related

- **Other Tier 2**: [[../design/MOC]] (장르별 루프 특성), [[../audio/MOC]] (피드백 오디오), [[../art/MOC]] (피드백 비주얼)
- **Root CLAUDE.md**: [[../../CLAUDE.md]] — 필수사항 §4 "MVP 우선 — 핵심 루프 검증 후 확장"

## NotebookLM 딥 리서치 (2026-04-20)

**원본 답변**: [../../.planning/research/nlm_result_01_indie_mvp_design.md](../../.planning/research/nlm_result_01_indie_mvp_design.md) §2-3 (핵심 루프 + 디자인 원칙)

### 30초·3분·30분 3-tier 루프 (외부 게임 기획 지식)
- **30초** — 전투·이동의 즉각적 재미 (기본 컨트롤·타격감)
- **3분** — 스테이지/웨이브 클리어 및 단기 보상 (작은 선택·업그레이드)
- **30분** — 빌드 완성·업그레이드·로그라이크 런 종료 후 메타 성장

**Feature Creep 조기 감지 신호**: "이 기능이 30초 핵심 루프의 재미를 높이는가?" 에 답 못 할 때.

### Flow Theory · Juice · Risk/Reward · Meaningful Choice
- **Flow**: 플레이어 실력 ↔ 게임 난이도 곡선 일치 → Modl:play AI QA 로 난이도 스파이크 자동 감지
- **Juice**: 파티클 + 화면 흔들림 + 조명 + 효과음 조합. Unity UI Toolkit + VFX Graph + Animator Pitch 랜덤 (0.9-1.1) 으로 극대화
- **Risk/Reward**: Slay the Spire 의 덱빌딩 = 무작위 속 통제감
- **Meaningful Choice**: 로그라이크/시뮬/RPG 하이브리드의 핵심

### 하이브리드 장르 사례 (벤치마킹)
- **Slay the Spire** — RNG + 덱빌딩 통제감 (Risk/Reward 표본)
- **Into the Breach** — 적 행동 완전 공개 → 퍼즐적 해결
- **Hades** — 죽음을 스토리텔링화 → 로그라이크 피로도 감소

### AI 연결
- **Beehave** (행동 트리) + **LLM 로컬 모델** → 지능형 NPC 반응
- **Modl:play** AI QA → 맵 시뮬레이션 → 난이도 밸런스 자동 점검

### Planned Nodes 상태
- [ ] `core_loop_30s_3m_30m.md` — 3-tier 루프 상세 설계
- [ ] `progression_systems.md` — meta-progression vs per-run (로그라이크)
- [ ] `economy_balancing.md` — 리소스 곡선
- [ ] `difficulty_curve.md` — Flow + Dynamic Difficulty
- [ ] `feedback_juice.md` — Game Feel 원칙 (nlm_result_01 §3)

---

*Scaffolded: 2026-04-20 · Updated: 2026-04-21 (NotebookLM 딥 리서치 반영)*
