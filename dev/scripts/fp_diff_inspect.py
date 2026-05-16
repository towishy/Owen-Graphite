#!/usr/bin/env python3
"""Print every property diff for a single fingerprint element.

Useful when fp_diff_summary.py points to a hot spot and you want to see which
specific computed properties drifted. Defaults to the light theme.

Usage:
    python dev/scripts/fp_diff_inspect.py reading-h1
    python dev/scripts/fp_diff_inspect.py callout-warning --theme dark
"""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("element", help="data-fp-id value of the element to inspect.")
    parser.add_argument("--theme", choices=["light", "dark"], default="light")
    args = parser.parse_args()

    baseline_path = ROOT / "docs" / "v3" / f"computed-fingerprint-v2.30.14-{args.theme}.json"
    candidate_path = ROOT / "docs" / "v3" / f"computed-fingerprint-v2.30.14-v3-{args.theme}.json"
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    candidate = json.loads(candidate_path.read_text(encoding="utf-8"))

    b = baseline["elements"].get(args.element, {})
    c = candidate["elements"].get(args.element, {})
    if not b and not c:
        print(f"element not found in either fingerprint: {args.element}")
        return 1
    any_diff = False
    for prop in sorted(set(b) | set(c)):
        bv = b.get(prop, "<absent>")
        cv = c.get(prop, "<absent>")
        if bv != cv:
            any_diff = True
            print(f"  {prop}")
            print(f"    - {bv}")
            print(f"    + {cv}")
    if not any_diff:
        print(f"{args.element}: no diffs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
