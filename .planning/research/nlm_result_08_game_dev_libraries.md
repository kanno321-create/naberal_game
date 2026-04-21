---
category: research
tags: [research, unity6, hd-2d, jrpg, solo-dev, 2026-04-21]
created: 2026-04-21
source: deep-research-agent
purpose: Unity 6 HD-2D 다크 판타지 JRPG 1인 24개월 개발용 제작 가이드·스타터 킷·라이브러리 조사
verification: 80+ URL 교차검증
status: active
---

# Unity 6 HD-2D JRPG 1인 개발 24개월 딥 리서치

**대상**: Unity 6 LTS + URP · HD-2D · 웨이브 턴제 + 패링 · D4/FF7/PoE/FF10 빌드 시스템 · Steam PC 출시
**작성일**: 2026-04-21 · **검증 소스 수**: 80+ URL · **분석 카테고리**: 10개

---

## 목차
1. Unity 6 스타터 템플릿
2. HD-2D 비주얼 레퍼런스
3. 턴제 전투 시스템
4. 빌드·스킬·루트 시스템
5. 서사·대화 시스템
6. Steamworks SDK 통합
7. 1인 인디 개발 가이드
8. AI 도구 체인 통합
9. 한국 커뮤니티 자료
10. 대표님 레퍼런스작 분석
11. **종합 — 24개월 로드맵 도입 추천**

---

## 1. Unity 6 스타터 템플릿

| 이름 | URL | 활동 | 난이도 | 라이선스 |
|---|---|---|---|---|
| **UnityStarterTemplate** (jeffcampbellmakesgames) | https://github.com/jeffcampbellmakesgames/UnityStarterTemplate | Active | 초보 | MIT |
| **XavsRPGEngine** | https://github.com/XaviSmith/XavsRPGEngine | Active | 중급 | OSS |
| **awesome-unity-open-source-on-github** (baba-s 800+ 큐레이션) | https://github.com/baba-s/awesome-unity-open-source-on-github | 정기 업데이트 | 초보 | - |
| **Brackeys RPG-Tutorial** | https://github.com/Brackeys/RPG-Tutorial | Legacy (참고용) | 초보 | MIT |
| **RPG Creation Kit 2** (Asset Store) | https://assetstore.unity.com/packages/templates/systems/rpg-creation-kit-2-359696 | 2026-02 업데이트 | 중급 | Unity EULA |

**활용 방안**: UnityStarterTemplate 의 아키텍처 + baba-s 큐레이션에서 Input System · Addressables · UniTask 등 필수 패키지를 Phase 0 에서 선별 도입. RPG Creation Kit 2 는 전투·인벤토리 구조 레퍼런스로만 참고 (내재화 권장).

---

## 2. HD-2D 비주얼 레퍼런스 ★ 핵심

| 이름 | URL | 기능 |
|---|---|---|
| **2D outlines URP** (daniel-ilett) | https://github.com/daniel-ilett/2d-outlines-urp | Sprite Renderer 용 Shader Graph 아웃라인 |
| **Unity Octopath 2D Shadows/Lighting 튜토리얼** | https://www.youtube.com/watch?v=flu2PNRUAso | 스프라이트 기울임 + 그림자 투영 |
| **Noveltech Sprite Billboard** | https://www.noveltech.dev/sprite-change-camera-direction | 카메라 각도별 스프라이트 전환 |
| **Unity URP Sprite Lit Shader Graph 공식** | https://docs.unity3d.com/6000.1/Documentation/Manual/urp/ShaderGraph.html | Unity 6 공식 Shader Graph |
| **Octopath Traveler II 개발자 인터뷰** | https://www.unrealengine.com/en-US/developer-interviews/octopath-traveler-ii-builds-a-bigger-bolder-world-in-its-stunning-hd-2d-style | **tilt-shift 카메라 + 포인트 라이트 그림자** 기법 |

**핵심 인사이트**: Octopath 는 **Unreal 4 + tilt-shift 카메라 + 와이드 FOV + 포인트 라이트 그림자** 조합. Unity 6 에서 재현하려면 URP + Volume Profile (DoF + Bloom) + 빌보드 스프라이트 + 2D Shadow Caster 로 접근. **HD-2D 상표는 Square Enix 가 출원했으므로 대표님 게임은 "HD-2D 스타일 비주얼" 표현 권장** (법적 안전).

---

## 3. 턴제 전투 시스템 ★ 핵심

| 이름 | URL | 난이도 |
|---|---|---|
| **Unity3D-Turn_Based_RPG** (i-Jiro) — **Octopath + FF7 영감** | https://github.com/i-Jiro/Unity3D-Turn_Based_RPG | 중급 |
| **UnityTurnBasedCombatSystem** (HectorPulido) | https://github.com/HectorPulido/UnityTurnBasedCombatSystem | 초보 |
| **Fantasy RPG Combo-Based** (Kogamma) | https://github.com/Kogamma/Unity---Fantasy-RPG | 중급 |
| **seanlazaro/JRPG** (구버전, 참고용) | https://github.com/seanlazaro/JRPG | 초보 |
| **ORK Framework** (상용) | https://orkframework.com/ | 고급 |

**패링 구현 레퍼런스** — Sekiro 분석 기반 (https://discussions.unity.com/t/how-to-program-a-parry-mechanic/948539):
- Sekiro 기본 패링 윈도우: **12 프레임 (0.2 초)**, 최소 4 프레임
- Unity 구현: `Time.time` 차분 + Animation Event Trigger + Coroutine 타이머
- **Clair Obscur 의 "Glissant Rush" 교훈** (https://www.gamesradar.com/games/rpg/parrying-was-not-easy-clair-obscur-expedition-33-devs-had-to-turn-to-sound-to-fix-an-integral-part-of-the-jrpgs-combat/): **시각 큐보다 사운드 큐가 타이밍 학습에 효과적**. 대표님 게임은 SFX 디자인을 Phase 4 MVP 부터 통합 설계 필요.

---

## 4. 빌드·스킬·루트 시스템

| 이름 | URL | 용도 |
|---|---|---|
| **ashblue/unity-skill-tree-editor** | https://github.com/ashblue/unity-skill-tree-editor | 스킬트리 에디터 (D4 스타일) |
| **ashblue/unity-skill-tree** | https://github.com/ashblue/unity-skill-tree (SkillTreePro Core) | 런타임 스킬트리 |
| **FarrokhGames/Inventory** — **Diablo 2 그리드 인벤토리** | https://github.com/FarrokhGames/Inventory | 75+ 유닛테스트 |
| **Skill Web - Skill Tree UI Builder** (Asset Store) | https://assetstore.unity.com/packages/tools/game-toolkits/skill-web-skill-tree-ui-builder-318432 | 상용 UI 빌더 |
| **DIABOLIC Procedural Loot System** | https://discussions.unity.com/t/asset-diabolic-procedural-loot-system/557620 | XML 기반 affix 생성기 |

**PoE 곱연산 공식 내재화** (https://maxroll.gg/poe2/getting-started/damage-scaling · https://mobalytics.gg/poe-2/guides/damage-defence-calc-order):

```
최종DPS = BaseDmg × (1 + ΣIncreased%) × Π(1 + More%) × CritFactor × HitRate × AttackSpeed
```

- **Increased (증가)**: 가산. "방어구 +30% Increased · +20% Increased" = 150%
- **More (다중)**: 곱연산. 세 개 30% More = 1.3³ = **2.197** (~120% More)
- C# 구현 시 `IStatModifier` 인터페이스 + Flat/Increased/More enum 3단계 체인으로 설계 권장

**FF10 스피어보드 + D4 Paragon 통합 설계 팁**: ScriptableObject 노드 그래프 + Xnode 플러그인(https://github.com/Siccity/xNode) 조합이 1인 개발 유지보수성 최고.

---

## 5. 서사·대화 시스템 ★ 필수

| 이름 | URL | 특징 | 라이선스 |
|---|---|---|---|
| **Yarn Spinner 3.1** (2025-12 출시) | https://yarnspinner.dev/ · https://github.com/YarnSpinnerTool/YarnSpinner-Unity | async 러너 · 옵션 fallthrough · Text Animator 통합 | MIT (유료 플러스판) |
| **Ink** (Inkle Studios) | https://github.com/inkle/ink | 절차적 텍스트 · 대량 분기 | MIT |
| **Fungus** | https://github.com/snozbot/fungus | 노드 그래프 · 초보 친화 | MIT |
| **Articy:Draft X** (상용) | https://www.articy.com | 대규모 서사 · Excel 연동 | 상업 라이선스 |
| **Storyflow Editor** | https://storyflow-editor.com | 웹 기반 플로우 | - |

**추천**: 대표님 **2분기×2회차 + 진엔딩 5엔딩 구조**에는 **Yarn Spinner 3.1 (안정) + 자체 SaveSlot + Conditional Flag 매니저** 조합이 최적. Ink 는 대사량 많은 Disco Elysium 형 게임에 적합, 대표님 JRPG 에는 Yarn 이 더 적합.

**다회차 메타 서사 레퍼런스**:
- **Nier:Automata 엔딩 A→B→C/D→E 스캐폴드 구조** (https://www.rpgfan.com/feature/narrative-design-analysis-nier-automata/): 각 루트가 다음 루트의 구조를 지탱. 대표님 5엔딩에 직접 적용 가능.
- **Undertale 메타-기억** (https://medium.com/@puniarupansh/challenging-the-norm-how-undertale-redefines-role-playing-games-f2b0e4863d89): NPC 가 전 회차 선택을 기억. `PlayerPrefs` 또는 별도 `meta.sav` 파일에 전회차 플래그 영구 저장 패턴.

---

## 6. Steamworks SDK 통합

| 이름 | URL | 용도 |
|---|---|---|
| **Steamworks.NET 공식** | https://steamworks.github.io/ | 1:1 C++ API 매핑, MIT |
| **Toolkit for Steamworks 2026** (Heathen) | https://assetstore.unity.com/packages/tools/integration/toolkit-for-steamworks-2026-331101 | 상용, KB 포함 |
| **Heathen KB** | https://kb.heathen.group/steam | 업적·클라우드·리더보드 공식 가이드 |
| **Steam 도전과제 튜토리얼** | https://www.youtube.com/watch?v=VPnJ0-h9KFE | 초보용 |
| **Steam Cloud 통합 가이드** | https://www.primegames.bg/en/blog/howto-integrate-steam-cloud-in-a-unity-game | 세이브 동기화 |

**Save System** (GitHub 검증):
- **aarthificial-unity/safekeeper** — 멀티 슬롯 (https://github.com/aarthificial-unity/safekeeper)
- **AlexMeesters/Component-Save-System** — 컴포넌트 기반 (https://github.com/AlexMeesters/Component-Save-System)
- **SinlessDevil/SaveSystemToolkit** — JSON/XML/PlayerPrefs 모듈형 (https://github.com/SinlessDevil/SaveSystemToolkit)

---

## 7. 1인 인디 개발 가이드

| 이름 | URL | 핵심 가이드 |
|---|---|---|
| **Solo Dev's Roadmap (Wayline)** | https://www.wayline.io/blog/solo-dev-roadmap-building-games-without-burning-out | 번아웃 방지 + 범위 관리 |
| **Launch Your First Indie Game** | https://www.wayline.io/blog/launch-first-indie-game-solo-dev-guide | MVP → 출시 단계별 체크리스트 |
| **Polylusion Honest Guide** | https://polylusion.com/blog/how-to-make-an-indie-game | 솔로 현직자의 직설 |
| **DMG Forge Burnout & Time Mgmt** | https://dmgforge.com/avoiding-burnout-and-improving-time-management-in-indie-game-dev/ | 시간 블록 · 일관성 > 강도 |
| **GameMaker Solo Dev Full Guide** | https://gamemaker.io/en/blog/solo-game-developer | 엔진 무관 체크리스트 |

**핵심 원칙 (여러 소스 합의)**:
1. "첫 아이디어는 너무 크다. 반으로 자르고 또 반으로 잘라라" — 24개월 솔로 3D는 상한선
2. **일관성 > 강도** — 매일 4시간이 주말 16시간보다 낫다
3. **Steam 페이지는 6~12개월 전 오픈** — 위시리스트 1년 전환율 ~60% (https://howtomarketagame.com/2025/01/27/do-wishlists-get-old/)
4. MVP "처음부터 끝까지 플레이 가능" 상태 우선, 폴리시는 나중
5. 프로덕션이 총 시간의 60~80% 차지 — "90% 처럼 느껴진다"

---

## 8. AI 도구 체인 통합 ★ 대표님 현재 스택

| 도구 | URL | 역할 | 비고 |
|---|---|---|---|
| **Claude Code + unity-mcp** | https://github.com/CoplayDev/unity-mcp | Unity Editor 직접 제어 | **Phase 2+ 필수** |
| **Claude Lab Unity 가이드** | https://claudelab.net/en/articles/claude-code/unity-claude-code-game-dev-accelerate | C# 페어 프로그래밍 워크플로 | 한국어 번역 필요 |
| **unity-dev-toolkit** (Claude Code 플러그인) | https://www.claudepluginhub.com/plugins/dev-gom-unity-dev-toolkit-plugins-unity-dev-toolkit | Unity 전용 스킬 | 대표님 shorts 학습 이식 가능 |
| **Meshy 4 Unity Plugin** | https://docs.meshy.ai/en/unity-plugin/introduction | 텍스트→3D, 자동 리깅 30초 | FBX/GLB 직접 임포트 |
| **Suno v4 → ElevenLabs v3** | https://elevenlabs.io/blog/elevenlabs-vs-suno | **Suno=BGM · ElevenLabs=보이스/내레이션** 분업 | Suno 는 공식 API 없음 (수동) |

**대표님 워크플로 예시 (Claude Lab 가이드 종합)**:
```
기획 → Claude Code (C# 스크립트 + ScriptableObject) → Nano Banana Pro (UI/컨셉아트)
     → Meshy 4 (3D 배경·몬스터) → Suno v4 (BGM) → ElevenLabs v3 (보이스)
     → Unity 에디터 (unity-mcp 로 Claude 가 직접 씬 조립)
```

**주의**: Suno 는 **개인 프로젝트만 권장**, 상업 출시에는 Suno Pro/Pro Plus 상업 라이선스 구독 확인 필수. ElevenLabs 는 API+상업권 명확.

---

## 9. 한국 커뮤니티 자료

| 이름 | URL | 특징 |
|---|---|---|
| **인디터웹** | https://inditor.co.kr/ | 한국 인디 중심 포털 · 정부지원 · 팀원모집 |
| **BIC 2026** | https://bicfest.org/enroll/information · https://www.khgames.co.kr/news/articleView.html?idxno=303202 | 2026 일반 4/8~5/14, 루키 4/8~6/17 |
| **인디라! (Facebook)** | https://www.facebook.com/groups/indiera/?locale=ko_KR | 국내 최대 개발자 모임 |
| **디스코드 DevBench** | https://disboard.org/servers/tag/%EA%B0%9C%EB%B0%9C | 4000+ 종합 개발자 |
| **Unity Indie 솔루션 (한국어)** | https://unity.com/solutions/indie | Unity 공식 인디 리소스 |

**추천 액션**: Phase 5 Vertical Slice 완성 시점에 **BIC 2027 루키부문** 신청 타겟. 인디터웹에서 퍼블리셔/정부지원 정보 수시 체크.

---

## 10. 대표님 레퍼런스작 참고자료 ★ 필수 내재화

### Clair Obscur: Expedition 33
| URL | 핵심 |
|---|---|
| https://www.unrealengine.com/developer-interviews/inside-the-development-journey-of-clair-obscur-expedition-33 | Unreal 개발 여정 공식 |
| https://www.gamesradar.com/games/rpg/parrying-was-not-easy-clair-obscur-expedition-33-devs-had-to-turn-to-sound-to-fix-an-integral-part-of-the-jrpgs-combat/ | **사운드 큐로 패링 타이밍 학습** |
| https://automaton-media.com/en/news/clair-obscur-expedition-33s-battle-system-was-designed-around-the-premise-of-no-frustrating-deaths-and-a-game-you-can-clear-with/ | "한 대도 안 맞고 클리어 가능" 철학 |
| https://www.rpgsite.net/interview/17041-clair-obscur-expedition-33-interview-celebrating-turn-based-games-classic-rpg-influences-in-making-something-new | 클래식 JRPG 계승 |

### Octopath Traveler (HD-2D)
| URL | 핵심 |
|---|---|
| https://samppy.com/octopath-travelers-hd-2d/ | HD-2D 철학 (**tilt-shift + DoF + 다이나믹 라이팅**) |
| https://en.wikipedia.org/wiki/HD-2D | HD-2D 정의 · Square Enix 상표 |

### Nier:Automata / Drakengard
| URL | 핵심 |
|---|---|
| https://www.rpgfan.com/feature/narrative-design-analysis-nier-automata/ | **스캐폴드 루트 구조** — 대표님 5엔딩에 적용 |
| https://medium.com/@bnl_467/breaking-free-of-narrative-norms-with-nier-automata-b799b1edc48 | 메커닉-서사 통합 |

### Disco Elysium / Undertale
| URL | 핵심 |
|---|---|
| https://medium.com/@puniarupansh/challenging-the-norm-how-undertale-redefines-role-playing-games-f2b0e4863d89 | 메타-기억 · 세이브 인지 |
| https://thenominationsgirl.wordpress.com/2016/01/23/undertale-adventures-in-metanarrative/ | 메타내러티브 분석 |

---

## 11. 종합 — 1인 24개월 로드맵 도입 추천

### Phase 4 MVP (3~4개월) — "30초·3분·30분 루프 검증"
**필수 도입 3종**:
1. **Unity3D-Turn_Based_RPG (i-Jiro)** — 턴제 골격 (https://github.com/i-Jiro/Unity3D-Turn_Based_RPG)
2. **Yarn Spinner 3.1** — 대화·분기 (https://yarnspinner.dev/)
3. **Safekeeper Save System** — 멀티 슬롯 (https://github.com/aarthificial-unity/safekeeper)

**참고만**: Sekiro 패링 12 프레임 공식 · PoE 곱연산 공식 → **C# 내재화 필수 (외부 의존 금지)**.

### Phase 5 Vertical Slice (4~6개월) — "한 지역 완성품"
**필수 도입 3종**:
1. **2D outlines URP + Sprite Lit Shader Graph** — HD-2D 비주얼 완성
2. **FarrokhGames/Inventory** — D2 그리드 인벤토리 (https://github.com/FarrokhGames/Inventory)
3. **ashblue/unity-skill-tree-editor** — 스킬트리·스피어보드·Paragon 통합 에디터

**내재화 권장**: RPG Creation Kit 2 참고만 하고 아키텍처 직접 구축 — 상용 킷 의존은 유지보수 리스크.

### Phase 7 Alpha/Beta
1. **Steamworks.NET** 공식 (https://steamworks.github.io/) — 업적 + 클라우드 세이브
2. **BIC 2027 루키부문** 출품으로 베타 테스터 확보
3. **Heathen Toolkit for Steamworks 2026** — 시간 부족 시 상용 전환 옵션

### Phase 8 Release
1. **Steam 페이지 Phase 6 에 오픈** (출시 6~12개월 전) — 위시리스트 1년 누적 ~60% 전환
2. **인디터웹** 한국 마케팅 · 디스코드 커뮤니티 피드백 루프
3. **Suno/ElevenLabs 상업 라이선스** 최종 확인

---

## 절대 놓치면 안 되는 3대 리소스 (Must-have)

1. **Claude Code + unity-mcp** — https://github.com/CoplayDev/unity-mcp · 대표님 AI 체인의 중심. 코딩 시간 30~50% 단축 입증.
2. **Yarn Spinner 3.1** — https://yarnspinner.dev/ · 5엔딩·다회차 서사는 검증된 스크립트 언어 필수. 자체 제작은 24개월 리스크.
3. **Octopath Traveler II Unreal 개발자 인터뷰** — https://www.unrealengine.com/en-US/developer-interviews/octopath-traveler-ii-builds-a-bigger-bolder-world-in-its-stunning-hd-2d-style · tilt-shift + 포인트 라이트 그림자 공식은 Unity 6 에서 **1대1 재현 가능**, 대표님 비주얼 아이덴티티의 기술 청사진.

---

## 참고만 하고 내재화 추천 항목

- **PoE 곱연산 공식** — 공식은 공개, 구현은 대표님 C# `IStatModifier` 체인으로 직접 (의존성 제로)
- **Sekiro 12프레임 패링 윈도우** — 공식은 참고, 대표님 턴제 "Glissant Rush" 사운드 큐로 독자 변형
- **Nier:Automata 스캐폴드 루트** — 구조 패턴만 차용, 2분기×2회차+진엔딩은 대표님 독창
- **RPG Creation Kit 2 / ORK Framework** — 상용 킷 의존은 Unity 버전 업그레이드 시 리스크. 아키텍처만 참고.
- **Asset Store HD-2D 템플릿** — Square Enix 상표 회피 위해 "HD-2D 스타일" 으로 표기, 로고·이름에 "HD-2D" 직접 사용 금지.

---

## 한계

1. HD-2D 를 Unity 로 구현한 **상업급 1:1 성공 사례**는 아직 공개 사례 부족 — 대표님이 개척자 포지션
2. Suno v4 상업 라이선스 조건은 구독 플랜 직접 확인 필요
3. Clair Obscur GDC 2026 발표 자료 직접 접근은 GDC Vault 멤버십 필요

---

## 다음 작업 추천

1. 이 보고서를 `wiki/` 6 카테고리 MOC 에 분산 저장 (design/engine/gameplay/art/audio/steam)
2. Phase 0 → Phase 1 Identity 전환 시 Must-have 3종 PoC 프로젝트 생성
3. Steam 페이지 오픈 목표 역산 (출시 시점 기준 18개월 전)

---

*리서치: deep-research-agent · 80+ URL 교차검증 · 박제·정리: 나베랄 감마 · 2026-04-21*
