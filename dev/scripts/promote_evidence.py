#!/usr/bin/env python3
"""Promote a runtime evidence JSON file into a WIKI incident record."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INCIDENT_DIR = ROOT / "dev" / "WIKI" / "INCIDENTS"
EVIDENCE_DIR = INCIDENT_DIR / "evidence"


def resolve_incident(value: str) -> Path:
    path = Path(value)
    if not path.suffix:
        path = INCIDENT_DIR / f"{value}.md"
    elif not path.is_absolute():
        path = ROOT / path
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--incident", required=True, help="Incident markdown path or incident slug.")
    parser.add_argument("--evidence", required=True, type=Path, help="Runtime evidence JSON path.")
    args = parser.parse_args()

    incident = resolve_incident(args.incident)
    evidence = args.evidence if args.evidence.is_absolute() else ROOT / args.evidence
    if not incident.is_file():
        raise FileNotFoundError(f"incident not found: {incident}")
    if not evidence.is_file():
        raise FileNotFoundError(f"evidence not found: {evidence}")

    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    destination = EVIDENCE_DIR / evidence.name
    shutil.copy2(evidence, destination)
    rel = destination.relative_to(ROOT).as_posix()
    text = incident.read_text(encoding="utf-8")
    line = f"- Runtime evidence: `{rel}`"
    if line not in text:
        text = text.rstrip() + "\n" + line + "\n"
        incident.write_text(text, encoding="utf-8")
    print(f"OK: promoted {evidence.relative_to(ROOT)} -> {rel}")
    print(f"OK: updated {incident.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())