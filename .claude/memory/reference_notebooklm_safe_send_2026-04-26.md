---
name: NotebookLM safe_send.py · race condition 자동 우회 wrapper
description: ask_question.py 의 polling 이 직전 답변을 stable 로 잘못 인식하는 race condition 발생 시 hash 비교 자동 재시도. 세션 #14 5/5 쿼리 중 4 쿼리에서 race 발생 → wrapper 작성으로 영구 해결.
type: reference
priority: high
originSessionId: ee6ea3cc-3bec-49dc-ad4d-411ebfd62c3e
---
**도구 위치**: `c:\Users\PC\Desktop\naberal_group\studios\game\.planning\nlm_prompts\safe_send.py`

**해결 문제**: NotebookLM `ask_question.py` 의 polling 로직이 페이지 로드 직후 *직전 쿼리 답변 element* 를 발견 → 3 polls × 1초 = 3초 만에 stable 로 잘못 인식 → 7초만에 *복제 응답* 반환. 새 답변이 stream되기 전 race condition 발생.

**증상 식별**:
- 응답 시간 < 10초 (정상은 60~85초)
- 응답 본문 = 직전 쿼리 응답 100% 복제
- 노트북에 누적된 이전 대화 기록이 새 페이지 로드 시 표시되어 발생

**우회 메커니즘**:
1. 응답 받은 후 직전 응답들의 답변 본문 SHA-256 hash 와 비교
2. hash 일치 = 복제 → 자동 재시도 (최대 5회 · 매 150초 대기)
3. 150초 대기 = NotebookLM 답변 생성 cycle 보장 + 다음 호출 race 회피
4. timeout 기본 2400초 (대표님 *시간 넉넉히* 지시 반영)

**사용법**:
```bash
NLM_NOTEBOOK_ID=<uuid> python "c:/Users/PC/Desktop/naberal_group/studios/game/.planning/nlm_prompts/safe_send.py" \
  "c:/Users/PC/Desktop/naberal_group/studios/game/.planning/nlm_prompts/<NN>_<topic>.txt" \
  "c:/Users/PC/Desktop/naberal_group/studios/game/.planning/nlm_responses/<NN>_<topic>.md" \
  [timeout_s]
```

**Why (대표님 2026-04-26 세션 #14)**:
- 5 쿼리 (Q13~Q17) 다크판타지 정수 채굴 시도 → 첫 호출 4/5 race 발생
- 수동 재전송으로 우회 가능했으나 비효율 → wrapper 작성으로 영구 해결
- 대표님 지시: *"답변하는데 꽤 오래걸린다 시간좀 넉넉히줘라"* → timeout 2400 + WAIT 150 적용

**관련 자산**:
- `feedback_notebooklm_paste_only.md` (priority: critical · clipboard paste 우회)
- `.planning/nlm_prompts/run.py` (단일라인 변환 + .sent.txt 박제 + 환경변수 NLM_NOTEBOOK_ID 패치)
- `.planning/research/nlm_result_09_dark_fantasy_essence_2026-04-26.md` (세션 #14 5 쿼리 종합 박제)
- `c:\Users\PC\Desktop\shorts_naberal\.claude\skills\notebooklm\scripts\ask_question.py` line 128-170 (race 발생 polling 로직)

**향후 사용 원칙**:
1. **모든 NotebookLM 호출은 safe_send.py 통해서만** (run.py 직접 호출 금지)
2. race 감지 시 자동 재시도되므로 사용자 개입 불필요
3. 5회 모두 실패 시 = 노트북 자체 문제 (브라우저 state 만료 등) → 인증 재확인
4. timeout 2400s = 답변 생성 + race 재시도 4회 모두 수용 가능한 마진

**미해결 근본 문제**:
- `ask_question.py` 자체 polling 로직이 race 발생 원인 — 외부 스킬 코드 수정은 위험성 있어 wrapper 레벨에서 우회
- 향후 ask_question.py 가 *기존 element 개수 캐싱 → 새 element 추가 wait* 으로 패치되면 wrapper 불필요해짐
