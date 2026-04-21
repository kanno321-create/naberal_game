# naberal_game

> Unity 6 Steam 솔로 인디 게임 — 로그라이크/시뮬/RPG 방향 장기 창작 프로젝트.
> 대표님의 평생의 꿈이자, 나베랄 그룹 Layer 2 두 번째 스튜디오.

## 상속 인프라
- **Layer 1**: `../harness/` (naberal_harness v1.0)
- **Layer 2**: 이 저장소 (`naberal_game`) — 독립 git 저장소
- **자매 스튜디오**: `../shorts/` (AI 영상 제작, Phase 10 진입 대기)

## 기술 스택
- **엔진**: Unity 6 LTS
- **언어**: C# 12 (.NET 9)
- **플랫폼**: Steam PC (Steamworks SDK · Steamworks.NET)
- **AI 도구 체인**: Claude Code (C# 코드) · Nano Banana Pro (2D/UI) · Meshy 4 (3D) · Suno v4 (음악) · ElevenLabs v3 (보이스)
- **버전관리**: Git + Git LFS

## Phase 로드맵 (10 Phase)
`0 Bootstrap → 1 Identity/Pipeline → 2 Domain Definition → 3 Agent Team → 4 MVP Prototype → 5 Vertical Slice → 6 Steam Page → 7 Alpha/Beta → 8 Release → 9 Sustained Ops`

**현재**: Phase 0 Bootstrap 완료 (2026-04-20 창업일). Phase 1 진입 대기.

상세: [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)

## Quickstart

### 새 세션 시작 시
```bash
cd studios/game/
# Claude Code 세션에서 CLAUDE.md 자동 로드 (Session Init 5 문서)
# session_start.py Hook 이 자동 감사 + Navigator Coverage 리포트 주입
```

### AI 위키 + Obsidian 활용
`wiki/` 폴더를 Obsidian 으로 open → 그래프뷰·백링크·frontmatter 검색. AI 에이전트도 같은 폴더를 RAG 소스로 사용 (이중 용도).

### Navigator 커버리지 검증
```bash
python -m scripts.validate.navigator_coverage
# CLAUDE.md Navigator 매트릭스 ↔ .claude/agents/ + .claude/skills/ 동기화 확인
```

## 참조 게임 (솔로 인디 1인 Steam 히트)
- **Balatro** (LocalThunk, 2024) — 로그라이크 · Steam Top 10
- **Animal Well** (Billy Basso, 2024) — Metroidvania · GOTY 후보
- **Vampire Survivors** (poncle, 2022) — Bullet Heaven

## License
Private. 대표님 (kanno321-create) 개인 창작물.
