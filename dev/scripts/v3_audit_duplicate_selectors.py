"""Audit duplicate selectors across the v3 src/ tree.

Produces two reports:

1. **Safe in-file duplicates** — same `src/*.css` file, same selector
   (whitespace-normalised), same declaration body, same enclosing at-rule
   context. These are pure no-op duplicates whose removal cannot change
   rendered styles. Removal candidates.

2. **Cross-file selector groups** — same selector appears in 2+ different
   `src/*.css` files. These are usually intentional (dark / print / hotfix
   override layers). Reported for awareness only.

Read-only: never edits files.

Usage:
    python dev/scripts/v3_audit_duplicate_selectors.py
    python dev/scripts/v3_audit_duplicate_selectors.py --threshold 4
"""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT / "src"


def normalize_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def tokenize_blocks(css: str):
    """Yield (selector, body, at_context, line_no) for each top-level rule.

    Handles nested at-rules (`@media`, `@supports`, `@layer`, `@container`)
    by tracking the enclosing at-rule chain as `at_context`.
    """
    css = css.lstrip("\ufeff")
    i = 0
    n = len(css)
    at_stack: list[str] = []
    line = 1

    def advance_lines(start: int, end: int) -> None:
        nonlocal line
        line += css.count("\n", start, end)

    while i < n:
        if css.startswith("/*", i):
            j = css.find("*/", i + 2)
            if j == -1:
                return
            advance_lines(i, j + 2)
            i = j + 2
            continue
        ch = css[i]
        if ch.isspace():
            if ch == "\n":
                line += 1
            i += 1
            continue
        if ch == "@":
            j = i
            while j < n and css[j] not in "{;":
                if css[j] == "\n":
                    line += 1
                j += 1
            if j >= n:
                return
            if css[j] == ";":
                i = j + 1
                continue
            header = normalize_ws(css[i:j])
            at_stack.append(header)
            i = j + 1
            block_start = i
            depth = 1
            while i < n and depth > 0:
                c = css[i]
                if c == "/" and css.startswith("/*", i):
                    end = css.find("*/", i + 2)
                    if end == -1:
                        return
                    advance_lines(i, end + 2)
                    i = end + 2
                    continue
                if c == "{":
                    depth += 1
                elif c == "}":
                    depth -= 1
                    if depth == 0:
                        break
                if c == "\n":
                    line += 1
                i += 1
            inner = css[block_start:i]
            inner_line_offset = css.count("\n", 0, block_start) + 1
            for sel, body, inner_ctx, sub_line in tokenize_blocks(inner):
                full_ctx = " >> ".join(at_stack[:-1] + [header] + ([inner_ctx] if inner_ctx else []))
                yield sel, body, full_ctx, inner_line_offset + sub_line - 1
            at_stack.pop()
            i += 1
            continue
        sel_start = i
        j = i
        while j < n:
            c = css[j]
            if c == "/" and css.startswith("/*", j):
                end = css.find("*/", j + 2)
                if end == -1:
                    return
                advance_lines(j, end + 2)
                j = end + 2
                continue
            if c in "{}":
                break
            j += 1
        if j >= n or css[j] != "{":
            i = j + 1
            continue
        selector = css[sel_start:j].strip()
        advance_lines(i, j + 1)
        i = j + 1
        depth = 1
        body_start = i
        while i < n and depth > 0:
            c = css[i]
            if c == "/" and css.startswith("/*", i):
                end = css.find("*/", i + 2)
                if end == -1:
                    return
                advance_lines(i, end + 2)
                i = end + 2
                continue
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    break
            if c == "\n":
                line += 1
            i += 1
        body = css[body_start:i]
        at_context = " >> ".join(at_stack)
        yield normalize_ws(selector), normalize_ws(body), at_context, line
        i += 1


def scan_module(path: Path):
    css = path.read_text(encoding="utf-8")
    by_key: dict[tuple[str, str, str], list[int]] = defaultdict(list)
    for sel, body, ctx, line in tokenize_blocks(css):
        if not sel or not body:
            continue
        key = (sel, body, ctx)
        by_key[key].append(line)
    candidates = []
    for (sel, body, ctx), lines in by_key.items():
        if len(lines) > 1:
            candidates.append((sel, body, ctx, lines))
    return candidates


def cross_file_groups(src_dir: Path):
    """Map normalized selector -> list[(file, line, ctx)]."""
    by_sel: dict[str, list[tuple[str, int, str]]] = defaultdict(list)
    for css_path in sorted(src_dir.rglob("*.css")):
        css = css_path.read_text(encoding="utf-8")
        for sel, body, ctx, line in tokenize_blocks(css):
            if not sel:
                continue
            rel = css_path.relative_to(ROOT).as_posix()
            by_sel[sel].append((rel, line, ctx))
    return by_sel


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--threshold",
        type=int,
        default=4,
        help="Report cross-file selector groups with >= this many occurrences "
        "(default: 4). Lower the number to see more groups.",
    )
    args = parser.parse_args()

    if not SRC_DIR.is_dir():
        print(f"ERROR: src/ not found at {SRC_DIR}")
        return 2

    # === Report 1: safe in-file duplicates ===
    print("=" * 70)
    print("REPORT 1 - Safe in-file duplicates (auto-removable)")
    print("=" * 70)
    safe_total = 0
    safe_files = 0
    for css_path in sorted(SRC_DIR.rglob("*.css")):
        dupes = scan_module(css_path)
        if not dupes:
            continue
        safe_files += 1
        rel = css_path.relative_to(ROOT).as_posix()
        print(f"\n{rel} : {len(dupes)} group(s)")
        for sel, body, ctx, lines in sorted(dupes, key=lambda d: d[3][0]):
            ctx_note = f"  @ctx: {ctx}" if ctx else ""
            print(f"  lines {lines}  sel: {sel[:90]}{'...' if len(sel) > 90 else ''}{ctx_note}")
            safe_total += len(lines) - 1
    print(f"\n  TOTAL safe-removable extra copies: {safe_total}")
    print(f"  Modules with safe duplicates: {safe_files}")

    # === Report 2: cross-file selector groups ===
    print()
    print("=" * 70)
    print(f"REPORT 2 - Cross-file selector groups (>= {args.threshold} occurrences)")
    print("=" * 70)
    by_sel = cross_file_groups(SRC_DIR)
    big_groups = []
    cross_total = 0
    for sel, occurrences in by_sel.items():
        # Skip same-file groups (already covered by Report 1)
        files = {o[0] for o in occurrences}
        if len(files) < 2:
            continue
        if len(occurrences) >= args.threshold:
            big_groups.append((sel, occurrences))
        cross_total += 1
    big_groups.sort(key=lambda g: -len(g[1]))
    for sel, occurrences in big_groups[:30]:
        print(f"\n  {len(occurrences)}x  {sel[:100]}{'...' if len(sel) > 100 else ''}")
        for path, line, ctx in occurrences[:10]:
            ctx_note = f"  @ctx: {ctx[:40]}" if ctx else ""
            print(f"    {path}:{line}{ctx_note}")
        if len(occurrences) > 10:
            print(f"    ... (+{len(occurrences) - 10} more)")
    print(
        f"\n  Cross-file selector groups (any size): {cross_total}; "
        f"shown above (>= {args.threshold}): {len(big_groups)}."
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
