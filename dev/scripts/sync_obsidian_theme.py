#!/usr/bin/env python3
"""Bundle and sync Owen Graphite v3 into an Obsidian theme folder.

Re-bundles src/ via bundle_v3.py, promotes the bundle to theme.css, and
copies the release assets into <vault>/.obsidian/themes/Owen Graphite.

Reload Obsidian (Ctrl+R) after sync.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
THEME_FOLDER_NAME = "Owen Graphite"
RELEASE_ASSETS = [
    "theme.css",
    "manifest.json",
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
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
]
DEFAULT_VAULTS = [
    Path(r"H:\Owen-WIKI"),
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
    return [vault / ".obsidian" / "themes" / THEME_FOLDER_NAME for vault in DEFAULT_VAULTS]


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


def bundle_and_promote() -> None:
    bundle = load_module("bundle_v3", ROOT / "dev" / "scripts" / "bundle_v3.py")
    result = bundle.main([])
    if result:
        raise RuntimeError("bundle_v3.py failed")
    src = ROOT / "dist" / "theme-v3.css"
    dst = ROOT / "theme.css"
    shutil.copy2(src, dst)
    print(f"OK: promoted {src.relative_to(ROOT)} -> theme.css")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def copy_with_fallback(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    try:
        shutil.copy2(source, destination)
    except OSError as exc:
        print(f"WARN: copy2 failed for {source.relative_to(ROOT)} ({exc}); retrying with chunk copy")
        if destination.exists():
            destination.unlink()
        with source.open("rb") as src, destination.open("wb") as dst:
            for chunk in iter(lambda: src.read(32 * 1024), b""):
                dst.write(chunk)
    if sha256(source) != sha256(destination):
        raise RuntimeError(f"hash mismatch after copy: {source.relative_to(ROOT)}")


def copy_assets(target: Path, dry_run: bool) -> None:
    copied: list[dict[str, object]] = []
    for rel in RELEASE_ASSETS:
        source = ROOT / rel
        if not source.is_file() or source.stat().st_size == 0:
            raise FileNotFoundError(f"missing release asset: {rel}")
        destination = target / rel
        print(f"{'DRY-RUN' if dry_run else 'COPY'}: {rel} -> {destination}")
        if dry_run:
            continue
        copy_with_fallback(source, destination)
        copied.append({"path": rel, "sha256": sha256(source), "bytes": source.stat().st_size})
    if not dry_run:
        out = ROOT / "dev" / "TEMP" / "last-sync.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            json.dumps(
                {
                    "schema": "owen-graphite/sync-state/1",
                    "target": str(target),
                    "syncedAt": datetime.now(timezone.utc).isoformat(),
                    "assets": copied,
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        print(f"OK: wrote {out.relative_to(ROOT)}")


def verify_assets(target: Path) -> None:
    mismatches: list[str] = []
    for rel in RELEASE_ASSETS:
        source = ROOT / rel
        destination = target / rel
        if not source.is_file():
            mismatches.append(f"missing repo asset: {rel}")
            continue
        if not destination.is_file():
            mismatches.append(f"missing target asset: {rel}")
            continue
        if sha256(source) != sha256(destination):
            mismatches.append(f"hash mismatch: {rel}")
    if mismatches:
        raise RuntimeError("Obsidian sync verification failed: " + "; ".join(mismatches))
    print(f"OK: verified Owen Graphite assets in {target}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path, help="Obsidian theme folder to sync, e.g. H:\\Obsidian\\.obsidian\\themes\\Owen Graphite")
    parser.add_argument("--dry-run", action="store_true", help="Show copy operations without writing files.")
    parser.add_argument("--verify-only", action="store_true", help="Verify target assets match the repository without copying.")
    parser.add_argument("--skip-bundle", action="store_true", help="Reuse existing theme.css; skip bundle + promote.")
    parser.add_argument("--list-targets", action="store_true", help="Print known target candidates and exit.")
    args = parser.parse_args()

    if args.list_targets:
        for path in candidate_targets():
            marker = "exists" if path.exists() else "missing"
            print(f"{marker}: {path}")
        return 0

    target = find_target(args.target)
    print(f"Target: {target}")

    if args.verify_only:
        verify_assets(target)
        return 0

    if not args.skip_bundle:
        bundle_and_promote()

    copy_assets(target, args.dry_run)
    if not args.dry_run:
        print(f"OK: synced Owen Graphite to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
