#!/usr/bin/env python3
"""Finish an Owen Graphite task with validation guidance and summary."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PYTHON = sys.executable


def run(args: list[str]) -> int:
    return subprocess.run([PYTHON, *args], cwd=ROOT).returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Run core WIKI consistency and validation-plan scripts.")
    parser.add_argument("--full-check", action="store_true", help="Run release-confidence validation through validation_plan.py --full-check --run-safe.")
    parser.add_argument("--sync", action="store_true", help="Sync release assets to Obsidian after summary/checks.")
    parser.add_argument("--target", help="Target Obsidian theme folder for --sync.")
    args = parser.parse_args()

    exit_code = 0
    print("== Work summary ==")
    exit_code |= run(["dev/scripts/work_summary.py"])
    print("\n== Validation plan ==")
    exit_code |= run(["dev/scripts/validation_plan.py"])
    if args.check:
        print("\n== WIKI consistency ==")
        exit_code |= run(["dev/scripts/audit_wiki_consistency.py"])
    if args.full_check:
        print("\n== Full validation ==")
        exit_code |= run(["dev/scripts/validation_plan.py", "--full-check", "--run-safe"])
    if args.sync:
        print("\n== Obsidian sync ==")
        command = ["dev/scripts/sync_obsidian_theme.py", "--skip-bundle"]
        if args.target:
            command.extend(["--target", args.target])
        exit_code |= run(command)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())