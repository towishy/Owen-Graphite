#!/usr/bin/env python3
"""Run the Owen Graphite release publish playbook with safe defaults."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PYTHON = sys.executable
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")


def run(label: str, command: list[str]) -> None:
    print(f"\n== {label} ==")
    subprocess.run(command, cwd=ROOT, check=True)


def git_output(args: list[str]) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, text=True, capture_output=True, check=True).stdout.strip()


def promote_bundle() -> None:
    source = ROOT / "dist" / "theme-v3.css"
    target = ROOT / "theme.css"
    shutil.copyfile(source, target)
    print("OK: promoted dist/theme-v3.css -> theme.css")


def assert_clean_release_target(version: str) -> None:
    if git_output(["tag", "--list", version]):
        raise AssertionError(f"local tag already exists: {version}")
    if git_output(["ls-remote", "--tags", "origin", version]):
        raise AssertionError(f"remote tag already exists: {version}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", required=True, help="Numeric semver release version.")
    parser.add_argument("--publish", action="store_true", help="Commit, push main, create tag, push tag, and wait for GitHub Release.")
    parser.add_argument("--include-visual", action="store_true", help="Run static visual fixture audit through release_check.py.")
    parser.add_argument("--include-sync", action="store_true", help="Run release_check.py with Obsidian sync after validation.")
    parser.add_argument("--sync-target", help="Target Obsidian theme folder for --include-sync.")
    parser.add_argument("--no-wait", action="store_true", help="Do not wait for GitHub Release workflow after publishing.")
    args = parser.parse_args()

    try:
        version = args.version
        if not SEMVER_RE.match(version):
            raise AssertionError("version must be numeric semver without v prefix")
        assert_clean_release_target(version)

        run("Release preflight", [PYTHON, "dev/scripts/release_preflight.py", "--version", version])
        run("Bundle v3 CSS", [PYTHON, "dev/scripts/bundle_v3.py"])
        promote_bundle()
        run("Source usage map freshness", [PYTHON, "dev/scripts/build_source_usage_map.py", "--check"])
        run("Core principles", [PYTHON, "dev/scripts/audit_core_principles.py"])
        release_check = [PYTHON, "dev/scripts/release_check.py", "--tag", version, "--skip-bundle"]
        if args.include_visual:
            release_check.append("--include-visual")
        if args.include_sync:
            release_check.append("--include-sync")
            if args.sync_target:
                release_check.extend(["--sync-target", args.sync_target])
        run("Release check", release_check)
        run("Build manual install ZIP", [PYTHON, "dev/scripts/build_release.py"])
        run("Audit manual install ZIP", [PYTHON, "dev/scripts/audit_release_zip.py"])
        run("Test Style Settings localization bridge", [PYTHON, "compat/owen-graphite-style-settings-l10n/test.py"])
        run("Build localization companion ZIP", [PYTHON, "dev/scripts/build_companion_release.py"])

        if not args.publish:
            print("\nOK: release publish dry run complete. Re-run with --publish to commit, push, tag, and wait for GitHub Release.")
            return 0

        run("Git status before commit", ["git", "status", "--short"])
        run("Commit release", ["git", "add", "-A"])
        run("Create release commit", ["git", "commit", "-m", f"chore: release Owen Graphite {version}"])
        run("Push main", ["git", "push", "origin", "main"])
        run("Create numeric tag", ["git", "tag", version])
        run("Push numeric tag", ["git", "push", "origin", version])
        status_command = [PYTHON, "dev/scripts/check_release_status.py", "--version", version, "--require-complete"]
        if not args.no_wait:
            status_command.append("--wait")
        run("GitHub Release status", status_command)
        print(f"\nOK: release {version} published")
        return 0
    except Exception as exc:
        print(f"\nFAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
