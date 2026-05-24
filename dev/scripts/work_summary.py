#!/usr/bin/env python3
"""Summarize current work using Owen Graphite WIKI summary fields."""

from __future__ import annotations

import json
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


def last_sync_summary() -> str:
    path = ROOT / "dev" / "TEMP" / "last-sync.json"
    if not path.is_file():
        return "no"
    data = json.loads(path.read_text(encoding="utf-8"))
    theme = next((asset for asset in data.get("assets", []) if asset.get("path") == "theme.css"), {})
    digest = str(theme.get("sha256", ""))[:12]
    target = str(data.get("target", ""))
    when = str(data.get("syncedAt", ""))
    return f"yes; {target}; {when}; theme.css {digest}"


def runtime_evidence_summary() -> str:
    folder = ROOT / "dev" / "TEMP" / "runtime-evidence"
    if not folder.exists():
        return "n/a"
    files = sorted(path.relative_to(ROOT).as_posix() for path in folder.glob("*.json"))
    return ", ".join(files) if files else "n/a"


def changelog_candidate(files: list[str]) -> str:
    if any(path.startswith("src/") for path in files):
        return "polish/fix: source CSS changed; summarize user-visible surface and validation"
    if any(path.startswith("dev/scripts/") for path in files):
        return "process: workflow automation or audit tooling changed"
    if any(path.startswith("dev/WIKI/") for path in files):
        return "docs: WIKI workflow/process documentation changed"
    if any(path in {"manifest.json", "CHANGELOG.md"} for path in files):
        return "release: metadata changed"
    return "n/a"


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
    print(f"| Runtime evidence captured | {runtime_evidence_summary()} |")
    print(f"| Generated artifacts refreshed | {yes_no(generated)} |")
    print("| Audits passed | fill from terminal output |")
    print(f"| Obsidian synced | {last_sync_summary()} |")
    print("| Release/tag impact | n/a unless manifest/tag changed |")
    print(f"| Changelog candidate | {changelog_candidate(files)} |")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())