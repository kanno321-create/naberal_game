---
name: project_game_stack
description: Unity 6 LTS + Steam PC + C# 주력 스택 확정 (대표님 결정 2026-04-20) — 로그라이크/시뮬/RPG 방향 장기 솔로 인디 프로젝트
type: project
---

# Game Stack — Unity 6 + Steam + C#

## 대표님 결정 (2026-04-20 스튜디오 창업)

1. **장르 방향**: 복합 게임플레이 (로그라이크/시뮬/RPG) — 장기 창작 (12~24개월 예상)
2. **플랫폼**: Steam PC 출시 목표
3. **엔진**: Unity 6 LTS (C#)
4. **시간 배분**: 미정 — Phase 2 Domain Definition 에서 확정

## 스택 구성

| 영역 | 1순위 | 근거 |
|------|------|------|
| 엔진 | Unity 6 LTS | 상업 게임 1위, Asset Store, Steamworks SDK 네이티브 |
| 언어 | C# 12 (.NET 9) | Unity 네이티브, LINQ + 비동기 강력 |
| IDE | JetBrains Rider 2026 | C# 리팩토링 + Unity 통합 |
| 버전관리 | Git + Git LFS | 바이너리 에셋 분리 |
| AI 코드 | Claude Code + Cursor | C# 생성·리팩토링 |
| AI 아트 | Nano Banana Pro (UI/한국어 텍스트) + Meshy 4 (3D) | shorts 에서 검증된 한국어 텍스트 정확도 |
| AI 오디오 | Suno v4 (음악) + ElevenLabs v3 (보이스) | 한국어 네이티브 |
| 출시 | Steamworks SDK (C# wrapper: Steamworks.NET) | Achievements/Cloud Save/Leaderboard |

## AI 시대 솔로 인디 성공 공식 (2026-04 기준)

- **MVP 우선**: 핵심 루프 30초·3분·30분 3-tier 검증 후 확장
- **Steam 페이지 early open**: 출시 6개월 전 페이지 마련 → 위시리스트 축적
- **AI 도구 활용**: 1인 커버 범위 = 과거 10명 팀 수준
- **번아웃 방지**: 주간 시간 블록 고정 + 장기 프로젝트 페이스
- **참고 사례**: Balatro (LocalThunk 1인, 2024 Steam Top 10), Animal Well (Billy Basso 1인, 2024 GOTY 후보), Vampire Survivors (poncle 1인)

## 다음 결정 지점

- **Phase 2 Domain Definition**: 구체 장르 확정 (로그라이크 우선? 시뮬 우선? 하이브리드?)
- **Phase 2**: Unity 프로젝트 루트 생성 (`project/`) + Unity .gitignore 적용
- **Phase 3**: 에이전트 팀 설계 (game designer / unity coder / steam marketer / art director 등 후보)
- **Phase 4**: 첫 MVP 프로토타입

## Source

- 대표님 지시 2026-04-20 세션 (shorts 스튜디오 Navigator 재설계 완결 후 신규 스튜디오 창업)
- shorts 스튜디오 `docs/ARCHITECTURE.md` §4 (AI 도구 체인 검증 데이터 공유)
