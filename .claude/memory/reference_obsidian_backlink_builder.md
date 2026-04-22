---
name: Obsidian 자동 백링크 빌더 사용법
description: scripts/obsidian/build_backlinks.py — frontmatter 기반 자동 백링크 · idempotent · wiki/ 전 파일 대상
type: reference
created: 2026-04-22
originSessionId: aa89454c-e339-4aaa-9510-76f7c7d0d6ba
---
# build_backlinks.py — 사용 레퍼런스

## 위치

- 스튜디오 실행본: `scripts/obsidian/build_backlinks.py`
- 하네스 마스터: `../../harness/scripts/obsidian_build_backlinks.py`

## 실행

```bash
python scripts/obsidian/build_backlinks.py                # wiki/ 전체 갱신
python scripts/obsidian/build_backlinks.py --dry-run      # 변경 예상만 출력 (쓰기 없음)
python scripts/obsidian/build_backlinks.py --verbose      # 파일별 결정 출력
python scripts/obsidian/build_backlinks.py --root wiki/design/worldbuilding  # 하위 범위만
```

## 동작

각 `.md` 파일의 frontmatter `type:` · `kingdom:` · `subject:` 읽어 규칙 테이블 매칭 →
파일 하단에 `<!-- auto-generated-related:start --> ... :end -->` 마커로 감싼
`## 🔗 관련 (auto-generated)` 섹션 삽입/갱신.

**Idempotent** — 기존 마커 구간은 제거 후 재생성. 마커 바깥 본문은 절대 건드리지 않음.

## 규칙 테이블

| frontmatter `type` | 생성 링크 |
|-------------------|---------|
| `moc`, `master_index`, `readme`, `index` | **스킵** (허브는 수동 관리) |
| `village`, `city` + `kingdom: K` | 루트 MOC + kingdoms MOC + 왕국 영토 파일 + 형제 3개 |
| `political` | elucia MOC + 형제 4개 |
| `geography`, `economy`, `culture`, `roads`, `toponymy`, `ports`, `history`, `relations`, `chronicles` | elucia MOC + 같은 폴더 00_overview + 형제 3개 |
| 그 외 | 상위 MOC 만 |

## 결과 (2026-04-22 초기 실행)

- 838 파일 스캔
- 832 파일 업데이트 (99.3% 커버리지)
- 6 파일 스킵 (MOC · master_index)
- 에러 0

## 영속성 연결

- session_start.py Hook 의 `check_obsidian_vault()` 가 매 세션 커버리지 측정 → 85% 미만이면 경고 주입
- 새 wiki 파일 생성 후 반드시 재실행
