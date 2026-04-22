---
name: 대량 병렬 에이전트 fan-out 기본 모델 = sonnet 4.6
description: 월드빌딩·집필 등 대량 병렬 서브에이전트 fan-out 시 기본 모델을 sonnet 4.6 으로 지정. Agent tool 호출 시 model "sonnet" 파라미터 명시
type: feedback
originSessionId: a7033dcf-2d41-4bd0-950a-ba90de6fd9ad
---
# Rule
Agent tool 로 서브에이전트를 spawn 할 때 대량 병렬 fan-out (5+ 에이전트 동시) 에서는 기본 모델을 sonnet 으로 지정한다.

```json
{
  "subagent_type": "general-purpose",
  "model": "sonnet",
  "description": "...",
  "prompt": "..."
}
```

# Why
대표님 직접 지시 (2026-04-22 세션 #4): *"sonnet 4.6으로"*

합리성:
- 22 에이전트 동시 fan-out 에서 opus 는 비용·속도 불리
- 월드빌딩은 방대하지만 단일 도메인 반복 작업 — 지시 준수가 핵심이지 복잡 추론이 핵심 아님
- sonnet 4.6 의 지시 준수력 + 3~5 배 처리 속도가 이 업무 성격에 최적

# How to apply

## 기본 적용
- 월드빌딩·집필·critique·리서치 등 대량 병렬 fan-out 전체에 sonnet 4.6 기본
- 메인 오케스트레이터(현재 세션) 는 opus 유지 — 대표님과의 대화·결정·편집

## 예외 (opus 유지)
- Q-CORE 반전 구조 설계 등 **창작적 판단이 핵심** 인 단일 에이전트 작업
- prose-critique 의 최고 난도 비평 (아직 확정 아님, 대표님 결정 시)

## 호출 예시
```
Agent({
  subagent_type: "general-purpose",
  model: "sonnet",
  description: "Wave 2 · Toponymist",
  prompt: "<STEP 0 필독 블록 + briefing>"
})
```

# 검증 방법
실행 로그에서 각 에이전트 모델이 sonnet 인지 확인. opus 누락 시 설정 오류.
