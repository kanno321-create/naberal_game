---
category: engine
status: scaffold
tags: [moc, game, engine, unity]
updated: 2026-04-20
---

# Engine — Map of Content

> Tier 2 도메인-특화 지식 노드 맵. Unity 6 엔진 영역.

## Scope

Unity 6 LTS 설정, C# 코드 패턴 (ScriptableObject, Assembly Definition, Addressables), 렌더링 파이프라인 (URP/HDRP 선택), Asset Store 라이선스 규칙, Plastic SCM/Git LFS, Build 파이프라인.

## Planned Nodes

- [ ] `unity_version_lock.md` — Unity 6 LTS 단일 버전 pin + Editor 설정 표준
- [ ] `render_pipeline_choice.md` — URP (2D/3D 모바일·PC 적합) vs HDRP (AAA) 결정 근거
- [ ] `csharp_patterns.md` — ScriptableObject 기반 데이터, Event Bus, State Machine
- [ ] `asset_store_license.md` — 상업 라이선스 검증 체크리스트 + 금지 에셋 blacklist
- [ ] `version_control.md` — Git LFS + Unity meta 파일 관리, Plastic SCM 대안
- [ ] `performance_profiling.md` — Profiler + Frame Debugger + GC Alloc 감시

## Related

- **Other Tier 2**: [[../design/MOC]] (장르별 엔진 요구사항), [[../art/MOC]] (렌더 파이프라인 결정), [[../steam/MOC]] (Steamworks SDK 통합)
- **Root CLAUDE.md**: [[../../CLAUDE.md]] — 금기사항 §5 "Unity 6 이외 버전 혼용 금지"

## NotebookLM 딥 리서치 (2026-04-20)

**원본 답변**: [../../.planning/research/nlm_result_02_unity6_all.md](../../.planning/research/nlm_result_02_unity6_all.md) (18.6KB, 9,301자)

### 학습 로드맵 (C# 중급자 전제)
1. **Unity 공식 "Essentials"** (8-10h) — 엔진 인터페이스
2. **Code Monkey 3D 게임 튜토리얼** (Overcooked 클론, 10h) — C#↔엔진 상호작용
3. **Brackeys / Tarodev / GMTK** — 심화 디자인·아키텍처
4. **한국어**: 레트로(retr0) 원리·구조, 골드메탈 장르별·도트, 케이디 기능 구현, Unity Korea 공식

### C# 게임 프로그래밍 패턴 (결합도 낮추기)
- **ScriptableObject** 데이터 아키텍처 (인스펙터 튜닝)
- **Observer Pattern**: UnityEvent / ScriptableObject Event (UI ↔ 로직 분리)
- **State Machine**: Idle/Run/Attack 각 상태 개별 클래스
- **Awaitable (async/await)** — Unity 6 신기능, Coroutine 대체
- **Object Pooling** (총알/이펙트/적 GC 스파이크 방지)

### 비주얼 (URP 필수)
- **URP 선택** (HDRP 아님) — 2D/3D 복합 인디 최적
- **Global Volume** 포스트 프로세싱 (Bloom, Vignette, Color Grading)
- **Shader Graph** 노드 기반 (Outline/Toon)
- **Light Baking + APV** 정적 조명
- **2D Lights** (Gem Hunter Match 샘플 참고)

### 퍼포먼스 (Steam PC 배포 기준)
- **Profiler + Project Auditor** (Unity 6.1) 정기 실행
- **GC Alloc 제거**: Update 내 문자열 합치기/LINQ/`GetComponent`/`FindObjectOfType` 금지 → `Start()/Awake()` 캐싱
- **Non-Alloc 물리**: `Physics.OverlapSphereNonAlloc` (할당 0)
- **LOD Group** + **Addressables** 스트리밍
- **IL2CPP 빌드** (C# → C++ 컴파일, 실행 속도 + 보안)

### Unity 6 신기능 (2024-2026)
- **UI Toolkit + Data Binding** → MVVM UI
- **GPU Resident Drawer** → Draw Call 감소
- **Adaptive Probe Volumes (APV)** → 동적 GI
- **Spatial-Temporal Post-processing (STP)** 업스케일링
- **Unity MCP + Claude Code** 플러그인 → 에디터 밖 CLI 씬 분석·스크립트 생성

### Planned Nodes 상태
- [ ] `unity_version_lock.md` — Unity 6 LTS 단일 버전 pin
- [ ] `render_pipeline_choice.md` — URP 확정 (nlm_result_02 §C)
- [ ] `csharp_patterns.md` — 5개 패턴 (nlm_result_02 §B)
- [ ] `asset_store_license.md` — 상업 라이선스 체크리스트
- [ ] `version_control.md` — Git LFS + Unity meta
- [ ] `performance_profiling.md` — Profiler + Project Auditor (nlm_result_02 §E)

---

*Scaffolded: 2026-04-20 · Updated: 2026-04-21 (NotebookLM 딥 리서치 반영)*
