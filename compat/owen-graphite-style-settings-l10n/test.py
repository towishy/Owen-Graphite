#!/usr/bin/env python3
"""Translation completeness and compatibility tests for the locale companion."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


PLUGIN = Path(__file__).resolve().parent
ROOT = PLUGIN.parents[1]
sys.path.insert(0, str(PLUGIN))
import build  # noqa: E402


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    entries = build.parse_schema()
    before = [(entry["id"], entry["type"], entry.get("default", "")) for entry in entries]
    catalog = build.build_catalog()
    assert len(entries) == 62
    assert len(catalog) == len(entries)
    assert entries[0]["id"] == "ogd-settings-interface"
    assert entries[1]["id"] == "ogd-style-settings-language"
    assert entries[1]["default"] == "ogd-language-auto"
    assert [option["value"] for option in entries[1]["options"]] == ["ogd-language-auto", "ogd-language-ko", "ogd-language-en"]
    for entry in entries:
        setting_id = entry["id"]
        localized = catalog[setting_id]
        for locale in ("ko", "en"):
            assert localized[locale]["title"], f"missing {locale} title: {setting_id}"
            if entry.get("description"):
                assert localized[locale]["description"], f"missing {locale} description: {setting_id}"
            assert localized[locale]["default"] == entry.get("default", "")
            expected_values = {option.get("value", option.get("label")) for option in entry["options"]}
            assert set(localized[locale]["options"]) == expected_values, f"option coverage: {setting_id}/{locale}"
    build.main()
    first_hashes = {name: digest(PLUGIN / name) for name in ("main.js", "core.js", "catalog.generated.json")}
    build.main()
    assert first_hashes == {name: digest(PLUGIN / name) for name in first_hashes}, "build is not deterministic"
    after_entries = build.parse_schema()
    after = [(entry["id"], entry["type"], entry.get("default", "")) for entry in after_entries]
    assert before == after, "locale build changed Style Settings IDs/types/defaults"
    node_test = r"""
const core = require('./core.js');
const catalog = require('./catalog.generated.json');
const classes = (...values) => ({ contains: value => values.includes(value) });
if (core.localeFromClasses(classes('ogd-language-ko')) !== 'ko') process.exit(1);
if (core.localeFromClasses(classes('ogd-language-en')) !== 'en') process.exit(2);
if (core.localeFromClasses(classes(), 'ko-KR') !== 'ko') process.exit(3);
if (core.localeFromClasses(classes(), 'ja') !== 'en') process.exit(4);
if (core.localeFromClasses(classes('ogd-language-en'), 'ko') !== 'en') process.exit(5);
if (core.localeFromClasses(classes('ogd-language-ko'), 'en') !== 'ko') process.exit(6);
const ko = core.translateModel(catalog, 'ogd-style-settings-language', 'ko', ['ogd-language-auto','ogd-language-ko','ogd-language-en']);
const en = core.translateModel(catalog, 'ogd-style-settings-language', 'en', ['ogd-language-auto','ogd-language-ko','ogd-language-en']);
if (ko.title !== '언어' || en.title !== 'Language') process.exit(4);
if (ko.options[0] !== '자동 (Obsidian)' || en.options[0] !== 'Automatic (Obsidian)') process.exit(7);
console.log('OK: locale switching model');
"""
    subprocess.run(["node", "-e", node_test], cwd=PLUGIN, check=True)
    main_source = (PLUGIN / "src" / "main.js").read_text(encoding="utf-8")
    assert "Export settings for: " in main_source
    assert "Error importing style settings:" in main_source
    manifest = json.loads((PLUGIN / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["id"] == "owen-graphite-style-settings-l10n"
    print("OK: 62 titles, 46 descriptions, and every option label are complete in ko/en")
    print("OK: existing IDs, types, defaults, and stored-value namespace remain stable")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())