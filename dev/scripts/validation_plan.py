#!/usr/bin/env python3
"""Recommend validation commands from the current git diff."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from route_registry import route_check_models, route_for, route_names


ROOT = Path(__file__).resolve().parents[2]
LAST_VALIDATION = ROOT / "dev" / "TEMP" / "last-validation.json"

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


def normalize_command(command: str) -> str:
    return command.replace("/", "\\") if command.startswith(".\\.venv\\Scripts\\python.exe dev/") else command


def add_model(commands: list[dict[str, object]], command: str, source: str, safe: bool | None = None) -> None:
    normalized = normalize_command(command)
    if any(item["command"] == normalized for item in commands):
        return
    run_args = command_to_args(normalized)
    commands.append(
        {
            "command": normalized,
            "source": source,
            "safe": is_safe_command(normalized) if safe is None else bool(safe),
            "runnable": run_args is not None,
            "args": run_args or [],
        }
    )


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


def build_plan(surfaces: list[str], full_check: bool) -> dict[str, object]:
    files = changed_files()
    source_like = [path for path in files if path.startswith("src/") or path == "theme.css"]
    diff_text = subprocess.run(["git", "diff", "--", *source_like], cwd=ROOT, text=True, capture_output=True, check=True).stdout if source_like else ""
    commands: list[dict[str, object]] = []
    notes: list[str] = []

    if any(path.startswith("src/") or path == "theme.css" for path in files):
        add_model(commands, ".\\.venv\\Scripts\\python.exe dev\\scripts\\build_source_usage_map.py --check", "diff")
        add_model(commands, ".\\.venv\\Scripts\\python.exe dev\\scripts\\audit_core_principles.py", "diff")
        add_model(commands, ".\\.venv\\Scripts\\python.exe dev\\scripts\\release_check.py --skip-bundle", "diff")
    if any(path.startswith("dev/WIKI/") or path.startswith(".github/") or path.startswith("CONTRIBUTING") for path in files):
        add_model(commands, ".\\.venv\\Scripts\\python.exe dev\\scripts\\audit_docs_assets.py", "diff")
        add_model(commands, ".\\.venv\\Scripts\\python.exe dev\\scripts\\audit_wiki_consistency.py", "diff")
    if any(path.startswith("src/base/13-live-preview") or "cm-" in Path(path).name for path in files):
        add_model(commands, ".\\.venv\\Scripts\\python.exe dev\\scripts\\audit_v3_hit_routing.py", "diff")
    if any(term in diff_text for term in (":focus", "focus-visible", "focus-within", ".is-active")):
        add_model(commands, ".\\.venv\\Scripts\\python.exe dev\\scripts\\audit_runtime_evidence_requirements.py --strict", "diff")
        notes.append("Interactive state diff detected; strict runtime evidence check is recommended.")
    if "@media print" in diff_text or "@page" in diff_text:
        add_model(commands, ".\\.venv\\Scripts\\python.exe dev\\scripts\\audit_pdf_header_footer.py", "diff")
    if "--ogd-" in diff_text:
        notes.append("Token/design-language diff detected; check TOKENS guidance and Light/Dark impact.")
    if ".mermaid" in diff_text or ".dataview" in diff_text or ".canvas" in diff_text or ".graph" in diff_text:
        add_model(commands, ".\\.venv\\Scripts\\python.exe dev\\scripts\\wiki_route.py plugin", "diff")
        notes.append("Plugin/runtime selector diff detected; record real DOM evidence or fixture gap when claiming runtime correctness.")
    if any(path.startswith("src/chrome/") for path in files):
        notes.append("Chrome interactive changes may need runtime evidence for hover/focus/active states.")
    if any(path.startswith("src/plugins/") for path in files):
        notes.append("Plugin changes should include real plugin DOM evidence or note the fixture gap.")
    if any(path.startswith("src/features/41") or path.startswith("src/features/42") or path.startswith("src/features/43") for path in files):
        add_model(commands, ".\\.venv\\Scripts\\python.exe dev\\scripts\\audit_pdf_header_footer.py", "diff")
    if any(path in {"manifest.json", "CHANGELOG.md"} or "release-plan" in path or path.startswith(".github/workflows/release") for path in files):
        add_model(commands, ".\\.venv\\Scripts\\python.exe dev\\scripts\\release_preflight.py --version <version>", "diff", safe=False)

    for surface in surfaces:
        for model in route_check_models(route_for(surface)):
            command = f".\\.venv\\Scripts\\python.exe {model['command']}"
            safe = bool(model["safe"]) and not bool(model["requiresPlaceholder"])
            add_model(commands, command, f"surface:{surface}", safe=safe)
        if route_needs_runtime_note(surface):
            notes.append(f"Surface route '{surface}' can require runtime evidence for selected/hover/focus/active states.")

    if full_check:
        for command in FULL_CHECK_COMMANDS:
            add_model(commands, command, "full-check")

    if not commands:
        add_model(commands, ".\\.venv\\Scripts\\python.exe dev\\scripts\\audit_wiki_consistency.py", "default")

    return {
        "schema": "owen-graphite/validation-plan/1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "changedFiles": files,
        "surfaces": surfaces,
        "fullCheck": full_check,
        "commands": commands,
        "notes": notes,
    }


def print_plan(plan: dict[str, object]) -> None:
    files = list(plan["changedFiles"])
    commands = list(plan["commands"])
    notes = list(plan["notes"])
    print("Changed files:")
    if files:
        for path in files:
            print(f"- {path}")
    else:
        print("- n/a")
    surfaces = list(plan["surfaces"])
    if surfaces:
        print("\nSurface routes: " + ", ".join(str(surface) for surface in surfaces))
    if plan["fullCheck"]:
        print("\nFull check: enabled")
    print("\nRecommended validation:")
    for item in commands:
        print(f"- {item['command']}")
    if notes:
        print("\nNotes:")
        for note in notes:
            print(f"- {note}")


def write_validation_result(plan: dict[str, object], command_results: list[dict[str, object]]) -> None:
    LAST_VALIDATION.parent.mkdir(parents=True, exist_ok=True)
    payload = dict(plan)
    payload.update(
        {
            "schema": "owen-graphite/validation-result/1",
            "completedAt": datetime.now(timezone.utc).isoformat(),
            "results": command_results,
            "ok": all(int(result.get("exitCode", 1)) == 0 for result in command_results if result.get("ran")),
        }
    )
    LAST_VALIDATION.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


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
    parser.add_argument("--json", action="store_true", help="Print the validation plan/result as JSON.")
    args = parser.parse_args()

    surfaces = list(dict.fromkeys(args.surface))
    plan = build_plan(surfaces, args.full_check)

    if not plan["changedFiles"] and not surfaces and not args.full_check and not args.json:
        print("OK: no changed files")
        return 0
    if args.json and not args.run_safe:
        print(json.dumps(plan, indent=2, ensure_ascii=False))
        return 0
    if not args.json:
        print_plan(plan)
    if args.run_safe:
        command_results: list[dict[str, object]] = []
        if not args.json:
            print("\nRunning safe validation commands:")
        exit_code = 0
        for item in plan["commands"]:
            command = str(item["command"])
            run_args = list(item.get("args", []))
            safe = bool(item.get("safe", False)) and bool(item.get("runnable", False))
            if not safe:
                if not args.json:
                    print(f"SKIP: {command}")
                command_results.append({"command": command, "ran": False, "exitCode": None, "reason": "not-safe"})
                continue
            if not args.json:
                print(f"RUN: {command}")
            result = subprocess.run(run_args, cwd=ROOT)
            command_results.append({"command": command, "ran": True, "exitCode": result.returncode})
            exit_code |= result.returncode
        write_validation_result(plan, command_results)
        if args.json:
            payload = dict(plan)
            payload["results"] = command_results
            payload["ok"] = exit_code == 0
            print(json.dumps(payload, indent=2, ensure_ascii=False))
        return exit_code
    return 0


if __name__ == "__main__":
    raise SystemExit(main())