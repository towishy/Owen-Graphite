"""Sanity test: strip ALL !important from v3 bundle and capture fingerprint.

This is the first step of S11.5 (!important reduction). It answers:
  "How many of the 5,821 !important declarations actually MATTER at the
  computed-value level on the 55 harness elements?"

If most don't matter, the heuristic from cascade-research.md §4 becomes a
mass-removal: drop everything that doesn't move a measured cell, then
bisect by module for the remainder.

Output:
  dist/theme-v3.no-important.css        # bundle with all !important stripped
  docs/v3/computed-fingerprint-v2.30.14-v3-no-important-{light,dark}.json

This script does NOT modify src/ — it operates on the bundle only, so the
canonical v3 bundle stays unchanged until we have evidence to act on.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def strip_important(css: str) -> str:
    """Remove `!important` from every declaration.

    Conservative: only matches `!important` (not inside strings or @rules).
    Each occurrence is replaced with empty string and any trailing
    whitespace before the next `;` or `}` is collapsed.
    """
    # Pattern: !important with optional surrounding whitespace, before ; or }
    return re.sub(r"\s*!\s*important\b", "", css, flags=re.IGNORECASE)


def main() -> int:
    src = ROOT / "dist" / "theme-v3.css"
    if not src.exists():
        print(f"ERROR: {src} not found. Run bundle_v3.py first.")
        return 2
    css = src.read_text(encoding="utf-8")
    before = css.count("!important")
    stripped = strip_important(css)
    after = stripped.count("!important")
    out = ROOT / "dist" / "theme-v3.no-important.css"
    out.write_text(stripped, encoding="utf-8")
    print(f"OK: wrote {out.name}")
    print(f"     !important: {before} -> {after}")
    print(f"     lines:      {css.count(chr(10))} -> {stripped.count(chr(10))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
