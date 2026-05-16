"""Audit duplicate selectors across the v3 src/ tree and the bundle.

This is the v3 analogue of `scripts/find_safe_duplicate_selectors.py`, which only
scans `dev/` per-file. It produces two reports:

1. **Safe in-file duplicates** — same `src/*.css` file, same selector
   (whitespace-normalised), same declaration body, same enclosing at-rule
   context. These are pure no-op duplicates whose removal cannot change
   rendered styles. Removal candidates.

2. **Cross-file selector groups** — same selector appears in 2+ different
   `src/*.css` files. These are usually intentional (dark / print / hotfix
   override layers). Reported for awareness only.

Read-only: never edits files.

Usage:
    python scripts/v3_audit_duplicate_selectors.py
    python scripts/v3_audit_duplicate_selectors.py --threshold 4
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path

import sys

# Reuse the proven CSS tokenizer from the dev-side script
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from find_safe_duplicate_selectors import (  # type: ignore
    scan_module,
    tokenize_blocks,
    normalize_ws,
)

SRC_DIR = ROOT / "src"


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
    print("REPORT 1 — Safe in-file duplicates (auto-removable)")
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
            print(f"  lines {lines}  sel: {sel[:90]}{'…' if len(sel) > 90 else ''}{ctx_note}")
            safe_total += len(lines) - 1
    print(f"\n  TOTAL safe-removable extra copies: {safe_total}")
    print(f"  Modules with safe duplicates: {safe_files}")

    # === Report 2: cross-file selector groups ===
    print()
    print("=" * 70)
    print(f"REPORT 2 — Cross-file selector groups (>= {args.threshold} occurrences)")
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
        print(f"\n  {len(occurrences)}x  {sel[:100]}{'…' if len(sel) > 100 else ''}")
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
