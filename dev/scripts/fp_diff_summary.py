#!/usr/bin/env python3
"""Summarize the v3 fingerprint diff by element.

Reads both the v2.30.14 baseline and the freshly captured v3 candidate from
`docs/v3/computed-fingerprint-v<version>-*.json` and prints a per-element
count of mismatching properties. Useful for tracking S3-S6 closure progress.

Usage:
    python dev/scripts/fp_diff_summary.py
    python dev/scripts/fp_diff_summary.py --theme dark
"""

import argparse
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--theme", choices=["light", "dark"], default="light")
    parser.add_argument(
        "--baseline",
        type=Path,
        default=None,
        help="Baseline fingerprint JSON. Defaults to v2.30.14 baseline for the chosen theme.",
    )
    parser.add_argument(
        "--candidate",
        type=Path,
        default=None,
        help="Candidate fingerprint JSON. Defaults to v2.30.14 v3 build for the chosen theme.",
    )
    args = parser.parse_args()

    baseline_path = args.baseline or (
        ROOT / "docs" / "v3" / f"computed-fingerprint-v2.30.14-{args.theme}.json"
    )
    candidate_path = args.candidate or (
        ROOT / "docs" / "v3" / f"computed-fingerprint-v2.30.14-v3-{args.theme}.json"
    )
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    candidate = json.loads(candidate_path.read_text(encoding="utf-8"))

    b = baseline["elements"]
    c = candidate["elements"]

    per_element: Counter[str] = Counter()
    for elem in set(b) | set(c):
        bp = b.get(elem, {})
        cp = c.get(elem, {})
        for prop in set(bp) | set(cp):
            if bp.get(prop) != cp.get(prop):
                per_element[elem] += 1

    total = sum(per_element.values())
    print(f"baseline:  {baseline_path.relative_to(ROOT)}")
    print(f"candidate: {candidate_path.relative_to(ROOT)}")
    print(f"Total diffs:        {total}")
    print(f"Elements with diffs: {len(per_element)} / {len(set(b) | set(c))}")
    print()
    print(f"{'element':<32} {'diff count':>10}")
    for elem, n in per_element.most_common():
        print(f"{elem:<32} {n:>10}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
