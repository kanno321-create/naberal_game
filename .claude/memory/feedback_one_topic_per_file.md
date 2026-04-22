---
name: 한 주제 = 한 파일 원자화 원칙 (Zettelkasten)
description: 모든 세계관·역사·관계도·캐릭터·경제·문화 등 내용을 하나의 파일에 여러 주제로 묶지 말고 주제당 독립 파일로 분해. 지리 역사 관계도 등을 한 파일에 담지 말 것
type: feedback
originSessionId: a7033dcf-2d41-4bd0-950a-ba90de6fd9ad
---
# Rule
**모든 내용을 하나하나의 독립 문서로 만든다.** 한 파일에 여러 주제를 묶지 않는다.

구체:
- 지리 + 역사 + 관계도 → **각각 따로 파일**
- 왕국 1 개 = 1 파일 ❌
- 왕국 1 개 = 디렉토리 · 내부에 주제별 파일 ✅ (왕도지도·왕족 각자·귀족 각자·문화 세부 등)
- 왕족 5 명 = 1 파일 ❌ · 왕족 각자 1 파일 ✅
- 축제 · 의상 · 건축 · 음식 → 각자 1 파일 (`culture/X.md` 묶음 금지)

# Why
대표님 직접 지시 (2026-04-22 세션 #4): *"지리 역사 관계도 같은것들은 한파일에 넣지말고 다 따로 파일을 만들어서 넣어라 앞으로 모든 내용을 하나하나의 문서로 만들어라 하나의 문서에 여러내용을 담지마라"*

합리성:
- **Zettelkasten / 원자적 노트** 원리
- Obsidian 그래프뷰에서 관계가 명확히 시각화
- 변경 시 diff 범위 최소화 → 충돌 방지
- 특정 주제만 LLM 컨텍스트에 로드 가능 (token 효율)
- 검색·링크·백링크 정확도 향상

# How to apply

## 모든 에이전트 briefing 공통 반영
- 산출물 경로 설계 시 **주제별 파일 분해** 먼저
- 멀티 토픽 파일 금지 (overview·index 파일 예외)
- 파일당 3~10 KB 권장 (너무 작아도 500줄 넘지만 않음)

## 추가 원칙 (2026-04-22 대표님 재지시)
**왕국별 폴더를 달리하고 그 폴더 안에 관련 내용의 파일을 원자화한다.**
- 왕국 1 개 = 완결된 독립 폴더 (DDD bounded context)
- 왕국 고유 모든 것 (왕도·왕족·귀족·영지·역사·문화·군대·축제·의상) → 그 왕국 폴더 안
- 대륙 레벨 공통 (geography·history·relations) 만 별도 디렉토리
- 다른 왕국과 섞이지 말 것 · 왕국 폴더가 곧 그 왕국의 완결 우주

## 디렉토리 구조 예시 (서쪽 대륙 Elucia · 2026-04-22 최종)
```
wiki/design/worldbuilding/elucia/
├── geography/
│   ├── 00_overview.md
│   ├── coastlines.md
│   ├── mountain_ranges.md
│   ├── rivers.md
│   ├── forests.md
│   ├── plains.md
│   ├── climate_zones.md
│   └── elevation.md
├── political/
│   ├── 00_overview.md
│   ├── empire_papal_territories.md
│   ├── kingdom_silvan_territories.md
│   └── ... (12 국)
├── toponymy/
│   ├── 00_naming_system.md
│   ├── empire_papal_cities.md
│   ├── empire_papal_villages.md
│   ├── kingdom_silvan_cities.md
│   ├── kingdom_silvan_villages.md
│   └── ... (12 국 × 2)
├── roads/
│   ├── continental_highways.md
│   ├── kingdom_trade_routes.md
│   ├── regional_roads.md
│   ├── village_paths.md
│   └── ports_and_sea_lanes.md
├── economy/
│   ├── agriculture.md
│   ├── fishery.md
│   ├── mining.md
│   ├── crafts.md
│   ├── trade_networks.md
│   ├── slave_economy.md
│   └── hal_bae_free_magic.md
├── culture/
│   ├── clothing.md
│   ├── festivals.md
│   ├── cuisine.md
│   ├── architecture.md
│   ├── language.md
│   └── religion.md
├── history/
│   ├── timeline.md
│   ├── primordial_era.md
│   ├── mazok_era.md
│   ├── collapse.md
│   ├── divine_era.md
│   ├── human_era_early.md
│   ├── empire_founding.md
│   ├── kingdom_silvan_founding.md
│   ├── kingdom_silvan_dynasties.md
│   ├── kingdom_silvan_wars.md
│   └── ... (왕국별 주제별 분해)
├── relations/
│   ├── alliances.md
│   ├── conflicts.md
│   ├── marriage_ties.md
│   ├── trade_treaties.md
│   └── religious_division.md
├── kingdoms/
│   ├── empire_papal/
│   │   ├── 00_overview.md
│   │   ├── capital_map.md
│   │   ├── royals/
│   │   │   ├── pope_current.md
│   │   │   ├── cardinal_X.md
│   │   │   └── ...
│   │   ├── nobles/
│   │   │   ├── duke_X.md
│   │   │   ├── count_Y.md
│   │   │   └── ...
│   │   ├── knights_orders.md
│   │   ├── heraldry.md
│   │   ├── military.md
│   │   └── festivals.md
│   ├── kingdom_silvan/
│   │   └── ... (동일 구조)
│   └── ... (12 국)
├── historical_texts/
│   ├── annals_of_elucia_book_I.md
│   ├── annals_of_elucia_book_II.md
│   ├── chronicles_of_silvan.md
│   └── ...
├── maps/
│   └── annotations.md
├── graphs/
│   └── relationship_graph.md
└── MASTER_index.md  (전체 네비게이션만, 내용 서술 금지)
```

## 예외
- `00_overview.md` · `MASTER_index.md` — 순수 인덱스·네비게이션만 (내용 서술 금지)
- `00_timeline.md` — 시간 참조용 시계열 파일 (각 시대는 별도 파일)

## 검증
- World-Integrator 가 최종 단계에서 멀티 토픽 파일 검출 시 에이전트 재작업 요청
- 각 파일은 단일 주제 · 단일 질문에 답해야 함
