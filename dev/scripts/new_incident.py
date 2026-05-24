#!/usr/bin/env python3
"""Create a WIKI incident entry from the standard template."""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INCIDENT_DIR = ROOT / "dev" / "WIKI" / "INCIDENTS"
TEMPLATE = INCIDENT_DIR / "incident-template.md"
VALID_TYPES = {
    "runtime-selected-state",
    "live-preview-hit-routing",
    "table-widget-boundary",
    "pdf-layout-drift",
    "plugin-dom-mismatch",
    "token-misuse",
    "late-repair-layer",
    "release-process",
}


def slug(value: str) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip()).strip("-")
    return text.lower() or "incident"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--type", required=True, choices=sorted(VALID_TYPES), help="Incident taxonomy type.")
    parser.add_argument("--name", required=True, help="Short incident name.")
    parser.add_argument("--surface", default="", help="Affected surface.")
    parser.add_argument("--state", default="", help="Runtime state, if any.")
    parser.add_argument("--evidence", action="store_true", help="Create and link a runtime evidence scaffold.")
    args = parser.parse_args()

    INCIDENT_DIR.mkdir(parents=True, exist_ok=True)
    path = INCIDENT_DIR / f"{slug(args.name)}.md"
    if path.exists():
        raise FileExistsError(f"incident already exists: {path.relative_to(ROOT)}")

    text = TEMPLATE.read_text(encoding="utf-8")
    text = text.replace("# Incident: <short-name>", f"# Incident: {args.name}")
    frontmatter = (
        f"Incident type: `{args.type}`  \n"
        f"Created: `{date.today().isoformat()}`  \n"
        f"Surface: `{args.surface or 'tbd'}`  \n"
        f"Runtime state: `{args.state or 'tbd'}`\n\n"
    )
    text = text.replace("## Trigger\n", frontmatter + "## Trigger\n", 1)
    evidence_path: Path | None = None
    if args.evidence:
        evidence_dir = ROOT / "dev" / "TEMP" / "runtime-evidence"
        evidence_dir.mkdir(parents=True, exist_ok=True)
        evidence_path = evidence_dir / f"{date.today().isoformat()}-{slug(args.surface or args.type)}-{slug(args.name)}.json"
        payload = {
            "schema": "owen-graphite/runtime-evidence/1",
            "surface": args.surface,
            "name": args.name,
            "runtimeState": args.state,
            "incident": path.relative_to(ROOT).as_posix(),
            "domChain": [],
            "computedGeometry": {},
            "matchedRules": [],
            "decision": {},
            "notes": "",
        }
        evidence_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        text = text.replace("- DOM/runtime evidence:", f"- DOM/runtime evidence: `{evidence_path.relative_to(ROOT).as_posix()}`")
    path.write_text(text, encoding="utf-8")
    print(f"OK: wrote {path.relative_to(ROOT)}")
    if evidence_path:
        print(f"OK: wrote {evidence_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())