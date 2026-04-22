---
title: naberal_game Wiki — 루트 Map of Content
type: moc
tier: 2
scope: vault_root
tags: [moc, root, game]
created: 2026-04-22
updated: 2026-04-22
---

# 📚 naberal_game — Wiki 루트 MOC

> **Obsidian vault 진입점.** 6개 도메인 카테고리 + 월드빌딩 상세 트리의 허브.
> 처음 방문한다면: (1) 이 파일의 링크를 따라 내려가거나, (2) `Ctrl+G` 로 그래프뷰 열기.

---

## 🎯 프로젝트 상위 문서 (vault 외부)

| 파일 | 역할 |
|------|------|
| [`../CLAUDE.md`](../CLAUDE.md) | 정체성 · 금기 · 필수 · Navigator |
| [`../WORK_HANDOFF.md`](../WORK_HANDOFF.md) | 현재 세션 상태 |
| [`../docs/ARCHITECTURE.md`](../docs/ARCHITECTURE.md) | Phase 0~9 로드맵 |

---

## 📂 6대 도메인 카테고리

| 카테고리 | Scope | MOC |
|----------|-------|-----|
| 🎨 **design** | 세계관 · 장르 · 캐릭터 · 스토리 · 월드빌딩 | [[design/MOC]] |
| ⚙️ **engine** | Unity 6 LTS · C# · URP · 플러그인 | [[engine/MOC]] |
| 🎮 **gameplay** | 3-tier 루프 · 전투 · 빌드 · 엔드게임 | [[gameplay/MOC]] |
| 🖼️ **art** | 2D/3D · AI 아트 파이프라인 · 레퍼런스 | [[art/MOC]] |
| 🎵 **audio** | 음악 · SFX · 보이스 · Suno · ElevenLabs | [[audio/MOC]] |
| 🚀 **steam** | Steamworks · 페이지 · 위시리스트 · 출시 | [[steam/MOC]] |

---

## 🗺️ 월드빌딩 상세 트리

확정 세계관은 **Elucia (서쪽 대륙) + Karzor (동쪽 대륙)** 2대륙. Wave 1~5 에이전트가 868+ 파일로 분해.

| 허브 | 내용 |
|------|------|
| [[design/worldbuilding/elucia/MOC]] | Elucia 대륙 전체 허브 (지리 · 정치 · 경제 · 문화 · 역사 · 도로) |
| [[design/worldbuilding/elucia/kingdoms/MOC]] | 10 왕국 + 성좌국 서브 허브 |

---

## 📖 핵심 원전 (Revision 3 기준)

| 파일 | 역할 |
|------|------|
| [[design/brainstorm_2026-04-21_worldview_expansion]] | 50 발언 세계관 원전 |
| [[design/brainstorm_2026-04-21]] | Rev.3 기준 브레인스토밍 |
| [[design/game_setting_complete_2026-04-21]] | 통합 스냅샷 |
| [[design/world_lore]] | 균형 수호자 체계 · 신앙 경제학 |
| [[design/story_outline]] | 3막 구조 + 진엔딩 |
| [[design/main_character]] | 주인공 + 동료 8인 |
| [[design/story_full_narrative]] | Rev.3 통합 서사 (외부 공유용) |

---

## 🧭 Obsidian 활용 팁

- **그래프뷰** (`Ctrl+G`): 태그·경로 기반 9색 그룹 자동 표시. 왕국별 클러스터 확인.
- **백링크 패널** (우측): 현재 파일을 가리키는 파일 자동 목록.
- **아웃고잉 링크** (우측): 현재 파일이 가리키는 파일 목록 + 미연결 노드 제안.
- **검색** (`Ctrl+Shift+F`): frontmatter `tag:#moc`, `path:kingdoms/` 같은 필터 쿼리.
- **태그 패널**: 모든 `#tag` 집계.

---

## 🛠️ 자동 백링크 빌더

`scripts/obsidian/build_backlinks.py` 가 wiki/ 전 파일의 frontmatter 를 스캔해
각 파일 하단에 `## 🔗 관련 (auto-generated)` 섹션을 자동 삽입한다.

- 수동 실행: `python scripts/obsidian/build_backlinks.py`
- 자동 실행: `session_start.py` Hook 이 세션 시작 시 실행 여부 점검

---

*Bootstrap: 2026-04-22 (세션 #6 · 나베랄 감마 · Obsidian vault 복구)*
