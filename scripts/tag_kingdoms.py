"""
Layer C Tagging Agent — Vaelin + Ilaris kingdoms
Applies Layer 2 frontmatter to all files, Layer 1 to 00_overview (already done).
"""
import os
import re

BASE = r"C:\Users\PC\바탕 화면\naberal_group\naberal_game-main"
VAELIN_DIR = os.path.join(BASE, "wiki", "design", "worldbuilding", "elucia", "kingdoms", "kingdom_vaelin")
ILARIS_DIR = os.path.join(BASE, "wiki", "design", "worldbuilding", "elucia", "kingdoms", "kingdom_ilaris")

FRONTMATTER_RE = re.compile(r'^---\n(.*?)\n---', re.DOTALL)


def get_category_tag(filepath, kingdom):
    fp = filepath.replace("\\", "/")
    fname = os.path.basename(fp)
    if "royals" in fp:
        return "royals"
    if "nobles" in fp:
        return "nobles"
    if "houses" in fp:
        return "houses"
    if "orders" in fp:
        return "orders"
    if "villages" in fp:
        return "villages"
    if "cities" in fp:
        return "cities"
    if "roads" in fp:
        return "roads"
    if "festivals" in fp:
        return "festivals"
    if "history" in fp:
        return "history"
    if "military" in fname:
        return "military"
    if "heraldry" in fname:
        return "heraldry"
    if "architecture" in fname:
        return "architecture"
    if "clothing" in fname:
        return "clothing"
    if "cuisine" in fname:
        return "cuisine"
    if "dialect" in fname:
        return "dialect"
    if "capital_map" in fname:
        return "geography"
    return "worldbuilding"


def get_canon_anchors(filepath, kingdom):
    fp = filepath.replace("\\", "/")
    fname = os.path.basename(fp)

    if kingdom == "kingdom_vaelin":
        base_anchors = [
            ('  - src: "[[political_divisions]]:53"',
             '    quote: "바엘린 / Vaelin / 북부 평원"'),
            ('  - src: "[[story_full_narrative]]"',
             '    quote: "세계관 철학 3조 — 불완전성·한결같음·영혼 평등"'),
        ]
        if "royals" in fp or "nobles" in fp:
            base_anchors.insert(0, (
                '  - src: "[[kingdom_vaelin/history/founding_2026-04-22]]:37"',
                '    quote: "초원의 늑대가 한 전사를 왕으로 인정했을 때, 그의 이름이 바엘린이 되었다."'
            ))
        elif "history" in fp:
            base_anchors.insert(0, (
                '  - src: "[[kingdom_vaelin/history/founding_2026-04-22]]:37"',
                '    quote: "초원의 늑대가 한 전사를 왕으로 인정했을 때, 그의 이름이 바엘린이 되었다."'
            ))
        elif "military" in fname or "orders" in fp:
            base_anchors.insert(0, (
                '  - src: "[[brainstorm_2026-04-21_worldview_expansion]] 발언 5"',
                '    quote: "서쪽은 징병제가 발달한 중세 유럽 스타일 봉건국가들"'
            ))
        elif "villages" in fp or "cities" in fp:
            base_anchors.insert(0, (
                '  - src: "[[political_divisions]]:109"',
                '    quote: "Havren / 하브렌 / 북서 해안 / 모란·바엘린 왕국"'
            ))
    else:  # kingdom_ilaris
        base_anchors = [
            ('  - src: "[[political_divisions]]:55"',
             '    quote: "일라리스 / Ilaris / 서해안"'),
            ('  - src: "[[story_full_narrative]]"',
             '    quote: "세계관 철학 3조 — 불완전성·한결같음·영혼 평등"'),
        ]
        if "royals" in fp or "nobles" in fp or "houses" in fp:
            base_anchors.insert(0, (
                '  - src: "[[kingdom_ilaris/history/founding_2026-04-22]]"',
                '    quote: "교황청과의 관계: 복종하되 이단 심문관 파견은 내심 불만"'
            ))
        elif "military" in fname or "orders" in fp:
            base_anchors.insert(0, (
                '  - src: "[[brainstorm_2026-04-21_worldview_expansion]] 발언 5"',
                '    quote: "좌측은 강이 많고 풍요로움"'
            ))
        elif "villages" in fp or "cities" in fp:
            base_anchors.insert(0, (
                '  - src: "[[political_divisions]]:110"',
                '    quote: "Silvan / 실반 / 서해안 숲 / 일라리스 왕국"'
            ))
        elif "history" in fp:
            base_anchors.insert(0, (
                '  - src: "[[brainstorm_2026-04-21_worldview_expansion]] 발언 5"',
                '    quote: "좌측은 강이 많고 풍요로움"'
            ))

    # Build YAML block
    lines = ["canon_anchors:"]
    for src, quote in base_anchors[:3]:
        lines.append(src)
        lines.append(quote)
    return "\n".join(lines)


def get_related(filepath, kingdom):
    fp = filepath.replace("\\", "/")
    fname = os.path.basename(fp)

    if kingdom == "kingdom_vaelin":
        related = ["  - \"[[kingdom_vaelin/00_overview]]\""]
        if "royals" in fp:
            related += [
                "  - \"[[kingdom_vaelin/houses/house_vaen_2026-04-22]]\"",
                "  - \"[[kingdom_vaelin/military_2026-04-22]]\""
            ]
        elif "nobles" in fp:
            related += [
                "  - \"[[kingdom_vaelin/military_2026-04-22]]\"",
                "  - \"[[kingdom_vaelin/heraldry_2026-04-22]]\""
            ]
        elif "houses" in fp:
            related += [
                "  - \"[[kingdom_vaelin/heraldry_2026-04-22]]\"",
                "  - \"[[kingdom_vaelin/royals/king_aldric_vaen_2026-04-22]]\""
            ]
        elif "orders" in fp:
            related += [
                "  - \"[[kingdom_vaelin/military_2026-04-22]]\"",
                "  - \"[[kingdom_vaelin/royals/king_aldric_vaen_2026-04-22]]\""
            ]
        elif "villages" in fp:
            related += [
                "  - \"[[kingdom_vaelin/capital_map_2026-04-22]]\"",
                "  - \"[[political_divisions]]\""
            ]
        elif "cities" in fp:
            related += [
                "  - \"[[kingdom_vaelin/capital_map_2026-04-22]]\"",
                "  - \"[[kingdom_vaelin/military_2026-04-22]]\""
            ]
        elif "roads" in fp:
            related += [
                "  - \"[[kingdom_vaelin/capital_map_2026-04-22]]\"",
                "  - \"[[political_divisions]]\""
            ]
        elif "festivals" in fp:
            related += [
                "  - \"[[kingdom_vaelin/clothing_2026-04-22]]\"",
                "  - \"[[kingdom_vaelin/cuisine_2026-04-22]]\""
            ]
        elif "history" in fp:
            related += [
                "  - \"[[kingdom_vaelin/royals/king_aldric_vaen_2026-04-22]]\"",
                "  - \"[[kingdom_vaelin/military_2026-04-22]]\""
            ]
        else:
            related += [
                "  - \"[[kingdom_vaelin/military_2026-04-22]]\"",
                "  - \"[[political_divisions]]\""
            ]
    else:  # kingdom_ilaris
        related = ["  - \"[[kingdom_ilaris/00_overview]]\""]
        if "royals" in fp:
            related += [
                "  - \"[[kingdom_ilaris/houses/house_maeran_2026-04-22]]\"",
                "  - \"[[kingdom_ilaris/military_2026-04-22]]\""
            ]
        elif "nobles" in fp:
            related += [
                "  - \"[[kingdom_ilaris/military_2026-04-22]]\"",
                "  - \"[[kingdom_ilaris/heraldry_2026-04-22]]\""
            ]
        elif "houses" in fp:
            related += [
                "  - \"[[kingdom_ilaris/heraldry_2026-04-22]]\"",
                "  - \"[[kingdom_ilaris/royals/king_aerric_maeran_2026-04-22]]\""
            ]
        elif "orders" in fp:
            related += [
                "  - \"[[kingdom_ilaris/military_2026-04-22]]\"",
                "  - \"[[kingdom_ilaris/royals/king_aerric_maeran_2026-04-22]]\""
            ]
        elif "villages" in fp:
            related += [
                "  - \"[[kingdom_ilaris/capital_map_2026-04-22]]\"",
                "  - \"[[political_divisions]]\""
            ]
        elif "cities" in fp:
            related += [
                "  - \"[[kingdom_ilaris/capital_map_2026-04-22]]\"",
                "  - \"[[kingdom_ilaris/military_2026-04-22]]\""
            ]
        elif "roads" in fp:
            related += [
                "  - \"[[kingdom_ilaris/capital_map_2026-04-22]]\"",
                "  - \"[[political_divisions]]\""
            ]
        elif "festivals" in fp:
            related += [
                "  - \"[[kingdom_ilaris/clothing_2026-04-22]]\"",
                "  - \"[[kingdom_ilaris/cuisine_2026-04-22]]\""
            ]
        elif "history" in fp:
            related += [
                "  - \"[[kingdom_ilaris/royals/king_aerric_maeran_2026-04-22]]\"",
                "  - \"[[kingdom_ilaris/military_2026-04-22]]\""
            ]
        else:
            related += [
                "  - \"[[kingdom_ilaris/military_2026-04-22]]\"",
                "  - \"[[political_divisions]]\""
            ]

    lines = ["related:"] + related[:3]
    return "\n".join(lines)


def build_new_frontmatter(title, kingdom, cat_tag, canon_anchors_str, related_str, is_ashenveil=False):
    overview_ref = f"[[{kingdom}/00_overview]]"
    moc_path = "[[../../../../design/MOC]]"

    fm = f"""---
title: {title}
layer: 2
canon_tier: detail
tags: [worldbuilding, elucia, {kingdom}, {cat_tag}]
updated: 2026-04-22
kingdom: "{kingdom}"
parent: "{overview_ref}"
moc: "{moc_path}"
derived_from:
  - "[[story_full_narrative]]"
  - "[[brainstorm_2026-04-21_worldview_expansion]]"
{canon_anchors_str}
{related_str}
agent_briefing_level: reference"""
    fm += "\n---"
    return fm


def process_file(fpath, kingdom):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Parse existing frontmatter
    m = FRONTMATTER_RE.match(content)
    if not m:
        print(f"  [SKIP - no frontmatter] {os.path.basename(fpath)}")
        return False

    existing_fm = m.group(1)
    body = content[m.end():]

    # Extract title
    title_match = re.search(r'^title:\s*(.+)$', existing_fm, re.MULTILINE)
    if not title_match:
        print(f"  [SKIP - no title] {os.path.basename(fpath)}")
        return False
    title_val = title_match.group(1).strip()

    # Check if already tagged
    if re.search(r'^layer:\s*\d', existing_fm, re.MULTILINE):
        print(f"  [ALREADY TAGGED] {os.path.basename(fpath)}")
        return False

    # Special case: ashenveil - frontmatter only, no body change
    is_ashenveil = "ashenveil" in fpath.replace("\\", "/").lower() and kingdom == "kingdom_ilaris"

    cat_tag = get_category_tag(fpath, kingdom)
    canon_anchors_str = get_canon_anchors(fpath, kingdom)
    related_str = get_related(fpath, kingdom)

    new_fm = build_new_frontmatter(title_val, kingdom, cat_tag, canon_anchors_str, related_str, is_ashenveil)

    # Preserve remaining existing fields that are NOT in new FM (type, role, wave, agent, etc.)
    # We keep them appended after agent_briefing_level
    # Actually let's preserve them by inserting them before closing ---
    preserve_keys = []
    for line in existing_fm.split("\n"):
        key_match = re.match(r'^(\w[\w_]*):', line)
        if key_match:
            key = key_match.group(1)
            if key not in {"title", "layer", "canon_tier", "tags", "updated", "kingdom",
                           "parent", "moc", "derived_from", "canon_anchors", "related",
                           "agent_briefing_level", "created", "agent", "wave", "type", "role",
                           "status", "version", "selected_protagonist_village", "qcore_version",
                           "region", "tier"}:
                preserve_keys.append(line)
            elif key in {"created", "type", "role", "agent", "wave", "region", "tier",
                         "selected_protagonist_village", "qcore_version"}:
                preserve_keys.append(line)

    if preserve_keys:
        # Insert before closing ---
        new_fm = new_fm[:-4] + "\n" + "\n".join(preserve_keys) + "\n---"

    new_content = new_fm + body

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True


def main():
    total = 0
    updated = 0
    skipped = 0

    for base_dir, kingdom in [(VAELIN_DIR, "kingdom_vaelin"), (ILARIS_DIR, "kingdom_ilaris")]:
        for root, dirs, files in os.walk(base_dir):
            dirs.sort()
            for fname in sorted(files):
                if not fname.endswith(".md"):
                    continue
                if fname == "00_overview.md":
                    continue  # already done
                fpath = os.path.join(root, fname)
                total += 1
                result = process_file(fpath, kingdom)
                if result:
                    updated += 1
                    print(f"  [UPDATED] {fname}")
                else:
                    skipped += 1

    print(f"\n=== DONE ===")
    print(f"Total: {total} | Updated: {updated} | Skipped: {skipped}")


if __name__ == "__main__":
    main()
