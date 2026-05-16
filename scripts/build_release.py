#!/usr/bin/env python3
"""Build a manual-install release ZIP for Owen Graphite v3.

Bundles src/ via bundle_v3.py, promotes the result to theme.css, and packages
the standard release assets into dist/Owen-Graphite-<version>.zip.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import shutil
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
    "screenshots/light.png",
    "screenshots/dark.png",
    "screenshots/report.png",
]


def version() -> str:
    return json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))["version"]


def bundle_v3() -> Path:
    script = ROOT / "scripts" / "bundle_v3.py"
    spec = importlib.util.spec_from_file_location("bundle_v3", script)
    if spec is None or spec.loader is None:
        raise RuntimeError("unable to load scripts/bundle_v3.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    module.main()
    return ROOT / "dist" / "theme-v3.css"


def promote_to_theme_css(bundle: Path) -> None:
    target = ROOT / "theme.css"
    if not bundle.is_file():
        raise FileNotFoundError(f"bundle missing: {bundle}")
    shutil.copy2(bundle, target)
    print(f"OK: promoted {bundle.relative_to(ROOT)} -> theme.css")


def build(output_dir: Path, skip_bundle: bool = False) -> Path:
    if not skip_bundle:
        bundle = bundle_v3()
        promote_to_theme_css(bundle)
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
    parser.add_argument("--skip-bundle", action="store_true", help="Reuse existing theme.css; skip bundle + promote.")
    args = parser.parse_args()
    build(args.output_dir, skip_bundle=args.skip_bundle)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
