#!/usr/bin/env python3
"""Build a manual-install release ZIP for Owen Graphite."""

from __future__ import annotations

import argparse
import json
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FILES = [
    "theme.css",
    "manifest.json",
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
    "snippets/zz-obsidian-gray-force-override-v2.css",
]


def version() -> str:
    return json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))["version"]


def build(output_dir: Path) -> Path:
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