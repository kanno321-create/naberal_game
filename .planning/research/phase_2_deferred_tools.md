---
category: research
tags: [deferred, phase-2, unity, tools, 2026-04-21]
created: 2026-04-21
purpose: Phase 2 Unity 프로젝트 생성 시점에 설치할 도구 목록
status: deferred
---

# Phase 2 대기 도구 (2026-04-21 기준)

**현재 Phase**: 0 완료 (2026-04-20 창업일)
**설치 예정 시점**: Phase 2 Domain Definition 진입 시 (Unity 프로젝트 생성)

---

## 1. Claude Code + unity-mcp ⭐ Must-have 1

- **URL**: https://github.com/CoplayDev/unity-mcp
- **역할**: Claude 가 Unity 에디터를 직접 제어 (MCP 서버 방식)
- **효과**: 코딩 시간 30-50% 단축 (검증된 수치)
- **전제 조건**: Unity 6 LTS 프로젝트 생성 완료
- **설치 방식**: Unity Package Manager + `.mcp.json` 설정
- **설치 시점**: Phase 2 Unity 프로젝트 초기화 직후

---

## 2. Yarn Spinner 3.1 ⭐ Must-have 2

- **URL**: https://yarnspinner.dev/ · https://github.com/YarnSpinnerTool/YarnSpinner-Unity
- **출시**: 2025-12 (최신 안정 버전)
- **역할**: 5엔딩·다회차 서사 관리 (대표님 2분기 × 2회차 + 진엔딩 구조 필수)
- **라이선스**: MIT (유료 Plus 판 별도)
- **전제 조건**: Unity 프로젝트
- **설치 방식**: Unity Package Manager → Yarn Spinner 3.1 임포트
- **설치 시점**: Phase 4 MVP 서사·대화 구현 시작 시

---

## 3. nicmarti/skills-weaver

- **URL**: https://github.com/nicmarti/skills-weaver
- **역할**: Go CLI + Claude Agent SDK · 3막 구조 자동화 · NPC journal
- **라이선스**: CC BY-SA 4.0 (저작자 표시 필수)
- **전제 조건**: **Go 1.25 설치 필요** (현재 기기에 Go 없음)
- **보류 이유**: 오늘 Go 미설치 상태라 빌드 불가
- **설치 방식**: `go install` 또는 `make build`
- **설치 시점**: 대표님이 Go 설치 결정 후 (필요성 판단 필요)
- **우선순위**: 낮음 — 다른 4개 창작 skill (이미 설치 완료) 로 대부분 기능 커버 가능

---

## 오늘 설치 완료된 도구

참고용. Phase 0 시점 (2026-04-21) 에 이미 활성화:

| 도구 | 출처 | 카테고리 |
|---|---|---|
| skills 22개 (story-skills 5 + creative-writing 12 + cw-router + dnd) | 3개 GitHub 레포 | Claude Code 전역 |
| agents 17개 (creative-writing 에이전트) | haowjy/creative-writing | Claude Code 전역 |

**설치 위치**: `~/.claude/skills/` · `~/.claude/agents/`
**활용 범위**: naberal_group 전체 스튜디오 (game + shorts) 공유

---

## Phase 4 MVP 도입 예정 Unity 패키지

리서치 결과 (nlm_result_08) 의 Phase 4 추천:
1. Unity3D-Turn_Based_RPG (i-Jiro) — 턴제 골격
2. Yarn Spinner 3.1 — 위의 Must-have 2
3. Safekeeper Save System — 멀티 슬롯 세이브

## Phase 5 Vertical Slice 도입 예정
1. 2D outlines URP + Sprite Lit Shader Graph — HD-2D 비주얼
2. FarrokhGames/Inventory — D2 그리드 인벤토리
3. ashblue/unity-skill-tree-editor — 스킬트리 에디터

## Phase 7 Alpha/Beta 도입 예정
1. Steamworks.NET — 업적·클라우드 세이브
2. BIC 2027 루키부문 출품 검토

---

*박제: 2026-04-21 · 나베랄 감마*
