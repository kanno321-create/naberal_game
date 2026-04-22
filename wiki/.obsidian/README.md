---
title: .obsidian/ vault 설정 앵커
purpose: Obsidian vault 영속성 보장
created: 2026-04-22
---

# .obsidian/ — vault 설정 앵커 (커밋 필수)

이 폴더는 Obsidian이 `wiki/`를 vault 로 인식하게 만드는 필수 설정이다. **삭제 금지, 재생성 금지.**

## 커밋 파일 (3종)

| 파일 | 역할 |
|------|------|
| `app.json` | 에디터 기본 동작 — live preview · wikilink 단축 문법 · 새 파일 위치 |
| `core-plugins.json` | 코어 플러그인 활성화 — graph · backlink · outgoing-link · tag-pane · outline · page-preview |
| `graph.json` | 그래프뷰 — 태그·경로 기반 색상 그룹 (왕국·지리·경제·문화 별 색) · 고립 노드 표시 · 레이아웃 파라미터 |

## Gitignore 제외 파일

다음은 `../../. gitignore` 에 의해 git에서 제외된다 (per-user 상태):
- `workspace.json` — 대표님의 창 레이아웃·열어둔 탭
- `workspace-mobile.json`
- `cache`
- `.trash/`

## 영속성 보장

세션마다 이 폴더가 유지되는 이유:
1. **Git commit** 됨 — clone 하거나 다른 기기에서도 동일
2. **session_start.py Hook** 이 세션 시작 시 `.obsidian/app.json` · `core-plugins.json` · `graph.json` 존재 여부 검증 → 누락 시 경고 주입
3. **하네스 template** 에 동일 파일 보관 (`../../../harness/templates/obsidian-vault/`) — 새 스튜디오 생성 시 자동 복사

## 사용법 (대표님)

1. Obsidian 실행 → `Open vault` → `wiki/` 폴더 선택
2. 좌측 사이드바 → `Graph view` 아이콘 (또는 Ctrl+G)
3. 그래프에서 태그별 색상 그룹 자동 표시됨
4. MOC 파일 (`wiki/MOC.md`) 부터 시작해서 링크 따라가기

---

*Bootstrap: 2026-04-22 · naberal 감마*
