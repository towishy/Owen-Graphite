#!/usr/bin/env python3
"""Install the locale companion without modifying Style Settings data.json."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path


PLUGIN = Path(__file__).resolve().parent
PLUGIN_ID = "owen-graphite-style-settings-l10n"
ASSETS = ("manifest.json", "main.js", "core.js", "catalog.generated.json", "LICENSE", "README.md")
LANGUAGE_ID = "ogd-style-settings-language"
INTERFACE_ID = "ogd-settings-interface"


def digest(path: Path) -> str | None:
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None


def version_tuple(value: str) -> tuple[int, ...]:
    return tuple(int(part) for part in re.findall(r"\d+", value))


def interface_schema() -> str:
    source = PLUGIN.parents[1] / "src" / "features" / "40-style-settings.css"
    text = source.read_text(encoding="utf-8")
    match = re.search(
        r"(?ms)^  -\r?\n    id: ogd-settings-interface\r?\n.*?(?=^  -\r?\n    id: ogd-settings-reading\r?$)",
        text,
    )
    if not match:
        raise RuntimeError("interface language schema entries not found in Owen Graphite source")
    return match.group(0).rstrip() + "\n"


def patch_installed_theme(config: Path, dry_run: bool) -> None:
    theme = config / "themes" / "Owen Graphite" / "theme.css"
    installed_manifest = theme.parent / "manifest.json"
    repo_manifest = PLUGIN.parents[1] / "manifest.json"
    if not theme.is_file() or not installed_manifest.is_file():
        raise RuntimeError(f"installed Owen Graphite theme not found: {theme.parent}")
    installed_version = json.loads(installed_manifest.read_text(encoding="utf-8-sig"))["version"]
    repo_version = json.loads(repo_manifest.read_text(encoding="utf-8-sig"))["version"]
    original = theme.read_text(encoding="utf-8")
    schema = interface_schema()
    if INTERFACE_ID in original:
        pattern = re.compile(
            r"(?ms)^  -\r?\n    id: ogd-settings-interface\r?\n.*?(?=^  -\r?\n    id: ogd-settings-reading\r?$)"
        )
        match = pattern.search(original)
        if not match:
            raise RuntimeError("installed interface locale schema entries could not be isolated")
        if match.group(0).rstrip() == schema.rstrip():
            print(f"OK: installed Owen Graphite {installed_version} already contains current interface language schema")
            return
        patched = original[: match.start()] + schema + original[match.end() :]
        operation = "update interface language schema"
    elif LANGUAGE_ID in original:
        pattern = re.compile(
            r"(?ms)^  -\r?\n    id: ogd-style-settings-language\r?\n.*?(?=^  -\r?\n    id:)"
        )
        match = pattern.search(original)
        if not match:
            raise RuntimeError("installed locale schema entry could not be isolated")
        patched = original[: match.start()] + schema + original[match.end() :]
        operation = "upgrade locale schema to interface group"
    else:
        marker = "id: owen-graphite-document\nsettings:\n"
        if marker not in original:
            raise RuntimeError("installed theme does not contain the expected Owen Graphite settings schema")
        patched = original.replace(marker, marker + schema, 1)
        operation = "inject interface language schema"
    if patched.count(INTERFACE_ID) != 1 or patched.count(LANGUAGE_ID) != 1:
        raise RuntimeError("interface language schema patch is not unique")
    action = "PATCH-DRY-RUN" if dry_run else "PATCH"
    relation = "newer" if version_tuple(installed_version) > version_tuple(repo_version) else "same/older"
    print(f"{action}: Owen Graphite {installed_version} ({relation} than repo {repo_version}); {operation} only")
    if dry_run:
        return
    backup = theme.with_name(f"theme.css.pre-l10n-{digest(theme)[:12]}.bak")
    if not backup.exists():
        shutil.copy2(theme, backup)
    theme.write_text(patched, encoding="utf-8")
    if json.loads(installed_manifest.read_text(encoding="utf-8-sig"))["version"] != installed_version:
        raise RuntimeError("installed theme manifest changed during locale patch")
    print(f"OK: preserved manifest {installed_version}; backup={backup.name}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--obsidian-config", type=Path, required=True, help="Path to the vault .obsidian folder")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    config = args.obsidian_config.resolve()
    upstream_data = config / "plugins" / "obsidian-style-settings" / "data.json"
    before = digest(upstream_data)
    if before is None:
        raise SystemExit(f"ERROR: Style Settings data not found: {upstream_data}")
    patch_installed_theme(config, args.dry_run)
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
    if not community.is_file():
        raise SystemExit(f"ERROR: community plugin registry not found: {community}")
    enabled = json.loads(community.read_text(encoding="utf-8-sig"))
    if PLUGIN_ID not in enabled:
        enabled.append(PLUGIN_ID)
        print(f"{'DRY-RUN' if args.dry_run else 'UPDATE'}: enable {PLUGIN_ID} in {community}")
        if not args.dry_run:
            community.write_text(json.dumps(enabled, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if digest(upstream_data) != before:
        raise RuntimeError("Style Settings data.json changed during companion installation")
    print(f"OK: preserved Style Settings data.json sha256={before}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())