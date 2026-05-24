#!/usr/bin/env python3
"""Create a runtime evidence capture scaffold under dev/TEMP."""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "dev" / "TEMP" / "runtime-evidence"


def slug(value: str) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip()).strip("-")
    return text.lower() or "runtime"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--surface", required=True, help="Surface name, e.g. table, chrome, pdf, plugin.")
    parser.add_argument("--name", required=True, help="Short issue name.")
    parser.add_argument("--state", default="", help="Runtime state, e.g. selected, hover, focus, active.")
    parser.add_argument("--owner", default="", help="Suspected owner module, if known.")
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUT_DIR / f"{date.today().isoformat()}-{slug(args.surface)}-{slug(args.name)}.json"
    if path.exists():
        raise FileExistsError(f"runtime evidence file already exists: {path.relative_to(ROOT)}")

    payload = {
        "schema": "owen-graphite/runtime-evidence/1",
        "surface": args.surface,
        "name": args.name,
        "runtimeState": args.state,
        "ownerCandidate": args.owner,
        "environment": {
            "obsidianVersion": "",
            "os": "",
            "themeVersion": "",
            "vaultPath": "",
        },
        "evidenceSource": {
            "captureTool": "",
            "isApproximation": False,
            "fixtureGap": "",
        },
        "domChain": [],
        "rectChain": [],
        "computedGeometry": {},
        "matchedRules": [],
        "inlineStyle": "",
        "decision": {
            "themeRuleResponsible": None,
            "ownerModule": args.owner,
            "cssAllowedByContract": None,
            "workflow": "",
            "audits": [],
        },
        "verification": {
            "runtimeStateRechecked": None,
            "screenshotOrNote": "",
            "auditsRun": [],
        },
        "notes": "",
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"OK: wrote {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())