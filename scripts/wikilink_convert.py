"""
STEP 4 — Wikilink 전환 스크립트
00_overview 파일 인덱스 섹션의 backtick 파일 참조를 wikilink로 전환.
일반 파일 내 cross-ref backtick도 전환.
ashenveil 본문은 건드리지 않음.
"""
import os
import re

BASE = r"C:\Users\PC\바탕 화면\naberal_group\naberal_game-main"
VAELIN_DIR = os.path.join(BASE, "wiki", "design", "worldbuilding", "elucia", "kingdoms", "kingdom_vaelin")
ILARIS_DIR = os.path.join(BASE, "wiki", "design", "worldbuilding", "elucia", "kingdoms", "kingdom_ilaris")

FRONTMATTER_RE = re.compile(r'^(---\n.*?\n---\n)', re.DOTALL)

# Pattern: `filename_2026-04-22.md` or `path/filename.md`
# In table cells: | `filename.md` | description |
# In list: - `filename.md`
# In cross-refs: → `filename.md` or `filename.md` 참조

def convert_backtick_to_wikilink(line):
    """Convert `filename.md` to [[filename]] style wikilinks in a line."""
    # Match backtick-wrapped .md file references
    # Skip if it's a code block fence or longer code content
    # Pattern: `something.md`
    def replace_md_backtick(m):
        path = m.group(1)
        # Strip .md extension and path prefix for shortest link
        basename = os.path.basename(path).replace('.md', '')
        # Preserve original path context but use shortest form for wikilink
        return f"[[{basename}]]"

    # Replace `*.md` patterns (file references in prose/tables/lists)
    # But not in code blocks
    result = re.sub(r'`([^`]+\.md)`', replace_md_backtick, line)
    return result


def process_file(fpath, kingdom, is_ashenveil=False):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Split into frontmatter + body
    m = FRONTMATTER_RE.match(content)
    if not m:
        return False

    frontmatter = m.group(1)
    body = content[len(frontmatter):]

    # ashenveil: don't touch body
    if is_ashenveil:
        return False

    # Convert body lines
    lines = body.split('\n')
    new_lines = []
    in_code_block = False
    changed = False

    for line in lines:
        # Track code blocks
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            new_lines.append(line)
            continue

        if in_code_block:
            new_lines.append(line)
            continue

        # Convert backtick .md references
        new_line = convert_backtick_to_wikilink(line)
        if new_line != line:
            changed = True
        new_lines.append(new_line)

    if not changed:
        return False

    new_body = '\n'.join(new_lines)
    new_content = frontmatter + new_body

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True


def main():
    total = 0
    updated = 0

    for base_dir, kingdom in [(VAELIN_DIR, "kingdom_vaelin"), (ILARIS_DIR, "kingdom_ilaris")]:
        for root, dirs, files in os.walk(base_dir):
            dirs.sort()
            for fname in sorted(files):
                if not fname.endswith(".md"):
                    continue
                fpath = os.path.join(root, fname)
                is_ashenveil = (fname == "village_ashenveil_2026-04-22.md" and kingdom == "kingdom_ilaris")
                total += 1
                result = process_file(fpath, kingdom, is_ashenveil)
                if result:
                    updated += 1
                    print(f"  [WIKILINK] {fname}")

    print(f"\n=== DONE ===")
    print(f"Total: {total} | Wikilink-converted: {updated}")


if __name__ == "__main__":
    main()
