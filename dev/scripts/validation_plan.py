#!/usr/bin/env python3
"""Recommend validation commands from the current git diff."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def changed_files() -> list[str]:
    result = subprocess.run(["git", "status", "--short"], cwd=ROOT, check=True, text=True, capture_output=True)
    return [line[3:].replace("\\", "/") for line in result.stdout.splitlines() if len(line) > 3]


def add(commands: list[str], command: str) -> None:
    if command not in commands:
        commands.append(command)


def command_to_args(command: str) -> list[str] | None:
    prefix = ".\\.venv\\Scripts\\python.exe "
    if not command.startswith(prefix):
        return None
    parts = command[len(prefix):].split()
    if "<version>" in parts:
        return None
    return [sys.executable, *parts]


def is_safe_command(command: str) -> bool:
    # Keep run-safe bounded: no bundling, release ZIP, sync, or publishing.
    blocked = ("build_release.py", "sync_obsidian_theme.py", "--include-sync", "--include-zip")
    return not any(term in command for term in blocked)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-safe", action="store_true", help="Run recommended commands that do not require placeholders.")
    args = parser.parse_args()

    files = changed_files()
    source_like = [path for path in files if path.startswith("src/") or path == "theme.css"]
    diff_text = subprocess.run(["git", "diff", "--", *source_like], cwd=ROOT, text=True, capture_output=True, check=True).stdout if source_like else ""
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
    if any(term in diff_text for term in (":focus", "focus-visible", "focus-within", ".is-active")):
        add(commands, ".\\.venv\\Scripts\\python.exe dev\\scripts\\audit_runtime_evidence_requirements.py --strict")
        notes.append("Interactive state diff detected; strict runtime evidence check is recommended.")
    if "@media print" in diff_text or "@page" in diff_text:
        add(commands, ".\\.venv\\Scripts\\python.exe dev\\scripts\\audit_pdf_header_footer.py")
    if "--ogd-" in diff_text:
        notes.append("Token/design-language diff detected; check TOKENS guidance and Light/Dark impact.")
    if ".mermaid" in diff_text or ".dataview" in diff_text or ".canvas" in diff_text or ".graph" in diff_text:
        add(commands, ".\\.venv\\Scripts\\python.exe dev\\scripts\\wiki_route.py plugin")
        notes.append("Plugin/runtime selector diff detected; record real DOM evidence or fixture gap when claiming runtime correctness.")
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
    if args.run_safe:
        print("\nRunning safe validation commands:")
        exit_code = 0
        for command in commands:
            run_args = command_to_args(command)
            if run_args is None or not is_safe_command(command):
                print(f"SKIP: {command}")
                continue
            print(f"RUN: {command}")
            exit_code |= subprocess.run(run_args, cwd=ROOT).returncode
        return exit_code
    return 0


if __name__ == "__main__":
    raise SystemExit(main())