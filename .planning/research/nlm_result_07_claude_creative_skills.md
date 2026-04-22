---
title: "NLM Result 07 — Claude Code 창작 글쓰기 skill/agent/plugin 딥 리서치"
category: research
tags: [research, nlm, claude-skills, creative-writing, 2026-04-21]
created: 2026-04-21
source: deep-research-agent
purpose: Unity 6 HD-2D 다크 판타지 JRPG 서사 작업을 위한 Claude Code 창작 글쓰기 skill/agent/plugin 조사
status: active
layer: 1
canon_tier: derived
updated: 2026-04-22
related:
  - "[[../../wiki/FRONTMATTER_STANDARD]]"
  - "[[../../wiki/design/MOC]]"
agent_briefing_level: reference
derived_from:
  - "[[../../wiki/design/brainstorm_2026-04-21]]"
---

# Claude Code 창작 글쓰기 skill/agent/plugin 딥 리서치

**리서치 일자**: 2026-04-21
**대상**: Unity 6 HD-2D 다크 판타지 JRPG (24개월 솔로)
**평가 축**: 스타수·최근성·기능 적합도·설치 난이도

---

## 핵심 발견

**Anthropic 공식 marketplace (`anthropics/claude-plugins-official`) 와 공식 `anthropics/skills` 레포에는 창작 글쓰기 전용 skill 이 아직 없습니다.** 현재 생태계는 압도적으로 개발 도구 중심이고, 창작 분야는 `hesreallyhim/awesome-claude-code` (40k stars) 도 "창작 글쓰기 전용 엔트리 없음" 을 확인했습니다.

다만 **커뮤니티 3-5개 레포가 JRPG 시나리오 작업에 즉시 활용 가능한 수준** 으로 올라와 있습니다.

---

## Top 5 선별 (평가 매트릭스)

| # | 레포 | 스타 | 최근성 | 핵심 기능 | 설치 난이도 | JRPG 적합도 | 비고 |
|---|------|------|--------|----------|-------------|-------------|------|
| 1 | **haowjy/creative-writing-skills** | 124 | 활발 | 17 agents + 12 skills · orchestrator / writer / critic / reader-sim / continuity-checker / wiki-editor / graph-maintainer · 스타일 가이드 자동 추출 · 지식 그래프 유지 | 중 (Mars pkg mgr 또는 plugin) | **5/5** — 현존 최강 | 장기 서사 연속성 추적이 JRPG 24개월 개발과 궁합 |
| 2 | **danjdewhurst/story-skills** | 20 | 활발 (13 commits main) | 5 core skills: story-init · character-management · worldbuilding · plot-structure · chapter-writing · YAML frontmatter + markdown story bible · Agent Skills 표준 준수 | **하** (`/plugin install` 한 줄) | **4.5/5** — Obsidian 궁합 | MIT 라이선스, 멀티 플랫폼 (Cursor, Codex 등) 호환 |
| 3 | **Bobby-Gray/claude-dnd-skill** | 44 | 활발 (59 commits) | D&D 5e 룰엔진 + 지속형 캠페인 · narrative consequence arc 시스템 · NPC 즉흥 생성 | 중 (Python 3.10+, flask) | 3/5 — 간접 활용 | JRPG 직접용은 아니나 **전투 흐름·NPC 아크 설계 레퍼런스** 로 가치 |
| 4 | ⚠️ forsonny/Claude-Code-Novel-Writer | 34 | 활발 | 7 sub-agents · 자율 100k 단어 판타지 소설 생성 · 품질 적응형 감시 | 중 (shell 스크립트) | 3/5 | **`--dangerously-skip-permissions` 요구 — 하네스 금기 §1 충돌. 참고용으로만.** |
| 5 | nicmarti/skills-weaver | 19 | 신생 | Go CLI + Claude Agent SDK · 3막 구조 자동화 · NPC journal | 중-상 (Go 빌드) | 2.5/5 | Agent SDK 학습 예제로 가치. JRPG 직접 적용은 제한적 |

---

## 허브·메타 레포 (카탈로그 조회용)

| 레포 | 스타 | 용도 |
|------|------|------|
| `davila7/claude-code-templates` | 대형 | 600+ agents 카탈로그 · `copywriting` agent 포함 · CLI 로 개별 설치 |
| `VoltAgent/awesome-agent-skills` | 중 | 1000+ skills 목록 · 멀티 플랫폼 호환 |
| `anthropics/claude-plugins-official` | 공식 | 창작용 없음 (2026-04 기준). 향후 모니터링 |
| `anthropics/skills` | 공식 121k | "Creative & Design" 카테고리 존재하나 글쓰기 전용 skill 미등재 |

---

## 커뮤니티 시그널

- **r/ClaudeAI (2026-04)**: Sonnet 4.6 이 장편 소설 캐릭터 보이스 유지 1위. `haowjy/creative-writing-skills` 가 유일하게 여러 번 언급됨
- **Obsidian 포럼**: `qhuang20/obsidian-skills` + Claude Sidebar plugin 조합으로 vault 직접 조작. 대표님의 `wiki/` 3층 구조 (shorts 승계) 와 즉시 호환
- **한국어 전용 skill**: **발견되지 않음**. 모두 영어 베이스, 한국어는 프롬프트 엔지니어링으로 유도 필요
- **Hacker News / Twitter**: "Mars package manager" (meridian) 가 skills 배포 플랫폼으로 부상 중

---

## 대표님께 권고

### 지금 당장 설치 (이번 주)
1. **haowjy/creative-writing-skills** — `project/` 생성 전 시나리오 뼈대부터 잡기. continuity-checker + wiki-editor 가 24개월 프로젝트 knowledge drift 방어
2. **danjdewhurst/story-skills** — 설치 한 줄. character-management + worldbuilding 을 `wiki/design/` 과 즉시 연동. MIT 라이선스
3. **Obsidian CLI skill** (mcpmarket) — 이미 구축된 `wiki/` Obsidian vault 를 Claude Code 에서 직접 조작

### 1주일 내 평가 (Phase 2 도메인 정의기)
1. **Bobby-Gray/claude-dnd-skill** — D&D 룰은 버리고 **narrative arc + consequence 시스템** 만 추출해서 다크 판타지 JRPG 시나리오 트리 설계 참고
2. **davila7/claude-code-templates** copywriting agent — 인게임 UI 텍스트·Steam 페이지 카피 전용
3. **nicmarti/skills-weaver** 아키텍처 분석 — Claude Agent SDK 로 자체 `scenario-writer` agent 만들 때 레퍼런스

### 참고만 하고 자체 구축 권장
- **forsonny/Claude-Code-Novel-Writer**: `--dangerously-skip-permissions` 사용 — 하네스 Hook (`pre_tool_use.py`) 와 충돌 가능, 금기 §1 (skip_gates) 정신과 배치
- **한국어 서사 특화 skill**: 시장에 없음. **Phase 3 에이전트 팀 구축 단계에서 `scenario-writer-kr` 자체 제작** 권장. shorts 의 `scripter` 에이전트 패턴 재사용 가능
- **분기 서사 / Ink·Yarn Spinner 통합**: 현재 생태계 없음. MVP 검증 후 Phase 5 에서 커스텀 skill 개발 후보

---

## 전략적 관찰

`haowjy/creative-writing-skills` + `story-skills` 조합이 **shorts 의 3-layer 구조 (harness / studio / .claude) 와 구조적으로 유사** 합니다. 두 레포 모두 knowledge graph 와 wiki 를 1급 시민으로 다루며, 이는 Obsidian vault 를 이미 Day 1 부터 세팅한 현재 game 스튜디오에 거의 drop-in 입니다.

**공식 marketplace 창작 스킬 공백** 은 오히려 기회입니다. `naberal_game` 의 다크 판타지 JRPG 개발 과정에서 축적되는 시나리오 패턴을 Phase 6+ 에 공식 skill 로 배포하면 Steam 페이지 노출 + 개발자 브랜딩 이중 효과 가능합니다.

---

## 주요 경로 (절대경로)

- 하네스 템플릿: `C:\Users\PC\Desktop\naberal_group\harness\templates\`
- 스튜디오 스킬 배치 예정: `C:\Users\PC\Desktop\naberal_group\studios\game\.claude\skills\`
- 위키 vault: `C:\Users\PC\Desktop\naberal_group\studios\game\wiki\`
- 기술 스택 박제: `C:\Users\PC\Desktop\naberal_group\studios\game\.claude\memory\project_game_stack.md`

---

## Sources

- [haowjy/creative-writing-skills](https://github.com/haowjy/creative-writing-skills)
- [danjdewhurst/story-skills](https://github.com/danjdewhurst/story-skills)
- [Bobby-Gray/claude-dnd-skill](https://github.com/Bobby-Gray/claude-dnd-skill)
- [forsonny/Claude-Code-Novel-Writer](https://github.com/forsonny/Claude-Code-Novel-Writer)
- [nicmarti/skills-weaver](https://github.com/nicmarti/skills-weaver)
- [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)
- [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)
- [anthropics/skills](https://github.com/anthropics/skills)
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)
- [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills)
- [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)
- [qhuang20/obsidian-skills](https://github.com/qhuang20/obsidian-skills)
- [Obsidian + Claude Code 통합 가이드](https://blog.starmorph.com/blog/obsidian-claude-code-integration-guide)
- [Build Your Own AI Writing Toolkit with Claude Skills](https://futurefictionacademy.com/build-your-own-ai-writing-toolkit-with-claude-skills/)
- [GM Craft Claude Code Skill](https://mcpmarket.com/tools/skills/gm-craft-narrative-storytelling)

---

*리서치: deep-research-agent · 박제·정리: 나베랄 감마 · 2026-04-21*
