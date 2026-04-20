---
category: steam
status: scaffold
tags: [moc, game, steam, publishing]
updated: 2026-04-20
---

# Steam — Map of Content

> Tier 2 도메인-특화 지식 노드 맵. Steam 출시 영역.

## Scope

Steamworks API 통합 (Achievements, Cloud Save, Workshop), Steam 페이지 최적화 (위시리스트 축적), Early Access 정책, 출시 체크리스트, 수익 구조 (70/30), 지역별 가격 책정.

## Planned Nodes

- [ ] `release_checklist.md` — Steam 출시 6개월 로드맵 (페이지 오픈 → 위시리스트 → 축제·데모 → 출시)
- [ ] `steamworks_sdk.md` — Steamworks.NET 통합 + Achievements/Cloud Save/Leaderboard
- [ ] `early_access_policy.md` — EA 장단점 + 가격·기간 전략 (Balatro 케이스 연구)
- [ ] `wishlist_optimization.md` — Steam 페이지 4요소 (트레일러/스크린샷/설명/태그) 최적화
- [ ] `pricing_regional.md` — 지역별 가격 책정 + 할인 정책 (Steam 권장가)
- [ ] `next_fest.md` — Steam Next Fest 참가 조건 + 데모 전략

## Related

- **Other Tier 2**: [[../design/MOC]] (장르별 Steam 성공 패턴), [[../gameplay/MOC]] (데모 컷 범위)
- **Root CLAUDE.md**: [[../../CLAUDE.md]] — 필수사항 §5 "Steam 페이지 early open (출시 6개월 전 룰)"

## NotebookLM 딥 리서치 (2026-04-20)

**원본 답변**: [../../.planning/research/nlm_result_05_steam_marketing.md](../../.planning/research/nlm_result_05_steam_marketing.md) (26.6KB, 12,182자 — 두 번째로 풍부)

### Steamworks Partner 등록 (한국 개발자)
- $100 앱 크레딧 (게임 매출 $1,000 돌파 시 환급)
- **W-8BEN / W-8BEN-E** 세금 양식 → 한/미 조세조약 → 원천세 **30% → 10%** 감면
- **Foreign TIN**: 주민등록번호(개인) 또는 사업자등록번호(법인) 기입
- **SWIFT 외화 통장** 사전 개설 (영문 은행명·SWIFT 정확)
- 심사: 신원 확인 최대 7일, 페이지 검수 3-5일
- **출시 쿨타임**: 앱 수수료 결제 후 30일, Coming Soon 공개 후 14일

### Steamworks SDK 통합
- **Steamworks.NET** (C# 래퍼 표준) — 프로젝트 루트에 `steam_appid.txt` 생성
- 부트 씬에서 `SteamAPI.Init()` 호출
- **Achievements**: 더미 ID 알파 단계부터 심기 (`SteamUserStats.SetAchievement("ACH_WIN_ONE_GAME")`)
- **Auto-Cloud** 세이브: 코드 없이 포털 설정만으로 구현
- **SteamPipe** 비밀번호 베타 브랜치 → 라이브 환경 테스트

### Steam 페이지 4요소 최적화
1. **헤더 캡슐** — 로고 크고 명확, 필요 시 Fiverr 외주로 CTR 극대화
2. **트레일러 "5초 훅"** — 스튜디오 로고·긴 시네마틱 금지, 핵심 게임플레이 즉시 노출
3. **스크린샷 5-10장** — 인게임 UI 선명, 전투·인벤토리·건설 루프 가시화
4. **태그 Top 5** — 알고리즘 가중치 최대. "인디/싱글플레이어" 광범위 태그 금지, "로그라이크/콜로니 심/RPG" 구체 서브장르
5. **장문 설명** — GIF 3MB 이하 삽입, 핵심 메커니즘 시각화

### 위시리스트 축적
- **출시 12개월 전** Coming Soon 페이지 오픈 (임시 아트 + 트레일러 1개면 충분)
- **10,000** = "Popular Upcoming" 마법 임계치
- 외부 트래픽 (Reddit r/gamedev·r/IndieGaming, TikTok, YouTube Shorts) → 페이지 전환율
- 테마 페스트 (로그라이크 페스트, 덱빌딩 페스트) 참여
- 모든 외부 CTA 통일: **"스팀 위시리스트 추가하기"**

### Steam Next Fest (일회성!)
- **출시 2-4개월 전** 참가 — 퀄리티 정점일 때
- 데모 **20-45분** — 튜토리얼 → 첫 보스/핵심 빌드 완성
- 데모 메뉴·엔딩 "위시리스트 추가" CTA 강제
- 사전 녹화 영상 **무한 루프 스트리밍**
- Devtodev 분석 → 이탈 구간 역추적 → 본편 수정

### 가격·할인 전략
- 로그라이크/시뮬 솔로 인디: **$14.99 ~ $19.99** 표준
- EA = 정식의 **70-80%**
- Steam 지역별 권장가 수락 (한국·중국·남미 구매력)
- **10-15% Launch Discount** 필수 (찜 목록 이메일 알림 트리거)
- **30일 쿨다운** — 여름/가을/겨울 세일 30일 전 개인 할인 금지

### Early Access 판단
- EA 적합: 로그라이크·뱀파이어 서바이버 스타일 (수평적 콘텐츠 확장)
- **코어 루프 100% 완성 + 볼륨 50-70% 상태**에서 EA 시작 (Balatro 공식)
- EA → 1.0 전환 시 "신규 출시" 탭 재노출 → 제2의 런칭 기회

### 한국 특수 마케팅
- **레딧**: r/gamedev / r/IndieGaming / r/Unity3D — "개발 로그" 영상 (광고 X)
- **디스코드 서버** 플레이테스터 모집
- **카카오톡 오픈채팅** "인디게임 개발", "Unity Korea"
- **BIC 부산 인디 커넥트 페스티벌** · **PlayX4** 출품 (현장 반응 관찰)
- 스트리머: 구독자 **1만-10만** 타겟 + **impress.games 프레스킷**

### 출시 후 유지
- **24-48시간** Day 1 핫픽스 + 스팀 공지
- 부정 리뷰 정중 답변 (다른 유저가 감동)
- 월 1회 Devlog
- 소규모 무료 콘텐츠 패치 (DAU 유지 → 알고리즘 부스트)
- 유료 DLC = 본편의 **20-30%**

### Planned Nodes 상태
- [ ] `release_checklist.md` — 12개월 타임라인 (nlm_result_05 §A)
- [ ] `steamworks_sdk.md` — Steamworks.NET 통합 (§B)
- [ ] `early_access_policy.md` — EA 판단 기준 (§G)
- [ ] `wishlist_optimization.md` — 10,000 달성 전략 (§D)
- [ ] `pricing_regional.md` — 가격 공식 (§F)
- [ ] `next_fest.md` — 참가 전략 (§E)

---

*Scaffolded: 2026-04-20 · Updated: 2026-04-21 (NotebookLM 딥 리서치 반영)*
