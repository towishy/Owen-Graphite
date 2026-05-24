#!/usr/bin/env python3
"""Preflight numeric release metadata before tagging."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")


def text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def git_output(args: list[str]) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, text=True, capture_output=True, check=True).stdout.strip()


def fail(message: str) -> None:
    raise AssertionError(message)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", required=True, help="Numeric semver version, e.g. 3.1.58.")
    args = parser.parse_args()
    try:
        version = args.version
        if not SEMVER_RE.match(version):
            fail("version must be numeric semver without v prefix")
        manifest_version = json.loads(text("manifest.json"))["version"]
        if manifest_version != version:
            fail(f"manifest version {manifest_version} != {version}")
        checks = {
            "CHANGELOG.md": f"## v{version}",
            "README.md version": f"**Owen Graphite v{version}**",
            "README.md zip": f"Owen-Graphite-{version}.zip",
            "screenshots/README.md": f"Owen Graphite v{version}",
            "dev/WIKI/DOCS/v3/release-plan.md latest": f"latest: v{version}",
            "dev/WIKI/DOCS/v3/release-plan.md manifest": f"| `manifest.json` version | `{version}` |",
        }
        for label, needle in checks.items():
            path = label.split()[0]
            if needle not in text(path):
                fail(f"{label} missing {needle!r}")
        local_tag = git_output(["tag", "--list", version])
        if local_tag:
            fail(f"local tag already exists: {version}")
        remote_tag = git_output(["ls-remote", "--tags", "origin", version])
        if remote_tag:
            fail(f"remote tag already exists: {version}")
        v_tag = git_output(["tag", "--list", f"v{version}"])
        if v_tag:
            fail(f"v-prefixed local tag exists and is forbidden: v{version}")
        print(f"OK: release preflight clean for {version}")
        return 0
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())