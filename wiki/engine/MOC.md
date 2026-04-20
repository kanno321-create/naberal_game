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

---

*Scaffolded: 2026-04-20 (Phase 0 Bootstrap)*
