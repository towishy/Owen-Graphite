#!/usr/bin/env python3
"""Warn when current diff touches runtime-sensitive files without evidence notes."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EVIDENCE_DIR = ROOT / "dev" / "TEMP" / "runtime-evidence"
SENSITIVE_PREFIXES = (
    "src/base/13-live-preview.css",
    "src/chrome/",
    "src/plugins/",
)
SENSITIVE_TERMS = (":hover", ":focus", "focus-visible", "focus-within", ".is-active", ".cm-", "HyperMD", "cm-table-widget")


def changed_files() -> list[str]:
    result = subprocess.run(["git", "status", "--short"], cwd=ROOT, check=True, text=True, capture_output=True)
    return [line[3:].replace("\\", "/") for line in result.stdout.splitlines() if len(line) > 3]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="Fail when runtime-sensitive diff has no evidence file.")
    args = parser.parse_args()

    files = changed_files()
    sensitive = [path for path in files if path.startswith(SENSITIVE_PREFIXES)]
    diff = subprocess.run(["git", "diff", "--", *sensitive], cwd=ROOT, text=True, capture_output=True).stdout if sensitive else ""
    needs_evidence = bool(sensitive and any(term in diff for term in SENSITIVE_TERMS))
    evidence_files = list(EVIDENCE_DIR.glob("*.json")) if EVIDENCE_DIR.exists() else []
    if needs_evidence and not evidence_files:
        level = "FAIL" if args.strict else "WARN"
        print(f"{level}: runtime-sensitive diff detected without dev/TEMP/runtime-evidence/*.json", file=sys.stderr)
        print(f"{level}: create one with dev/scripts/new_runtime_evidence.py when claiming runtime correctness", file=sys.stderr)
        return 1 if args.strict else 0
    print("OK: runtime evidence requirement check clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())