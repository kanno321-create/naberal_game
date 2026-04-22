---
name: cd 금지 · 절대경로만 사용
description: Bash 도구에서 cd 로 작업 디렉토리를 옮기면 프로젝트 상대경로 Hook 이 깨진다
type: feedback
originSessionId: 0c22c80f-004b-4b15-afc0-7e72e41cb1c8
---
# cd 금지 · 절대경로만 사용

**규칙**: Bash 도구 안에서 `cd` 로 작업 디렉토리를 **옮기지 말 것**. 모든 명령은 **절대경로** 로 수행.

**Why**: 2026-04-21 세션에서 `cd ~/.claude && ...` 로 작업 디렉토리 변경 후, 프로젝트의 `post_tool_use.py` Hook 이 상대경로 `.claude/hooks/post_tool_use.py` 를 현재 cwd 기준으로 해석 → `C:\Users\PC\.claude\.claude\hooks\post_tool_use.py` 로 찾아 파일 미존재 에러 발생. Hook 설계가 프로젝트 루트 cwd 를 전제로 하기 때문.

**How to apply**:
- `cd` 대신 모든 경로를 **절대경로로** 표기. 예: `ls ~/.claude/skills/` 가 아니라 `ls "C:/Users/PC/.claude/skills/"` (단 `~` 는 Git Bash 에서 안전하게 확장됨).
- 여러 폴더에서 작업할 경우 명령마다 대상 경로를 절대경로로 명시. `cd dir1 && cmd1; cd dir2 && cmd2` 금지.
- 스크립트로 여러 디렉토리 순회가 필요할 때는 `for d in /abs/path/*/; do ...; done` 형식.
- 시스템 프롬프트에도 명시된 원칙: *"Try to maintain your current working directory throughout the session by using absolute paths and avoiding usage of cd"*.

**예외**: 사용자가 명시적으로 `cd` 를 요청한 경우에만 허용 (예: *"로컬 레포에 cd 해서 빌드해"*). 그런 경우에도 사후에 cwd 를 프로젝트 루트로 복귀.
