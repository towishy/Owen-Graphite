#!/usr/bin/env python3
"""Contract and runtime-model tests for the localization bridge."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

import build


PLUGIN = Path(__file__).resolve().parent


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    entries = build.parse_schema()
    catalog = build.build_catalog()
    assert len(entries) == 62
    assert len(catalog) == len(entries)
    assert entries[0]["id"] == "ogd-settings-interface"
    assert entries[1]["id"] == "ogd-style-settings-language"
    assert entries[1]["default"] == "ogd-language-auto"
    assert [option["value"] for option in entries[1]["options"]] == [
        "ogd-language-auto",
        "ogd-language-ko",
        "ogd-language-en",
    ]
    for entry in entries:
        localized = catalog[str(entry["id"])]
        for locale in ("en", "ko"):
            assert localized[locale]["title"]
            assert localized[locale]["default"] == entry.get("default", "")

    build.main()
    first = {name: digest(PLUGIN / name) for name in ("main.js", "catalog.generated.json")}
    build.main()
    assert first == {name: digest(PLUGIN / name) for name in first}, "build is not deterministic"
    subprocess.run(["node", "--check", "main.js"], cwd=PLUGIN, check=True)

    node_test = r"""
const core = require('./src/core.js');
const catalog = require('./catalog.generated.json');
const classes = (...values) => ({ contains: value => values.includes(value) });
if (core.localeFromClasses(classes('ogd-language-ko'), 'en') !== 'ko') process.exit(1);
if (core.localeFromClasses(classes('ogd-language-en'), 'ko') !== 'en') process.exit(2);
if (core.localeFromClasses(classes(), 'ko-KR') !== 'ko') process.exit(3);
if (core.localeFromClasses(classes(), 'en') !== 'en') process.exit(4);
if (catalog['ogd-settings-reading'].ko.title !== '읽기와 본문') process.exit(5);
if (catalog['ogd-style-settings-language'].ko.options['ogd-language-auto'] !== '자동 (Obsidian)') process.exit(6);
console.log('OK: auto/ko/en locale model');
"""
    subprocess.run(["node", "-e", node_test], cwd=PLUGIN, check=True)
    manifest = json.loads((PLUGIN / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["id"] == "owen-graphite-style-settings-l10n"
    print("OK: localized schema and deterministic runtime bundle")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())