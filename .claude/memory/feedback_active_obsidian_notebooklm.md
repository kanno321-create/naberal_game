---
name: Obsidian + NotebookLM 을 능동적으로 활용할 것
description: 하네스·AI 위키·Obsidian 삼위일체 효과는 나베랄 감마의 능동적 활용이 있어야만 실현됨
type: feedback
originSessionId: 0c22c80f-004b-4b15-afc0-7e72e41cb1c8
---
# Obsidian + NotebookLM 을 **능동적으로** 활용할 것

**규칙**: `wiki/` 의 `[[wiki-link]]` · MOC · frontmatter 를 읽기만 하지 말고 **실제 탐색·확장·검증 수단으로 사용**. 동시에 NotebookLM(`reference_notebooklm_game.md`) 의 노트북을 리서치 쿼리 소스로 적극 호출. 단순히 "이 문서에 있다" 고 가리키지 말고, 링크를 따라가서 맥락을 병합하고 drift 를 찾아내야 함.

**Why**: 대표님 2026-04-21 지시 — *"우리 옵시디언이랑 노트북lm활용을 너가 진짜 제대로 활용해야되 그래야 하네스+ai wiki +옵시디언의 효과를 볼수있다"*. 하네스(코드 강제) + AI 위키(지식 구조) + Obsidian(그래프·백링크) + NotebookLM(딥 리서치) 은 각자 존재만으로는 효과가 없고, 에이전트가 네 층위를 실제로 왕복할 때 비로소 시너지가 발생함. shorts 에서 검증된 조합을 game 에서도 똑같이 써야 "검증된 조합" 이 됨.

**How to apply**:
- 새 박제·수정 작업 시 **반드시 관련 MOC 부터 진입** — `wiki/{design,gameplay,engine,art,audio,steam}/MOC.md` 중 해당 도메인 MOC 를 읽고 `[[wiki-link]]` 를 따라가 문맥 병합 후 작업.
- 수정 후 **백링크 · frontmatter · MOC 인덱스 3개를 동시 갱신** (대표님이 Obsidian 으로 열었을 때 그래프뷰가 깨지지 않도록).
- 리서치가 필요한 상황에서 **웹 검색 전에 NotebookLM 노트북부터 확인** — 대표님이 이미 자료를 올렸을 가능성이 큼. 결과는 `.planning/research/nlm_result_*.md` 로 박제.
- drift 발견 시 (문서 간 모순, 링크 끊김, MOC 누락) **reactive 가 아니라 proactive 로** 보고 — `drift-detection` 스킬 즉시 호출.
- 문서 수가 늘어나면 `harness-audit` / `progressive-disclosure` 스킬로 정기 건강 검진.
