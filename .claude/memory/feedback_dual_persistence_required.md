---
name: 이중 박제 원칙 · git + Claude Code 메모리 동시 저장 강제
description: 중요 Canon·결정은 반드시 git 프로젝트 로컬(.claude/memory/) + Claude Code 전역 auto-memory 양쪽에 동시 저장. 어느 한쪽만 하면 영속성 실패로 대표님이 매 세션 반복 설명 피로.
type: feedback
priority: critical
---
**규칙**: 프로젝트에서 **중요도 있는 모든 메모리**(특히 `priority: critical`, Canon 락업, 대표님 반복 지적)는 **양쪽 경로에 동시 박제**.

- 📁 git 프로젝트 로컬: `.claude/memory/<name>.md` → git commit 으로 **영속 보존**
- 🧠 Claude Code 전역: `C:\Users\PC\.claude\projects\<encoded-cwd>\memory\<name>.md` → Claude Code 자동 주입 (시스템 리마인더 채널)

**Why (대표님 2026-04-23 세션 #8 진입 시)**:
- 세션 #7 에서 박제한 "priority: critical 메모리 2건 자동 주입 앵커 #3" 이 **실제로는 전역에만 저장되어 git 박제 안 됨** → session_start.py §6.5 로컬 스캔과 경로 불일치로 무력화 (FAIL-017)
- 대표님 원문: *"깃에도 박재하고, 메모리에도 박제해라 매번까먹어서 너가, 나 힘듦"*
- 한쪽만 저장하면:
  - 전역만 → git 미반영 · 다른 PC·저장소 복구 불가 · 삭제 위험
  - 로컬만 → Claude Code 자동 주입 대상 밖 · 세션 시작 시 Claude 가 스스로 로딩 안 함
- 대표님은 이미 이 건으로 **세션 #7 에 분노 3회** 겪음 · 세션 #8 시작 시 동일 구조 재확인으로 추가 피로 발생

**How to apply**:
1. 새 메모리 저장 시 **두 경로 모두 Write** (프로젝트 로컬 먼저, 전역 동시 복사)
2. `priority: critical` 마커는 둘 다 박아야 §6.5 자동 주입 + frontmatter contract 일관
3. 기존 메모리 갱신 시에도 **두 경로 모두 갱신** (한쪽만 고치면 다음 세션에 stale 값이 역주입됨)
4. `session_start.py` 가 자동으로 전역 → 로컬 sync 하도록 구현되어 있음 (새 전역 메모리는 다음 세션 시작 시 자동으로 로컬에도 반영됨). 로컬에 새 메모리 수동 추가 시에는 전역으로도 수동 복사 필요.
5. git commit 시 `.claude/memory/` 전체 포함 확인 (`git status` 로 검증)

**Related FAILURES**:
- FAIL-016 (세션 #7) — 샘플링 독서 근본 원인 → 앵커 #3 신설로 해결 시도
- FAIL-017 (세션 #8) — 앵커 #3 자체가 이중 박제 미적용으로 무력화됨 → 본 원칙으로 해결

**Related Memories**:
- `feedback_knight_canon_locked.md` (priority: critical · 나이트 Canon)
- `feedback_no_sampling_full_read.md` (priority: critical · 샘플링 금지)
- `feedback_naming_intuitive_dated.md` (파일명 원칙)
- `feedback_one_topic_per_file.md` (원자화 원칙)
