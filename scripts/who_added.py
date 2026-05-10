#!/usr/bin/env python3
"""Look up which commit / version introduced (or last touched) a given
selector substring.

Usage:
  python scripts/who_added.py ".cm-callout"
  python scripts/who_added.py "HyperMD-table-row" --module dev/05-live-preview.css

Reads `dev/MAP/selector-provenance.json` (build with
`scripts/build_selector_provenance.py`).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "dev" / "MAP" / "selector-provenance.json"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="substring to search inside selectors")
    parser.add_argument("--module", help="restrict to a specific dev/*.css module")
    parser.add_argument("--limit", type=int, default=20)
    args = parser.parse_args()

    if not INDEX.is_file():
        print(
            f"who_added: provenance index not found at {INDEX.relative_to(ROOT)}.\n"
            f"  Run: python scripts/build_selector_provenance.py",
            file=sys.stderr,
        )
        return 2
    data: dict[str, dict] = json.loads(INDEX.read_text(encoding="utf-8"))
    matches = []
    for key, entry in data.items():
        if args.module and entry["module"] != args.module:
            continue
        if args.query.lower() not in entry["selector"].lower():
            continue
        matches.append(entry)
    if not matches:
        print(f"who_added: no selector matched '{args.query}'")
        return 1
    matches.sort(key=lambda e: e["first_date"])
    for entry in matches[: args.limit]:
        print(
            f"{entry['module']}\n"
            f"  {entry['selector']}\n"
            f"  introduced: {entry['first_commit']}  {entry['first_date'][:10]}  {entry['first_subject']}\n"
            f"  last touch: {entry['last_commit']}  {entry['last_subject']}\n"
        )
    if len(matches) > args.limit:
        print(f"... {len(matches) - args.limit} more matches truncated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
