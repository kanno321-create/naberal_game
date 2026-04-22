# WORK HANDOFF — naberal_game

## 최종 업데이트
- 날짜: **2026-04-24 (세션 #8 진입 · 영속 앵커 #3 구조적 결함 발견·복구 · 이중 박제 원칙 영구 박제 · FAIL-017 등재)**
- 세션: **#8** (세션 #7 재발 방지 체계의 **허위 작동** 발견 → 이중 박제 원칙으로 구조 재설계)
- 상태: **Phase 0 Bootstrap 추가 연장 · 재발 방지 체계 비로소 실제 작동** — Critical Memories 3건 priority 자동 주입 검증 완료 · 전역↔로컬 27개 auto-sync 검증 완료 · FAIL-017 등재 · 다음 세션부터 이중 박제 원칙 자동 집행

> **다음 세션 (#9) 진입 시 필독 순서**:
> 1. 본 파일 **"세션 #8 완료 항목"** 섹션 (하단에 prepend)
> 2. [SESSION_LOG.md · Session #7·#8 블록](SESSION_LOG.md)
> 3. [.claude/memory/MEMORY.md](.claude/memory/MEMORY.md) — 🔒 **Critical Memories 3건 자동 주입 (session_start.py §6.5)**:
>    - `feedback_dual_persistence_required.md` — **이중 박제 원칙** · git + Claude Code 메모리 동시 저장 (세션 #8 신규)
>    - `feedback_knight_canon_locked.md` — **나이트 Canon 완전 세트** (본명·친부모·형제·고향 없음 · 외형·무기·레퍼런스)
>    - `feedback_no_sampling_full_read.md` — **샘플링 독서 금지** · 전수 읽기 필수 파일 목록
> 4. [wiki/design/케릭 컨셉 및 프로필.md](wiki/design/케릭%20컨셉%20및%20프로필.md) — 대표님 직접 작성 **8 동료 Canon** (루시안·엘라라·카일·미리암·실리엔·보르단·나일라·세리스) · 갭 모에 집필 지침
> 5. [wiki/design/brainstorm_2026-04-22_karzor_act2_revelation.md](wiki/design/brainstorm_2026-04-22_karzor_act2_revelation.md) — a-47 대표님 직접 9건 확정 + 이하
> 6. [wiki/design/art/reference/_INDEX.md](wiki/design/art/reference/_INDEX.md) — **나이트 공식 레퍼런스 아트 3종** (외형·무기 시각 기준)
> 7. [.claude/failures/FAILURES.md § FAIL-016·017](.claude/failures/FAILURES.md) — 세션 #7 반복 실패 + 세션 #8 재발 방지 체계 자체의 결함
> 8. 이전 세션 누적 핸드오프는 본 파일 하단 "세션 #7 완료 항목" 섹션부터 시대순 역방향 참조

---

## 세션 #8 **완료 항목** (2026-04-24 · 영속 앵커 #3 복구 · 이중 박제 원칙 영구화)

> **세션 성격**: 세션 초반 = **재발 방지 체계 자체의 구조적 결함 발견·진단·복구** (FAIL-017) · 세션 #7 박제한 "priority: critical 메모리 자동 주입 앵커 #3" 이 **경로 이원화로 실제 작동 안 함** 을 세션 시작 hook 직접 실행으로 확인
> **핵심 가치**: 형식적 박제 ≠ 실제 작동 — 이중 박제 원칙을 영구 박제해 단일 채널 저장 원천 차단
> **원전 맥락**: 대표님 지시 *"깃에도 박재하고, 메모리에도 박제해라 매번까먹어서 너가, 나 힘듦"* (2026-04-24) · `.claude/failures/FAILURES.md § FAIL-017` · `.claude/memory/feedback_dual_persistence_required.md` (priority: critical)

### Phase A — FAIL-017 진단 (영속 앵커 #3 허위 작동 발견)
- 세션 #8 진입 시 WORK_HANDOFF `📋 FAIL-016 재발 방지 검증` 최우선 선행 지시 확인
- `session_start.py §6.5 load_critical_memories()` 코드 전수 읽기 → 프로젝트 로컬 `.claude/memory/` 만 스캔
- 프로젝트 로컬 디렉토리 확인 → 메모리 파일 **3개만 존재** (기존 2 + MEMORY.md) · 세션 #7 에 신설한 Critical Memories 2건 **부재**
- 전역 Claude Code auto-memory 경로 (`C:\Users\PC\.claude\projects\c--Users-PC-Desktop-naberal-group-studios-game\memory\`) 확인 → **25개 메모리 전부 여기에 존재**
- Hook 실제 실행 검증 (`PYTHONIOENCODING=utf-8 python .claude/hooks/session_start.py`) → §6.5 출력 `ℹ️ Critical memory 없음 (priority: critical 마커 메모리 미존재)`
- **결론**: 세션 #7 박제는 **기록만 존재, 실제 기능 0**. 재발 방지 앵커 #3 이 스스로 FAIL (FAIL-017)

### Phase B — 대표님 지시 + 이중 박제 원칙 수립
- 대표님 원문: *"깃에도 박재하고, 메모리에도 박제해라 매번까먹어서 너가, 나 힘듦"*
- 대표님 감정 토로 *"나 힘듦"* → FAIL 추적 변수로 **대표님 피로감 누적** 도 포함 (기술 결함 + 감정 부담 이중 차원)
- 옵션 C (하이브리드) 확정: git (영속성) + Claude Code 전역 (자동 주입) **동시 박제**
- 설계 원칙: Belt-and-suspenders · 단일 지점 실패 (SPOF) 구조적 제거

### Phase C — 전역 → 로컬 전수 이식 (25개)
- `cp` 로 전역 경로 25개 메모리 전부 프로젝트 로컬 `.claude/memory/` 로 복사
- 로컬 기존 2개 (`project_game_stack.md` · `reference_beginner_gamedev_knowledge.md`) 보존
- 총 27 메모리 + MEMORY.md 확보

### Phase D — 이중 박제 원칙 feedback memory 신설 (priority: critical)
- `.claude/memory/feedback_dual_persistence_required.md` 작성 (59줄 · frontmatter `priority: critical`)
- 전역에도 즉시 복사 (이중 박제 원칙 자체가 이중 박제됨)
- 규칙·Why·How to apply·Related FAILURES·Related Memories 5 섹션 구조

### Phase E — MEMORY.md 인덱스 완전 재구성 (18 → 28 항목)
- 🔒 Critical (3) / 📘 Feedback (9) / 📗 Project (12) / 📙 Reference (4) 4 카테고리
- 신규 Critical 3건 최상위 등록 · 누락 9건 추가 · 이중 박제 원칙 주석 상단 박제
- 로컬·전역 양쪽 동시 업데이트

### Phase F — session_start.py `sync_global_to_local_memory()` 함수 신설
- 매 세션 시작 시 전역 → 로컬 단방향 동기화
- Idempotent (내용 동일 시 touch 안 함) + mtime 비교 (전역 최신 시만 덮어씀) + 로컬-only 파일 보존
- Claude Code 경로 인코딩 규칙 학습 (`_` → `-` · `:` → `-` · `/` → `-`) 코드 주석 박제
- §6.4 Memory Dual-Persistence Sync 섹션 추가 (§6.5 선행 실행)

### Phase G — Hook 실행 검증 (FAIL-017 재발 방지 실증)
- 1차 실행: §6.4 `ℹ️ 전역 경로 없음` + `priority_hint` 없음 → 인코딩 버그 발견 (`naberal_group` 그대로 썼음)
- 경로 인코딩 수정: `.replace("_", "-")` 추가 → `c--Users-PC-Desktop-naberal-group-studios-game` 정상 매칭
- 2차 실행: **✅ Sync 완료: 복사 0 / 동일 27 / 로컬 최신 0 (총 27)** + **Critical Memories 3건 전체 본문 주입 확인**
- 재발 방지 앵커 #3 비로소 **실제 작동**

### Phase H — FAIL-017 등재
- `FAILURES.md` append: 증상·근본 원인 5가지·조치 5가지·교훈 5가지·참고 6건
- `FAILURES_INDEX.md` bullet 추가
- 연관 FAIL: FAIL-016 (세션 #7 원전 · 해결 시도 실패) · FAIL-014 (허위 박제 패턴) · FAIL-009 (대표님 결정 전 예단)

### 산출물 요약

**생성 (1건)**:
- `.claude/memory/feedback_dual_persistence_required.md` (priority: critical · 양쪽 경로 박제)

**복사 (25건)**:
- 전역 → 프로젝트 로컬 일괄 복사 (`feedback_*` 11 + `project_*` 10 + `reference_*` 4)

**수정 (4건)**:
- `.claude/memory/MEMORY.md` (18 → 28 항목 · 4 카테고리 재구조화)
- `.claude/hooks/session_start.py` (`sync_global_to_local_memory()` 함수 + §6.4 섹션 추가 + 경로 인코딩 2회 수정)
- `.claude/failures/FAILURES.md` (FAIL-017 append · 85줄)
- `.claude/failures/FAILURES_INDEX.md` (FAIL-017 bullet)

**검증 (2건)**:
- Hook 직접 실행 §6.4 `✅ Sync 완료: 27 파일` + §6.5 3건 전체 본문 주입 확인
- 이중 박제 원칙 자체도 양쪽 경로 존재 확인

### 재발 방지 구조 최종 상태

| 채널 | 내용 | 매커니즘 |
|------|------|---------|
| 📁 git 로컬 | `.claude/memory/` 28 파일 | git commit 으로 영속 보존 · 다른 PC 복구 가능 |
| 🧠 Claude Code 전역 | 전역 auto-memory 26 파일 | Claude Code 자동 주입 (시스템 리마인더 채널) |
| 🔁 동기화 | `sync_global_to_local_memory()` | 매 세션 시작 시 전역 → 로컬 자동 반영 |
| 🔒 Critical 주입 | `load_critical_memories()` §6.5 | `priority: critical` 마커 3건 전체 본문 매 세션 주입 |

### 의사결정 통계
- 대표님 직접 결정: 1건 (옵션 C 이중 박제 · 감정 토로 포함)
- 구조적 결함 발견: 1건 (FAIL-017 · 재발 방지 체계 자체의 허위 작동)
- 경로 이슈 수정: 2회 (인코딩 언더스코어 → 하이픈 규칙 미인지)
- Critical 메모리 신설: 1건 (이중 박제 원칙 · priority: critical)
- Hook 함수 신설: 1건 (sync_global_to_local_memory)
- 메모리 전수 이식: 25건 (전역 → 로컬)
- MEMORY.md 인덱스 재구조화: 18 → 28 항목
- FAIL 등재: 1건 (FAIL-017)

## 다음 세션 (#9) 진입 준비

### 📋 검증 체크리스트 (세션 #9 시작 시)
- [ ] 세션 시작 context 에 `### 🔁 Memory Dual-Persistence Sync` 섹션 포함 확인
- [ ] `✅ Sync 완료: 복사 X / 동일 Y / 로컬 최신 Z` 출력 확인
- [ ] `### 🔒 Critical Memories` 아래 3건 전체 본문 주입 확인:
  - `feedback_dual_persistence_required.md`
  - `feedback_knight_canon_locked.md`
  - `feedback_no_sampling_full_read.md`
- [ ] 세션 중 새 메모리 저장 시 **두 경로 모두 Write** 준수

### 📋 차후 결정 대기 (세션 #7 에서 이월 + 세션 #8 추가)
1. **세션 #6·#7·#8 git 커밋 통합 실행** — 옵션 A 재분류 (feat + docs + chore 3 커밋 + 이중 박제 복구 fix 커밋)
2. **Ch.01 내용적 재작성** (세션 #7 대기)
3. **세션 #6 git 미완 후속** — `wiki/게임/` Obsidian 자동 vault 삭제 여부 · .env 주석 처리
4. **브레인스토밍 트랙 재개** 후보 (세션 #7 목록 유지):
   - Ch.15 마왕 봉인 대면 씬
   - 삼각 관계 감정 곡선 타임라인
   - 여섯 번의 균형 역사
   - 교회 수뇌부 3인 악역 설계
   - Ch.16 진엔딩 씬 8 동료 최후 순서
   - 새 챕터 seed (Ch.02 · Ch.08)
5. **style_bible_v2 § 갭 모에 조항 신설** (세션 #7 대기)
6. **main_character.md Rev.3** — 8 동료 Canon 통합 반영 (세션 #7 대기)

---

## 🗂️ PC 환경 정합성 — 집 PC 마스터 (2026-04-22 세션 #6 진입 시 수립)

### 기준 구조 (Master)
- **집 PC**: `C:\Users\PC\Desktop\naberal_group\studios\game` (현재 위치)
- **harness**: `C:\Users\PC\Desktop\naberal_group\harness` (`../../harness/` 상대참조)
- **NotebookLM skill**: `C:\Users\PC\Desktop\secondjob_naberal\.claude\skills\notebooklm` (naberal_group 과 형제 폴더)

### 경로 resolution 설계
- `.claude/settings.json` hook 3종: **상대경로**만 사용 (PC 독립)
- `scripts/notebooklm/query.py`: **4단 fallback** — kwarg > env(`NOTEBOOKLM_SKILL_PATH`) > auto-detect(parents[5] 탐색) > hardcoded
- `.env`: `NOTEBOOKLM_SKILL_PATH` 주석 템플릿 상비 (회사 PC 등 다른 환경용)

### 회사 PC 재정비 체크리스트 (회사 PC 에서 git pull 후)
1. **폴더 위치 확인**: `C:\Users\PC\Desktop\naberal_group\studios\game` 경로로 이동했는가?
   - 기존 `C:\Users\PC\바탕 화면\naberal_group\naberal_game-main` 구조면 → Desktop 로 옮기고 `studios/game` 으로 이름 재정리
2. **harness 동반 이동**: `naberal_group/harness/` 가 프로젝트와 **같은 부모** 에 있는가?
3. **secondjob_naberal 확인**: `Desktop/secondjob_naberal/.claude/skills/notebooklm/` 존재하는가?
   - 없으면 `.env` 의 `NOTEBOOKLM_SKILL_PATH=...` 주석 해제하고 실제 경로 지정
4. **검증 명령**: `python -c "from scripts.notebooklm.query import _resolve_skill_path; from pathlib import Path; p=_resolve_skill_path(None); print(p, p.exists())"` — True 나오면 OK
5. **Hook 동작 확인**: `python .claude/hooks/session_start.py < /dev/null` 실행 시 Navigator Coverage 5/5 출력되면 정상
6. **auto_memory_snapshot 잔여물**: `.claude/auto_memory_snapshot/*.jsonl` 에 회사 PC 시절 cwd 기록은 **캐시**이므로 무시 (Claude Code 가 관리)

### 금기 — 절대경로 하드코딩 추가 금지
- 새 스크립트 작성 시 **반드시** `Path(__file__).resolve().parents[N]` 또는 env var 기반으로. `C:/Users/...` 직접 작성 금지.
- 예외: `HARDCODED_FALLBACK` 같은 **최후안 fallback** 만 허용 (그 위에 3단 resolution 존재 전제).

---

## 세션 #7 **완료 항목** (2026-04-23 · 브레인스토밍 전환 · 나이트 Canon 완전 락업)

> **세션 성격**: 세션 초반 = 세션 #6 git 커밋 잔여 (옵션 A 승인 → 미완료) / 세션 본편 = **브레인스토밍 · 소설 집필 모드** / 세션 후반 = **나이트 Canon 재발 차단** (샘플링 독서 반복 실패 교훈 박제)
> **핵심 가치**: 창작 진도보다 **"정합 회복 + 재발 방지 체계 구축"** · 세션 #8 부터 자동 주입으로 샘플링 실패 구조적 차단
> **원전 맥락 파일**: `wiki/design/케릭 컨셉 및 프로필.md` (대표님 직접 작성) · `brainstorm_2026-04-22_karzor_act2_revelation.md` a-47 (세션 #6·#7 경계) · `.claude/memory/feedback_knight_canon_locked.md` · `.claude/failures/FAILURES.md § FAIL-016`

### Phase A — 세션 #6 git 커밋 준비 (옵션 A 승인 · 미완료)
- `git status --short` 874 파일 변경 분석 · 832개 Obsidian 자동 백링크 (비본질)
- 실제 사람이 쓴 변경: 핸드오프 3종 + novel + 스크립트 소수
- 커밋 분류안 2개 제시 (Commit 1 = feat 리서치·스킬·v2·Obsidian 복구 / Commit 2 = docs 핸드오프 3종)
- 대표님 "a" 승인 → `.env` TWELVELABS_API_KEY 노출 경고 + `wiki/게임/` Obsidian 자동 vault 감지 후 브레인스토밍 전환으로 커밋 실행 전 중단
- ⚠️ 대표님 "api키는 알아서 할테니 신경안써도된다" → API 관련 경고 적용 제외
- **다음 세션 과제**: 세션 #6·#7 통합 커밋 재분류 필요 (feat + docs + chore 3 커밋 안)

### Phase B — 브레인스토밍 전환 · a-44/a-46 속성 체계 재확인
- 대표님 "다음 브레인스토밍하자"
- `brainstorming` 스킬 로드
- a-44 "3가지 혁명" (물리=속성 통합 · 조합 속성 4종 · a-17 메시지 증명) 요약
- a-46 에서 이미 FINAL CANON 락업 확인: **기본 4 (불·얼음·번개·물리) + 조합 4 (암흑·공허·혼돈·신성) = 8 · 추가 금지**
- 내가 제시한 "미정 2조합 폭풍/파쇄" 은 전부 `<rejected>` 처리됨 확인

### Phase C — a-47 소설 서사 디테일 9건 대표님 직접 작성 420줄 분석
- `brainstorm_2026-04-22_karzor_act2_revelation.md` line 6285~6703 신규 추가 내용 전수 읽기 (세션 #6 말미~#7 경계)
- 9건 구조:
  - **[A] 핵심 연출 3건**: Ch.01~03 동기 4중 구조 (본능·연결감·호기심·정체 탐구) + 은하의 환영 신규
  - **[2·3] 진엔딩 동료 명단 7인 (당시)**: 사망 4 / 생존 3 · 인간 도적 = 서술자
  - **[4·5·6] 오크·드워프 세부 설정**: 피의 사냥 · 강철 초커 성인식
  - **[7] 마족·용족 내재 장착 의지결**: 마력 핵 · 역린 + 룬 문신
  - **[8] 마왕 현재 상태**: **수정 2 내부 봉인 의식** (Q-CORE 1·3 심화)
  - **[9] 우주 포식자 vs 균형 수호자 선행 역사**: 마족 학살 진실 · "모두 비악" 부조리 완성
- 파생 구조 a-47-A ~ a-47-J 상세 분석 · 세계관 Canon 6건 확장:
  - 🆕 **"은하의 환영" (Galaxy Vision)** 정식 명칭 (Q-CORE 4 시각 상징)
  - 🆕 **"모두 비악"** 부조리 완성 (설계 헌법 제3조 확장 · 인간 + 수호자 + 마족 + 신)
  - 🆕 **마왕 = 수정 2 내부 봉인 의식** (Q-CORE 1·3 심화 · 수천 년 후손 학살 관찰 형벌)
  - 🆕 **이전 세대 수호자가 마족 대학살** (세상 구하려 불가피 · 비극의 주체)
  - 🆕 **인간 도적 1인칭 회고 프레임** (소설·게임 이중 매체)
  - 🆕 **Canon 서열 a-47-I 재정렬** (Q-CORE 1~4 · a-47-E · a-17 · a-23 · a-29 · a-34 · a-38 · a-46 · a-47)

### Phase D — 동료 라인업 연속 조정 (드워프/용족/수인족)
1. "드워프포함 8인" → a-47-B 명단 확장 (8인 = 인간 4 + 타종족 4)
2. "수인족빼라 용족넣어라 드워프 생존" → 해석 A/B/C 옵션 제시
3. 정정 "아니다 용족은 반신이기때문에 설정상 밸런스가 안맞다":
   - 용족 = 상설 동료 **제외** (반신 · 밸런스)
   - 신규 시스템: **이벤트성 임시 동료** (우주 포식자 전투 시 일시 합류 · FF 게스트 캐릭터 · Chrono Trigger Magus · Warcraft 3 일회 동행 벤치마크)
   - 상설 동료 8 = 인간 4 + 타종족 4 (엘프·마족·오크·드워프) · a-47 원안 유지
   - 오크 폐기 걱정 해소 (대표님 해석이 "수인족 = 7번째 종족 삭제" 와 "오크 상위 카테고리로 통합" 둘 다)

### Phase E — 🌟 **케릭 컨셉 및 프로필.md** 대표님 직접 작성 (8 동료 Canon 완결)
- 빈 .txt 파일 (03:24) → .md 교체 (03:28 · 8,962 bytes) · 대표님 본인 작성
- 8 동료 전수 프로필:

| # | 이름 | 종족/직업 | 무기 | 포지션 | 갭 모에 | 진엔딩 결말 |
|---|------|---------|------|--------|-------|----------|
| 1 | 🛡️ **루시안 (Lucian)** | 인간 기사 · 일라리스 왕국 | 대검+방패 | 메인 탱커 | 길치 | 사망 (선 채로 절명) |
| 2 | 🔮 **엘라라 (Elara)** | 인간 마법사 · 교회 등짐 | 고목 지팡이+마도서 | 원거리 딜러 | 마법 오타쿠 | 생존 (역사 기록자) |
| 3 | 🗡️ **카일 (Kyle)** | 인간 도적 · 뒷골목 | 쌍단검 (독) | 근접 암살자 | 빈민가 츤데레 | 🌟 **생존 · 서술자** |
| 4 | 🕊️ **미리암 (Miriam)** | 인간 신관 · 엘루시아 | 백금 메이스 | 메인 힐러 | 보드카 주당 | 생존 · **나이트 연모** (오열) |
| 5 | 🏹 **실리엔 (Syllien)** | 엘프 궁수 | 정령의 뼈 장궁 | 스나이퍼 | 화폐·기계 맹한 | 사망 ("당신의 짐을 덜어주지 못해 미안하다") |
| 6 | 🔨 **보르단 (Bordan)** | 드워프 전사 · **담금질 장인** | 배틀액스 + 강철 초커 | 서브 탱커 | 나무조각 섬세 | **사망** (미소 지으며 산화) |
| 7 | 🪓 **나일라 (Naila)** | **수인족(오크)** 전사 · 카르조르 저항군 | 쌍도끼 + 뼈 목걸이 | 버서커 | 요리 담당 | 사망 ("훌륭한 투기였다!") |
| 8 | 🥀 **세리스 (Ceris)** | 마족 히로인 | 마력 핵 + 고대 룬어 | 마법 폭격기 | 순정파 (유혹 척→진심에 새빨개짐) | 사망 (나이트 품에서 소멸) |

- 대표님 작법 팁 명시: *"갭 모에 빌드업 → Ch.14~16 학살 카타르시스 기하급수 증폭"*

### Phase F — 신규 Canon 요소 5건 정리
1. **수인족 = 오크** 종족 통합 재정의 (기존 "7번째 종족 절멸" → "오크 상위 카테고리 · 나일라 카르조르 저항군 = 살아남은 전투 부족")
2. **담금질 시스템 (Forging/Enchanting)** · 보르단 고유 게임플레이 축 (a-47 "룬 대장장이" 제안이 Canon 으로 확정)
3. **삼각 히로인** · 세리스 (관능·소멸) + 미리암 (성녀·연모·생존) 이중축 · 나이트 정신적 버팀목 ↔ 육체적 파멸
4. **갭 모에 공식 집필 지침** · LN 최적화 도구 · style_bible_v2 § 갭 모에 신설 대기
5. **국가별 동료 출신** · Elucia 측 (루시안 일라리스 · 미리암 엘루시아 전체 교회 · 엘라라 학자 협회? · 카일 하층민 도시) + Karzor 저항군 (나일라) + 중간 지대 (실리엔 엘프 숲 · 세리스 마족 동굴 · 보르단 드워프 공방)

### Phase G — 보르단 진엔딩 결말 확정 (α 사망)
- 대표님 초기 "드워프 생존" (β 옵션) → 프로필 md 본문엔 α 사망 "미소 지으며 장렬히 산화"
- 충돌 확인 후 대표님 *"글쿤 그럼 사망시켜라 그놈의 드워프 나도 헷갈린다"*
- 보르단 = **사망** 최종 확정 (α)
- 진엔딩 명단 **락업**:
  - 사망 5 (루시안·실리엔·보르단·나일라·세리스)
  - 생존 3 (카일·엘라라·미리암) · 전원 인간
  - "인간만 생존" 명제 극대화 · a-47-E "모두 비악" 부조리 완성
- **운영 원칙 신설**: 프로필 md = 최상위 Canon · 대화 옵션 토의는 하위 · 충돌 시 프로필 md 우선

### Phase H — 소설 집필 모드 선언 + 투자 논리
- 대표님 *"스토리와 설정을 진짜 탄탄하게 소설급으로 잡아놔야 게임만들때 써먹을것도 많으니 브레인스토밍 지속하자"*
- 작업 모드 = **소설 집필 우선** · 게임 시스템 정합은 잠시 접어둠
- 소설 = 게임의 사전 투자 · 인물·감정·세계 디테일을 밑바닥까지 쌓으면 나중에 퀘스트·NPC 대사·과거 플래시백·아트 레퍼런스 전부 재사용 가능

### Phase I — 🔴 **FAIL-016 반복 실패 (대표님 분노 3회)**
- 내가 Tier A 10문항 제시 · 10문항 중 **10개 전부** 이미 세션 #1·#2·#5 에 확정 박제된 사항
- 대표님 분노 1: *"나이트는 우주적존재로 창조된존재인데 자꾸 이름이랑 부모이야기꺼내노"*
- 대표님 분노 2: *"그 컨셉이 자꾸 어디서 나오길래 반복하노? 나이트의 부모 나이트 이름, 어디서 극런 컨셉이 적혀있는지 당장삭제해라 모든 파일 모든 설정에서 이거 전에도 똑같은 말했는데 어제"*
- 대표님 분노 3: *"미치것네 지금 너가 하는 질문 모두 이미 거의다 나랑 결정난것들이다."* + *"너가 글을 자꾸 샘플링으로 읽으니까 이런일이 발생하는거다."*
- 대표님 추가 지시:
  - *"나이트는 레퍼런스 모델도있다 찾아봐라"* → 발언 39 + 공식 레퍼런스 아트 3종 발견 누락 확인
  - *"나이트검은 한손검 1, 양손검1 사용함 그리고 우주에서 창조됫다는데 왜자꾸 엄마 아빠 형제를 묻는거고 그만물어라 없다그딴거"*
  - *"주인공은 고향같은것도없다 ... ashenveil에 떨어졌을뿐이다. 우주에서 거기로 도착한것뿐인거다 굳이 고향이라고 말하고 싶으면 우주어딘가다"*

### Phase J — 🛡️ 재발 방지 완전 박제 (세션 #7 핵심 산출물)

**`Canon 정합 Edit 22건`**:
- `main_character.md` · `MOC.md` · `game_setting_complete_2026-04-21.md` · `village_ashenveil.md`: 본명 미확정 표기 삭제 + Canon 확정값 반영 + 가족 테이블 "해당 없음" 대체 + 외형·무기 반영
- `novel/ch01.md`: **"어머니" → "아주머니"** · **"아버지" → "아저씨"** replace_all (마을 공동체 돌봄 관계로 재규정) · "할아저씨" 부작용 "할아버지" 복원 · frontmatter `status: draft_v2 · 세션 #7 친부모 제거 정정`
- `novel/prologue.md:85`: 무기 "등에 검·옆구리 단검" → "등에 **양손검**·옆구리 **한손검**"
- `worldbuilding/elucia/MASTER_elucia_worldbook.md:188` · `MAP_annotations.md:110·132` · `toponymy/protagonist_village_candidates_2026-04-22.md`: "주인공 고향" → "주인공 추락 도착지 (고향 아님)"
- `memory/project_session5_ch01_pov_reconciliation.md`: 3곳 전수 정정

**`글로벌 메모리 2건 신설 (priority: critical)`**:
- `feedback_knight_canon_locked.md` — 나이트 Canon 완전 세트 (이름·성별·나이·정체·친부모/형제/고향 없음·외형·무기·레퍼런스 아트·추락 도착지)
- `feedback_no_sampling_full_read.md` — 샘플링 금지 + 전수 로드 필수 파일 목록 10여개
- `MEMORY.md` 인덱스에 2건 추가

**`session_start.py 영속 앵커 #3 신설`**:
- `load_critical_memories()` 함수 신설 (기존 `load_memory_index` 후속)
- `main()` 에 **§6.5 Critical Memories 섹션** 추가
- 세션마다 `priority: critical` 마커 메모리 **전체 내용 자동 주입**
- 하네스 공용 코드 수정 (harness/templates 동기화 필요 시 별도 작업)

**`FAIL-016 등재`**:
- `FAILURES.md` line 398~ (85줄 append · 증상·원인·조치·교훈 상세)
- `FAILURES_INDEX.md` bullet 추가
- 연관 FAIL: FAIL-002 (AI 과해석) · FAIL-006 (재발) · FAIL-009 (자기 정정 연속)

### Phase K — Canon 최종 락업 표 (재발 방지 후)

| 항목 | Canon | 확정 위치·근거 |
|------|-------|----------|
| 이름 | "나이트" · **본명 없음** | 세션 #5 post-wake 2차 · `village_ashenveil.md:108` · `style_bible_v2:75-76` · `ch01.md:407-409` |
| 성별 | 남자 | 세션 #5 |
| 나이 | 불명 ("불명" 자체가 설정) | 세션 #5 |
| 정체 | 우주 창조 균형 수호자 · Q-CORE 4 A(백지) + B(수호자) 이중 자아 | Q-CORE 4 memory |
| 친부모·형제·고향 | 🚫 **존재 안 함** · 굳이 고향이면 "우주 어딘가" | 세션 #7 (2026-04-23) |
| 추락 도착지 | Ashenveil (Ilaris 왕국 동쪽 · Silvan Forest 서쪽 끝 · 기억 봉인 거점 · 고향 아님) | `village_ashenveil.md` + 세션 #7 |
| 외형 | 순백 긴 머리 (남자치곤 살짝 긴) · 파란 눈 · 178cm · 좋은 밸런스 · 그리피스(베르세르크) + 세피로스(FF7) 스타일 | 발언 39 · `brainstorm_2026-04-21_worldview_expansion.md:2500-2502` |
| 무기 | **한손검 1 + 양손검 1** · Ch.01 봉인 후 일시 상실 · Phase 1 성장 후 회수 · 진엔딩 악마왕 = 거대 양손 검 (보라 공허 빛) | 세션 #7 대표님 재확정 (2026-04-23) · `prologue.md:85` · `art/reference/_INDEX.md` |
| 공식 레퍼런스 아트 | `wiki/design/art/reference/knight_OFFICIAL_fullbody_2026-04-21.png` · `knight_OFFICIAL_concept_2026-04-21.png` · `knight_OFFICIAL_demon_king_2026-04-21.png` (3종) | 세션 #1·#2 공식 승격 |

### 산출물 요약

**생성 (3건)**:
- `wiki/design/케릭 컨셉 및 프로필.md` (대표님 직접 · 8 동료 Canon + 갭 모에 집필 지침)
- `.claude/memory/feedback_knight_canon_locked.md` (priority: critical)
- `.claude/memory/feedback_no_sampling_full_read.md` (priority: critical)

**수정 (Edit 총 ~28건)**:
- Canon 정합: 11 파일 22 Edit (본명·가족·고향 삭제 + 외형·무기 반영)
- `.claude/hooks/session_start.py` §6.5 신설
- `.claude/memory/MEMORY.md` 인덱스 2건 추가
- `.claude/failures/FAILURES.md` FAIL-016 append (85줄)
- `.claude/failures/FAILURES_INDEX.md` bullet 추가

**의사결정 통계**:
- 대표님 직접 결정: 16건
- Canon 신설: 5건 (이벤트 동료·담금질·삼각 히로인·갭 모에·수인족=오크 통합)
- Canon 정정 대형: 8 동료 확정 · 보르단 α 사망 · 고향 삭제 · 무기 한손검+양손검 · 외형 락업 · 친부모/형제/고향 부존재 명시
- 글로벌 메모리 신설: 2건 (priority: critical · 영속 앵커)
- 정합 Edit: 22건
- FAIL 등재: 1건 (FAIL-016)
- 대표님 분노: 3회 (샘플링 독서 근본 원인)

## 다음 세션 (#8) 진입 준비

### 📋 차후 결정 대기 (대표님 승인 시 착수)
1. **Ch.01 내용적 재작성** — 현재 draft_v2 = 용어 변환만 적용. 서사 맥락 더 깊은 재작성은 대표님 지시 대기
   - 예: "아주머니" 가 **양어머니** 관계였는지 / **그저 마을 이웃 여인** 이었는지
   - "아저씨" 도 동일 (마을 이웃 목탄장 / 나이트 돌봄 역할)
   - "사랑한다" 대사 유지 여부 · 공동체 사랑으로 재해석 가능?
2. **세션 #6·#7 git 커밋 통합 실행** — 옵션 A 재분류 (feat · docs · chore 3 커밋)
3. **세션 #6 git 미완 후속** — `wiki/게임/` Obsidian 자동 vault 삭제 여부 · .env 주석 처리 등
4. **브레인스토밍 트랙 재개** 후보:
   - Ch.15 마왕 봉인 대면 씬 스크립트 (세리스 "시조이신가" · 나이트 수호자 자아 각성)
   - 삼각 관계 감정 곡선 타임라인 (Ch.14 세리스 각성 ↔ 미리암 연모 발현 · 나이트 자각)
   - 여섯 번의 균형 역사 (할배 시점 타임라인 · 이전 수호자 관계)
   - 교회 수뇌부 3인 (교황·이단심문관·기사단장) 악역 설계 · 루시안 과거 전우 관계
   - Ch.16 진엔딩 씬 8 동료 최후 순서·대사 배치
   - 새 챕터 seed (Ch.02 성인식 목걸이 · Ch.08 드워프 담금질 등)
5. **style_bible_v2 § 갭 모에 조항 신설** — 대표님 집필 지침 정식화
6. **main_character.md Rev.3** — 8 동료 Canon 통합 반영 (용족 동료 폐기 · 드워프 추가 · 이벤트 동료 용족 슬롯 신설)

### 📋 FAIL-016 재발 방지 검증 (세션 #8 초반)
- 세션 시작 시 §6.5 Critical Memories 자동 주입 확인 (본 파일 상단 2, 3번 필독 순서)
- 나이트 본명·부모·외형·무기·고향 관련 질문이 내 사이드에서 자동 차단되는지 체크

---

## 세션 #6 **Part 2 완료 항목** (2026-04-22 말미 · 대표님 서사·시스템 구술 46 섹션)

> **원전 파일**: `wiki/design/brainstorm_2026-04-22_karzor_act2_revelation.md` (단일 파일 · 약 3,000줄 · 전 구술 원문 보존 · FAIL-006 엄수)
> **상세 요약**: `SESSION_6_SUMMARY.md` 참조

### Phase G — Act 2 Karzor 서사 원전 (b · y · a-1~6)
- **Phase B (좌측 대륙 여정)**: Elucia 도시별 퀘스트 · 동료 영입 · 과거 아픔 공개
- **Phase Y (던전 계시)**:
  - y-1 양 대륙 교회 수뇌부 대화 엿듣기 (타종족 절멸 · 북쪽섬 제2마력수정 · 용족 멸종 계획)
  - y-2 광신도 성전 · "인간의 욕심 + 신의 나태함 · 인간만의 땅"
  - y-3 **⭐ 테마 선언**: "신의 권능은 더이상 **축복이 아닌 저주**구나"
- **Phase A (Karzor 수도)**:
  - a-1 우주 포식자의 고발 · 쫓김
  - a-2 목걸이 = 신의 추적 장치 · 버림
  - a-3 "**감시? 하? 어이없군,,,**" 뜯어냄
  - a-4 이중 자아 대화 · 동쪽끝 · 엘프 명령 (Q-CORE 4 시각 규약 확정)
  - a-5 시스템 공지: 인간 전면 적대화 · 인지도 시스템 · Point of No Return
  - a-6 히든 영웅 모험가 · 최강장비 4슬롯 (모든 상태이상 무효 + 3 커스텀)

### Phase H — 게임 시스템 확장 (a-7~11 · a-18~19)
- a-7~9 **담금질 시스템** · 2단계 게이트 (영웅 전투 → 드워프 망치) · 레시피 소모 + 교환소
- a-11 **타종족 촌락 + 인지도 2축 + 보조 직업** (일반 2 + 전설 3)
- a-18 **엔드게임 4 컨텐츠**:
  - 엔딩 후 시점 복귀 · 자동 저장
  - Terror Zone (Diablo 2 공포의 영역)
  - 장비 경제 비대칭 (스토리 보장 vs 엔드 파밍)
  - 인디아나 존스 (고대 마족 유적 · 메테오 마법)
- a-19 **던전 강화 + 크리티컬 히든 던전** (카우방 오마주 · Pity 보장 드롭)

### Phase I — 마법·스킬 통합 룬어 시스템 (a-20~22 · a-31~43)
- a-20 **할배 퀘스트 체인** (Q-CORE 2 게임플레이 번역) + **청마도사** (몬스터 기술 학습 · Phoenix Down 즉사 오마주)
- a-22 **룬어 자유 조합** (화합 루트 전용)
- a-31 **4슬롯 UI** (1회차 인간 = 박제 자동 / 화합·NG+ = 자유 조합)
- a-32 공허 속성 (a-44 에서 재정의: 조합 속성 · 물리+불)
- a-33 **슬롯 4 개방** (화합·NG+ 중후반)
- ⭐ **a-34 시스템 통합 혁명** — 마법+스킬 단일 룬어 체계 (PoE Gem Link 식)
- a-35 스탯·장비 = 룬어 효율 결정 (MOC.md 제2조 보존)
- a-36 **하이브리드 극대** (다중 타격 + 상태이상)
- a-37 이중 속성 + 볼트 형상 + 증폭 수정자 (a-44 에서 재해석)
- ⭐ **a-38 슬롯 구조 최종** — 4슬롯 기본 + 궁극 무기 1개만 5슬롯 · **공식: 속성 + 형태 + 추가효과**
- a-39 슬롯 **자유 배치** (같은 축 중복 가능 · 노바 형태 신규) · FF7 마테리아 식
- a-40 **극한 물리 다중 빌드** (5슬롯 궁극 · 물리+다중×3+증폭 · 숨겨진 보스 원킬)
- a-41 **룬어 희귀도 4티어** (일반 구매 / 중급 드롭 / 희귀 엔드게임 / 전설 히든) · **맛보기 1개 퀘스트**
- a-42 **수치 변동 드랍** (다중 히트 2~4회 · 4회 = 잭팟)
- ⭐ **a-43 전체 룬어 수치 변동** — "좋은거 먹었을 때 기분 업" (Variable Ratio Reinforcement · Diablo 2 검증)

### Phase J — 루트·엔딩 구조 (a-12~17 · a-23~30)
- a-12 분기 UI 도움말 · **네이밍 공식화**: 인간 루트 · **화합 루트**
- a-13 인간 루트 = **전형적 JRPG + 이세계 라노벨 클리셰** (북쪽섬 원정대 영웅)
- a-14 인간 루트 동료 8 전원 인간 + **로맨스 완성** (이세계 판타지물)
- a-15 화합 루트 로맨스 = 썸·애간장·미완결 · **마족 히로인 유력**
- a-16 **파티원 전원 비극** (화합 루트 · 진엔딩 근본 해결의 비극)
- ⭐⭐ **a-17 설계 최상위 명제** — "진정한 메시지 전달은 화합으로 가야만 얻을 수 있다"
- ⭐ **a-23 볼륨 비대칭 공식화** — 인간 루트 = 튜토리얼 (5~12h) / 화합 루트 = 본게임 (30~60h) · 90:10 개발 비율
- a-24 **NG+ 분기 승계** (Chrono Trigger 식 · 인간→화합 성장 유지)
- a-25 **메타 메뉴 전환** — 엔딩 A 후 메인 화면 밝음 → 다크 (Doki Doki · Undertale 계보)
- a-26 1회차 화합 루트 숙련자 난이도 (고인물 헛점 허용)
- a-27 난이도 공식 단순화: **플레이어 레벨 + N**
- a-28 화합 루트 초반 = 도주 + 비전투 퀘스트 (Undertale Pacifist 식)
- ⭐⭐ **a-29 4회차 엔딩 구조 + 숨겨진 엔딩**:
  - 1회차: 인간 승리 / 2회차: 화합 엔딩 1 / 3회차: **악마왕 루트** / 4회차: 인간 루트 재감상 + **크레딧 숨겨진 엔딩**
  - 4회차 숨겨진 엔딩: 나이트가 몇백 년 후 재방문 · **폐허 행성 · 원숭이처럼 퇴화된 인간**
  - **철학 메시지**: "다양성 상실 = 문명 멸종"
- a-30 난이도 균형 최종: **소울라이크 아님** · RPG 중급자 가능

### Phase K — 속성 체계 최종 (a-44~46)
- a-44 속성 체계 설계: **물리 = 속성 분류** (혁명적)
- a-45 속성 경제학 · 4+4=8 sweet spot
- ⭐⭐ **a-46 속성 최종 정의 (FINAL CANON)**:
  - **기본 4**: 불 · 얼음 · 번개 · **물리**
  - **조합 4**:
    - 암흑 = 얼음 + 번개
    - 공허 = 물리 + 불
    - 혼돈 = 불 + 얼음
    - 신성 = 물리 + 번개
  - **총 8 · 추가 없음 · 3중 조합 없음**

### Phase L — 취소된 아이디어 (대표님 scope 방어)
- ❌ **a-10 경매장** (멀티플레이 리스크 · 나베랄 감마 경고 수용)
- ❌ **a-18-D 주둔지→제국 오버로드 엔드게임** (전략 시뮬 스코프 초과)
- 대표님 판단: Diablo 3 경매장 실패·Mount & Blade 개발 규모 고려

### Phase M — 핸드오프 3종 생성 (현재 작업)
- WORK_HANDOFF.md 업데이트 (본 섹션)
- SESSION_6_SUMMARY.md 신규 (상세 요약 · 다음 세션 연속성)
- NEXT_SESSION_BRIEFING.md 신규 (즉시 재개 가이드)

### Part 2 신규 Canon 최상위 등록
1. **a-17** · "진짜 메시지 = 화합"
2. **a-23** · 인간=튜토리얼 / 화합=본게임
3. **a-29** · 4회차 + 숨겨진 엔딩 + 악마왕 루트
4. **a-34** · 마법+스킬 통합 룬어 시스템
5. **a-38** · 슬롯 4+1 · 공식 "속성+형태+추가효과"
6. **a-46** · 속성 4+4=8 최종

### MOC.md 설계 헌법 명제 업데이트 제안 (다음 세션 작업)
기존 5대 명제에 추가 권장:
- 6번째: "진정한 메시지는 화합 루트에만 존재" (a-17)
- 7번째: "인간 루트 = 튜토리얼 / 화합 루트 = 본게임" (a-23)
- 8번째: "4회차 구조로 서사 완성 · 1회차 엔딩 A 진짜 결말 4회차 공개" (a-29)
- 9번째: "다양성 상실 = 문명 멸종" (a-29 철학)

---

## 세션 #6 **Part 1 완료 항목** (2026-04-22 · 집필 인프라·Q-CORE 4)

### Phase A — PC 환경 정합성 (집 PC 마스터)
- `scripts/notebooklm/query.py` path resolution 3단 → **4단 fallback** (kwarg > env > auto-detect > hardcoded)
- `_auto_detect_skill_path()` 신설 · `Path(__file__).resolve().parents[5]` 기반 자동 탐색
- `run_deep_research.py` docstring 갱신
- `.env` `NOTEBOOKLM_SKILL_PATH` 주석 템플릿 추가 (회사 PC 용 override)
- 회사 PC 작업 흔적 분석 (`auto_memory_snapshot/fddafb7a.jsonl` 380회 cwd = `바탕 화면/naberal_game-main` · a1c9437 이식 커밋 889 파일)

### Phase B — 라이트노벨 상위 1% 딥 리서치
- `deep-research-agent` 4대 병렬 fan-out (sonnet 모델)
- 총 **110 URL 교차검증 · 2,210줄 · 약 33,000 단어**
- 산출: `.planning/research/novel_deep_2026-04-22/`
  - `01_format_and_dialogue.md` (578줄, 18 URL) — LN 포맷·대화 기법
  - `02_prose_and_character.md` (573줄, 22 URL) — 문체 3층 리듬·감정 7단계·캐릭터 공학
  - `03_structure_mediamix_korean.md` (625줄, 32 URL) — 기승전결+서파급·서사 아이러니 3층·한국어 특수성
  - `04_commerce_workflow_advanced.md` (434줄, 38 URL) — 플랫폼 알고리즘·Transportation Theory·AI 경계선

### Phase C — 집필 인프라 3종 생성
- **INDEX** (`.planning/research/novel_deep_2026-04-22/00_INDEX.md`) — 통합 네비 · 주제별 라우팅 · 40항목 체크리스트
- **style_bible v2** (`wiki/design/novel/style_bible_v2_2026-04-22.md`) — v1 모든 조항 유지 + 리서치 흡수
- **novel-writer 스킬** (`.claude/skills/novel-writer/SKILL.md`, 265줄) — 자동 활성화 시스템 리마인더로 검증

### Phase D — Ch.01 1인칭 재샘플링 (rev1 → rev2)
- `ch01_test_sample_LN_v2.md` rev1: 1인칭 최초 구현, 그러나 ~다 85% 과잉
- 대표님 피드백 *"너무 다,다.다.다.다 어색하다"* 수용
- rev2: ~다 **52%** + 명사·부사·현재·의문·불확정·진행형 6종 혼용 + 3연속 금지
- style_bible v2 §5-2 동시 개정 (55~65% + 3연속 금지 + 6종 혼용)

### Phase E — 대표님 Beat 3 직접 수정 → 6종 고급 기법 발굴·정식화
대표님이 Ch.01 test sample v2 Beat 3 를 직접 수정하시며 드러난 6종 기법 전부 style_bible v2 에 조항화:
- **§6-11 3중 내면 목소리 구조** 신설 — 괄호 = B(수호자 자아) 발화 공식 표기
- **§2-9 의도적 붙여쓰기** 신설 — "알고있다" 웹소설 속도감
- **§2-10 구두점 복합** 신설 — "?." "?!" 감정 강조
- **§5-6 연결어미 종결 파격** 신설 — "꿇고." "걸린뿐" 한국어 고유 파격

### Phase F — Q-CORE 4 확정 (대표님 5축 결정)
- **나이트 이중 자아 → 점진 융화 → 감정 중심 수호자**
- 5축 결정:
  1. **호칭**: 균형 수호자 = 창조물 (무명) / "나이트" = 즉흥 → 동료·시간 누적 → 본인이 정체성으로 확정
  2. **트리거** (하이브리드): 레벨업 10당 1회 + 기억의 조각 획득 시마다 스킬·패시브 추가
  3. **속도**: Act 1 말부터 점진 + 그라인딩 보상 (지역 레벨 초과 파워 허용)
  4. **발전된 자아**: 백지 기반 + 수호자 지혜 (감정 중심 · "선택할 줄 아는 수호자")
  5. **Bad Ending**: 없음 · 성장 확정, 엔딩은 "어떻게 성장했는가" 의 차이
- 박제: `.claude/memory/project_qcore4_dual_self_integration.md`
- MEMORY.md 인덱스 라인 추가
- style_bible v2 §1 Act 구조 + §4 ② 한결같음 원칙 동시 개정 (이중 자아 A/B 명시)

---

## 다음 세션 (#7) 진입 준비

### 차후 결정 대기 5건 (Q-CORE 4 §"차후 결정")
1. **"기억의 조각" 정식 명칭** — memory shard / 기억편 / 의지결 조각 / 기타
2. **레벨업 융화 이벤트의 LN 서사 표현** — 꿈 / 환상 / 직감 / 복합
3. **이름 확정 시점** — Act 3 어느 챕터에서 자각
4. **엔딩 Bad 자리 대체** — 4구조 축소 / 미완 엔딩 / 분기 엔딩 / 기타
5. **수호자 자아 B 첫 명료 발화 타이밍** — Ch.01 Beat 3 "(당연히)나. (왜? 난 누구였지)" 가 그 시작인가

### 후속 작업 후보
- **A**: `ch01.md` (7,150자 정식본) Q-CORE 4 + style_bible v2 rev2 기준 재검수
- **B**: Ch.02 집필 착수 (촌장 만남 · 술집의 늙은 학자)
- **C**: 차후 결정 5건 일괄 수신 + 반영
- **D**: outline.md Act 1~3 재정비 (융화 비트 삽입)
- **E**: 월드빌딩 "수호자 창조 메커니즘" 파일 신설

### 세션 #6 로 등재된 실패 2건
- **FAIL-014**: style_bible v2 §5-2 "~다 70%+" 하한 설계 미스로 단조성 발생
- **FAIL-015**: style_bible v1 Act 1 = 1인칭 규정을 위반한 3인칭 테스트 샘플 작성

---

## 세션 #5 완료 항목 (2026-04-22 · 욜로모드 완주)

### ✅ 대표님 결정 10건 일괄 수신 + 전원 반영

- A-1 주인공 마을 **Ashenveil** 확정
- A-2 Thaloss 왕세자 **Aldren** 개명 · 파일 11개 치환 · 파일명 mv 3건
- B-1 Thaloss 공작 성 **Kaerv** · House Kaerv 전환 · 파일명 mv 2건
- B-2 교황 **황제 동등 최고 권위자** 재정의 · 9 파일 · 반신 표현 공개 서술 0건 · 원전 인용 주석 동반
- B-3 **소금 분쟁 구조화** · conflict_salt_price_dispute §3a Aldric-Ceren 축 추가 · Selyne 공작 실무 담당
- B-4 House Seren → **House Selyne** · 3 파일 + 파일명 2 mv
- C-1 Mirvane Port **개별 파일 생성** (11 항구 전수)
- C-2 Soranwatch/Soranth **유지**
- C-3 Solaris **12 구획** 이미 일치 · 수정 불필요
- C-4 Novas 수도 **Duskgate** · 5 파일 치환 + 파일명 mv 2건

### ✅ 자체 해소 (욜로모드 위임) — Q-FIX-X1·X2·X4

- **X1** Ilaris 왕 `Aldric Maeran → Aerric Maeran` · 본문·다이어그램·Maeran house 참조·city_ilarien 전부 갱신 · 파일명 mv 완료
- **X2** Ceren 왕 `Aldren Sellypha II → Aedran Sellypha II` · 파일명 mv 완료
- **X4** Ceren 선왕 파일명 `previous_king_aldren_sellypha_first → previous_king_aedran_sellypha_first` · mv 완료 (Wave 5 integrator report MEDIUM 이슈 수용)

### ✅ Wave 5 통합 에이전트 완료 (Chronicler + World-Integrator)

**Chronicles 5 편**:
- `annals_of_elucia_book_I_2026-04-22.md` (7,666 B · 116 줄)
- `annals_of_elucia_book_II_2026-04-22.md` (9,250 B · 125 줄)
- `chronicles_of_silvan_2026-04-22.md` (7,816 B · 114 줄) — Ashenveil 간접 언급
- `the_heretics_account_2026-04-22.md` (7,944 B · 111 줄) — 이름 없는 노인 증언 3편
- `mining_guilds_testimony_2026-04-22.md` (7,641 B · 117 줄)

**Master 4 파일**:
- `MASTER_elucia_worldbook.md` (248 줄 · §1~§11)
- `MAP_annotations.md` (143 줄 · 랜드마크 36 항목)
- `relationship_graph.md` (mermaid 2 · 노드 25 · 엣지 16+)
- `integrator_report_2026-04-22.md` (모순 8건 검출 · HIGH 4·MEDIUM 3·LOW 1)

### ✅ 주인공 마을 Ashenveil 심화

- 위치: `wiki/design/worldbuilding/elucia/kingdoms/kingdom_ilaris/villages/village_ashenveil_2026-04-22.md`
- 지리·풍경·주민·가족·6 주요 NPC·경제·역사·전설·연간 수입·의복·외부 연결·방어·약점·Rev.3 서사 접점·집필 감도·프로즈 초안 문장
- 후보 파일 `protagonist_village_candidates_2026-04-22.md` 에 확정 표시 · `selected: ashenveil`

### ✅ Ch.01 LN 본격 집필 초안

- 파일: `wiki/design/novel/ch01.md` (draft_v1 · ~7,100 자)
- 시점: **1인칭 주인공** (대표님 LN 선호 세션 #2 반영 · 세션 #3 3인칭 제한과 재조정)
- 6 섹션 (I 회색빛 아침 · II 이름 없는 할배 · III 서쪽의 까마귀 · IV 목책 너머 · V 붉은 것 · VI 연기, 서쪽으로)
- Q-CORE 1·2·3 봉인 준수 · 마왕·할배·수정·의지결 명칭 직접 서술 X · 은유·감각으로 처리
- 주인공 이름·성별·정확한 나이 `[대표님 결정 대기]` 마커 유지

### ✅ Karzor 동쪽 대륙 MVP 20 파일

- 대륙 레벨 5 (`00_overview` · `geography` · `political_divisions` · `economy` · `culture`)
- 자치구 15 (수도 Zarahim + 14 자치구: Amash · Qorath · Serak · Nahir · Izar · Thari · Morak · Jalim · Azim · Tilnar · Vashir · Rakhel · Omari · Sabin)
- 타종족 75% · 오아시스 도시국가 3 · 사막 부족 4 · 해안 항구 4 · 산악 소수종족 2 · Azim Pass 관문 1 · Zarahim 수도
- 출력 루트: `wiki/design/worldbuilding/karzor/`
- **AI 자율 설계 · 대표님 기상 시 승인/조정 5 포인트**

### ✅ 운영 기록

- 메모리 박제 5건 (세션 #5)
  - `project_session5_qfix_decisions.md` — 10 결정 원문
  - `project_session5_yolo_mode_authorization.md` — 욜로모드 위임 박제
  - `project_session5_qfix_extended_x1_x2.md` — X1·X2 자체 해소
  - `project_session5_qfix_x3_x4_pending.md` — X3·X4 대기
  - `project_session5_ch01_pov_reconciliation.md` — 시점 재조정
- FAIL-011 (cd 3회 재발 · 근본 Hook 재설계 권고)
- FAIL-012 (세션 #4 audit 교차 검사 공백 · 왕명 인덱스 검사관 부재)
- FAIL-013 (세션 #3/#5 POV 설정 드리프트 집필 직전 발견)

---

## 세션 #5 post-wake 대표님 결정 10건 전원 반영 완료

### ✅ A축 — Ch.01 집필 연속 확보

1. **Q-FIX-X3 Oryn 왕세자**: `Aldric Erevorn → Aldryk Erevorn` 확정 · 7 파일 치환 + 파일명 mv 완료 · 모계 혈통 설명 재서술 ("어머니 Lyanna 의 고향 Aldric 왕국 이름에서 음 알드리크")
2. **주인공 확정**: 이름 **나이트** · 성별 **남자** · 나이 **불명** · Ch.01·Ashenveil 심화·outline 전부 반영 완료
3. **시점**: 1인칭 유지 (묵시 승인) · style_bible §1 Act 별 시점 체계로 재조정 (Act 1 1인칭 · Act 2 3인칭 제한 · Act 3 혼용) · "나이트" 이름 이중성 해석 박제

### ✅ B축 — 구조 정합성

4. **생존 확정**: 어머니·아버지·이장·할배·소꿉친구·약초 할머니 **전원 생존** · 사냥꾼 아저씨만 Ch.01 전사 (Act 2 재회 서사 성립) · Ashenveil 파일에 마커
5. **재건 확정**: Act 2 후반 Ashenveil 재건 · 완전 소실 X · 건물 피해 + 생존자 재건 중 · 파일 반영 완료

### ✅ C축 — Karzor MVP 5 결정

6. **Zarahim 성좌 단독** 확정 · 14 자치구 총독은 하위 칭호 X · 기존 현지 호칭 유지 · 00_zarahim 반영
7. **Ch.16 마족 동굴 = Tilnar 중앙 대사막 심부** 확정 · Act 3 핵심 목적지 · tilnar 파일 반영
8. **Nahir 소금 분쟁 해결됨** 확정 · 교역 안정 · 과거 역사적 긴장으로만 · nahir 파일 반영
9. **Thari 인간-타종족 묵인 공존 유지** 확정 · Karzor 내 예외 공간 · thari 파일 반영
10. **Sabin Azim Pass 마법 감지** 확정 · 의지결 각성 주인공 위장 난이도 극대화 · Act 2+ 동료 합류 동기 구조화 · sabin 파일 반영

---

## 다음 세션 (#6) 진입 준비

### 🎯 1순위 — Ch.02 집필

Ch.02 "마을의 저녁" (outline 기존) 집필 조건 충족:
- Ashenveil 탈출 후 나이트가 숲을 며칠 방황
- 첫 인간 마을 도달 (Misthollow 또는 Fernhollow 후보)
- 촌장 환대 · 술집 늙은 학자 만남
- ~6,000~8,000 자 1인칭 LN 스타일 유지

### 🎯 2순위 — Ch.02 전 필요 결정 (대표님 확인)

- 나이트 외형 (머리색·눈색·체형)
- 나이트 가족 이름 (아버지·어머니·형제 유무)
- 소꿉친구 동행 여부·인원
- 이장 할아버지 본명
- Ch.02 도착 마을 선택: Misthollow vs Fernhollow

### 🎯 3순위 — 시스템·장기

- Hook 재설계 (FAIL-011 근본 해결 — CLAUDE_PROJECT_DIR 절대경로)
- 원자 커밋 25~30개 정리 (세션 #3~#5 산출 868+Karzor 20+novel 3)
- Unity 6 Phase 1 착수 (대표님 시간 배분 검토)

---

## 기존 세션 #4 내용 (이력 보존)

## 세션 #4 완료 항목 (2026-04-22) — 대규모 월드빌딩 + 검증 파이프라인

### ✅ Q-CORE 3건 전원 해소 (대표님 직접 확정)

**Q-CORE 1 (마왕 ↔ 할배 관계)**:
- 마왕 ≠ 할배 (완전 별개 존재)
- 마왕 = 태초의 마족 (= 최초의 마족 단독 존재)
- 첫 번째 신 = 할배 = 영감 (3 중 호칭)
- 수호자가 마족 절멸 중 1 명을 선택하여 신으로 승격 → 첫 번째 신
- 시간축 확정: 태초 마왕 → 마족 증식 → 마족 시대 → 마족 붕괴·수호자 개입 → 신 시대 → 인간 시대
- 박제: `memory/project_qcore1_resolved_demon_king_separate.md`

**Q-CORE 2 (할배 동기)**:
- 속죄 확정 — 자신의 판단 미스로 많은 생명을 앗아간 것에 대한 속죄
- 현재 인간의 삶 · 서민에게 유용 생활 마법 무료 배포
- 자기 은닉 원칙 절대 — 신이었던·마족이었던 과거 절대 발설 안 함
- 인간 사회 인식: 그저 "마법 잘하는 착한 할배" (신격·정체 전혀 모름)
- 박제: `memory/project_qcore2_resolved_hope_atonement.md`

**Q-CORE 3 (수정 1·2 기원)**:
- 수정 2 = 태초 마왕이 마족 증식 위해 제작 · 당시 불안정한 마력 붕괴를 수정에 담아 완성
- 수정 1 = 균형 수호자가 **수정 2 를 모방** 해 제작 · 목적 = 마족 발전 제한·감시 · 현재 마족이 자기 장치인 줄 알고 사용
- 수호자의 이중 관리 구조: 할배 (인간 쪽) + 수정 1 (마족 쪽)
- 박제: `memory/project_qcore3_resolved_crystal_two_origin.md`

### ✅ 운영 원칙 4건 박제 (feedback memory)

- `feedback_agent_context_enforcement.md` — 에이전트 spawn 시 STEP 0 필독 7 파일 + 인용 증명 강제
- `feedback_agent_model_default_sonnet.md` — 대량 병렬 fan-out 기본 모델 sonnet 4.6
- `feedback_one_topic_per_file.md` — 한 주제 = 한 파일 원자화 · 왕국별 폴더 독립 · 멀티 토픽 금지
- `feedback_naming_intuitive_dated.md` — 직관적 위치·네이밍 + `<topic>_YYYY-MM-DD.md` 날짜 표기
- MEMORY.md 인덱스 전면 갱신

### ✅ 월드빌딩 에이전트 파이프라인 구축

- **공통 briefing**: `.claude/agents/worldbuilding/_shared_briefing.md` (v2 · 원자 파일 + 왕국 폴더 + 네이밍 규칙 + 날짜 표기 + Q-CORE 봉인)
- **Kingdom-Detailer 템플릿**: `.claude/agents/worldbuilding/kingdom_detailer_template.md`
- **출력 루트**: `wiki/design/worldbuilding/elucia/`

### ✅ Wave 1~4 전원 완료 (총 868 파일)

| Wave | 에이전트 | 파일 |
|------|----------|------|
| 1 | Geographer | 10 |
| 2-1 | Political-Cartographer | 16 |
| 2-2 | Toponymist | 102 (naming 5 + cities 56 + villages 29 + ports 11 + 후보 1) |
| 2-3 | Road-Engineer | 16 |
| 2-4 | Economist | 16 |
| 2-5 | Culturalist | 18 |
| 3-1 | Historian | 31 |
| 3-2 | Diplomat | 37 |
| 4 empire_choir | Kingdom-Detailer | 61 |
| 4 Vaelin | Kingdom-Detailer | 60 |
| 4 Moran | Kingdom-Detailer | 51 |
| 4 Ilaris | Kingdom-Detailer | 62 |
| 4 Ceren | Kingdom-Detailer | 53 |
| 4 Thaloss | Kingdom-Detailer | 54 |
| 4 Maerith | Kingdom-Detailer | 56 |
| 4 Novas | Kingdom-Detailer | 55 |
| 4 Oryn | Kingdom-Detailer | 57 |
| 4 Sylren | Kingdom-Detailer | 58 |
| 4 Aldric | Kingdom-Detailer | 55 |
| **총** | **19 에이전트 (+ 템플릿 공통)** | **868** |

### ✅ 2단계 전수 검사 (10 검사관)

**1차 검사** (Wave 1~3 대륙 레벨 · 176 파일):
- 검사관 A Geography + Political: Cr 0 · Mj 2 · Mn 2
- 검사관 B Economy + Culture: Cr 3 · Mj 6 · Mn 6 (Q-CORE 2 오케스트레이터 설계 오류 포함)
- 검사관 C Roads + Relations: Cr 0 · Mj 1 · Mn 3
- 검사관 D Toponymy + History + Ports: Cr 0 · Issue 1 · Notice 2
- 누적 Cr 3 · Mj 10 · Mn 13

**2차 검사** (Wave 4 왕국 폴더 · 622 파일):
- 검사관 E Empire Choir: Cr 4 · Mj 5 · Mn 4
- 검사관 F North (Vaelin+Thaloss): Cr 1 · Mj 2 · Mn 1
- 검사관 G Coast (Moran+Ilaris+주인공 마을): Cr 2 · Mj 4 · Mn 1
- 검사관 H Wetland (Ceren+Aldric): Cr 2 · Mj 6 · Mn 8
- 검사관 I Forest (Oryn+Maerith): Cr 0 · Mj 2 · Mn 2 (+ 자발적 17 파일 정리)
- 검사관 J South (Sylren+Novas): Cr 0 · Mj 4 · Mn 7
- 누적 Cr 9 · Mj 23 · Mn 23+

### ✅ 수정 작업 3단계

- **1차 통합 수정** (Audit-Fix Integrator): 11건 / 28 파일
  - Critical 3: CR-01 economy overview · CR-02 파일명 `hal_bae_*` → `nameless_scholar_*` · CR-03 religion 격리
  - Major 8: V-001 Frosthelm→Icehelm (5 파일) · V-002 Greyveil Ridge→Veilorn Ridge (15 파일) · MA 및 MAJOR-001
- **검사관 I 자발적 정리**: 17 파일 (Oryn+Maerith + economy·history·relations·empire_choir 의 "할배 마법" 잔재 전수 소거)
- **2차 통합 수정** (Audit-Fix 2nd Integrator): 완료 — Critical 8 + Major 19 + Minor 1 = **28건 / 26 파일**
- 누적 수정: 약 71 파일 (1차 28 + 검사관 I 17 + 2차 26)
- 드리프트 결과: "할배" 공개 노출 전 파일 소거 · Q-CORE 원문 직접 서술 전부 HTML 주석 격리 완료

### ✅ 주인공 마을 후보 20개 산출
- 위치: `wiki/design/worldbuilding/elucia/toponymy/protagonist_village_candidates_2026-04-22.md`
- Silvan 권역 (서쪽 변방 숲) · Toponymist 상위 5 추천:
  1. Ashenveil (안개·회색빛)
  2. Graymoss (이끼·돌 · Nier 감성)
  3. Fernhollow (골짜기 깊숙이 숨겨진)
  4. Dawnwick (새벽 이름이 운명 복선)
  5. Misthollow (마을 전체가 비밀 숨김 · Disco 식)

### ✅ FAIL-007~010 신규 박제 (세션 #4 패턴)
- FAIL-007: 오케스트레이터 설계 오류 — `hal_bae` 파일명 Q-CORE 2 봉인 위반
- FAIL-008: 원전 인용 증명 섹션이 Q-CORE 원문을 공개 산출물에 박제한 역설
- FAIL-009: 자기 정정 5 회 연속 — 대표님 결정 전 가설 강약 추정 반복
- FAIL-010: 병렬 fan-out 왕국 간 이름 공간 충돌 (Aldric·Edric 동명)

---

## 대표님 결정 (세션 #4)

### 확정
1. **Q-CORE 1**: 마왕 ≠ 할배 · 마왕이 태초 마족 · 할배=첫신=영감=승격 마족
2. **Q-CORE 2**: 할배 동기 = 속죄 · 무료 생활 마법 · 자기 정체 절대 은닉
3. **Q-CORE 3**: 수정 2 = 마왕 증식 장치 · 수정 1 = 수호자 함정
4. **인간 사회의 할배 인식** = 그냥 "착한 할배" (신격 미인식)
5. **운영 원칙 4**: 에이전트 원전 필독 · sonnet 4.6 기본 · 한 주제 한 파일 · 날짜 표기 네이밍
6. **에이전트 대규모 fan-out 승인** — 22 에이전트 스쿼드 (최종 19 실행)
7. **전수 검사 지시** — 샘플링 없이 모든 파일 읽기
8. **1차·2차 수정 GO 사인**

### 대기 (Q-FIX 9건)
- [ ] **Q-FIX-1**: Mirvane Port 파일 생성 / `ports/00_overview` 에서 삭제
- [ ] **Q-FIX-2**: Soranwatch (Oryn) vs Soranth (Sylren 권역) 접두 중복 → 유지 / 개명
- [ ] **Q-FIX-3**: Solaris 왕도 지구 수 — 10 / 12 / 13 구획 중 확정
- [ ] **Q-FIX-4**: 교황 "반신적 존재" 표현 — 완전 삭제 / 메모 격리 / 현행 유지
- [ ] **Q-FIX-5**: Aldric 왕(Vaelin) vs Aldric 왕세자(Thaloss) 동명 — 한쪽 개명 / 유지
- [ ] **Q-FIX-6**: Edric Vaen(Vaelin) vs Edric Varn(Thaloss) 공작 동명 — 한쪽 개명 / 유지
- [ ] **Q-FIX-7**: Novas 수도명 Duskgate vs Duskmoor — 원전 기준 / Wave 4 기준
- [ ] **Q-FIX-8**: Coastfen(Aldric) 해염 생산 vs Ceren 소금 독점 — Coastfen 자체 소비만 / 독점 완화 / 분쟁 구조화
- [ ] **Q-FIX-9**: House Seren(Aldric) vs Ceren 왕국 동음 — 가문 개명 / 유지

### 주인공 마을 대표님 선정 대기
- 20 후보 중 택 1 (상위 5: Ashenveil · Graymoss · Fernhollow · Dawnwick · Misthollow)

---

## 다음 세션 (세션 #5) 할 일

### 🎯 1순위 — Q-FIX 9건 결정 + 2차 수정 마무리
- [ ] Q-FIX 1~9 순차 or 일괄 결정
- [ ] 2차 수정 에이전트 완료 보고 확인 · 남은 수정 집행
- [ ] 드리프트 재검증 (Grep `hal_bae` · `Frosthelm` · `Greyveil` = 0 건 확인)

### 🎯 2순위 — Wave 5 (Chronicler + World-Integrator)
- [ ] **Chronicler**: 인-월드 역사 문헌 3~5 편 작성
  - *Annals of Elucia* Book I~III (제국 관점)
  - *Chronicles of Silvan* (북부 왕국 관점)
  - *The Heretics' Account* (양심파 교회 관점)
  - Ch.15·18 벽화 씬에 발췌 인용 가능한 원전
- [ ] **World-Integrator**: 868+ 파일 cross-check
  - 모순 검출·해결 (Seren·Aldric 동명 등 Q-FIX 결정 반영)
  - 지도 오버레이 주석 가이드 (공식 지도 `world_map_OFFICIAL_2026-04-21.png` 좌표 라벨)
  - 전체 관계 그래프 (knowledge-graph skill)
  - MASTER_elucia_worldbook.md · MAP_annotations.md · relationship_graph.md

### 🎯 3순위 — 동쪽 대륙 Karzor 월드빌딩 시작
- [ ] 같은 파이프라인 재사용 — Wave 1 Geographer (Karzor) · Wave 2 5 에이전트 · Wave 3·4·5
- [ ] 26 정치단위 중 동쪽 15 (수도 Zarahim + 14 자치구) 심층 설계
- [ ] 동쪽 특수 요소: 75% 타종족 분포 · 거친 노예시장 · Azim Pass 남단

### 🎯 4순위 — 주인공 마을 확정 + Ch.01 본격 집필
- [ ] 주인공 마을 20 후보 중 대표님 선정
- [ ] 선정 마을 심화 파일 Write
- [ ] Ch.01 LN 스타일 본격 집필 (세션 #3 테스트 샘플 기반)
- [ ] prose-critique skill 사후 검수

### 🎯 5순위 — 세계관 축 나머지 완결
- [ ] 질문 큐 (brainstorm 파일 내 다수) 재검토
- [ ] F 일상 문화 심화 · B 의지결 마족·용족 내재 메커니즘 · E 경제·정치 세부

### 🎯 6순위 — 원자 커밋 대정리
- [ ] 868+ 파일 → 논리 그룹별 원자 커밋 15~25 개
  1. 메모리 박제 (feedback 4 + project 3)
  2. briefing + 템플릿 (2)
  3. Wave 1 Geography (10)
  4. Wave 2-1 Political (16)
  5. Wave 2-2 Toponymy (102)
  6. Wave 2-3 Roads (16)
  7. Wave 2-4 Economy (16)
  8. Wave 2-5 Culture (18)
  9. Wave 3-1 History (31)
  10. Wave 3-2 Relations (37)
  11. Wave 4 empire_choir (61)
  12. Wave 4 Vaelin (60) ... 각 왕국별 커밋
  23. Audit reports (10) + fix_log
  24. FAIL-007~010 추가
  25. 핸드오프 3종 (WORK_HANDOFF · SESSION_LOG · FAILURES)

---

## 세션 #3 완료 항목 (2026-04-21/22)

### ✅ 세계관 브레인스토밍 대규모 확장 (50 발언 원전 capture)
- 신규 원전: `wiki/design/brainstorm_2026-04-21_worldview_expansion.md`
- brainstorming + worldbuilding skill 능동 호출 (FAIL-004 교훈 준수)
- 대표님 발언 50 건 원문 앵커 + AI 해석 + hidden 작가 전용
- 11 개 축 (A~K) 중 6 개 진행 (D·J·A·B·F·E) · 원환 완성

### ✅ 세계관 근본 반전 5단 구조 (Ch.23B 진실 공개)
- 발언 17: 첫 번째 신 = 마족 할배 (실체 버린 정령급)
- 발언 18: 마족 수정 = 슈퍼컴퓨터·AI 판타지 번역
- 발언 19: 황금기 · 인간 기억 왜곡 · 엘프·용족이 진실 보유
- 발언 20: 마족의 인간 멸종 시도 → 균형 수호자 개입
- 발언 27·28: 신성마법 = 마족 창조 · 수정 1 제한 장치 · 수정 2 봉인

### ✅ 마법 시스템 5 계층 확정
- 마족 네이티브 / 할배 주문 (인간 4속성+신성+소환) / 용언·고대 / 오크 주술 / 엘프 자연 마법

### ✅ 세계 지리·정치 완성
- Elucia (서) · Karzor (동) · Veilglass (북 얼음섬) · Nomen (중간섬) · Azim Pass
- **11 정치 단위** (성좌국 1 + 10 왕국) + **15 동쪽** = 26 정치 단위 · **20 권역**
- 네이밍 세트 B 확정 · "술탄" → "성좌" 호칭
- 문서: `wiki/design/political_divisions.md`

### ✅ 캐릭터 공식 레퍼런스 아트 3종 + 세계 지도 공식 (Rev.6)

### ✅ Ch.01 LN 스타일 테스트 샘플 (~2,950자)

### ✅ Nano Banana Pro 스크립트 10+ 개 / 라노벨 3권 분량 결정

### ✅ 운영 원칙 메모리 2건 박제
- `feedback_light_novel_style_preference.md`
- `feedback_brainstorm_question_batching.md`

### ✅ 실패 사례 박제: FAIL-005 (cd 재발) · FAIL-006 (과해석 재발 4건)

---

## 세션 #2 완료 항목 (2026-04-21 후반)

### ✅ 세계관 철학 3조 조문화
- 가. 불완전성 · 나. 나이트 인격체 (한결같음) · 다. 영혼 평등

### ✅ 엔딩 체계 5구조 확정
- 2분기 (인간 vs 화합) × 2회차 + 진엔딩 E

### ✅ 과해석 10건 집단 정정 (FAIL-002)

### ✅ 동료 구조 전면 재편
- Act 1 인간 4 / Act 2 중반 인간 전원 이탈 / Act 2 후반 타종족 4 / Act 3 선택 분기

### ✅ 의지결 × 성인식 장비 시스템 확정 (4층 스킬)

### ✅ 종족 생태학·신앙 경제학

### ✅ 설계 원전 · 종합 스냅샷 · Rev.3 서사

### ✅ 창작 skill 라이브러리 설치 (전역 · 22 skills + 17 agents)
