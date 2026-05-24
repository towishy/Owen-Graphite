#!/usr/bin/env python3
"""Recommend validation commands from the current git diff."""

from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def changed_files() -> list[str]:
    result = subprocess.run(["git", "status", "--short"], cwd=ROOT, check=True, text=True, capture_output=True)
    return [line[3:].replace("\\", "/") for line in result.stdout.splitlines() if len(line) > 3]


def add(commands: list[str], command: str) -> None:
    if command not in commands:
        commands.append(command)


def main() -> int:
    files = changed_files()
    commands: list[str] = []
    notes: list[str] = []

    if not files:
        print("OK: no changed files")
        return 0

    if any(path.startswith("src/") or path == "theme.css" for path in files):
        add(commands, ".\\.venv\\Scripts\\python.exe dev\\scripts\\build_source_usage_map.py --check")
        add(commands, ".\\.venv\\Scripts\\python.exe dev\\scripts\\audit_core_principles.py")
        add(commands, ".\\.venv\\Scripts\\python.exe dev\\scripts\\release_check.py --skip-bundle")
    if any(path.startswith("dev/WIKI/") or path.startswith(".github/") or path.startswith("CONTRIBUTING") for path in files):
        add(commands, ".\\.venv\\Scripts\\python.exe dev\\scripts\\audit_docs_assets.py")
        add(commands, ".\\.venv\\Scripts\\python.exe dev\\scripts\\audit_wiki_consistency.py")
    if any(path.startswith("src/base/13-live-preview") or "cm-" in Path(path).name for path in files):
        add(commands, ".\\.venv\\Scripts\\python.exe dev\\scripts\\audit_v3_hit_routing.py")
    if any(path.startswith("src/chrome/") for path in files):
        notes.append("Chrome interactive changes may need runtime evidence for hover/focus/active states.")
    if any(path.startswith("src/plugins/") for path in files):
        notes.append("Plugin changes should include real plugin DOM evidence or note the fixture gap.")
    if any(path.startswith("src/features/41") or path.startswith("src/features/42") or path.startswith("src/features/43") for path in files):
        add(commands, ".\\.venv\\Scripts\\python.exe dev\\scripts\\audit_pdf_header_footer.py")
    if any(path in {"manifest.json", "CHANGELOG.md"} or "release-plan" in path or path.startswith(".github/workflows/release") for path in files):
        add(commands, ".\\.venv\\Scripts\\python.exe dev\\scripts\\release_preflight.py --version <version>")

    print("Changed files:")
    for path in files:
        print(f"- {path}")
    print("\nRecommended validation:")
    for command in commands or [".\\.venv\\Scripts\\python.exe dev\\scripts\\audit_wiki_consistency.py"]:
        print(f"- {command}")
    if notes:
        print("\nNotes:")
        for note in notes:
            print(f"- {note}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())