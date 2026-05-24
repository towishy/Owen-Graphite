#!/usr/bin/env python3
"""Summarize current work using Owen Graphite WIKI summary fields."""

from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def git_lines(args: list[str]) -> list[str]:
    result = subprocess.run(["git", *args], cwd=ROOT, check=True, text=True, capture_output=True)
    return [line for line in result.stdout.splitlines() if line.strip()]


def changed_files() -> list[str]:
    return [line[3:] for line in git_lines(["status", "--short"]) if len(line) > 3]


def owner_modules(files: list[str]) -> list[str]:
    owners = [path for path in files if path.startswith("src/") or path.startswith("dev/scripts/") or path.startswith("dev/WIKI/")]
    return sorted(set(owners))


def yes_no(condition: bool) -> str:
    return "yes" if condition else "no"


def main() -> int:
    files = changed_files()
    owners = owner_modules(files)
    generated = any(path.startswith("dev/WIKI/MAP/") or path == "theme.css" for path in files)
    runtime_related = any(part in " ".join(files) for part in ("runtime", "chrome", "plugins", "live-preview", "table"))

    print("# Work Summary")
    print("")
    print("| Field | Value |")
    print("| --- | --- |")
    print("| WIKI consulted | dev/WIKI/README.md, CORE-PRINCIPLES.md, QUICK-ROUTING.md, relevant workflow |")
    print(f"| Owner modules changed | {', '.join(owners) if owners else 'n/a'} |")
    print(f"| Runtime evidence required | {yes_no(runtime_related)} |")
    print("| Runtime evidence captured | n/a |")
    print(f"| Generated artifacts refreshed | {yes_no(generated)} |")
    print("| Audits passed | fill from terminal output |")
    print("| Obsidian synced | fill after sync |")
    print("| Release/tag impact | n/a unless manifest/tag changed |")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())