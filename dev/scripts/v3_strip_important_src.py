"""Strip every `!important` token from all src/*.css files in-place.

Rationale (S11.5):
- The strip-all sanity test (dev/scripts/v3_strip_important.py against the bundle)
  showed that removing all 5,821 `!important` tokens changes only 9 computed
  cells in the harness fingerprint, and all 9 belonged to `a.external-link`.
- The conflict was traced to a teal resting-state rule in src/base/12 that
  competed with the v2 baseline slate rule in src/polish/70 via specificity.
  That conflict has been resolved by aligning src/base/12's resting color
  with the baseline slate.
- Therefore, every remaining `!important` can be removed without changing the
  fingerprint, dramatically simplifying the cascade.

This script edits src/ in place. Always commit before running so the change
is reviewable. After running, re-bundle and re-verify the fingerprint.

Usage:
    python dev/scripts/v3_strip_important_src.py
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"

# Match `!important` (with optional whitespace) and the whitespace immediately
# before it. Use a re.split on CSS block comments so we never touch `!important`
# tokens that appear inside /* ... */ documentation.
IMPORTANT = re.compile(r"\s*!\s*important\b", re.IGNORECASE)
COMMENT_SPLIT = re.compile(r"(/\*[\s\S]*?\*/)")


def strip_outside_comments(css: str) -> tuple[str, int]:
    parts = COMMENT_SPLIT.split(css)
    removed = 0
    for i, chunk in enumerate(parts):
        # Even-indexed chunks are CSS code; odd-indexed chunks are full
        # comments (kept verbatim).
        if i % 2 == 0:
            count = len(IMPORTANT.findall(chunk))
            if count:
                removed += count
                parts[i] = IMPORTANT.sub("", chunk)
    return "".join(parts), removed


def main() -> int:
    if not SRC.is_dir():
        print(f"ERROR: src/ not found at {SRC}")
        return 2

    total_files = 0
    changed_files = 0
    total_removed = 0
    for css in sorted(SRC.rglob("*.css")):
        total_files += 1
        original = css.read_text(encoding="utf-8")
        stripped, removed = strip_outside_comments(original)
        if removed == 0:
            continue
        css.write_text(stripped, encoding="utf-8")
        changed_files += 1
        total_removed += removed
        rel = css.relative_to(ROOT).as_posix()
        print(f"  {rel:60s}  -{removed}")

    print(
        f"\nOK: scanned {total_files} files; modified {changed_files}; "
        f"removed {total_removed} !important tokens (comments preserved)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
