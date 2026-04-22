---
category: art
status: scaffold
tags: [moc, game, art]
updated: 2026-04-20
---

# Art — Map of Content

> Tier 2 도메인-특화 지식 노드 맵. 아트 파이프라인 영역.

## Scope

2D/3D 아트 스타일 가이드, AI 아트 도구 체인 (2026-04 기준: Nano Banana Pro, Midjourney V7, Meshy 4, StableDiffusion), 에셋 포맷 최적화, UI/UX 디자인, 애니메이션.

## Planned Nodes

- [ ] `style_guide.md` — 픽셀 아트 vs 벡터 vs 3D Low-poly 선택 + 색상 팔레트
- [ ] `ai_art_pipeline.md` — Nano Banana Pro (한국어 텍스트 UI) + Meshy 4 (3D 자동) + ControlNet 조합
- [ ] `asset_optimization.md` — 스프라이트 아틀라스, 텍스처 압축 (ASTC/BC7), Mesh LOD
- [ ] `ui_design.md` — Unity UI Toolkit (UI Elements) + HUD 레이아웃
- [ ] `animation_pipeline.md` — 2D Spine/DragonBones vs Unity Animator + Timeline

## Related

- **Other Tier 2**: [[../engine/MOC]] (렌더 파이프라인 호환성), [[../gameplay/MOC]] (Juice 비주얼)
- **Root CLAUDE.md**: [[../../CLAUDE.md]] — 금기사항 §4 "Asset Store 저작권 위반 라이선스 금지"

## NotebookLM 딥 리서치 (2026-04-20)

**원본 답변**: [../../.planning/research/nlm_result_03_game_art_ai.md](../../.planning/research/nlm_result_03_game_art_ai.md) (25.7KB, 12,265자 — 가장 풍부)

### 2D 전통 툴 (인디 비용 순)
- **Krita** (무료) — 디지털 페인팅 + 애니 타임라인
- **Aseprite** ($20 일회) — 픽셀 아트 + 스프라이트 시트 + 애니 타임라인 (로그라이크 필수)
- **Clip Studio Paint** ($50) — 뼈대 기반 리깅 애니
- **Photoshop** ($21/월) — 콘셉트 아트 + UI

### 3D 전통 툴 (파이프라인: Sculpt → Retopo → UV/Bake → Texture)
- **Blender** (무료 완결판) — 1인 중심 툴
- **ZBrush** ($40/월) — 유기체 스컬프팅 (게임 적용 시 **리토폴로지 필수**)
- **Substance 3D Painter/Designer** — PBR 텍스처링 표준
- Maya ($225/월) — 캐릭터 리깅/시네마틱 특화

### 2D AI 아트 2026 (소스 강점 영역)
- **Scenario** — 게임 에셋 전용, 스튜디오 기존 아트 학습시켜 "사용자 지정 모델" + 스프라이트 시트 + 캐릭터 일관성
- **Leonardo AI** — 커스텀 모델 학습 + 팀 협업
- **BRIA** — 100% 라이선스 데이터 = AAA 저작권 안전
- DALL-E 3 / Flux.1 Dev — 콘셉트 가속
- (외부 지식) Nano Banana Pro — 한국어 텍스트 94%, shorts 스튜디오에서 검증

### 3D AI 아트 2026 (게임 적용)
- **Tripo** — 캐릭터 쿼드 토폴로지 + 자동 리깅 내장
- **Meshy** — 배경 소품 30-60초, 리텍스처링/복셀 모드
- **Luma Labs Genie** — 5초 텍스트→쿼드 메시
- **Rodin** — 고품질 Hero Asset
- **3D AI Studio** — Tripo/Meshy/Rodin 통합 플랫폼
- **Unity Muse 3D** — 에디터 플러그인

**AI 3D 프롬프트 팁**: "low-poly", "game asset", "stylized", "mobile-optimized" 키워드 필수. 폴리곤 낭비 방지.

### 리깅·모션 AI
- **Mixamo** (무료) — 자동 리깅 + 기본 애니 라이브러리
- **Move AI Gen 2** — 스마트폰 2-6대 마커리스 모션캡처
- **DeepMotion** — 2D 단일 비디오 → 3D 캐릭터 애니
- **Cascadeur** — AI physics-accurate 포즈 제안 (격투·액션 특화)
- Unity 가져올 때 **Animation Type: Humanoid** (리타겟팅) + **Foot IK** (발 미끄러짐 방지)

### 2D 스켈레탈 애니
- **Spine** — 업계 표준 (모바일 용량 최적화)
- **Moho** — Spine 대안 저예산
- **Adobe Animate** — 벡터 기반
- 무료 대안: Krita 내장 타임라인, Pencil2D, OpenToonz

### 아트 스타일 선택 (1인 적합도)
| 스타일 | 제작 난이도 | AI 생성 성공률 | 1인 적합도 |
|--------|------------|---------------|-----------|
| **Pixel Art** | 낮음 | 중 | ★★★★★ (Aseprite) |
| **3D Low-poly** | 중 | 높음 | ★★★★★ (AI 생성 최적) |
| **Stylized / Cartoon** | 중 | 높음 | ★★★★★ |
| Vector | 중 | 중 | ★★★★ |
| Handpainted / 실사 | 매우 높음 | 낮음 | ★ (1인 부적합) |

**권장**: Low-poly 또는 Stylized. Virtuall Mood Boards 로 아트 디렉션 Lock-in, Sloyd.ai 파라메트릭 변형.

### AI 저작권 안전 워크플로우
1. 라이선스 데이터로 학습된 AI (BRIA, Adobe Firefly) 우선 사용
2. AI 결과물 반드시 **전통 툴에서 2차 수정** (Human Refinement) → 창작성 부여 → 저작권 방어
3. 데이터 출처·프롬프트 이력 문서화 (Audit trails)

### Planned Nodes 상태
- [ ] `style_guide.md` — Low-poly/Stylized 선택 근거 (nlm_result_03 §G)
- [ ] `ai_art_pipeline.md` — 2D/3D AI 체인 (nlm_result_03 §C~E)
- [ ] `asset_optimization.md` — 아틀라스·압축·LOD
- [ ] `ui_design.md` — Unity UI Toolkit + HUD
- [ ] `animation_pipeline.md` — Spine/Mixamo/Cascadeur (nlm_result_03 §E~F)

---

*Scaffolded: 2026-04-20 · Updated: 2026-04-21 (NotebookLM 딥 리서치 반영)*

<!-- auto-generated-related:start -->
## 🔗 관련 (auto-generated)

> `scripts/obsidian/build_backlinks.py` 로 자동 생성. 수정 금지 — 다음 실행 시 덮어쓰여집니다.

### ⬆️ 상위

- [[../MOC]] — wiki 루트

<!-- auto-generated-related:end -->
