---
category: audio
status: scaffold
tags: [moc, game, audio]
updated: 2026-04-20
---

# Audio — Map of Content

> Tier 2 도메인-특화 지식 노드 맵. 오디오 파이프라인 영역.

## Scope

음악·SFX·보이스 제작, AI 오디오 도구 체인 (2026-04 기준: Suno v4, ElevenLabs Multilingual v3), Unity 오디오 엔진 (AudioMixer, FMOD/Wwise 대안), LUFS 정규화.

## Planned Nodes

- [ ] `music_pipeline.md` — Suno v4 프롬프트 규칙 + 게임 음악 loop 처리
- [ ] `sfx_production.md` — AI SFX (ElevenLabs Sound Effects) + 라이브러리 소스 믹스
- [ ] `voice_korean.md` — ElevenLabs 한국어 보이스 + Typecast (shorts 와 공유 가능)
- [ ] `audio_mixer.md` — Unity AudioMixer 그룹 + LUFS -16 정규화
- [ ] `middleware_choice.md` — FMOD vs Wwise vs Unity 기본 AudioMixer 결정

## Related

- **Tier 1**: 향후 Korean TTS 공용 노드 승격 후보 (shorts 의 `voice-producer` 와 공유)
- **Other Tier 2**: [[../gameplay/MOC]] (Juice 사운드), [[../engine/MOC]] (Unity 오디오 구성)

## NotebookLM 딥 리서치 (2026-04-20)

**원본 답변**: [../../.planning/research/nlm_result_04_game_audio.md](../../.planning/research/nlm_result_04_game_audio.md) (20.3KB, 9,665자)

### AI 오디오 2026 (소스 강점)
- **Soundraw.io** — 반복 가능 BGM 루프, 장르별 프로토타이핑 최적
- **Lami.ai** — Text-to-SFX (마법 스킬, 타격음 등)
- **Sononym** — AI 음향 검색 (메타데이터 아닌 "음향적 특성" 기반)
- **ElevenLabs** — 75ms 초저지연 실시간 TTS (지능형 NPC)
- (외부 지식) Suno v4 / Udio — `[Loopable][Seamless][120 BPM][Chiptune]` 태그 필수

### Unity 오디오 엔진 기본
- **Audio Random Container** — 타격음 무작위 (단조로움 방지)
- 압축: BGM/앰비언트 → **Vorbis + Streaming**, 짧은 SFX → **ADPCM + Compressed In Memory**
- **Audio Spatializer** — 3D 위치 기반 사운드
- Low Pass/High Pass/Echo/Reverb Filter 런타임 환경 변화

### 미들웨어 결정 트리
1. **MVP 단계** → Unity 기본 AudioMixer (무거운 미들웨어 통합 X)
2. **복잡 Adaptive 음악 필요** → **FMOD** (인디 무료 연 50만$ 미만) 또는 Wwise
3. 미들웨어 통합 시 AudioSource → **Event Emitter** 컴포넌트 대체

### 한국어 TTS
- **Typecast** — 한국어 감정 연기 (화남/슬픔) 강점
- **Naver Clova Voice** — 한국어 자연성
- **ElevenLabs Multilingual v3** — 다국어 더빙 (동일 목소리 여러 언어)
- (보조) **Voicemod** 변조 → 오크/로봇 보이스 질감

### 품질·믹싱 표준
- **LUFS -16** 라우드니스 정규화 (게임 업계 표준)
- **-1 ~ -3dB** 트루 피크 헤드룸 (Master Limiter)
- 주파수 마스킹: BGM EQ 중대역 낮춰 대사·SFX 선명도 확보
- **Audio Ducking**: NPC 대사 시 BGM 일시 감소

### 출시 직전 오디오 QA
- **Modl:test** AI 봇 — 오디오 트리거 버그 자동 탐지
- Audio Profiler — 동시 재생 Voice count CPU 낭비 체크
- **Zero-crossing 검증** — 루프 음악 시작/끝 동일 → Pop 노이즈 제거
- AI 데이터 출처·상업 사용권 감사 (Audit trails)

### Planned Nodes 상태
- [ ] `music_pipeline.md` — Soundraw/Suno 프롬프트 (nlm_result_04 §A)
- [ ] `sfx_production.md` — Lami.ai + Sononym + Freesound 조합
- [ ] `voice_korean.md` — Typecast/Clova/ElevenLabs 비교
- [ ] `audio_mixer.md` — Unity AudioMixer 그룹 설계
- [ ] `middleware_choice.md` — FMOD vs Wwise 결정 기준

---

*Scaffolded: 2026-04-20 · Updated: 2026-04-21 (NotebookLM 딥 리서치 반영)*
