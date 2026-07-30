#!/usr/bin/env python3
"""Install the Owen Graphite localization bridge without changing Style Settings data."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


PLUGIN = Path(__file__).resolve().parent
PLUGIN_ID = "owen-graphite-style-settings-l10n"
ASSETS = ("manifest.json", "main.js", "catalog.generated.json", "README.md")


def digest(path: Path) -> str | None:
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--obsidian-config", type=Path, required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    config = args.obsidian_config.resolve()
    upstream_data = config / "plugins" / "obsidian-style-settings" / "data.json"
    before = digest(upstream_data)
    if before is None:
        raise SystemExit(f"ERROR: Style Settings data not found: {upstream_data}")

    target = config / "plugins" / PLUGIN_ID
    for asset in ASSETS:
        source = PLUGIN / asset
        if not source.is_file():
            raise SystemExit(f"ERROR: build asset missing: {source}")
        destination = target / asset
        print(f"{'DRY-RUN' if args.dry_run else 'COPY'}: {source.name} -> {destination}")
        if not args.dry_run:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)

    community = config / "community-plugins.json"
    enabled = json.loads(community.read_text(encoding="utf-8-sig"))
    if PLUGIN_ID not in enabled:
        enabled.append(PLUGIN_ID)
        print(f"{'DRY-RUN' if args.dry_run else 'UPDATE'}: enable {PLUGIN_ID}")
        if not args.dry_run:
            community.write_text(json.dumps(enabled, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if digest(upstream_data) != before:
        raise RuntimeError("Style Settings data.json changed during bridge installation")
    print(f"OK: preserved Style Settings data.json sha256={before}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())