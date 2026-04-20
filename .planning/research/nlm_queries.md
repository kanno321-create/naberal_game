---
date: 2026-04-20
notebook_id: a0bb9e88-b8cc-4a8d-a55a-75ffa01996eb
purpose: 초보 1인 인디 게임 개발자 + 나베랄 감마 AI 공동 학습 (Unity 6 + Steam + AI 도구 체인)
method: NotebookLM source-grounded deep research (6 분할 쿼리, D-6 single-string)
pacing: 쿼리 timeout 420s (7분), 사이 10s sleep, 총 예상 30-40분
---

# NotebookLM Deep Research — 초보 1인 게임 개발자 전 영역 온보딩

## 배경

대표님이 지정하신 NotebookLM 노트북 (`a0bb9e88-b8cc-4a8d-a55a-75ffa01996eb`) 의 소스 자료를 근거로, Unity 6 LTS + Steam PC 출시 목표 12~24개월 장기 창작을 위한 **전체 지식 영역** 을 획득합니다.

대표님 추가 지시 (2026-04-20):
- 유니티 사용 전반 포괄
- AI 3D (게임 적용)
- 게임 아트 관련 툴 + 관련 AI 전부
- "너무 빡빡하게 하지 말 것 + 15분까지 필요없다" → 6 분할, 각 timeout 420s (7분), 사이 10s

## D-6 single-string 규율

`scripts/notebooklm/query.py:query_notebook()` 이 각 쿼리를 argv 로 1회 전달.
쿼리 내부 newline 없이 단일 문자열 (문장 간 공백 연결).

## 쿼리 분할 (6)

| # | 영역 | 주제 | timeout |
|---|------|------|---------|
| 1 | 인디 현실 + MVP + 디자인 원칙 | 1인 성공 공식, MVP 3-tier, Flow/Juice/Risk-Reward, 장르별 공식 | 420s |
| 2 | Unity 6 전부 | 학습 로드맵 + 스크립팅 + 비주얼 + 퍼포먼스·빌드 | 420s |
| 3 | 게임 아트 (전통 툴 + AI) | 2D/3D 툴 + AI 아트 2026 생태계 전체 + 리깅/애니 AI | 420s |
| 4 | 게임 오디오 | 음악/SFX/보이스/미들웨어/한국어 TTS | 420s |
| 5 | Steam + 마케팅 + 한국 인디 | Steamworks SDK, 페이지, 위시리스트, Next Fest, 인플루언서 | 420s |
| 6 | 관리/멘털 + 법률(한국) + AI 2026 | 장기 페이스, 사업자 등록, 세금, AI 페어 프로그래밍 | 420s |

## 쿼리 #1 — 인디 현실 + MVP + 게임 디자인 원칙

저는 Unity 6 LTS + Steam PC 플랫폼을 목표로 하는 한국의 완전 초보 1인 인디 게임 개발자입니다. 장르는 로그라이크/시뮬레이션/RPG 방향 복합 게임플레이이며 12~24개월 장기 창작을 계획하고 있습니다. Claude Code, Nano Banana Pro, Suno, ElevenLabs 같은 AI 도구를 적극 활용할 예정이며 Balatro, Animal Well, Vampire Survivors 같은 1인 성공 사례를 참고합니다. 이 노트북의 소스 자료에 근거하여 다음 3개 영역에 대해 구체적이고 실행 가능한 답변을 한국어 정중 존댓말로 작성해 주십시오. 각 항목마다 출처(소스 파일명/페이지)를 인용하고 즉시 실행 가능한 팁을 5개 이상 포함해 주십시오. 답변 길이 제한은 없으니 소스가 허락하는 한 상세하게 작성해 주십시오. (1) 1인 인디 게임 개발의 현실 — 성공 확률 통계, 흔한 실패 패턴, Balatro/Animal Well/Vampire Survivors 공통 성공 요인, 초보가 빠지기 쉬운 함정, 한국 인디 시장 특수 상황. (2) MVP 설계와 스코프 관리 — 핵심 루프 30초·3분·30분 3-tier 개념 상세, MVP 정의 방법, 스코프 블로트 방지 체크리스트, Feature Creep 조기 감지 신호, MVP→수직 슬라이스→출시 진화 경로. (3) 게임 디자인 원칙 — 핵심 루프 설계 이론(Flow Theory, Juice, Risk/Reward, Meaningful Choice), 로그라이크/시뮬레이션/RPG 각 장르의 디자인 공식과 차이점, 하이브리드 장르 사례(Slay the Spire, Into the Breach, Hades) 분석, 플레이어 경험 최적화 기법, 초보가 장르 선택 시 고려할 기준.

## 쿼리 #2 — Unity 6 LTS 전부 (학습 로드맵 + 스크립팅 + 비주얼 + 퍼포먼스)

저는 Unity 6 LTS + Steam PC 솔로 인디 개발자이며 C# 중급 수준이지만 Unity 는 완전 초보입니다. 이 노트북의 소스 자료에 근거하여 Unity 6 LTS 전반에 대해 구체적이고 실행 가능한 답변을 한국어 정중 존댓말로 작성해 주십시오. 출처 인용 필수, 각 항목마다 실행 가능한 팁 5개 이상, 답변 길이 제한 없이 상세하게 작성해 주십시오. 다루어야 할 주제는 다음과 같습니다. (A) Unity 6 LTS 단계별 학습 로드맵 — 초보에서 중급, 고급까지 순서, 반드시 완주해야 할 튜토리얼/강의/도서 추천, 학습 시 피해야 할 초보 실수 Top 10, 한국어 학습 자료 리스트. (B) C# 게임 프로그래밍 핵심 패턴 — ScriptableObject 기반 데이터 아키텍처, Event Bus/UnityEvent, State Machine 구현, Addressables 에셋 관리, Input System(새 버전), Coroutine vs async/await, Object Pooling. (C) Unity 6 비주얼 시스템 — URP 대 HDRP 선택 기준과 2D/3D 인디 게임 권장, Shader Graph 기초, 라이팅(Light Baking/Reflection Probe/GI), 포스트프로세싱(Volume/Bloom/Color Grading), VFX Graph, 2D Lights. (D) Unity 6 애니메이션 — Animator State Machine, Animation Timeline, Cinemachine, 2D Skeletal Animation(Sprite Rigging), 3D 임포트 설정. (E) Unity 6 퍼포먼스와 빌드 — Profiler 활용법, GC Alloc 최소화, Mesh LOD, Texture Streaming, Build Settings 및 PC Standalone 빌드, Steam 배포용 설정, IL2CPP 전환. (F) Unity 6 최신 기능 — 2024-2026 업데이트 중 인디에게 중요한 신기능.

## 쿼리 #3 — 게임 아트 종합 (2D/3D 전통 툴 + AI 아트 2026 + 리깅/애니 AI)

저는 Unity 6 + Steam 솔로 인디 개발자이며 게임 아트 제작에 AI 도구 체인을 적극 활용하려 합니다. 이 노트북의 소스 자료에 근거하여 2026년 현재 게임 아트 전 영역에 대해 구체적이고 실행 가능한 답변을 한국어 정중 존댓말로 작성해 주십시오. 출처 인용 필수, 각 항목마다 실행 가능한 팁 5개 이상, 답변 길이 제한 없이 상세하게 작성해 주십시오. 다루어야 할 영역은 다음과 같습니다. (A) 2D 전통 툴 — Aseprite(픽셀아트), Adobe Photoshop, Krita, Procreate, Clip Studio Paint 각각의 강점·약점·인디 적합도, 스프라이트 아틀라스·애니메이션·UI 제작 워크플로우. (B) 3D 전통 툴 — Blender(오픈소스 완결판), Autodesk Maya, ZBrush(스컬프팅), Substance 3D Painter·Designer(머티리얼), 3D 모델링→리토폴로지→UV→베이킹→텍스처링 파이프라인. (C) 2D AI 아트 2026 생태계 — Midjourney V7, Nano Banana Pro(Gemini 3 Pro Image, 한국어 텍스트 94% 정확도), StableDiffusion XL, Flux, Ideogram, Leonardo AI, Scenario(게임 에셋 전용), PromeAI, ControlNet(자세·구도 제어), LoRA 훈련(자체 스타일), 업스케일링 도구(Topaz Gigapixel, Magnific). (D) 3D AI 아트 2026 생태계 (게임 적용) — Meshy 4(text/image-to-3D), Tripo, Luma AI Genie, CSM(Common Sense Machines), Rodin, Unity Muse 3D, StableDiffusion 3D, 게임 임포트 가능한 포맷(FBX/GLB), 리토폴로지 자동화. (E) 리깅·애니메이션 AI — Mixamo(자동 리깅), Anything World, DeepMotion(비디오→모션), Move AI, Plask, 캐릭터 컨트롤러 통합. (F) 2D 스켈레탈 애니 툴 — Spine, DragonBones, Adobe Animate, Unity 2D Animation 패키지. (G) 아트 스타일 선택 전략 — Pixel/Vector/3D Low-poly/Abstract/Handpainted 각각의 제작 난이도와 1인 인디 적합도, 선택 기준. (H) AI 생성 에셋 저작권 이슈 — 2026년 현재 판례, 학습 데이터 출처 이슈, Steam 정책, 안전한 워크플로우.

## 쿼리 #4 — 게임 오디오 종합 (음악 + SFX + 보이스 + 미들웨어 + LUFS)

저는 Unity 6 + Steam 솔로 인디 개발자이며 게임 오디오도 AI 도구와 전통 툴을 혼합해 제작합니다. 이 노트북의 소스 자료에 근거하여 게임 오디오 전 영역에 대해 구체적이고 실행 가능한 답변을 한국어 정중 존댓말로 작성해 주십시오. 출처 인용 필수, 각 항목마다 실행 가능한 팁 5개 이상, 답변 길이 제한 없이 상세하게 작성해 주십시오. 다룰 주제는 다음과 같습니다. (A) 게임 음악 제작 — Suno v4(최신 프롬프트 기법), Udio, AIVA, Mubert, 전통 DAW(FL Studio/Ableton/Logic/Cubase), 장르별 음악 제작(로그라이크/시뮬/RPG), 루프 음악 처리, 다이나믹 뮤직(Adaptive/Interactive). (B) SFX 제작 — ElevenLabs Sound Effects, Freesound(CC 라이선스), 녹음·편집 도구(Audacity/Reaper/Audition), Foley 기법, 피드백 사운드 원칙(Juice). (C) 보이스·TTS — 한국어 TTS 시장(Typecast, ElevenLabs Multilingual v3, Supertone, Naver Clova Voice) 비교, 상업 사용권 조건, 성우 섭외 대안, 내레이션·NPC 보이스·감정 표현. (D) Unity 오디오 엔진 — AudioMixer 그룹 설계, AudioSource/AudioListener, 3D 사운드, Audio Spatializer. (E) 오디오 미들웨어 — FMOD Studio(인디 무료 티어 조건), Wwise, Unity 기본 AudioMixer 각각의 적합 케이스, 통합 방법. (F) 오디오 품질·믹싱 — LUFS -16 정규화(게임 표준), 헤드룸 관리, 라우드니스 전쟁, 마스터링 기본, 오디오 압축 포맷(WAV/OGG/MP3). (G) 출시 직전 오디오 체크리스트 — 플랫폼별 오디오 검증, 소음 제거, 음량 밸런스.

## 쿼리 #5 — Steam 출시 + 마케팅 + 한국 인디 씬

저는 Unity 6 + Steam PC 솔로 인디 개발자이며 12~24개월 후 첫 Steam 정식 출시를 목표로 합니다. 이 노트북의 소스 자료에 근거하여 Steam 출시·마케팅 전 영역에 대해 구체적이고 실행 가능한 답변을 한국어 정중 존댓말로 작성해 주십시오. 출처 인용 필수, 각 항목마다 실행 가능한 팁 5개 이상, 답변 길이 제한 없이 상세하게 작성해 주십시오. 다룰 주제는 다음과 같습니다. (A) Steamworks Partner 등록 전 과정 — 필요 서류, $100 수수료 결제, 한국 개발자 특수 처리(해외 결제·세금 양식), 심사 기간, 페이지 생성 권한 획득. (B) Steamworks SDK 통합 기초 — Steamworks.NET(C# 래퍼), Achievements·Cloud Save·Leaderboard·Workshop 구현 기초, 테스트 환경 설정. (C) Steam 페이지 4요소 최적화 — 트레일러 제작 공식(길이·구조·훅), 스크린샷 5-10장 선택 기준, 설명문(단문·장문) 작성법, 태그 전략(20개 최적화), 헤더 이미지·카드 이미지 제작. (D) 위시리스트 축적 전략 — 페이지 오픈 시점(출시 6-12개월 전), 달성 임계치(1만/5만/10만), 캠페인·페스티벌 활용, Steam 알고리즘 이해. (E) Steam Next Fest — 참가 조건, 데모 범위(20-60분), 데모 기간 활용 극대화. (F) 가격·할인 전략 — 장르별 권장 가격대, 지역별 가격 차등(한국·중국·남미), 출시 할인, 세일 캘린더(여름·가을·겨울). (G) Early Access 대 정식 출시 — 판단 기준, EA 가격 전략(Balatro·Vampire Survivors 사례), EA→정식 전환 타이밍. (H) 마케팅·커뮤니티 — Twitter/X·Discord·Reddit·TikTok·YouTube 각각의 활용법, 개발 로그 운영 패턴(주기·형식·플랫폼), 인플루언서·스트리머 컨택 방법·프레스 키 제작, 한국 인디 씬 특수 상황(국내 커뮤니티·BIC·지스타·해외 동시 진출). (I) 출시 후 커뮤니티 유지 — 패치·DLC·이벤트 주기.

## 쿼리 #6 — 프로젝트 관리·멘털 + 법률(한국) + AI 시대 2026 현실

저는 대한민국의 1인 인디 게임 개발자로서 12~24개월 장기 프로젝트를 계획하며 AI 도구를 적극 활용합니다. 이 노트북의 소스 자료에 근거하여 다음 3개 영역에 대해 구체적이고 실행 가능한 답변을 한국어 정중 존댓말로 작성해 주십시오. 출처 인용 필수, 각 항목마다 실행 가능한 팁 5개 이상, 답변 길이 제한 없이 상세하게 작성해 주십시오. (1) 프로젝트 관리와 멘털 — 1년 이상 장기 프로젝트 페이스 관리(주간·월간·분기 마일스톤 설계), 번아웃 방지 전략(시간 박스·휴식·취미), 시간 배분(개발 대 아트 대 오디오 대 마케팅 대 관리), 1인 개발자 멘털 함정(Perfectionism·Comparison·Isolation·Impostor Syndrome) 극복법, 동기부여 유지 기법(공개 빌드·커뮤니티·작은 성공 축적), 중도 포기를 막는 심리적·구조적 장치. (2) 법률·비즈니스 (한국 기준) — 1인·개인사업자 등록 절차(온라인 홈택스), 간이과세자 대 일반과세자 판단, Steam 수익 정산(해외 송금·원천세 처리·부가세 환급), 저작권·상표권 등록(게임 이름·로고·음악·캐릭터 보호, 한국·해외 동시 출원), AI 생성물 저작권 이슈(2026년 현재 한국·미국 판례), 한국 인디 개발자에게 적용되는 주요 법적 리스크, 계약·NDA 기초(파트너·외주 계약서 필수 조항). (3) AI 시대 1인 개발자 2026 현실 — Claude Code·Cursor·Copilot 같은 AI 페어 프로그래밍 실용 활용법과 한계(어디서 쓰고 어디서 안 쓰나), AI 아트·오디오·3D 자동화의 한계와 경계선(AI 대 사람 필수 영역), 1인이 커버 가능한 작업 범위 확장 정도(2024 대 2026 비교), AI 로 대체 불가한 창의 영역(게임 느낌·플레이어 경험·스토리텔링·게임 디자인 센스·커뮤니티 관계), AI 오남용 시 흔한 실패 패턴과 그 방지책.

## 실행

`scripts/notebooklm/run_deep_research.py` 가 위 6개 쿼리를 `query_notebook()` 으로 순차 호출, 각 응답을 별도 파일로 저장. 쿼리 사이 10초 sleep, timeout 420s.

결과 파일 경로: `.planning/research/nlm_result_0{1..6}_*.md`

박제:
- `.claude/memory/reference_beginner_gamedev_knowledge.md` — 핵심 인덱스
- 각 `wiki/<category>/MOC.md` 의 `Planned Nodes` 갱신 + 새 노드 생성
