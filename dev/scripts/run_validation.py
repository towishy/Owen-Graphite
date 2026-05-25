#!/usr/bin/env python3
"""Run validation commands with stable UTF-8 output and JSON summary."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "dev" / "TEMP" / "validation-runner.json"

PRESETS = {
    "core": [
        ["dev/scripts/build_source_usage_map.py", "--check"],
        ["dev/scripts/build_coverage_priority_plan.py", "--check"],
        ["dev/scripts/audit_wiki_consistency.py"],
        ["dev/scripts/audit_core_principles.py"],
        ["dev/scripts/release_check.py", "--skip-bundle"],
    ],
    "table": [
        ["dev/scripts/audit_direct_owner_guard.py"],
        ["dev/scripts/audit_v3_hit_routing.py"],
        ["dev/scripts/audit_lp_pdf_selector_ownership.py"],
    ],
    "release": [
        ["dev/scripts/build_source_usage_map.py", "--check"],
        ["dev/scripts/audit_core_principles.py"],
        ["dev/scripts/release_check.py", "--skip-bundle"],
        ["dev/scripts/audit_release_zip.py"],
    ],
}


def run_command(args: list[str]) -> dict[str, object]:
    command = [sys.executable, *args]
    env = os.environ.copy()
    env.setdefault("PYTHONIOENCODING", "utf-8")
    env.setdefault("PYTHONUTF8", "1")
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, env=env)
    return {
        "command": command,
        "exitCode": result.returncode,
        "stdoutTail": result.stdout.splitlines()[-80:],
        "stderrTail": result.stderr.splitlines()[-80:],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preset", action="append", choices=sorted(PRESETS), default=[], help="Validation preset to run. Repeatable.")
    parser.add_argument("--command", action="append", default=[], help="Extra Python script command, e.g. 'dev/scripts/audit_docs_assets.py'.")
    parser.add_argument("--out", default=str(OUT), help="JSON output path.")
    args = parser.parse_args()

    commands: list[list[str]] = []
    for preset in args.preset or ["core"]:
        commands.extend(PRESETS[preset])
    for command in args.command:
        commands.append(command.split())

    results = []
    exit_code = 0
    for command in commands:
        result = run_command(command)
        results.append(result)
        exit_code = exit_code or int(result["exitCode"])
        status = "OK" if result["exitCode"] == 0 else "FAIL"
        print(f"{status}: {' '.join(result['command'])}")
        if result["exitCode"] != 0:
            for line in result["stdoutTail"]:
                print(line)
            for line in result["stderrTail"]:
                print(line, file=sys.stderr)
            break

    payload = {
        "schema": "owen-graphite/validation-runner/1",
        "completedAt": datetime.now(timezone.utc).isoformat(),
        "ok": exit_code == 0,
        "results": results,
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE: {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
