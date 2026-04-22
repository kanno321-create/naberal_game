---
title: "NLM Summary — NotebookLM 딥 리서치 핵심 요약 인덱스"
date: 2026-04-20
notebook_id: a0bb9e88-b8cc-4a8d-a55a-75ffa01996eb
total_answer_chars: 57609
total_queries: 6
layer: 1
canon_tier: derived
tags: [research, nlm, summary, index]
updated: 2026-04-22
related:
  - "[[../../wiki/FRONTMATTER_STANDARD]]"
  - "[[nlm_queries]]"
  - "[[../../wiki/gameplay/MOC]]"
  - "[[../../wiki/engine/MOC]]"
agent_briefing_level: reference
derived_from:
  - "[[../../wiki/design/brainstorm_2026-04-21]]"
---

# NotebookLM Deep Research — 핵심 요약 인덱스

대표님 노트북(`a0bb9e88-...`) 의 소스 자료 + NotebookLM 외부 게임 기획 지식을 결합한
**초보 1인 인디 게임 개발자 + 나베랄 감마 AI 공동 학습 종합 결과**.
원본 전체 답변은 `nlm_result_0{1..6}_*.md` 에 보존.

## 상황 → 원본 파일 라우팅

| 질문 주제 | 원본 파일 |
|---------|---------|
| "인디 현실" / "MVP" / "장르 선택" / "핵심 루프" / "Flow/Juice/Risk-Reward" | [[nlm_result_01_indie_mvp_design]] |
| "Unity 6 학습" / "C# 패턴" / "ScriptableObject" / "URP" / "Profiler" / "IL2CPP" | [[nlm_result_02_unity6_all]] |
| "게임 아트" / "Aseprite/Blender/ZBrush" / "Nano Banana/Scenario/Leonardo" / "Meshy/Tripo/Mixamo" | [[nlm_result_03_game_art_ai]] |
| "게임 오디오" / "Suno/ElevenLabs/Sononym" / "FMOD/Wwise/AudioMixer" / "LUFS" | [[nlm_result_04_game_audio]] |
| "Steam 출시" / "Steamworks" / "위시리스트" / "Next Fest" / "EA 전략" / "마케팅" / "BIC" | [[nlm_result_05_steam_marketing]] |
| "번아웃" / "멘털" / "사업자 등록" / "세금" / "AI 저작권" / "CLAUDE.md 스코프 통제" | [[nlm_result_06_mental_legal_ai]] |

## 핵심 발견 — 2026 1인 인디 게임 개발 프레임

### 1. 14-Tool Arsenal (1인 개발자용 도구 세트 프레임워크)
노트북 소스의 핵심 개념. 2026 AI 도구 체인으로 1인이 기획·코딩·아트·사운드·QA·마케팅을 모두 커버 가능. **개발자 87% 가 AI 결과물에 "인간 후처리" 필수라고 인정** — AI 는 가속기, 최종 결정권은 사람.

### 2. MVP 이중 의미
- **코드 아키텍처 MVP** = Model-View-Presenter (View/Logic 분리, 스코프 블로트 방지)
- **제품 MVP** = Minimum Viable Product (30초·3분·30분 3-tier 루프 검증 우선)

### 3. 성공 공식 (Balatro / Animal Well / Vampire Survivors)
"그래픽" 이 아니라 **"독창적·직관적 코어 메커니즘 + 극대화된 게임성"**. 1인 개발에서 Juice (타격감/피드백) 를 최우선 폴리싱 대상으로.

### 4. 실패 패턴 (반드시 회피)
- **튜토리얼 지옥** — 복붙만 하고 원리 이해 안 함. 대응: AI 러버덕 디버깅 ("왜 작동하는가?")
- **AI Slop** — AI 가 생성한 미이해 코드를 PR로 투척. 대응: `CLAUDE.md` 로 AI 스코프·스타일 통제
- **Scope Bloat / Feature Creep** — "이 기능이 30초 루프 재미를 높이는가?" 기준 적용
- **Perfectionism / Comparison / Isolation / Impostor Syndrome** — 커뮤니티 + Timeboxing + 작은 성공 축적

### 5. 한국 1인 개발자 특수 경로
- 한국어 학습 자료: **레트로(retr0) · 골드메탈 · 케이디 · Unity Korea 공식**
- 로컬 커뮤니티: **카카오톡 오픈채팅 (Unity Korea 등) · 네이버 카페**
- 오프라인 행사: **BIC 부산 인디 커넥트 · PlayX4**
- 세무: **홈택스 간이과세자 + 통신판매업 + 소프트웨어 개발/공급업**
- 해외 원천세 감면: **W-8BEN + 한/미 조세조약 (30% → 10%)**
- 상표권: **KIPO + 마드리드 조약 (해외 출원)**

### 6. Steam 마일스톤 (출시 12개월 전 타임라인)
| 시점 | 액션 |
|------|------|
| T-12 개월 | Coming Soon 페이지 오픈 + 5초 훅 트레일러 |
| T-6 개월 | 위시리스트 10,000 돌파 ("Popular Upcoming" 임계치) |
| T-2~4 개월 | Next Fest 참가 (일회성, 20-45분 데모) |
| T-30 일 | 100달러 수수료 결제 (출시 쿨타임 시작) |
| T-14 일 | Coming Soon → Release 버튼 활성 쿨타임 |
| T-0 | 10-15% Launch Discount + Day 1 패치 준비 |
| T+24h | 핫픽스 첫 패치 + 스팀 공지 ("개발자 소통 중") |
| T+6~12 개월 | 유료 DLC (본편 20-30% 가격) |

### 7. 가격 공식
- 로그라이크/시뮬 솔로 인디: **$14.99 ~ $19.99** 표준
- EA 가격 = 정식 가격의 **70-80%**
- 30일 쿨다운 (할인 종료 후)
- 지역별 가격 (Steam Regional Pricing) 수락

## 기술 스택 — 레이어별 선택 (2026-04-20)

### 엔진·언어
- **Unity 6 LTS + C#** (대표님 결정) — Mono → **IL2CPP** 빌드 전환
- 학습 순서: Unity Essentials (8-10h) → Code Monkey 3D (10h) → Brackeys/Tarodev/GMTK → 한국어 레트로(retr0)/골드메탈
- **URP** 선택 (HDRP 아님) — 2D/3D 복합 인디 최적
- **AI 페어 프로그래밍**: Claude Code + Cursor + **Unity MCP 플러그인** (에디터 밖에서 씬 분석·스크립트 생성)

### 코드 패턴
- **ScriptableObject** 데이터 아키텍처
- **Observer Pattern** (UnityEvent / ScriptableObject Event)
- **State Machine** (Idle/Run/Attack 분리)
- **Awaitable (async/await)** — Unity 6 신기능, Coroutine 대체
- **Object Pooling** (총알/이펙트/적)
- **GC Alloc 제거**: Update 내 문자열 합치기 / LINQ / GetComponent / FindObjectOfType 금지
- **Physics.OverlapSphereNonAlloc** (할당 0)
- **Addressables** 에셋 스트리밍

### Unity 6 신기능 (2024-2026)
- **UI Toolkit + Data Binding** → MVVM UI
- **GPU Resident Drawer** → Draw Call 대폭 감소
- **Adaptive Probe Volumes (APV)** → 동적 오브젝트 GI
- **Spatial-Temporal Post-processing (STP)** → 업스케일링

### 아트 파이프라인
- **2D 전통**: Aseprite (픽셀 $20), Photoshop ($21/월), Clip Studio Paint ($50), Krita (무료)
- **3D 전통**: **Blender** (무료 완결판), ZBrush (스컬프팅 $40/월), Substance Painter/Designer (PBR)
- **2D AI**: **Scenario** (게임 전용), Leonardo AI, **BRIA** (100% 라이선스 데이터 = 저작권 안전)
- **3D AI**: **Tripo** (캐릭터 쿼드 토폴로지 + 자동 리깅), **Meshy** (배경 소품 30-60초), **Luma Genie**, **Rodin** (고품질)
- **리깅/모션**: **Mixamo** (무료 자동 리깅), **Move AI Gen 2** (스마트폰 2-6대), **DeepMotion**, **Cascadeur** (AI physics-accurate)
- **2D 스켈레탈**: Spine (표준), Moho (저예산 대안), Adobe Animate
- **스타일 선택**: **Low-poly 또는 Stylized** 우선 (1인 효율 + AI 생성 성공률)

### 오디오 파이프라인
- **음악**: **Soundraw** (루프/BGM), Suno v4 / Udio, AIVA, 전통 DAW (FL Studio/Ableton)
- **SFX**: **Lami.ai** (Text-to-SFX), **Sononym** (음향 특성 기반 검색), Freesound (CC0), Audacity/Reaper
- **보이스**: ElevenLabs (75ms 초저지연), **한국어**: Typecast / Naver Clova Voice
- **Unity 오디오**: AudioMixer + Snapshot, Audio Random Container, Audio Spatializer (3D)
- **미들웨어**: FMOD (인디 무료 티어 연 50만$ 미만), Wwise (AAA)
- **품질**: LUFS **-16** (게임 표준), Peak Limiter -1~-3dB 헤드룸, Vorbis 압축

### QA
- **Modl:test / Modl:play** — AI 봇 자동화 QA (1인 취약점 보완)

### Steam 통합
- **Steamworks.NET** (가장 널리 쓰이는 C# 래퍼) — `SteamAPI.Init()` 부트 스트랩
- Auto-Cloud (코드 없이 클라우드 세이브)
- SteamPipe 비밀번호 보호 베타 브랜치

## 대표님 + 나베랄 감마 다음 액션 (Phase 1 진입)

1. **장르 구체화**: 로그라이크/시뮬/RPG 중 **MVP 방향 1개 확정** (로그라이크가 1인 적합도 최상 — Balatro 사례)
2. **CLAUDE.md 에 AI 스코프 통제 규칙 보강** — 현재 `CLAUDE.md` 의 금기/필수 항목에 "AI Slop 차단 규칙" 추가 후보
3. **Unity 6 LTS 설치 + 레트로(retr0) 채널 선행 학습 계획**
4. **Steamworks Partner 등록 준비** — 영문 주소/이름, SWIFT 외화 통장, W-8BEN 사전 작성
5. **시간 배분 결정** (개발 40% / 아트 30% / 폴리싱 15% / 마케팅·관리 15% 외부 지식 권장)
6. **Phase 2 Domain Definition** 진입 — `.planning/ROADMAP.md` 작성 + MVP 1-page 컨셉

## 소스 grounding 진단

각 쿼리마다 NotebookLM 이 정직하게 **"소스 외부 지식"** 표기:
- 소스 자료 강한 영역: AI 도구 체인 (Ziva, Claude Code, Scenario, Leonardo, BRIA, Tripo, Meshy, Mixamo, Move AI, Soundraw, Lami.ai, Sononym, Modl 등), Unity 6 신기능, 게임 디자인 유튜버
- 소스 외부 지식 영역: 30초·3분·30분 루프 이론, 한국 세법, Steam 위시리스트 알고리즘 임계치, LUFS 정규화 수치

→ 노트북 소스는 **AI 도구 체인 / Unity 6 기술 / 커뮤니티** 영역에 특히 풍부.
Steam 비즈니스 / 한국 법률 / 게임 디자인 순수 이론 은 외부 지식 보완 필요.

---

*원본 답변 파일 57,609자 전부 보존. 이 요약은 네비게이션 인덱스 + 박제 키워드만 추출.*
