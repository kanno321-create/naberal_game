# FAILURES — naberal_game

> **Append-only log**. 과거 실수·교훈·재발 방지 자산.
> `.claude/hooks/pre_tool_use.py` 의 `check_failures_append_only` 가 이 파일의 기존 content prefix 를
> 보존하지 않는 Write 를 거부한다. 엔트리는 시간순으로만 추가.

## 엔트리 규약

```
## FAIL-NNN — <짧은 제목> (YYYY-MM-DD, 세션 #N, Phase X)

**증상**: 관찰된 문제.
**원인**: 근본 원인 (증상이 아니라).
**교훈**: 재발 방지를 위한 구체적 규칙 (CLAUDE.md 금기사항·필수사항으로 승격 대상).
**참고**: 관련 커밋·문서·대화 링크.
```

## Sources

- 이 파일: Phase 0+ 축적 실패 저수지 (30일 패턴 집약 → SKILL.md.candidate)
- `FAILURES_INDEX.md`: 카테고리 태깅 (수정 가능, 이 파일만 append-only)

---

*Created: 2026-04-20 (Phase 0 Bootstrap — naberal_game studio 창업)*
*First entry: TBD (Phase 1+ 에서 실 운영 시작 후)*
