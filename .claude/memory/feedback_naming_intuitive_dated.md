---
name: 파일명·위치 직관성 + 날짜 표기 원칙
description: 모든 파일은 필요할 때 즉시 찾을 수 있는 직관적 위치에 배치하고, 파일명만 봐도 내용·성격·시점이 파악되도록 명명하며 생성 날짜(YYYY-MM-DD)를 파일명에 포함
type: feedback
originSessionId: a7033dcf-2d41-4bd0-950a-ba90de6fd9ad
---
# Rule
모든 파일·폴더는 다음 3 원칙을 동시에 만족한다:

## 1. 직관적 위치
- 폴더 계층이 곧 탐색 경로
- 폴더명만 봐도 그 안 내용 즉시 추론 가능
- 국가·왕국·지역·주제 순서로 계층화
- 관련 있는 것은 가까이 · 무관한 것은 분리

**예시**:
```
wiki/design/worldbuilding/elucia/kingdoms/kingdom_silvan/royals/king_edric_iii_2026-04-22.md
                                                      ↑
                                                      경로만 봐도 "Elucia 대륙 · Silvan 왕국 · 왕족 · 에드릭 3세 왕 · 2026-04-22 생성"
```

## 2. 직관적 네이밍
- 소문자 + 언더스코어 (`snake_case`)
- 파일명 보면 내용·성격 즉시 파악
- 계층 중복 정보 허용 (왕국 폴더 안에 `king_edric_iii` · 필요 시 `silvan_king_edric_iii` 가능)

**파일명 패턴**:

| 주제 | 패턴 | 예시 |
|------|------|------|
| 왕족 | `king_<name>_<date>.md`, `queen_<name>_<date>.md`, `prince_<name>_<date>.md`, `princess_<name>_<date>.md` | `king_edric_iii_2026-04-22.md` |
| 귀족 | `duke_<domain>_<date>.md`, `count_<domain>_<date>.md`, `baron_<domain>_<date>.md` | `duke_ravencrest_alaric_2026-04-22.md` |
| 도시 | `city_<name>_<date>.md` | `city_silvanholme_2026-04-22.md` |
| 마을 | `village_<name>_<date>.md` | `village_thornbrook_2026-04-22.md` |
| 지리 feature | `<type>_<specific>_<date>.md` | `mountain_dragonspine_range_2026-04-22.md` |
| 도로 | `road_<from>_to_<to>_<date>.md` 또는 `highway_<name>_<date>.md` | `highway_via_imperialis_2026-04-22.md` |
| 역사 사건 | `event_<name>_<date>.md` | `event_silvan_succession_war_2026-04-22.md` |
| 가문 | `house_<name>_<date>.md` | `house_ravencrest_2026-04-22.md` |
| 기사단 | `order_<name>_<date>.md` | `order_silver_wolves_2026-04-22.md` |

## 3. 날짜 표기
- 형식: `YYYY-MM-DD` (ISO 8601)
- 위치: 파일명 **끝** (`<topic>_<date>.md`)
- **파일명 날짜 = 최초 생성일 고정** (수정해도 파일명 날짜는 불변)
- 업데이트 이력은 frontmatter `updated:` 에 누적 기록
- 폴더에는 날짜 표기 없음 (폴더는 개념적 구분)

**예시**:
```
capital_map_silvan_2026-04-22.md    ← 최초 작성 날짜 고정
```

frontmatter:
```yaml
---
title: Silvan 왕도 지도
created: 2026-04-22
updated: 2026-04-22
# 이후 수정 시 updated 만 갱신, 파일명 고정
---
```

# Why
대표님 직접 지시 (2026-04-22 세션 #4): *"뭐든지 필요할때 직관적으로 바로바로 찾을수있게 위치시키고 네이밍도 그렇게해라 날짜까지 표기해서"*

합리성:
- **검색 효율**: 경로·파일명만 보고도 원하는 것 찾음
- **LLM 정확도**: 의미 있는 키워드가 경로에 박혀 있어야 에이전트가 정확히 탐색
- **Obsidian 백링크**: 파일명 날짜 고정 시 백링크 안정
- **버전 추적**: frontmatter updated 누적으로 변경 이력 보존

# How to apply

## 모든 에이전트 briefing 반영
- 파일 생성 전 위치·네이밍을 이 원칙에 맞추어 설계
- 날짜 누락 금지 (단, `00_overview.md` 같은 인덱스 파일은 예외로 날짜 생략 가능)
- 파일 생성일 = 대표님 세션 기준 현재 날짜 (2026-04-22)

## 폴더 구조 규칙
- 계층 순서: `<대륙>/<도메인>/<구체 주제>/`
- 왕국은 왕국명으로 폴더 (예: `kingdoms/kingdom_silvan/`)
- 그 안 주제 폴더는 영어 공통 (예: `royals/`, `nobles/`, `cities/`, `villages/`, `history/`)

## 예외
- `00_overview.md`, `MASTER_index.md` — 날짜 없음 (불변 인덱스)
- `README.md` — 날짜 없음

## 검증
- World-Integrator 가 최종 단계에서 네이밍 원칙 위반 파일 검출 → 재명명 요청
