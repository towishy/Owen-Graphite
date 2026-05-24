#!/usr/bin/env python3
"""Warn when current diff touches runtime-sensitive files without evidence notes."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EVIDENCE_DIR = ROOT / "dev" / "TEMP" / "runtime-evidence"
SCHEMA_PATH = ROOT / "dev" / "WIKI" / "runtime-evidence-schema.json"
SENSITIVE_PREFIXES = (
    "src/base/13-live-preview.css",
    "src/chrome/",
    "src/plugins/",
)
SENSITIVE_TERMS = (":hover", ":focus", "focus-visible", "focus-within", ".is-active", ".cm-", "HyperMD", "cm-table-widget")


def changed_files() -> list[str]:
    result = subprocess.run(["git", "status", "--short"], cwd=ROOT, check=True, text=True, capture_output=True)
    return [line[3:].replace("\\", "/") for line in result.stdout.splitlines() if len(line) > 3]


def validate_evidence_files(evidence_files: list[Path]) -> list[str]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    required = list(schema.get("required", []))
    properties = dict(schema.get("properties", {}))
    problems: list[str] = []
    for path in evidence_files:
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            problems.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
            continue
        for key in required:
            if key not in payload:
                problems.append(f"{path.relative_to(ROOT)}: missing {key}")
        if payload.get("schema") != "owen-graphite/runtime-evidence/1":
            problems.append(f"{path.relative_to(ROOT)}: unexpected schema {payload.get('schema')!r}")
        for key, spec in properties.items():
            if key not in payload or not isinstance(spec, dict):
                continue
            nested_required = spec.get("required", [])
            if nested_required:
                value = payload.get(key)
                if not isinstance(value, dict):
                    problems.append(f"{path.relative_to(ROOT)}: {key} must be an object")
                    continue
                for nested_key in nested_required:
                    if nested_key not in value:
                        problems.append(f"{path.relative_to(ROOT)}: missing {key}.{nested_key}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="Fail when runtime-sensitive diff has no evidence file.")
    args = parser.parse_args()

    files = changed_files()
    sensitive = [path for path in files if path.startswith(SENSITIVE_PREFIXES)]
    diff = subprocess.run(["git", "diff", "--", *sensitive], cwd=ROOT, text=True, capture_output=True).stdout if sensitive else ""
    needs_evidence = bool(sensitive and any(term in diff for term in SENSITIVE_TERMS))
    evidence_files = list(EVIDENCE_DIR.glob("*.json")) if EVIDENCE_DIR.exists() else []
    schema_problems = validate_evidence_files(evidence_files)
    if schema_problems:
        level = "FAIL" if args.strict else "WARN"
        for problem in schema_problems:
            print(f"{level}: {problem}", file=sys.stderr)
        return 1 if args.strict else 0
    if needs_evidence and not evidence_files:
        level = "FAIL" if args.strict else "WARN"
        print(f"{level}: runtime-sensitive diff detected without dev/TEMP/runtime-evidence/*.json", file=sys.stderr)
        print(f"{level}: create one with dev/scripts/new_runtime_evidence.py when claiming runtime correctness", file=sys.stderr)
        return 1 if args.strict else 0
    print("OK: runtime evidence requirement check clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())