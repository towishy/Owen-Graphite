#!/usr/bin/env python3
"""Diff two effective snapshot JSON files."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("baseline", type=Path)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--limit", type=int, default=200)
    args = parser.parse_args()
    baseline = json.loads(args.baseline.read_text(encoding="utf-8"))
    candidate = json.loads(args.candidate.read_text(encoding="utf-8"))
    failures: list[str] = []
    b_targets = baseline.get("targets", {})
    c_targets = candidate.get("targets", {})
    for target in sorted(set(b_targets) | set(c_targets)):
        if target not in b_targets:
            failures.append(f"EXTRA target {target}")
            continue
        if target not in c_targets:
            failures.append(f"MISSING target {target}")
            continue
        for part in ("element", "before", "after"):
            b_part = b_targets[target].get(part, {})
            c_part = c_targets[target].get(part, {})
            for prop in sorted(set(b_part) | set(c_part)):
                if prop == "__tokens":
                    continue
                if b_part.get(prop) != c_part.get(prop):
                    failures.append(f"{target}.{part}.{prop}: {b_part.get(prop)!r} != {c_part.get(prop)!r}")
    if failures:
        print(f"DIFF: {len(failures)} effective snapshot differences")
        for failure in failures[: args.limit]:
            print(f"  - {failure}")
        if len(failures) > args.limit:
            print(f"  ... (+{len(failures) - args.limit} more)")
        return 1
    print("OK: effective snapshots match")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())