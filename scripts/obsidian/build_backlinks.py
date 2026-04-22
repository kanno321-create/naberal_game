#!/usr/bin/env python3
"""
build_backlinks.py — Obsidian wiki 자동 백링크 빌더

각 .md 파일의 frontmatter 메타데이터를 스캔해 하단에
<!-- auto-generated-related:start --> / :end 마커로 감싼
"## 🔗 관련 (auto-generated)" 섹션을 자동 삽입/갱신한다.

Idempotent — 동일 입력이면 동일 출력. 마커 바깥의 본문은 절대 건드리지 않음.

규칙 (frontmatter 기반):
  type == moc | master_index | readme | index  →  스킵
  type == village + kingdom:K                  →  루트 MOC + kingdoms/MOC + 왕국 영토 + 형제 마을 3
  type == city + kingdom:K                     →  루트 MOC + kingdoms/MOC + 왕국 영토
  type == political                            →  elucia/MOC + 형제 political
  type in {geography, economy, culture, roads, toponymy, ports, history, relations, chronicles}
                                               →  elucia/MOC + 같은 폴더 00_overview + 형제 2~3
  그 외                                         →  상위 MOC.md 만 링크

실행:
  python scripts/obsidian/build_backlinks.py                # 기본: wiki/ 전체
  python scripts/obsidian/build_backlinks.py --dry-run      # 변경 예상만 출력 (쓰기 없음)
  python scripts/obsidian/build_backlinks.py --root wiki/design/worldbuilding
  python scripts/obsidian/build_backlinks.py --verbose      # 파일별 결정 출력

영속성: session_start.py Hook 이 세션 시작 시 이 스크립트 실행 여부 점검.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

MARKER_START = "<!-- auto-generated-related:start -->"
MARKER_END = "<!-- auto-generated-related:end -->"

SKIP_TYPES = {"moc", "master_index", "readme", "index", "readme_tier2"}
TERRITORY_CATEGORIES = {
    "geography",
    "economy",
    "culture",
    "roads",
    "toponymy",
    "ports",
    "history",
    "relations",
    "chronicles",
    "audit",
}


@dataclass
class NoteMeta:
    """파일의 frontmatter 메타 + 경로 정보."""

    path: Path
    rel_to_wiki: Path
    ntype: str = ""
    kingdom: str = ""
    subject: str = ""
    wave: str = ""
    title: str = ""

    @property
    def slug(self) -> str:
        return self.path.stem

    @property
    def category_dir(self) -> Path:
        """상위 카테고리 폴더 (geography/, political/ 등)."""
        return self.path.parent


@dataclass
class Stats:
    scanned: int = 0
    skipped: int = 0
    updated: int = 0
    unchanged: int = 0
    errors: list[str] = field(default_factory=list)


# ==========================================================================
# Frontmatter 파서 (표준 라이브러리만 사용)
# ==========================================================================


FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """(frontmatter_dict, body_without_frontmatter) 반환.

    YAML 전체가 아니라 `key: value` 단순 1-level 만 파싱. type/kingdom/subject
    같은 스칼라만 필요.
    """
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text

    fm_text = m.group(1)
    body = text[m.end() :]
    result: dict[str, str] = {}

    for line in fm_text.splitlines():
        line = line.rstrip()
        if not line or line.startswith("#") or line.startswith(" ") or line.startswith("\t"):
            # 들여쓴 줄은 list/block — 무시
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        # 따옴표 제거
        if (value.startswith('"') and value.endswith('"')) or (
            value.startswith("'") and value.endswith("'")
        ):
            value = value[1:-1]
        # 배열 리터럴 제거 (첫 요소만 취급)
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            value = inner.split(",")[0].strip().strip('"').strip("'")
        # multiline marker
        if value in {">", "|", ">-", "|-"}:
            value = ""
        result[key] = value

    return result, body


# ==========================================================================
# 규칙 테이블 — frontmatter → 관련 링크 목록
# ==========================================================================


def relpath_wikilink(from_file: Path, target: Path, wiki_root: Path) -> str:
    """from_file 에서 target 까지의 상대경로 wikilink ([[../foo/bar]])."""
    try:
        rel = Path(target).relative_to(wiki_root)
    except ValueError:
        rel = target
    # from_file 도 wiki_root 기준
    try:
        src_rel = from_file.relative_to(wiki_root)
    except ValueError:
        src_rel = from_file
    # os.path.relpath 유사
    src_parts = list(src_rel.parent.parts)
    dst_parts = list(rel.parent.parts)
    # 공통 prefix 제거
    common = 0
    for a, b in zip(src_parts, dst_parts):
        if a == b:
            common += 1
        else:
            break
    up = len(src_parts) - common
    down = dst_parts[common:]
    pieces = [".."] * up + list(down) + [rel.stem]
    link_path = "/".join(pieces) if pieces else rel.stem
    return f"[[{link_path}]]"


KINGDOM_SLUG_ALIASES: dict[str, list[str]] = {
    # frontmatter slug 와 실제 파일명 slug 가 다른 경우의 별칭.
    # 2026-04-22 세션 #6: Wave 2 에이전트 드리프트로 empire_choir (폴더·frontmatter) vs
    # empire_papal (파일명) 분열 발견. frontmatter 는 empire_choir 로 통일했으나
    # political/empire_papal_territories_*.md 파일명은 외부 레퍼런스 보호 위해 유지 →
    # 빌더가 alias 통해 양쪽을 연결.
    "empire_choir": ["empire_papal"],
}


def find_territory_file(wiki_root: Path, kingdom: str) -> Path | None:
    """political/<kingdom|alias>_territories_YYYY-MM-DD.md 탐색."""
    political = wiki_root / "design" / "worldbuilding" / "elucia" / "political"
    if not political.exists():
        return None
    candidates = [kingdom] + KINGDOM_SLUG_ALIASES.get(kingdom, [])
    # 복합 슬러그 처리: empire_choir_sylren_oryn → 첫 토큰만 사용
    if "_" in kingdom:
        head = kingdom.split("_")[0]
        # kingdom_X 복합은 X 만, empire_X 복합은 "empire_X"까지
        if kingdom.startswith("kingdom_") or kingdom.startswith("empire_"):
            parts = kingdom.split("_")
            if len(parts) >= 2:
                base = "_".join(parts[:2])
                if base != kingdom:
                    candidates.append(base)
                    candidates.extend(KINGDOM_SLUG_ALIASES.get(base, []))
    for slug in candidates:
        for p in political.glob(f"{slug}_territories_*.md"):
            return p
    return None


def find_siblings(file_path: Path, n: int = 3) -> list[Path]:
    """같은 폴더의 형제 .md 파일 최대 n 개 (자기 자신 + MOC/overview 제외)."""
    result = []
    for sibling in sorted(file_path.parent.glob("*.md")):
        if sibling == file_path:
            continue
        stem_lower = sibling.stem.lower()
        if stem_lower in {"moc", "00_overview", "_index", "readme"}:
            continue
        result.append(sibling)
        if len(result) >= n:
            break
    return result


def build_related_section(meta: NoteMeta, wiki_root: Path) -> str | None:
    """NoteMeta → 관련 섹션 markdown. 스킵이면 None."""
    ntype = meta.ntype.lower()
    if ntype in SKIP_TYPES:
        return None

    blocks: list[tuple[str, list[str]]] = []  # (section_title, [wikilinks])

    wiki_moc = wiki_root / "MOC.md"
    elucia_moc = wiki_root / "design" / "worldbuilding" / "elucia" / "MOC.md"
    kingdoms_moc = wiki_root / "design" / "worldbuilding" / "elucia" / "kingdoms" / "MOC.md"

    # 상위 허브 — 모든 타입에 공통
    upper = []
    if wiki_moc.exists():
        upper.append(relpath_wikilink(meta.path, wiki_moc, wiki_root) + " — wiki 루트")
    if meta.path.is_relative_to(wiki_root / "design" / "worldbuilding" / "elucia") and elucia_moc.exists():
        upper.append(relpath_wikilink(meta.path, elucia_moc, wiki_root) + " — Elucia 허브")
    if upper:
        blocks.append(("⬆️ 상위", upper))

    # 타입별 규칙
    if ntype == "village" or ntype == "city":
        if meta.kingdom and kingdoms_moc.exists():
            blocks.append(
                (
                    "👑 왕국 허브",
                    [relpath_wikilink(meta.path, kingdoms_moc, wiki_root) + " — 10 왕국 + 성좌국"],
                )
            )
        if meta.kingdom:
            territory = find_territory_file(wiki_root, meta.kingdom)
            if territory:
                blocks.append(
                    (
                        "🏛️ 소속 왕국 영토",
                        [relpath_wikilink(meta.path, territory, wiki_root)],
                    )
                )
        siblings = find_siblings(meta.path, n=3)
        if siblings:
            blocks.append(
                (
                    "🏘️ 형제 " + ("마을" if ntype == "village" else "도시"),
                    [relpath_wikilink(meta.path, s, wiki_root) for s in siblings],
                )
            )

    elif ntype == "political":
        # 정치 폴더 내 형제
        siblings = find_siblings(meta.path, n=4)
        if siblings:
            blocks.append(
                (
                    "🗳️ 형제 정치 문서",
                    [relpath_wikilink(meta.path, s, wiki_root) for s in siblings],
                )
            )

    elif ntype in TERRITORY_CATEGORIES or meta.path.parent.name in TERRITORY_CATEGORIES:
        overview = meta.path.parent / "00_overview.md"
        if overview.exists() and overview != meta.path:
            blocks.append(
                (
                    "📑 카테고리 개요",
                    [relpath_wikilink(meta.path, overview, wiki_root)],
                )
            )
        siblings = find_siblings(meta.path, n=3)
        if siblings:
            blocks.append(
                (
                    "🔗 형제 노드",
                    [relpath_wikilink(meta.path, s, wiki_root) for s in siblings],
                )
            )

    if not blocks:
        return None

    lines = [
        "",
        MARKER_START,
        "## 🔗 관련 (auto-generated)",
        "",
        "> `scripts/obsidian/build_backlinks.py` 로 자동 생성. 수정 금지 — 다음 실행 시 덮어쓰여집니다.",
        "",
    ]
    for title, links in blocks:
        lines.append(f"### {title}")
        lines.append("")
        for ln in links:
            lines.append(f"- {ln}")
        lines.append("")
    lines.append(MARKER_END)
    lines.append("")
    return "\n".join(lines)


# ==========================================================================
# 파일 처리 (idempotent 갱신)
# ==========================================================================


MARKER_BLOCK_RE = re.compile(
    re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END) + r"\n?",
    re.DOTALL,
)


def process_file(path: Path, wiki_root: Path, dry_run: bool, verbose: bool) -> str:
    """파일 처리 결과 문자열: 'skip' | 'update' | 'unchanged' | 'error:...'."""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        return f"error: read {e}"

    fm, body = parse_frontmatter(text)
    if not fm:
        if verbose:
            print(f"  [no-fm] {path.relative_to(wiki_root)}")
        return "skip"

    meta = NoteMeta(
        path=path.resolve(),
        rel_to_wiki=path.relative_to(wiki_root.resolve()) if path.is_relative_to(wiki_root.resolve()) else path,
        ntype=fm.get("type", ""),
        kingdom=fm.get("kingdom", ""),
        subject=fm.get("subject", ""),
        wave=fm.get("wave", ""),
        title=fm.get("title", ""),
    )

    section = build_related_section(meta, wiki_root.resolve())
    if section is None:
        if verbose:
            print(f"  [skip-rule] {meta.rel_to_wiki} (type={meta.ntype})")
        return "skip"

    # 기존 마커 구간 제거 → 재삽입
    cleaned = MARKER_BLOCK_RE.sub("", text).rstrip() + "\n"
    new_text = cleaned + section

    if new_text == text:
        return "unchanged"

    if not dry_run:
        path.write_text(new_text, encoding="utf-8", newline="\n")
    if verbose:
        print(f"  [update] {meta.rel_to_wiki}")
    return "update"


def main() -> int:
    parser = argparse.ArgumentParser(description="Obsidian wiki 자동 백링크 빌더")
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="스캔 루트 (기본: <project_root>/wiki)",
    )
    parser.add_argument("--dry-run", action="store_true", help="쓰기 없이 예상만 출력")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    # 프로젝트 루트 자동 탐색 (.claude/ 있는 곳)
    if args.root is None:
        cur = Path.cwd().resolve()
        for _ in range(10):
            if (cur / ".claude").is_dir() and (cur / "wiki").is_dir():
                args.root = cur / "wiki"
                break
            if cur.parent == cur:
                break
            cur = cur.parent
        if args.root is None:
            print("ERROR: wiki/ 루트 자동 탐색 실패. --root 명시 필요.", file=sys.stderr)
            return 2

    wiki_root = args.root.resolve()
    if not wiki_root.exists():
        print(f"ERROR: {wiki_root} 없음.", file=sys.stderr)
        return 2

    print(f"[build_backlinks] root = {wiki_root}")
    print(f"[build_backlinks] dry_run = {args.dry_run}")

    stats = Stats()
    for md in sorted(wiki_root.rglob("*.md")):
        if ".obsidian" in md.parts:
            continue
        stats.scanned += 1
        result = process_file(md, wiki_root, args.dry_run, args.verbose)
        if result == "update":
            stats.updated += 1
        elif result == "unchanged":
            stats.unchanged += 1
        elif result == "skip":
            stats.skipped += 1
        else:
            stats.errors.append(f"{md.relative_to(wiki_root)}: {result}")

    print()
    print(f"[build_backlinks] scanned : {stats.scanned}")
    print(f"[build_backlinks] updated : {stats.updated}")
    print(f"[build_backlinks] unchanged: {stats.unchanged}")
    print(f"[build_backlinks] skipped : {stats.skipped}")
    if stats.errors:
        print(f"[build_backlinks] errors : {len(stats.errors)}")
        for e in stats.errors[:10]:
            print(f"  - {e}")
    return 0 if not stats.errors else 1


if __name__ == "__main__":
    sys.exit(main())
