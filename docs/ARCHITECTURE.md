# ARCHITECTURE — naberal_game

**⏱ Reading time:** ~3 min (Phase 0 Bootstrap — minimal; Phase 2+ 에서 확장)
**Last updated:** 2026-04-20
**Audience:** 세션 시작 시 이 프로젝트를 처음 로드하는 AI
**Phase status:** **Phase 0 Bootstrap 완료** (2026-04-20, 스튜디오 창업일). Phase 1 "Identity + 계획" 진입 대기.

---

## TL;DR

- **What**: 대표님의 평생의 꿈 — **Unity 6 Steam 솔로 인디 게임** (로그라이크/시뮬/RPG 방향, 12~24개월 장기 창작 프로젝트).
- **Stack**: Unity 6 LTS + C# + Steamworks.NET, AI 도구 체인 (Nano Banana Pro 아트 / Suno 음악 / ElevenLabs 보이스 / Claude Code 코드).
- **Status**: Phase 0 Bootstrap — 하네스 스캐폴드 + AI 위키 Tier 2 (6 카테고리) + Obsidian vault 준비 완료. 실 Unity 프로젝트 생성은 Phase 2 이후.
- **Parallel**: `studios/shorts/` (Phase 10 진입 대기) 와 병행. 시간 배분은 대표님 결정 대기.

## Phase 로드맵 (초안, Phase 2 에서 확정)

| Phase | 이름 | 목표 | 상태 |
|-------|------|------|------|
| 0 | Bootstrap | 하네스 스캐폴드 + Wiki + Obsidian + GitHub | ✅ 완료 (2026-04-20) |
| 1 | Identity + Pipeline Draft | 도메인 정체성 + 파이프라인 초안 + 금기/필수 확정 | 진입 대기 |
| 2 | Domain Definition | 장르 구체화 (로그라이크/시뮬/RPG 비중) + MVP 컨셉 1-pager | — |
| 3 | Agent Team Design | 게임 개발 에이전트 팀 (game-designer / unity-coder / art-director / steam-marketer 등) | — |
| 4 | MVP Prototype | 30초 핵심 루프 재생 가능한 Unity 프로토타입 | — |
| 5 | Vertical Slice | 3분 루프 완성 + 1개 레벨 폴리싱 | — |
| 6 | Steam Page | 페이지 오픈 + 위시리스트 축적 (출시 6개월 전 룰) | — |
| 7 | Alpha / Beta | 클로즈드 테스트 + Steam Next Fest 데모 | — |
| 8 | Release | Steam 정식 출시 | — |
| 9 | Sustained Ops | 패치 · DLC · 커뮤니티 | — |

> 위 Phase 는 shorts 스튜디오의 10-phase 패턴을 게임 개발 lifecycle 에 맞게 이식한 초안입니다. Phase 2 에서 최종 확정.

## 현재 구조 (Phase 0 직후)

```
studios/game/
├── CLAUDE.md                      # Perfect Navigator (96줄 목표)
├── README.md                      # 프로젝트 개요
├── WORK_HANDOFF.md                # 세션 핸드오프
├── SESSION_LOG.md                 # 세션 로그
├── .gitignore                     # 하네스 템플릿
├── .claude/
│   ├── hooks/                     # pre_tool_use / post_tool_use / session_start (Step 6b Navigator Coverage 포함)
│   ├── skills/                    # 5 공용 스킬 (하네스 상속)
│   ├── agents/                    # _patterns_reference (6 pattern 레퍼런스)
│   ├── memory/                    # MEMORY.md + project_game_stack.md
│   ├── failures/                  # FAILURES.md (append-only) + FAILURES_INDEX.md
│   ├── deprecated_patterns.json   # 5 regex (하네스 공용 원칙 승계)
│   └── settings.json              # Claude Code Hook 설정
├── .obsidian/                     # Obsidian vault anchor (빈 폴더, 자동 초기화)
├── .planning/                     # (Phase 1+ 에서 ROADMAP/REQUIREMENTS/PHASES 채움)
├── .preserved/                    # (향후 외부 자산 읽기 전용 저장소)
├── config/                        # (환경 설정)
├── docs/
│   └── ARCHITECTURE.md            # 이 파일
├── scripts/
│   └── validate/
│       └── navigator_coverage.py  # Navigator drift 자동 검증 (shorts 에서 이식)
└── wiki/                          # Tier 2 AI 위키 + Obsidian vault
    ├── README.md
    ├── design/MOC.md
    ├── engine/MOC.md
    ├── gameplay/MOC.md
    ├── art/MOC.md
    ├── audio/MOC.md
    └── steam/MOC.md
```

## 하네스 상속

- **Layer 1**: `../harness/` (naberal_harness v1.0)
- **원칙**: `../harness/CLAUDE.md` + `../harness/docs/ARCHITECTURE.md`
- **Whitelist 헌법**: `../harness/STRUCTURE.md` — Layer 1 자체 구조 규율 (Layer 2 는 독립)
- **공용 스킬**: 5종 자동 설치 (progressive-disclosure, drift-detection, gate-dispatcher, context-compressor, harness-audit)
- **업데이트**: `python ../harness/scripts/new_domain.py update game --only <skill>`

## AI 위키 + Obsidian 이중 용도 설계

`wiki/` 폴더 하나가 두 역할을 겸합니다:
1. **AI 에이전트 RAG 소스**: Phase 3+ 에서 에이전트가 `@wiki/game/<category>/MOC.md` 형식으로 참조
2. **대표님 Obsidian vault**: `.obsidian/` 폴더 자동 초기화 → 그래프뷰 + 백링크 + frontmatter 검색

AI 와 사람이 같은 폴더를 읽는 **단일 source of truth**. 동기화 문제 원천 차단.

## shorts 스튜디오와의 관계

| 공유 | 독립 |
|------|------|
| 하네스 Layer 1 (동일 버전 v1.0) | git 저장소 (`naberal_game` vs `shorts_studio`) |
| 나베랄 감마 Identity | 도메인 파이프라인 (게임 개발 vs 영상 제작) |
| AI 도구 체인 (Nano Banana/Suno/ElevenLabs/Claude Code) | 에이전트 팀 구성 |
| 하네스 공용 스킬 5종 | 도메인 특화 스킬·에이전트 (Phase 3+) |
| Perfect Navigator 패턴 (shorts 에서 2026-04-20 학습) | 금기·필수 세부 (장르별 차이) |

## 다음 액션 (Phase 1 진입)

1. Phase 1 ROADMAP 초안 작성 (`.planning/ROADMAP.md`)
2. 장르 3 후보 (로그라이크 / 시뮬 / RPG 하이브리드) 중 MVP 방향 확정
3. 시간 배분 결정 (주당 개발 시간)
4. Unity 6 LTS 설치 + Steamworks 파트너 등록 계획

---

*Created: 2026-04-20 — Phase 0 Bootstrap, 스튜디오 창업일.*
