#!/usr/bin/env python3
"""Generate and stage the Owen Graphite Style Settings locale companion."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PLUGIN = Path(__file__).resolve().parent
SCHEMA = ROOT / "src" / "features" / "40-style-settings.css"
SOURCE = PLUGIN / "src"


def normalize(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def parse_schema() -> list[dict[str, object]]:
    text = SCHEMA.read_text(encoding="utf-8")
    match = re.search(r"/\*\s*@settings(?P<body>.*?)\*/", text, re.DOTALL)
    if not match:
        raise RuntimeError("Owen Graphite @settings block not found")
    entries: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    current_option: dict[str, str] | None = None
    for line in match.group("body").splitlines():
        if line == "  -":
            if current is not None:
                entries.append(current)
            current = {"options": []}
            current_option = None
            continue
        if current is None:
            continue
        field = re.match(r"^    (id|title|description|type|default):\s*(.*)$", line)
        if field:
            current[field.group(1)] = normalize(field.group(2))
            continue
        if line == "      -":
            current_option = {}
            current["options"].append(current_option)
            continue
        simple_option = re.match(r"^      -\s+(.+)$", line)
        if simple_option:
            value = normalize(simple_option.group(1))
            current["options"].append({"label": value, "value": value})
            current_option = None
            continue
        option_field = re.match(r"^        (label|value):\s*(.*)$", line)
        if option_field and current_option is not None:
            current_option[option_field.group(1)] = normalize(option_field.group(2))
    if current is not None:
        entries.append(current)
    return entries


def build_catalog() -> dict[str, dict[str, object]]:
    english = json.loads((SOURCE / "en.json").read_text(encoding="utf-8"))
    option_labels = english.pop("_optionLabels")
    entries = parse_schema()
    catalog: dict[str, dict[str, object]] = {}
    for entry in entries:
        setting_id = str(entry["id"])
        if setting_id not in english:
            raise RuntimeError(f"missing English translation for {setting_id}")
        translated = english[setting_id]
        if not translated.get("title"):
            raise RuntimeError(f"missing English title for {setting_id}")
        if entry.get("description") and not translated.get("description"):
            raise RuntimeError(f"missing English description for {setting_id}")
        ko_options: dict[str, str] = {}
        en_options: dict[str, str] = {}
        for option in entry["options"]:
            value = option.get("value", option.get("label"))
            label = option.get("label", value)
            if not value or not label:
                raise RuntimeError(f"invalid option in {setting_id}")
            ko_options[value] = label
            en_options[value] = option_labels.get(label, label)
        catalog[setting_id] = {
            "ko": {
                "title": entry["title"],
                "description": entry.get("description", ""),
                "options": ko_options,
                "default": entry.get("default", ""),
            },
            "en": {
                "title": translated["title"],
                "description": translated.get("description", ""),
                "options": en_options,
                "default": entry.get("default", ""),
            },
        }
    if set(english) != set(catalog):
        extra = sorted(set(english) - set(catalog))
        raise RuntimeError(f"translations without schema entries: {extra}")
    return catalog


def main() -> int:
    catalog = build_catalog()
    generated = SOURCE / "catalog.generated.json"
    generated.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for filename in ("main.js", "core.js", "catalog.generated.json"):
        shutil.copy2(SOURCE / filename, PLUGIN / filename)
    print(f"OK: built locale companion ({len(catalog)} schema entries)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())