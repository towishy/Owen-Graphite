#!/usr/bin/env python3
"""Audit release version metadata across manifest, README, changelog, and docs."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")


def read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def manifest_version() -> str:
    data = json.loads(read_text("manifest.json"))
    version = str(data.get("version", ""))
    if not SEMVER_RE.match(version):
        raise AssertionError(f"manifest.json version is not semver: {version!r}")
    return version


def first_changelog_version() -> str:
    changelog = read_text("CHANGELOG.md")
    match = re.search(r"^## v(\d+\.\d+\.\d+)\s*$", changelog, re.MULTILINE)
    if not match:
        raise AssertionError("CHANGELOG.md has no top-level release heading like '## vX.Y.Z'")
    return match.group(1)


def assert_contains(path: str, needle: str) -> None:
    text = read_text(path)
    if needle not in text:
        raise AssertionError(f"{path} does not contain {needle!r}")


def assert_contains_any(path: str, needles: list[str]) -> None:
    text = read_text(path)
    if not any(needle in text for needle in needles):
        raise AssertionError(f"{path} does not contain any of {needles!r}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tag", help="Optional numeric git/GitHub tag to compare with manifest version.")
    args = parser.parse_args()

    try:
        version = manifest_version()
        expected_tag = args.tag if args.tag else None
        if expected_tag and not SEMVER_RE.match(expected_tag):
            raise AssertionError(f"release tag must be numeric semver without a leading v: {args.tag!r}")
        if expected_tag and expected_tag != version:
            raise AssertionError(f"tag {args.tag!r} does not match manifest version {version!r}")

        changelog_version = first_changelog_version()
        if changelog_version != version:
            raise AssertionError(f"CHANGELOG latest v{changelog_version} does not match manifest {version}")

        assert_contains("README.md", f"**Owen Graphite v{version}**")
        assert_contains_any("README.md", [f"| **Version** | `{version}` |", f"| **버전** | `{version}` |"])
        assert_contains_any("README.md", [
            f"| **Baseline / rollback target** | `v{version}` |",
            f"| **베이스라인 / 롤백 기준** | `v{version}` |",
        ])
        assert_contains("README.md", f"Owen-Graphite-{version}.zip")
        assert_contains("screenshots/README.md", f"Owen Graphite v{version}")
        assert_contains("dev/WIKI/DOCS/v3/release-plan.md", f"latest: v{version}")
        assert_contains("dev/WIKI/DOCS/v3/release-plan.md", f"baseline = `v{version}`")
        assert_contains("dev/WIKI/DOCS/v3/release-plan.md", f"| `manifest.json` version | `{version}` |")
        assert_contains("dev/WIKI/DOCS/v3/release-plan.md", f"dist/Owen-Graphite-{version}.zip")
        assert_contains(".github/workflows/release.yml", "screenshots/fonts.png")
        assert_contains(".github/workflows/release.yml", "screenshots/readme/owen-kit.png")

        print(f"OK: release metadata is consistent for {version}")
        return 0
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
