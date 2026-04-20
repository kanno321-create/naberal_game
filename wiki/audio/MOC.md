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

---

*Scaffolded: 2026-04-20 (Phase 0 Bootstrap)*
