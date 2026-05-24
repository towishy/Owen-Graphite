#!/usr/bin/env python3
"""Audit the generated manual-install release ZIP."""

from __future__ import annotations

import argparse
import json
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PREFIX = "Owen Graphite/"
REQUIRED_FILES = (
    "theme.css",
    "manifest.json",
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
    "dev/WIKI/MAP/map-info-classification.md",
    "dev/WIKI/MAP/theme-css-risk-map.html",
    "dev/WIKI/MAP/theme-css-risk-map.json",
    "dev/WIKI/MAP/selector-provenance.json",
    "screenshots/light.png",
    "screenshots/dark.png",
    "screenshots/readme/workspace-chrome-connected-glass.svg",
    "screenshots/readme/top-tabs-liquid-glass.svg",
    "screenshots/readme/workspace-writing-surface.jpg",
    "screenshots/readme/style-settings-report-options.jpg",
    "screenshots/readme/pdf-customer-delivery-feature.png",
    "screenshots/readme/owen-editor-toolbar-settings.jpg",
    "screenshots/readme/file-explorer-type-badges.svg",
    "screenshots/readme/sponsor-coffee.svg",
)


def repo_version() -> str:
    return json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))["version"]


def default_zip_path(version: str) -> Path:
    return ROOT / "dist" / f"Owen-Graphite-{version}.zip"


def read_zip_text(archive: zipfile.ZipFile, rel: str) -> str:
    return archive.read(PREFIX + rel).decode("utf-8")


def audit(zip_path: Path) -> None:
    version = repo_version()
    if not zip_path.exists():
        raise FileNotFoundError(f"release ZIP missing: {zip_path}")
    if zip_path.name != f"Owen-Graphite-{version}.zip":
        raise AssertionError(f"ZIP filename {zip_path.name!r} does not match manifest version {version}")
    if zip_path.stat().st_size < 100_000:
        raise AssertionError(f"release ZIP is unexpectedly small: {zip_path.stat().st_size} bytes")

    with zipfile.ZipFile(zip_path) as archive:
        names = set(archive.namelist())
        root_leaks = [name for name in names if name and not name.startswith(PREFIX)]
        if root_leaks:
            raise AssertionError("ZIP contains files outside 'Owen Graphite/': " + ", ".join(sorted(root_leaks)[:8]))

        missing = [rel for rel in REQUIRED_FILES if PREFIX + rel not in names]
        if missing:
            raise AssertionError("ZIP missing required assets: " + ", ".join(missing))

        for rel in REQUIRED_FILES:
            info = archive.getinfo(PREFIX + rel)
            if info.file_size == 0:
                raise AssertionError(f"ZIP asset is empty: {rel}")

        zip_manifest = json.loads(read_zip_text(archive, "manifest.json"))
        if zip_manifest.get("version") != version:
            raise AssertionError(f"ZIP manifest version {zip_manifest.get('version')!r} != repo version {version!r}")

        zip_theme = archive.read(PREFIX + "theme.css")
        repo_theme = (ROOT / "theme.css").read_bytes()
        if zip_theme != repo_theme:
            raise AssertionError("ZIP theme.css differs from repo root theme.css")

        zip_readme = read_zip_text(archive, "README.md")
        if f"Owen Graphite v{version}" not in zip_readme:
            raise AssertionError("ZIP README does not mention the current version")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("zip_path", nargs="?", type=Path, help="ZIP to audit. Defaults to dist/Owen-Graphite-<manifest version>.zip")
    args = parser.parse_args()

    try:
        version = repo_version()
        zip_path = args.zip_path or default_zip_path(version)
        audit(zip_path)
        print(f"OK: release ZIP contract passed for {zip_path.relative_to(ROOT)}")
        return 0
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
