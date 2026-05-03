#!/usr/bin/env python3
"""Build a manual-install release ZIP for Owen Graphite."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FILES = [
    "theme.css",
    "manifest.json",
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
    "dev/MAP/map-info-classification.md",
    "dev/MAP/theme-css-risk-map.html",
    "dev/MAP/theme-css-risk-map.json",
    "screenshots/light.png",
    "screenshots/dark.png",
    "screenshots/report.png",
]


def version() -> str:
    return json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))["version"]


def bundle_theme() -> None:
    script = ROOT / "scripts" / "bundle_theme.py"
    spec = importlib.util.spec_from_file_location("bundle_theme", script)
    if spec is None or spec.loader is None:
        raise RuntimeError("unable to load scripts/bundle_theme.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    module.write_bundle()


def build(output_dir: Path) -> Path:
    bundle_theme()
    release_version = version()
    output_dir.mkdir(parents=True, exist_ok=True)
    zip_path = output_dir / f"Owen-Graphite-{release_version}.zip"
    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for rel in DEFAULT_FILES:
            source = ROOT / rel
            if not source.is_file() or source.stat().st_size == 0:
                raise FileNotFoundError(f"missing release asset: {rel}")
            archive.write(source, Path("Owen Graphite") / rel)

    print(f"OK: built {zip_path} ({zip_path.stat().st_size // 1024} KB)")
    return zip_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist", help="Directory for generated release ZIP.")
    args = parser.parse_args()
    build(args.output_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())