---
name: Obsidian vault 3층 시너지 복구 (세션 #6)
description: 하네스+wiki+Obsidian 3층 시너지가 공식 작동 — vault 설정, MOC 계층, 자동 백링크 빌더, 영속성 3중 앵커 전부 박제 완료
type: project
created: 2026-04-22
originSessionId: aa89454c-e339-4aaa-9510-76f7c7d0d6ba
---
# Obsidian vault 3층 시너지 시스템 (세션 #6 구축)

## 핵심 사실

**2026-04-22 세션 #6에 나베랄 감마가 Obsidian vault 시스템을 전면 복구했다.** 이전까지 `wiki/`에 838개 파일이 있었지만 `.obsidian/`가 비어 있어 대표님이 그래프뷰·백링크를 사용할 수 없었다. 대표님의 "파일 하나하나 연결 다 해야하나" 지적으로 원인 진단 → 시스템 복구 수행.

**Why**: 대표님이 강조한 "하네스+AI wiki+Obsidian 3층 시너지"는 이 시스템이 작동할 때만 프로젝트의 가치가 발생한다. 하나라도 끊어지면 에이전트는 파일을 쏟아내지만 대표님은 관계성을 이해 못하는 비대칭이 발생.

**How to apply**: 향후 월드빌딩·캐릭터·게임플레이 파일 추가 시 아래 규칙 엄수.

## 3층 구조

1. **Layer 1 하네스** (`naberal_group/harness/`)
   - `templates/obsidian-vault/` — vault 기본 설정 3종 (app.json · core-plugins.json · graph.json)
   - `scripts/obsidian_build_backlinks.py` — 자동 백링크 빌더 마스터
   - `hooks/session_start.py` — `check_obsidian_vault()` 함수 포함 (game 버전 역이식됨)
   - `scripts/new_domain.py` Step 6b — 새 스튜디오 생성 시 위 3종 자동 scaffold

2. **Layer 2 AI wiki** (`game/wiki/`)
   - `MOC.md` (루트 허브) · `design/worldbuilding/elucia/MOC.md` · `kingdoms/MOC.md`
   - 838개 .md 파일 중 832개에 자동 생성된 `## 🔗 관련 (auto-generated)` 섹션 (커버리지 99.3%)
   - `MASTER_elucia_worldbook.md` — Wave5 통합 인덱스 유지 (링크 문법 점진 전환)

3. **Layer 3 Obsidian** (대표님 인터페이스)
   - `wiki/.obsidian/{app,core-plugins,graph}.json` 3종 commit됨
   - 그래프뷰 9색 그룹 (왕국·지리·정치·경제·문화·도로·역사 별 색상)
   - `wiki/.obsidian/workspace.json`은 per-user라 gitignore

## 영속성 3중 앵커 (다음 세션에도 유지 보장)

| 앵커 | 작동 방식 |
|------|---------|
| **Git commit** | vault 설정 3종 · MOC 3종 · build_backlinks.py 모두 commit 대상 |
| **session_start.py Hook** | 세션 시작 시 `check_obsidian_vault()` 자동 실행 → vault 설정 존재 + 백링크 커버리지 % 컨텍스트 주입. 85% 미만이면 경고 |
| **하네스 new_domain.py** | 새 스튜디오 생성 시 자동 scaffold Step 6b 로 이식 |

## 에이전트 룰 (월드빌딩)

`.claude/agents/worldbuilding/_shared_briefing.md` 에 추가된 조항:
- frontmatter 필수 key 표 (type·kingdom·subject)
- `<!-- auto-generated-related -->` 마커 구간 직접 작성 금지
- 파일 생성 후 `python scripts/obsidian/build_backlinks.py` 실행 의무
