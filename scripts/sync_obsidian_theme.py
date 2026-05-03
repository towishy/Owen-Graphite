#!/usr/bin/env python3
"""Bundle, validate, and sync Owen Graphite into an Obsidian theme folder."""

from __future__ import annotations

import argparse
import importlib.util
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
THEME_FOLDER_NAME = "Owen Graphite"
RELEASE_ASSETS = [
    "theme.css",
    "manifest.json",
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
    "docs/ai-document-guide.md",
    "docs/qa-checklist.md",
    "docs/fixtures/README.md",
    "docs/fixtures/liquid-glass-core-state-matrix.html",
    "docs/fixtures/refero-inspired-glass-states.html",
    "docs/liquid-glass-hover-study-sample.html",
    "dev/MAP/map-info-classification.md",
    "dev/MAP/theme-css-risk-map.html",
    "dev/MAP/theme-css-risk-map.json",
    "screenshots/light.png",
    "screenshots/dark.png",
    "screenshots/report.png",
]
LEGACY_ASSET_PATHS = [
    "docs/MAP",
]
DEFAULT_VAULTS = [
    Path(r"H:\Obsidian"),
    Path(r"D:\JAELE\Obsidian"),
    Path.home() / "Work" / "Obsidian",
    Path.home() / "work" / "Obsidian",
]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load {path.relative_to(ROOT)}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def candidate_targets() -> list[Path]:
    targets: list[Path] = []
    for vault in DEFAULT_VAULTS:
        targets.append(vault / ".obsidian" / "themes" / THEME_FOLDER_NAME)
    return targets


def find_target(explicit: Path | None) -> Path:
    if explicit:
        return explicit
    existing = [path for path in candidate_targets() if path.exists()]
    if existing:
        return existing[0]
    candidates = "\n".join(f"- {path}" for path in candidate_targets())
    raise SystemExit(
        "ERROR: no Obsidian target theme folder found. Pass --target explicitly.\n"
        f"Checked:\n{candidates}"
    )


def run_validator(*args: str) -> None:
    command = [sys.executable, str(ROOT / "scripts" / "validate_theme.py"), *args]
    subprocess.run(command, cwd=ROOT, check=True)


def bundle_theme() -> None:
    bundle = load_module("bundle_theme", ROOT / "scripts" / "bundle_theme.py")
    bundle.write_bundle()


def copy_assets(target: Path, dry_run: bool) -> None:
    for rel in LEGACY_ASSET_PATHS:
        legacy = target / rel
        if not legacy.exists():
            continue
        print(f"{'DRY-RUN' if dry_run else 'REMOVE'}: legacy {legacy}")
        if not dry_run:
            shutil.rmtree(legacy) if legacy.is_dir() else legacy.unlink()

    for rel in RELEASE_ASSETS:
        source = ROOT / rel
        if not source.is_file() or source.stat().st_size == 0:
            raise FileNotFoundError(f"missing release asset: {rel}")
        destination = target / rel
        print(f"{'DRY-RUN' if dry_run else 'COPY'}: {rel} -> {destination}")
        if dry_run:
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path, help="Obsidian theme folder to sync, e.g. H:\\Obsidian\\.obsidian\\themes\\Owen Graphite")
    parser.add_argument("--dry-run", action="store_true", help="Show copy operations without writing files.")
    parser.add_argument("--skip-precheck", action="store_true", help="Skip validation before copying.")
    parser.add_argument("--list-targets", action="store_true", help="Print known target candidates and exit.")
    args = parser.parse_args()

    if args.list_targets:
        for path in candidate_targets():
            marker = "exists" if path.exists() else "missing"
            print(f"{marker}: {path}")
        return 0

    target = find_target(args.target)
    print(f"Target: {target}")

    bundle_theme()
    if not args.skip_precheck:
        run_validator("--ci")

    copy_assets(target, args.dry_run)
    if not args.dry_run:
        run_validator("--target", str(target))
        print(f"OK: synced Owen Graphite to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
