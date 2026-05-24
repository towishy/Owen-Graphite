#!/usr/bin/env python3
"""Start an Owen Graphite task with WIKI routing and optional evidence scaffold."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PYTHON = sys.executable


def run(args: list[str]) -> None:
    subprocess.run([PYTHON, *args], cwd=ROOT, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--surface", required=True, help="Surface for wiki_route.py, e.g. table, chrome, plugin.")
    parser.add_argument("--name", default="", help="Short task/evidence name.")
    parser.add_argument("--state", default="", help="Runtime state when evidence is needed.")
    parser.add_argument("--evidence", action="store_true", help="Create runtime evidence scaffold.")
    args = parser.parse_args()

    print("== WIKI route ==")
    run(["dev/scripts/wiki_route.py", args.surface])
    print("\n== Validation plan ==")
    run(["dev/scripts/validation_plan.py"])
    if args.evidence:
        if not args.name:
            raise SystemExit("--name is required with --evidence")
        print("\n== Runtime evidence scaffold ==")
        command = ["dev/scripts/new_runtime_evidence.py", "--surface", args.surface, "--name", args.name]
        if args.state:
            command.extend(["--state", args.state])
        run(command)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())