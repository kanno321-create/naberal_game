# Memory Index — naberal_game

> 로컬 메모리 인덱스. `.claude/hooks/session_start.py` §6 이 매 세션 전체 주입 + §6.5 가 `priority: critical` 전체 본문 자동 주입.
> 각 메모리는 `name` / `description` / `type` / `priority` 필드 frontmatter 포함 (auto memory 규약).
> **이중 박제 원칙** (`feedback_dual_persistence_required.md`) — 신규 메모리는 본 로컬 경로 + Claude Code 전역 `C:\Users\PC\.claude\projects\c--Users-PC-Desktop-naberal-group-studios-game\memory\` 동시 저장.

## 🔒 Critical (priority: critical · §6.5 자동 주입)
- [이중 박제 원칙](feedback_dual_persistence_required.md) — git 프로젝트 로컬 + Claude Code 전역 양쪽에 동시 저장 강제 · 한쪽만 저장 시 영속성 실패
- [나이트 진정한 Canon (수십 년 분신 정체성)](project_knight_true_canon_2026-04-23.md) — 🔴 **최상위** · 균형의 수호자 · 전우주적 파견 시스템 · 기억 소거/감정 누수 · 각성·도주 · **자발적 수호 지속** · 방랑자 위장 · 자아 붕괴 반복 (세션 #9 · 2026-04-23)
- [나이트 외형·이름 보조 Canon](feedback_knight_canon_locked.md) — ⚠️ 무기·정체 서사는 `project_knight_true_canon_2026-04-23.md` 로 교체 · 본명·친부모·형제·고향 없음 원칙만 유효 (세션 #7 + #9 축소)
- [샘플링 독서 금지](feedback_no_sampling_full_read.md) — Canon 파일 부분 읽기 = FAIL-016 원인 · 전수 읽기 필수

## 📘 Feedback (대표님 지시 · 검증된 접근)
- [Obsidian + NotebookLM 능동 활용](feedback_active_obsidian_notebooklm.md) — 하네스·AI 위키·Obsidian 삼위일체는 나베랄 감마의 능동 호출이 있어야 실현
- [에이전트 원전 필독 강제 + 인용 증명](feedback_agent_context_enforcement.md) — 서브에이전트 spawn 시 STEP 0 필독 7종 + 인용 박제 강제 (세션 #4)
- [에이전트 기본 모델 sonnet 4.6](feedback_agent_model_default_sonnet.md) — 대량 병렬 fan-out 기본 모델 sonnet. `model: sonnet` 파라미터 명시 (세션 #4)
- [억지 이중성·양립 해석 금지](feedback_avoid_forced_duality_readings.md) — 설정 모순 발견 시 AI 자체 "양립 해석" 봉합 금지 · 대표님 결정 큐에 올리기 (세션 #5)
- [브레인스토밍 질문 일괄 제시](feedback_brainstorm_question_batching.md) — 질문은 파일 내 큐에 누적, 대표님 요청 시 일괄 제시 · 흐름 방해 방지 (세션 #2)
- [라이트노벨 스타일 선호](feedback_light_novel_style_preference.md) — 짧은 챕터·대화 중심·1인칭·삽화 전제. 집필·critique·style_bible 우선 적용 (세션 #2)
- [파일명·위치 직관성 + 날짜 표기](feedback_naming_intuitive_dated.md) — `<topic>_YYYY-MM-DD.md` 패턴 · 파일명 = 최초 생성일 고정 (세션 #4)
- [cd 금지 · 절대경로만 사용](feedback_no_cd_absolute_paths.md) — Bash cd 하면 프로젝트 상대경로 Hook 깨짐
- [한 주제 = 한 파일 원자화 원칙](feedback_one_topic_per_file.md) — Zettelkasten · Obsidian 그래프뷰 최적화 · 왕국별 폴더 독립 (세션 #4)

## 📗 Project (기술 결정 + 서사 Canon)
- [Unity 6 + Steam + C# 스택](project_game_stack.md) — 로그라이크/시뮬/RPG 방향 장기 솔로 인디 (2026-04-20 확정)
- [Obsidian vault 3층 시너지 복구](project_obsidian_vault_system_2026-04-22.md) — 하네스+wiki+Obsidian 정상 · 자동 백링크 99.3% (세션 #6)
- [Q-CORE 1 · 마왕 ≠ 할배](project_qcore1_resolved_demon_king_separate.md) — 마왕이 신보다 선행 · 세계관 시간축 근본 재정의 (세션 #4)
- [Q-CORE 2 · 할배 동기 = 속죄](project_qcore2_resolved_hope_atonement.md) — 판단 미스 속죄로 서민에게 무료 생활 마법 배포 (세션 #4)
- [Q-CORE 3 · 수정 2 = 마족 증식 / 수정 1 = 수호자 제한](project_qcore3_resolved_crystal_two_origin.md) — 이중 관리 구조 (할배=인간 + 수정1=마족)
- [Q-CORE 4 · 나이트 이중 자아 융화](project_qcore4_dual_self_integration.md) — 백지 + 수호자 점진 융화 → 감정 중심 수호자 · Bad End 없음 (세션 #6)
- [세션 #5 Ch.01 시점·주인공 재조정](project_session5_ch01_pov_reconciliation.md) — 3인칭 제한 vs Ashenveil 추락 도착지 모순 해소 (세션 #7 정정)
- [세션 #5 기상 후 결정 10건](project_session5_post_wake_decisions.md) — A축 3 + B축 2 + C축 5 박제
- [세션 #5 Q-FIX 10건](project_session5_qfix_decisions.md) — Q-FIX 1~9 + 주인공 마을 결정 · Wave 5 진입 게이트 해소
- [세션 #5 Q-FIX-X1·X2 자체 해소](project_session5_qfix_extended_x1_x2.md) — Aldric/Aldren 이름 공간 정리 (욜로모드)
- [세션 #5 Q-FIX-X3·X4 결정 대기](project_session5_qfix_x3_x4_pending.md) — 욜로모드 자체 판단 보류 · 대표님 결정 요청
- [세션 #5 욜로모드 위임](project_session5_yolo_mode_authorization.md) — 퍼미션 질문 금지 · AI 자율 판단 · Karzor 전체 파이프라인 완수
- [Episode 2 · 카라 시퀄](project_episode2_kara_sequel.md) — 여주인공 카라(Q-CORE 5) 가 마왕 나이트를 물리치는 시퀄 · 본편 미방문 지역(Thaloss·Vaelin·Nahir·Thari·북쪽 섬·용족 본거지) 무대 원칙 · 2026-04-24 대표님 확정

## 📕 Synthesis (wiki/design/brainstorm/2026-04-24_nlm_session/ 외부 링크)
- [페이즈 4.5 내부 갈등 설계](../../wiki/design/brainstorm/2026-04-24_nlm_session/synthesis_phase4_5_internal_conflict.md) — 인간 4인 vs 세리스 3막 갈등 · 은/음 속성 상극 Canon 신설 · 미냐 계열 룬어 (2026-04-24)
- [다크판타지 4원칙 작법](../../wiki/design/brainstorm/2026-04-24_nlm_session/synthesis_dark_fantasy_4principles.md) — 오감·반전+코스믹 호러·템포·병적 비유 · style_bible_v2 부록 편입 후보 (2026-04-24)

## 📙 Reference (외부 자료·스크립트 위치)
- [초보 1인 인디 게임 개발자 지식 인덱스](reference_beginner_gamedev_knowledge.md) — NotebookLM 6-쿼리 딥 리서치 결과 (Unity 6/Steam/AI/한국)
- [2026-04-21 브레인스토밍 원전](reference_brainstorm_original_2026-04-21.md) — Rev.3 통합 박제 작업 시 먼저 조회할 원안 보존 문서
- [NotebookLM — naberal_game 허브](reference_notebooklm_game.md) — 게임 제작·시나리오 리서치 자료 URL
- [Obsidian 자동 백링크 빌더](reference_obsidian_backlink_builder.md) — `scripts/obsidian/build_backlinks.py` · frontmatter 기반 · idempotent
