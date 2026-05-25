#!/usr/bin/env python3
"""Recommend validation commands from the current git diff."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from route_registry import route_check_commands, route_for, route_names


ROOT = Path(__file__).resolve().parents[2]

FULL_CHECK_COMMANDS = [
    ".\\.venv\\Scripts\\python.exe dev\\scripts\\build_source_usage_map.py --check",
    ".\\.venv\\Scripts\\python.exe dev\\scripts\\audit_core_principles.py",
    ".\\.venv\\Scripts\\python.exe dev\\scripts\\release_check.py --skip-bundle",
]
RUNTIME_PROPERTY_GROUPS = {"focus", "hit-routing", "interaction"}


def changed_files() -> list[str]:
    result = subprocess.run(["git", "status", "--short"], cwd=ROOT, check=True, text=True, capture_output=True)
    return [line[3:].replace("\\", "/") for line in result.stdout.splitlines() if len(line) > 3]


def add(commands: list[str], command: str) -> None:
    command = command.replace("/", "\\") if command.startswith(".\\.venv\\Scripts\\python.exe dev/") else command
    if command not in commands:
        commands.append(command)


def command_to_args(command: str) -> list[str] | None:
    prefix = ".\\.venv\\Scripts\\python.exe "
    if not command.startswith(prefix):
        return None
    parts = command[len(prefix):].split()
    if "<version>" in parts:
        return None
    return [sys.executable, *(part.replace("\\", "/") for part in parts)]


def is_safe_command(command: str) -> bool:
    # Keep run-safe bounded: no bundling, release ZIP, sync, or publishing.
    blocked = ("build_release.py", "sync_obsidian_theme.py", "--include-sync", "--include-zip")
    return not any(term in command for term in blocked)


def route_needs_runtime_note(surface: str) -> bool:
    registry = json.loads((ROOT / "dev" / "WIKI" / "MAP" / "owner-registry.json").read_text(encoding="utf-8"))
    surface_map = {item["id"]: item for item in registry.get("surfaces", [])}
    for surface_id in route_for(surface).get("surfaces", []):
        item = surface_map.get(surface_id, {})
        property_groups = {str(value) for value in item.get("propertyGroups", [])}
        if property_groups & RUNTIME_PROPERTY_GROUPS:
            return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--surface",
        action="append",
        choices=route_names(),
        default=[],
        help="Add validation recommended by a WIKI route. Repeat for multi-surface work.",
    )
    parser.add_argument("--full-check", action="store_true", help="Add the standard release-confidence checks for handoff or commit readiness.")
    parser.add_argument("--run-safe", action="store_true", help="Run recommended commands that do not require placeholders.")
    args = parser.parse_args()

    files = changed_files()
    source_like = [path for path in files if path.startswith("src/") or path == "theme.css"]
    diff_text = subprocess.run(["git", "diff", "--", *source_like], cwd=ROOT, text=True, capture_output=True, check=True).stdout if source_like else ""
    commands: list[str] = []
    notes: list[str] = []

    surfaces = list(dict.fromkeys(args.surface))

    if not files and not surfaces and not args.full_check:
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

    for surface in surfaces:
        for command in route_check_commands(route_for(surface)):
            add(commands, f".\\.venv\\Scripts\\python.exe {command}")
        if route_needs_runtime_note(surface):
            notes.append(f"Surface route '{surface}' can require runtime evidence for selected/hover/focus/active states.")

    if args.full_check:
        for command in FULL_CHECK_COMMANDS:
            add(commands, command)

    print("Changed files:")
    if files:
        for path in files:
            print(f"- {path}")
    else:
        print("- n/a")
    if surfaces:
        print("\nSurface routes: " + ", ".join(surfaces))
    if args.full_check:
        print("\nFull check: enabled")
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