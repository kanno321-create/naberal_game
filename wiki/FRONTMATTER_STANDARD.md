---
title: "Frontmatter Standard — naberal_game 3축 통합 인프라"
layer: 1
canon_tier: derived
tags: [standard, infrastructure, obsidian, canon, ai-wiki]
parent: "[[README]]"
related:
  - "[[../CLAUDE]]"
  - "[[../docs/ARCHITECTURE]]"
created: 2026-04-22
updated: 2026-04-22
status: active
version: "v1.0"
---

# Frontmatter Standard — 하네스 + AI 위키 + 옵시디언 3축 공통 언어

> **naberal_group Layer 2 스튜디오의 단일 표준.** 모든 `.md` 파일이 이 frontmatter 스펙을 따른다.
> 하네스 (Layer 1) · AI 위키 (에이전트 RAG) · 옵시디언 (대표님 탐색) **3축이 이 frontmatter 를 공통 언어로 공유**한다.

---

## 1. 철학 — 왜 이 표준이 필요한가

### 3축이 작동하려면 공통 언어가 필요

- **하네스 Hook** (`session_start.py`) 이 frontmatter 읽어서 Canon 주입
- **AI 에이전트** 가 frontmatter 읽어서 원전 검증 (drift 방지)
- **Obsidian** 이 frontmatter 읽어서 그래프·계층·쿼리 생성

같은 필드를 3 주체가 동시에 해석 → **한 번 박제 = 3축 모두 작동**.

### 해결하는 문제

| 문제 | 해결 필드 |
|---|---|
| 원전 검증 없이 집필 → drift 재발 (FAIL-002/006/009/014) | `layer` · `canon_anchors` · `derived_from` |
| 파일 900+ 고립 → 탐색 불가 | `parent` · `up` · `related` · `moc` |
| 에이전트가 원전 참조 안 함 | `agent_briefing_level` · `canon_anchors` |
| MOC 수동 관리 어려움 | `layer` + dataview 쿼리 자동화 |

---

## 2. 필수 필드 (모든 파일)

```yaml
---
title: "파일 제목 (한 줄)"
layer: 0 | 1 | 2            # Canon Hierarchy (아래 §3 참조)
tags: [novel, chapter]      # Obsidian 태그 검색
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: draft | active | archived | obsolete
---
```

## 3. Layer 체계 (Canon Hierarchy)

### Layer 0 · 원전 (Core · 변경 불가)

- **의미**: 대표님 원문 발언 · 확정 세계관 · Q-CORE · 최상위 진리
- **변경 정책**: 대표님 직접 승인 없이 수정 금지
- **예시 파일**:
  - `design/story_full_narrative.md` (Rev.3)
  - `design/brainstorm_2026-04-21.md`
  - `design/brainstorm_2026-04-21_worldview_expansion.md`
  - `design/game_setting_complete_2026-04-21.md`
  - Q-CORE 해결 메모리 (`.claude/memory/project_qcore*.md`)

```yaml
layer: 0
canon_tier: core
```

### Layer 1 · 파생 (Derived · Layer 0 검증 필수)

- **의미**: 원전을 구조화·스타일화한 운영 문서
- **변경 정책**: Layer 0 과 모순 발생 시 Layer 1 양보
- **예시 파일**:
  - `design/MOC.md` · 카테고리별 MOC 6종
  - `design/novel/outline.md` · `style_bible.md`
  - `design/main_character.md` · `world_lore.md` · `story_outline.md` · `political_divisions.md`
  - `gameplay/combat_system.md` · `build_system.md` · `endgame.md` · `mvp_phase4_scope.md`
  - `design/brainstorm_2026-04-22_game_second_round.md`

```yaml
layer: 1
canon_tier: derived
derived_from:
  - "[[story_full_narrative]]"
  - "[[brainstorm_2026-04-21]]"
```

### Layer 2 · 세부 (Detail · Layer 0+1 검증 필수)

- **의미**: 실제 집필본 · 원자 파일 · 챕터 · 왕국·도시·마을 박제
- **변경 정책**: Layer 0+1 원전 인용 박제 필수 (Canon Anchor)
- **예시 파일**:
  - `design/novel/ch01.md` · `ch02.md` · `prologue.md`
  - `design/worldbuilding/elucia/kingdoms/*/*.md` (900+ 파일)
  - `design/worldbuilding/karzor/subregions/*.md`

```yaml
layer: 2
canon_tier: detail
parent: "[[kingdom_ilaris]]"
up: "[[MOC]]"
derived_from:
  - "[[story_full_narrative]]"
canon_anchors:
  - src: "[[story_full_narrative]]:89"
    quote: "나이트. 수천 년 균형 수호자"
```

---

## 4. 관계 필드 (Obsidian 그래프 + 계층)

### parent · up (breadcrumbs · 계층)

- `parent`: 상위 문서 (1개)
- `up`: breadcrumbs 위로 이동 (1~N개 가능)

```yaml
parent: "[[kingdom_ilaris_00_overview]]"
up: "[[elucia_kingdoms_MOC]]"
```

### derived_from (Canon 파생 추적)

Layer 1·2 가 어떤 Layer 0·1 에서 파생됐는지 명시.

```yaml
derived_from:
  - "[[story_full_narrative]]"
  - "[[brainstorm_2026-04-21]]"
```

### related (수평 그래프)

주제·서사 관련된 다른 문서들 (3~7개 권장).

```yaml
related:
  - "[[village_ashenveil]]"
  - "[[ch01]]"
  - "[[hamil_chief]]"
```

### moc (MOC 소속)

어떤 카테고리 MOC 에 속하는지. dataview 자동 수집 기준.

```yaml
moc: "[[novel_MOC]]"
```

---

## 5. Canon Anchor (drift 방지 · AI 위키 RAG)

### canon_anchors

원전 직접 인용 (3~5건). 본문이 이 인용과 모순되면 즉시 폐기.

```yaml
canon_anchors:
  - src: "[[story_full_narrative]]:89"
    quote: "이름은 나이트(Knight). 수천 년을 수행한 균형 수호자."
  - src: "[[story_full_narrative]]:169"
    quote: "수천 년을 산 수호자가 16세 소년들 사이에 서서 목걸이를 받는다"
  - src: "[[story_full_narrative.txt]]:79"
    quote: "빛이 나이트를 휩싼다. 그의 권능이 봉인된다. 그의 기억이 박탈된다."
```

### agent_briefing_level (에이전트 RAG 우선순위)

- `required`: 에이전트 작업 전 반드시 Read
- `optional`: 참조 권장
- `reference`: 필요 시만

```yaml
agent_briefing_level: required
```

---

## 6. 완전 예시

### Layer 0 원전

```yaml
---
title: "Story Full Narrative — naberal_game"
layer: 0
canon_tier: core
tags: [canon, story, narrative]
status: active
version: "Rev.3"
agent_briefing_level: required
created: 2026-04-21
updated: 2026-04-22
---
```

### Layer 1 파생

```yaml
---
title: "Novel Outline — 25~30 챕터 지도"
layer: 1
canon_tier: derived
tags: [novel, outline, structure]
parent: "[[design_MOC]]"
moc: "[[design_MOC]]"
derived_from:
  - "[[story_full_narrative]]"
  - "[[brainstorm_2026-04-21]]"
related:
  - "[[style_bible]]"
  - "[[main_character]]"
status: active
agent_briefing_level: required
created: 2026-04-21
updated: 2026-04-22
---
```

### Layer 2 세부

```yaml
---
title: "Ch.01 — 안개, 그리고 서쪽에서 온 것"
layer: 2
canon_tier: detail
chapter: 01
tags: [novel, chapter, ch01, ashenveil]
parent: "[[outline]]"
up: "[[outline]]"
moc: "[[novel_MOC]]"
derived_from:
  - "[[story_full_narrative]]"
  - "[[outline]]"
  - "[[style_bible]]"
canon_anchors:
  - src: "[[story_full_narrative]]:89"
    quote: "나이트. 수천 년을 수행한 균형 수호자"
  - src: "[[story_full_narrative.txt]]:79"
    quote: "권능이 봉인된다. 기억이 박탈된다. 단검 한 자루만 남는다"
related:
  - "[[village_ashenveil]]"
  - "[[prologue]]"
  - "[[ch02]]"
status: "draft_v1 폐기 · v2 재집필 대기"
agent_briefing_level: required
pov: "1인칭 (주인공)"
created: 2026-04-22
updated: 2026-04-22
---
```

---

## 7. 링크 형식 — Wikilinks 전용

Obsidian app.json `useMarkdownLinks: false` · `newLinkFormat: "shortest"` 설정.

- ✅ `[[파일명]]`
- ✅ `[[파일명|표시 텍스트]]`
- ❌ `[표시 텍스트](상대경로/파일명.md)` — 금지 (기존 54건 전환 대상)

---

## 8. 3축 활용 시나리오

### 대표님 (옵시디언)
- `Ashenveil` 검색 → 백링크 20+ 노드 등장
- 그래프 뷰에서 Layer 색상 구분 (🔴 원전 · 🟠 파생 · 🔵 세부)
- breadcrumbs: `kingdom_ilaris → villages → village_ashenveil`
- dataview: 특정 `layer: 2` · `tags: [novel]` 파일 전수 자동 리스트

### AI 에이전트 (AI 위키 RAG)
- 작업 시작 전 `agent_briefing_level: required` 파일 전수 Read
- Layer 2 집필 시 `canon_anchors` 검증 GATE 통과 필수
- `derived_from` 체인 따라 Layer 0 까지 거슬러 원전 확인

### 하네스 (session_start.py)
- 매 세션 시작 시 Layer 0 파일 목록 주입
- Canon Anchor 검증 경고 주입
- drift-detection skill 자동 실행 → Layer 2 vs Layer 0 일치 스캔

---

## 9. 위반 탐지 — drift-detection skill 연동

Layer 2 파일 생성 시 자동 검사:
1. frontmatter `layer` 필드 존재?
2. Layer 2 면 `canon_anchors` 최소 2건?
3. `derived_from` 에 유효한 Layer 0/1 파일 명시?
4. 본문 키워드 vs Layer 0 원전 일치율 ≥ 80%?

위반 시 alert → FAILURES.md 기록.

---

## 10. 운영 규율

### 새 파일 생성 시

1. Frontmatter 표준 템플릿에서 시작
2. `layer` · `canon_anchors` (Layer 2 만) 필수
3. `parent` · `moc` 지정
4. 본문 작성 전 `canon_anchors` 먼저 박제

### 기존 파일 수정 시

- Layer 0 파일: 대표님 직접 승인 필수
- Layer 1 파일: Layer 0 과 모순 없는지 검증
- Layer 2 파일: `canon_anchors` 와 본문 일치 재확인

### 커밋 메시지 규율

- `feat(canon-L0): ...` — Layer 0 신규/수정
- `feat(canon-L1): ...` — Layer 1 신규/수정
- `feat(canon-L2): ...` — Layer 2 신규/수정
- `fix(drift): ...` — drift 수정

---

## Related

- [[../CLAUDE]] — 하네스 최상위 원칙
- [[../docs/ARCHITECTURE]] — Phase 로드맵
- [[README]] — wiki 루트
- [[../.claude/failures/FAILURES]] — drift 이력

---

*표준 박제: 2026-04-22 · 세션 #6 · workspace 브랜치 · v1.0*
*3축 (하네스 + AI 위키 + 옵시디언) 통합 인프라 원년.*
