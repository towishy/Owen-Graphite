#!/usr/bin/env python3
"""Build the Owen Graphite Style Settings localization bridge."""

from __future__ import annotations

import json
import re
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

        field = re.match(r"^    (id|title|title\.ko|description|description\.ko|type|default):\s*(.*)$", line)
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


def localized_label(label: str, locale: str) -> str:
    if " / " not in label:
        return label
    english, korean = label.split(" / ", 1)
    return korean if locale == "ko" else english


def build_catalog() -> dict[str, dict[str, object]]:
    catalog: dict[str, dict[str, object]] = {}
    for entry in parse_schema():
        setting_id = str(entry["id"])
        if not entry.get("title") or not entry.get("title.ko"):
            raise RuntimeError(f"missing localized title for {setting_id}")
        if bool(entry.get("description")) != bool(entry.get("description.ko")):
            raise RuntimeError(f"description locale mismatch for {setting_id}")

        localized: dict[str, object] = {}
        for locale in ("en", "ko"):
            options: dict[str, str] = {}
            for option in entry["options"]:
                value = str(option.get("value", option.get("label", "")))
                label = str(option.get("label", value))
                if not value:
                    raise RuntimeError(f"invalid option in {setting_id}")
                options[value] = localized_label(label, locale)
            localized[locale] = {
                "title": entry["title.ko"] if locale == "ko" else entry["title"],
                "description": entry.get("description.ko", "") if locale == "ko" else entry.get("description", ""),
                "options": options,
                "default": entry.get("default", ""),
            }
        catalog[setting_id] = localized
    return catalog


def build_main(catalog: dict[str, dict[str, object]]) -> str:
    core = (SOURCE / "core.js").read_text(encoding="utf-8").removeprefix('"use strict";\n\n')
    core = re.sub(r"\nmodule\.exports = \{.*?\};\s*$", "", core, flags=re.DOTALL)
    main = (SOURCE / "main.js").read_text(encoding="utf-8").removeprefix('"use strict";\n\n')
    main = main.replace('const catalog = require("./catalog.generated.json");\n', "")
    main = main.replace('const { localeFromClasses, localizedEntry, splitTooltipText } = require("./core.js");\n', "")
    embedded_catalog = json.dumps(catalog, ensure_ascii=False, separators=(",", ":"))
    return f'"use strict";\n\n{core}\n\nconst catalog = {embedded_catalog};\n\n{main}'


def main() -> int:
    catalog = build_catalog()
    (PLUGIN / "catalog.generated.json").write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (PLUGIN / "main.js").write_text(build_main(catalog), encoding="utf-8")
    print(f"OK: built localization bridge ({len(catalog)} schema entries)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())