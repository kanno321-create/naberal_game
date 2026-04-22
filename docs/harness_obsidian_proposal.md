# 하네스 개선 권고 — Obsidian + Canon Hierarchy 템플릿 이관

**작성**: 2026-04-22 · 세션 #6 · workspace 브랜치
**대상 저장소**: `naberal_group/harness/` (Layer 1 naberal_harness · 독립 git)
**발신 스튜디오**: `naberal_group/naberal_game-main/` (Layer 2)
**우선순위**: HIGH (FAIL-014 재발 방지 · shorts 스튜디오 자동 이식)

---

## 1. 배경 — 하네스 결함 발견

naberal_game 세션 #6 (2026-04-22) 에서 **FAIL-014 원전 무시 집필 오염 drift** 발생. 근본 원인 중 하나가 **하네스 `templates/` 에 Obsidian vault 설정 전무**.

### 현재 하네스 `templates/` 구조 (점검 결과)

```
harness/templates/
├── AGENT.md.template
├── CLAUDE.md.template
├── FAILURES.md.template
├── SKILL.md.template
└── studio.gitignore.template
```

### 결함 항목

| # | 결함 | 영향 |
|---|------|------|
| 1 | `.obsidian/` 템플릿 없음 | 신규 스튜디오마다 vault 미설정 → 탐색 불가 |
| 2 | `FRONTMATTER_STANDARD.md.template` 없음 | Canon Hierarchy · 3축 공통 언어 부재 |
| 3 | `scripts/new_domain.py` 내 "obsidian" 언급 0건 | 스캐폴드 단계에 Obsidian 이식 없음 |
| 4 | `CLAUDE.md.template` 에 3축 통합 원칙 미반영 | "shorts 에서 검증된 조합 Day 1 이식" 선언만 존재, 구현 공백 |

### shorts 스튜디오 교차 확인

`c:/Users/PC/바탕 화면/shorts_naberal/` 경로 확인 결과 **shorts 에도 `.obsidian/` vault 설정 없음**. 즉 "shorts 에서 검증된 3축 조합 Day 1 이식" 이라는 하네스 선언은 실제로는 구현된 적이 없었음. naberal_game 세션 #6 이 이 조합의 **실질적 원년**.

---

## 2. 제안 — 하네스 v1.0 → v1.1 업그레이드

### 제안 1 · `templates/obsidian.vault.template/` 신설

naberal_game 에서 검증된 `wiki/.obsidian/` 구조를 하네스 템플릿으로 이관:

```
harness/templates/obsidian.vault.template/
├── app.json                 # useMarkdownLinks: false · shortest path · detect extensions
├── appearance.json          # 다크 테마 기본
├── core-plugins.json        # 코어 플러그인 기본 활성
├── community-plugins.json   # [breadcrumbs, dataview, juggl]
├── graph.json               # Layer 0=빨강 · 1=주황 · 2=파랑 색상 코딩
├── hotkeys.json             # {} (빈 객체)
├── types.json               # frontmatter 필드 타입 선언 (layer:number · canon_anchors:multitext 등)
└── plugins/
    ├── breadcrumbs/         # 계층 네비게이션
    ├── dataview/            # 자동 대시보드
    └── juggl/               # 인터랙티브 그래프
```

**출처**: `naberal_group/naberal_game-main/wiki/.obsidian/` (2026-04-22 세션 #6 검증 완료).

### 제안 2 · `templates/FRONTMATTER_STANDARD.md.template` 신설

3축 공통 언어 표준. 모든 스튜디오가 이 표준 준수.

**출처**: `naberal_group/naberal_game-main/wiki/FRONTMATTER_STANDARD.md` v1.0 (세션 #6 작성).

핵심 섹션:
- §3 Layer Hierarchy (0 원전 · 1 파생 · 2 세부)
- §4 관계 필드 (parent · up · derived_from · related · moc)
- §5 Canon Anchor (drift 방지)
- §7 Wikilinks 전용 규율
- §8 3축 활용 시나리오
- §9 위반 탐지 (drift-detection skill 연동)

### 제안 3 · `scripts/new_domain.py` 에 Obsidian 스캐폴드 단계 추가

현재 `new_domain.py` 는 `.claude/` · `wiki/` · `CLAUDE.md` 등을 생성하지만 **Obsidian vault 는 생성하지 않음**. 다음 단계 추가:

```python
def scaffold_obsidian_vault(studio_root: Path, domain: str) -> None:
    """신규 스튜디오 wiki/.obsidian/ 생성 · 템플릿 복사."""
    src = HARNESS_ROOT / "templates" / "obsidian.vault.template"
    dst = studio_root / "wiki" / ".obsidian"
    if not src.exists():
        raise FileNotFoundError(f"Obsidian template missing: {src}")
    shutil.copytree(src, dst)
    # 도메인별 graph.json 튜닝 (tag 컬러 자동 삽입)
    _inject_domain_tag_colors(dst / "graph.json", domain)

def scaffold_frontmatter_standard(studio_root: Path) -> None:
    """wiki/FRONTMATTER_STANDARD.md 생성."""
    src = HARNESS_ROOT / "templates" / "FRONTMATTER_STANDARD.md.template"
    dst = studio_root / "wiki" / "FRONTMATTER_STANDARD.md"
    shutil.copy(src, dst)
```

`new_domain.py main()` 호출 순서에 추가:

```
1. .claude/ 스캐폴드
2. wiki/ 6 카테고리 MOC 생성
3. Obsidian vault 스캐폴드  ← 신규
4. FRONTMATTER_STANDARD.md 배치  ← 신규
5. CLAUDE.md.template 생성
```

### 제안 4 · `harness/CLAUDE.md` 3축 통합 원칙 추가

현재 harness CLAUDE.md 는 하네스 자체 원칙만 기술. **3축 통합 인프라 섹션**을 최상위에 추가:

```markdown
## 🏛 3축 통합 인프라 (Core · v1.1)
모든 Layer 2 스튜디오는 **하네스 + AI 위키 + 옵시디언** 3축 통합을 기본 작동 원리로 한다.
공통 언어 = frontmatter 표준 (`wiki/FRONTMATTER_STANDARD.md`).
- 하네스: session_start Hook 이 Canon 주입 · drift-detection skill 자동 스캔
- AI 위키: 에이전트가 canon_anchors · agent_briefing_level 필드 읽어 원전 검증
- 옵시디언: 대표님 탐색 · Layer 색상 그래프 · breadcrumbs 계층 · dataview 대시보드
```

### 제안 5 · `harness/hooks/session_start.py.template` 에 Canon 주입 함수 이관

naberal_game 세션 #6 에 추가한 `inject_canon_layer0()` 함수를 하네스 템플릿으로 이관. 모든 스튜디오에서 매 세션 시작 시 자동 작동.

**출처**: `naberal_game-main/.claude/hooks/session_start.py` (세션 #6 Step 6c 추가분).

---

## 3. 역이식 계획 — shorts 스튜디오

하네스 v1.1 업그레이드 후 다음 작업:

1. `shorts_naberal/` 에 `python ../harness/scripts/new_domain.py update shorts --only obsidian` 실행
2. shorts `wiki/.obsidian/` 자동 생성
3. shorts 기존 wiki 파일에 `layer` 필드 일괄 태깅 (shorts 전용 에이전트 분할)
4. shorts 에서도 Canon Anchor GATE 작동 확인

---

## 4. 실행 순서 권고

### 단기 (1~2주 내 · 하네스 저장소 PR 예정)

1. `harness/templates/obsidian.vault.template/` 신규 커밋 (naberal_game 에서 cp 이관)
2. `harness/templates/FRONTMATTER_STANDARD.md.template` 신규 커밋
3. `harness/scripts/new_domain.py` 에 scaffold 단계 추가
4. `harness/CLAUDE.md` 3축 섹션 추가

### 중기 (1개월 내)

5. shorts 스튜디오 역이식 (`update shorts --only obsidian + frontmatter`)
6. shorts wiki 파일 Layer 태깅 (에이전트 병렬)
7. 두 스튜디오 (naberal_game + shorts) 3축 통합 작동 검증

### 장기 (Phase 1+ 연속)

8. `drift-detection` skill 에 Canon 일치율 자동 스캔 추가
9. `canon_coverage.py` 스크립트 신규 작성 (Layer 2 → Layer 0 원전 검증)
10. 신규 3번째 Layer 2 스튜디오 생성 시 3축 인프라 자동 완성 검증

---

## 5. 기대 효과

| 개선 항목 | Before (v1.0) | After (v1.1) |
|---|---|---|
| 신규 스튜디오 Obsidian vault | 수동 설정 필요 (실제로는 건너뜀) | `new_domain.py` 자동 스캐폴드 |
| 3축 통합 구현 | 선언만 존재 (FAIL-014 원인) | 코드 강제 (Hook + frontmatter) |
| Canon Hierarchy | 없음 | Layer 0/1/2 · canon_anchors 박제 의무 |
| 문서 탐색성 | wiki-link 커버리지 2~3% | Obsidian 그래프 자동 · 레이어별 색상 |
| drift 감지 | 대표님 직접 읽기 | 자동 스캔 (drift-detection skill) |

---

## 6. 관련 문서

- **본 권고 출발점**: `.claude/failures/FAILURES.md` FAIL-014
- **naberal_game 구현 참조**: `wiki/.obsidian/` · `wiki/FRONTMATTER_STANDARD.md` · `CLAUDE.md` 3축 섹션
- **하네스 현행**: `../../harness/CLAUDE.md` · `templates/` · `scripts/new_domain.py`

---

*권고안 v1.0 · 2026-04-22 · 세션 #6 · naberal_game workspace 브랜치*
*하네스 저장소 PR 시 본 문서 인용 · 3축 인프라 원년 기록.*
