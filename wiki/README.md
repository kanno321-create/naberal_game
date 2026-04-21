---
tags: [readme, wiki-home, tier-2, game]
---

# 📚 naberal_game — Tier 2 Wiki

도메인-특화 지식 노드. naberal_game (Unity Steam 솔로 인디) 전용 RAG 소스 + Obsidian vault.

## Tier 분류

- **Tier 1** (`../../harness/wiki/`): 도메인-독립 공용 (모든 스튜디오 공유)
- **Tier 2** (이 폴더): 게임 개발 도메인 전용 (6 카테고리)
- **Tier 3** (`../.preserved/`): 향후 외부 자산 읽기 전용 저장소

## 카테고리 (6)

| 카테고리 | Scope | MOC |
|----------|-------|-----|
| `design/` | 장르 선택, 핵심 메카닉, 컨셉 문서, 게임 디자인 원칙 | [[design/MOC]] |
| `engine/` | Unity 6 설정, C# 패턴, 렌더링 파이프라인, 플러그인 | [[engine/MOC]] |
| `gameplay/` | 게임플레이 루프, 진행·경제 시스템, 밸런싱, 난이도 곡선 | [[gameplay/MOC]] |
| `art/` | 2D/3D 아트 파이프라인, AI 아트 도구 (Meshy, Nano Banana Pro) | [[art/MOC]] |
| `audio/` | 음악·SFX·보이스 (Suno, ElevenLabs, FMOD/Wwise) | [[audio/MOC]] |
| `steam/` | Steamworks API, 페이지 최적화, Early Access, 출시 체크리스트 | [[steam/MOC]] |

## Obsidian Vault 연동

이 `wiki/` 폴더 전체가 Obsidian vault. 대표님이 Obsidian 에서 이 폴더를 open 하면:
- `[[wiki-link]]` 자동 백링크·그래프뷰
- `tags:` frontmatter 기반 검색
- `.obsidian/` 폴더는 vault 설정 자동 저장

AI 에이전트도 같은 폴더를 읽음 — 이중 용도 설계.

## 현재 상태

**Phase 0 Bootstrap (2026-04-20)**: Scaffold — 6 카테고리 폴더 + MOC 스켈레톤만 존재. 실 노드는 Phase 2 Domain Definition 이후 채워짐.

**추가 절차:**
1. Phase 2 에서 각 카테고리의 `MOC.md` `Planned Nodes` checkbox 채우기
2. 노드 생성 시 frontmatter `status: stub → ready` 승격
3. 범용 노드(예: Unity 일반 패턴) 발견 시 Tier 1 (harness/wiki/) 이관 검토

---

*Scaffolded: 2026-04-20 (Phase 0 Bootstrap)*
