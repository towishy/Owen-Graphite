#!/usr/bin/env python3
"""Build and audit the Owen Graphite Style Settings locale companion ZIP."""

from __future__ import annotations

import argparse
import json
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COMPANION = ROOT / "compat" / "owen-graphite-style-settings-l10n"
FILES = (
    "manifest.json",
    "main.js",
    "core.js",
    "catalog.generated.json",
    "README.md",
    "LICENSE",
)
PREFIX = "owen-graphite-style-settings-l10n"


def build(output_dir: Path) -> Path:
    manifest = json.loads((COMPANION / "manifest.json").read_text(encoding="utf-8"))
    version = manifest["version"]
    output_dir.mkdir(parents=True, exist_ok=True)
    zip_path = output_dir / f"Owen-Graphite-Style-Settings-Language-{version}.zip"

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for filename in FILES:
            source = COMPANION / filename
            if not source.is_file() or source.stat().st_size == 0:
                raise FileNotFoundError(f"missing companion asset: {source.relative_to(ROOT)}")
            archive.write(source, Path(PREFIX) / filename)

    with zipfile.ZipFile(zip_path) as archive:
        names = set(archive.namelist())
        expected = {str(Path(PREFIX) / filename).replace("\\", "/") for filename in FILES}
        if names != expected:
            raise AssertionError(f"unexpected companion ZIP entries: {sorted(names ^ expected)}")
        packaged_manifest = json.loads(archive.read(f"{PREFIX}/manifest.json"))
        if packaged_manifest != manifest:
            raise AssertionError("packaged companion manifest differs from source")

    print(f"OK: built and audited {zip_path.relative_to(ROOT)}")
    return zip_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    build(args.output_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())