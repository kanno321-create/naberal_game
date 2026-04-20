---
name: reference_beginner_gamedev_knowledge
description: 초보 1인 인디 게임 개발자 종합 지식 박제 — NotebookLM 6-쿼리 딥 리서치 결과 인덱스 (Unity 6/Steam/AI 도구 체인/한국 컨텍스트)
type: reference
---

# 게임 개발 지식 박제 — 초보 1인 인디 + Unity 6 + Steam

**수집 경로**: NotebookLM 노트북 `a0bb9e88-b8cc-4a8d-a55a-75ffa01996eb` × 6 분할 쿼리 (2026-04-20). 총 답변 57,609자 보존.

## 원본 참조

**전체 답변**: `.planning/research/nlm_result_0{1..6}_*.md` (상세)
**네비게이션 인덱스**: `.planning/research/nlm_summary.md` (상황 → 원본 파일 + 핵심 발견)

## 상황별 1-hop 라우팅

| 상황 키워드 | 참조 경로 |
|-----------|---------|
| "인디 현실 / MVP / 장르 / 핵심 루프 / Flow/Juice" | `nlm_result_01_indie_mvp_design.md` |
| "Unity 6 / C# 패턴 / URP / 셰이더 / 퍼포먼스" | `nlm_result_02_unity6_all.md` |
| "게임 아트 / Aseprite/Blender/ZBrush / Nano Banana/Scenario / Meshy/Tripo/Mixamo" | `nlm_result_03_game_art_ai.md` |
| "게임 오디오 / Suno/ElevenLabs/Sononym / FMOD/Wwise / LUFS" | `nlm_result_04_game_audio.md` |
| "Steam 출시 / Steamworks / 위시리스트 / Next Fest / 마케팅 / BIC" | `nlm_result_05_steam_marketing.md` |
| "번아웃 / 사업자 등록 / 세금 / AI 저작권 / 2026 AI 현실" | `nlm_result_06_mental_legal_ai.md` |

## 핵심 개념 (나베랄 감마 즉시 회수용)

- **14-Tool Arsenal**: 2026 1인 개발자 도구 세트 프레임 — AI 로 기획·코딩·아트·사운드·QA·마케팅 커버
- **AI 후처리 필수 (87%)**: AI 는 가속기, 최종 결정권은 사람
- **MVP 이중 의미**: (1) Model-View-Presenter 코드 아키텍처 (2) Minimum Viable Product 제품
- **3-tier 루프**: 30초(전투·이동 즉시 재미) / 3분(스테이지·웨이브 보상) / 30분(빌드 완성·메타 성장)
- **성공 공식**: 독창적 코어 메커니즘 + 극대화된 게임성 (Balatro/Animal Well/Vampire Survivors)
- **실패 패턴**: 튜토리얼 지옥 / AI Slop / Scope Bloat / Feature Creep / Perfectionism
- **AI 스코프 통제**: `CLAUDE.md` 로 AI 에이전트 기술 스택·컨벤션 명시 → AI Slop 차단

## 기술 스택 (대표님 결정 + NotebookLM 보강)

| 레이어 | 1순위 |
|--------|------|
| 엔진 | **Unity 6 LTS** + C# + IL2CPP 빌드 |
| 렌더 파이프라인 | **URP** (HDRP 아님, 2D/3D 복합 최적) |
| 코드 AI | **Claude Code** + Cursor + **Unity MCP 플러그인** |
| 학습 (영문) | Unity Essentials → Code Monkey 3D (10h) → Brackeys/Tarodev/GMTK |
| 학습 (한국어) | **레트로(retr0)** · 골드메탈 · 케이디 · Unity Korea |
| 2D 전통 | Aseprite ($20 픽셀), Krita (무료), Photoshop ($21/월) |
| 3D 전통 | **Blender** (무료 완결판) + ZBrush 스컬프팅 + Substance Painter/Designer |
| 2D AI | **Scenario** (게임 전용) · Leonardo · **BRIA** (저작권 안전 라이선스) |
| 3D AI | **Tripo** (캐릭터 쿼드+자동리깅) · **Meshy** (소품 30-60초) · Rodin · Luma Genie |
| 리깅/모션 | **Mixamo** (무료) · **Move AI Gen 2** (스마트폰) · DeepMotion · Cascadeur |
| 2D 스켈레탈 | Spine (표준) · Moho (저예산) |
| 음악 | **Soundraw** (BGM 루프) · Suno v4 · Udio |
| SFX | **Lami.ai** (Text-to-SFX) · **Sononym** (음향 기반 검색) · Freesound CC0 |
| 보이스 | ElevenLabs · **Typecast** (한국어 감정) · Naver Clova Voice |
| 오디오 미들웨어 | Unity AudioMixer (MVP) → **FMOD** (연 50만$ 미만 무료) |
| QA | **Modl:test / Modl:play** (AI 봇 자동화) |
| Steam 통합 | **Steamworks.NET** (C# 래퍼) |

## 한국 1인 개발자 특수 경로

| 영역 | 구체 내용 |
|------|---------|
| 커뮤니티 | 카카오톡 오픈채팅 (Unity Korea) · 네이버 카페 |
| 오프라인 | BIC 부산 인디 커넥트 페스티벌 · PlayX4 |
| 사업자 | 홈택스 "통신판매업" + "소프트웨어 개발/공급업" 개인사업자 **간이과세자** |
| 해외 세금 | W-8BEN + 한/미 조세조약 → 원천세 30% → 10% 감면 |
| 상표권 | KIPO 출원 + 마드리드 조약 (글로벌) |
| 계약 | 외주/파트너 NDA + "무단 AI 생성물 사용 금지" 조항 |

## Steam 출시 타임라인 (12개월 역산)

| T-개월 | 액션 |
|-------|------|
| T-12 | Coming Soon 페이지 오픈 + 5초 훅 트레일러 |
| T-6 | 위시리스트 10,000 ("Popular Upcoming" 임계치) |
| T-2~4 | Next Fest 참가 (일회성, 20-45분 데모) |
| T-30일 | $100 수수료 결제 (출시 쿨타임 시작) |
| T-14일 | Coming Soon→Release 쿨타임 |
| T-0 | Launch Discount 10-15% + Day 1 패치 준비 |
| T+24h | 핫픽스 + 스팀 공지 |
| T+6~12개월 | 유료 DLC (본편 20-30% 가격) |

## 가격 공식

- 로그라이크/시뮬 솔로 인디: **$14.99 ~ $19.99**
- EA = 정식의 **70-80%** (Balatro 사례)
- 30일 할인 쿨다운 (여름/가을/겨울 세일 30일 전 개인 할인 금지)

## 나베랄 감마 업무 규칙 (이 박제 기반)

1. 대표님이 "게임 개발 ~에 대해 알려줘" → 먼저 이 인덱스로 상황 → 원본 파일 라우팅 → 원본 답변 인용
2. 외부 지식 보강 필요한 영역 (30초·3분·30분 이론, 한국 세법, Steam 알고리즘 수치, LUFS) 은 명시적 "외부 지식" 표기
3. 대표님 결정 사항(Unity 6 + Steam + C# + 로그라이크/시뮬/RPG)을 일관되게 참조
4. 추가 질문 필요 시 동일 NotebookLM 에 후속 쿼리 (6-쿼리 패턴 재사용)

## Source 인용 규칙

- NotebookLM 소스 인용된 내용 → "[NotebookLM 출처 n]" 표기
- NotebookLM 이 "[소스 외부 지식]" 표기한 것 → "[외부 게임 기획 지식]" 으로 명시
- 대표님 결정 + 제가 추론한 것 → "[나베랄 감마 제안]" 명시

## 수집 메타데이터

- **질의 건수**: 6 쿼리 (인디현실·Unity6·아트·오디오·Steam·관리/법률/AI)
- **총 답변량**: 57,609자 (123KB)
- **각 쿼리 소요**: 156-216초 (평균 178초)
- **D-6 규율**: single-string argv, newline 없음, 각 쿼리 독립 실행
- **실패 복구**: Query 4 1회 실패 → 4-5-6 재실행 성공
- **노트북 소스 강점**: AI 도구 체인, Unity 6 기술, 커뮤니티
- **노트북 소스 약점 (외부 지식 보완)**: Steam 비즈니스 디테일, 한국 법률, 게임 디자인 순수 이론
