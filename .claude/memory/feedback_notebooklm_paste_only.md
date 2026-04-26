---
name: NotebookLM 질문은 파일→복사→붙여넣기만 · 직접 타이핑 절대 금지
description: NotebookLM 입력창은 줄바꿈 = 전송 트리거. 직접 타이핑하면 줄바꿈마다 쿼리가 단편 전송되어 답변 무용 + 무료 50/일 한도 낭비. 반드시 임시 파일에 질문 작성 → 전체 복사 → NotebookLM 입력창 클릭 → 붙여넣기 → Enter 1회.
type: feedback
priority: critical
originSessionId: ee6ea3cc-3bec-49dc-ad4d-411ebfd62c3e
---
**규칙**: NotebookLM 입력창에 **직접 타이핑 절대 금지**. 모든 질문은 다음 4단계로만 전송:
1. 임시 파일(메모장·텍스트 에디터·`.md` 파일)에 **질문 전체** 작성 (배경 + 본 질문 + 원하는 답변 형식)
2. **Ctrl+A → Ctrl+C** 로 전체 복사
3. NotebookLM 입력창 클릭 → **Ctrl+V** 로 붙여넣기
4. **Enter 1회** 로 전송

**Why (대표님 2026-04-26 세션 #14 직접 지시)**:
- NotebookLM 입력창은 *Enter = 메시지 전송* 동작 (Shift+Enter 없음). 직접 타이핑 중 줄바꿈을 누르면 그 시점까지의 입력이 전송되고 나머지는 *다음 쿼리* 로 단편화됨
- 대표님 원문: *"줄바꿈행위가 메시지 보내기가 되어버려 제대로된 질문을 할수가없어 (...) 절대로 직접 입력창에서 입력하지마라 절대올바른 대답은커녕 쿼리만 다날라간다"*
- 결과:
  - 단편 1 만 받은 답변 = 컨텍스트 손실 → 무용
  - 단편 2~N = 컨텍스트 없는 후속 질문 → 무용
  - 무료 Google 계정 50 쿼리/일 한도가 단편마다 1 카운트로 빠르게 소진됨
- 클립보드 paste (`Ctrl+V`) 는 줄바꿈을 입력 이벤트가 아닌 *문자열 통째 삽입* 으로 처리 → Enter 트리거 회피

**How to apply**:
1. **대표님 직접 사용 시**: 메모장·VSCode·`.md` 파일 등에 질문 전체 작성 후 복사 → 붙여넣기. 입력창에서 직접 타이핑·줄바꿈 절대 금지
2. **나베가 ask_question.py 사용 시**: 이미 `pyperclip.copy(question)` + `page.keyboard.press("Control+V")` 방식으로 구현됨 (`shorts_naberal/.claude/skills/notebooklm/scripts/ask_question.py` line 107-119). 코드 주석 *"CRITICAL: human_type interprets \n as Enter which fragments prompt into many queries (see memory feedback_nlm_auto_enter_bug — session 77 discovery)"* 절대 보존
3. **나베가 신규 자동화 작성 시**: `page.type()` / `keyboard.type()` / `human_type()` 사용 절대 금지. **clipboard paste 만 허용**
4. **검증 체크리스트**: NotebookLM 답변이 비정상적으로 짧거나 질문 일부만 인지된 경우 = 단편 전송 의심 → 새 세션으로 재시도 + 본 메모리 절차 재확인

**Related Code**:
- `C:\Users\PC\Desktop\shorts_naberal\.claude\skills\notebooklm\scripts\ask_question.py` line 107-119 — 클립보드 paste 우회 구현 (보존 절대)
- `C:\Users\PC\Desktop\shorts_naberal\.claude\skills\notebooklm\` — NotebookLM 스킬 본체

**Related Memories**:
- `feedback_active_obsidian_notebooklm.md` — NotebookLM 능동 활용 원칙
- `reference_notebooklm_game.md` — game 도메인 NotebookLM 노트북 URL
- `feedback_dual_persistence_required.md` — 본 메모리도 이중 박제됨

**Related FAILURES** (잠재):
- 단편 전송 발생 시 `FAILURES.md` 에 신규 entry 추가 + 본 메모리 강화 사례로 인용
