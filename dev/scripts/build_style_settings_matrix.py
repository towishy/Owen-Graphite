#!/usr/bin/env python3
"""Generate a representative Style Settings coverage matrix."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
STYLE_SETTINGS = ROOT / "src" / "features" / "40-style-settings.css"
MANIFEST = ROOT / "manifest.json"
SETTING_BLOCK_RE = re.compile(r"/\*\s*@settings(?P<body>.*?)\*/", re.S)
FIELD_RE = re.compile(r"^\s{4}([a-zA-Z-]+):\s*(.*)\s*$")
VALUE_RE = re.compile(r"^\s{8}value:\s*(.*)\s*$")
SIMPLE_OPTION_RE = re.compile(r"^\s{6}-\s+([^\s].*)\s*$")
FUNCTIONAL_TYPES = {"class-toggle", "class-select", "variable-color", "variable-number-slider", "variable-select", "variable-text"}


def normalize(value: object) -> str:
    text = str(value).strip()
    if len(text) >= 2 and text[0] == text[-1] and text[0] in {'"', "'"}:
        return text[1:-1]
    return text


def version() -> str:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))["version"]


def parse_settings() -> list[dict[str, Any]]:
    match = SETTING_BLOCK_RE.search(STYLE_SETTINGS.read_text(encoding="utf-8"))
    if not match:
        raise AssertionError("missing @settings block")
    entries: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    for line in match.group("body").splitlines():
        if line.startswith("  -") and not line.startswith("      -"):
            if current is not None:
                entries.append(current)
            current = {"values": []}
            continue
        if current is None:
            continue
        field = FIELD_RE.match(line)
        if field:
            key, value = field.groups()
            current[key] = normalize(value)
            continue
        value_match = VALUE_RE.match(line)
        if value_match:
            current.setdefault("values", []).append(normalize(value_match.group(1)))
            continue
        simple_option = SIMPLE_OPTION_RE.match(line)
        if simple_option and "label:" not in simple_option.group(1):
            current.setdefault("values", []).append(normalize(simple_option.group(1)))
    if current is not None:
        entries.append(current)
    return entries


def value_points(entry: dict[str, Any]) -> list[str]:
    entry_type = entry.get("type")
    default = normalize(entry.get("default", ""))
    if entry_type == "class-toggle":
        return ["true", "false"]
    if entry_type in {"class-select", "variable-select"}:
        return [normalize(value) for value in entry.get("values", [])]
    if entry_type == "variable-number-slider":
        points = [normalize(entry.get("min", "")), default, normalize(entry.get("max", ""))]
        return [point for index, point in enumerate(points) if point and point not in points[:index]]
    if entry_type == "variable-color":
        return [default, "#0ea5e9", "#64748b"]
    if entry_type == "variable-text":
        return ["", "Prepared by", "Long label for clipping and ellipsis validation"]
    return [default]


def scenario_for(entry: dict[str, Any], value: str, index: int) -> dict[str, object]:
    setting_id = str(entry["id"])
    entry_type = str(entry.get("type"))
    body_classes = []
    if entry_type == "class-select" and value:
        body_classes.append(value)
    elif entry_type == "class-toggle" and value == "true":
        body_classes.append(setting_id)
    return {
        "id": f"setting-{setting_id}-{index}",
        "purpose": f"Cover {setting_id}={value!r}",
        "theme": "light",
        "media": "screen" if not setting_id.startswith("ogd-pdf") else "print",
        "settings": {setting_id: value},
        "bodyClasses": body_classes,
    }


def main() -> int:
    try:
        entries = [entry for entry in parse_settings() if entry.get("type") in FUNCTIONAL_TYPES]
        scenarios: list[dict[str, object]] = [
            {"id": "default-light-screen", "purpose": "Default light screen baseline", "theme": "light", "media": "screen", "settings": {}, "bodyClasses": []},
            {"id": "default-dark-screen", "purpose": "Default dark screen baseline", "theme": "dark", "media": "screen", "settings": {}, "bodyClasses": []},
            {"id": "default-light-print", "purpose": "Default light print baseline", "theme": "light", "media": "print", "settings": {}, "bodyClasses": []},
        ]
        coverage: dict[str, list[str]] = {}
        for entry in entries:
            points = value_points(entry)
            coverage[str(entry["id"])] = points
            for index, value in enumerate(points, start=1):
                scenarios.append(scenario_for(entry, value, index))
        scenarios.extend(
            [
                {
                    "id": "pdf-marginalia-dual-key-value",
                    "purpose": "Dependent PDF header/footer dual key/value labels with independent palettes.",
                    "theme": "light",
                    "media": "print",
                    "settings": {
                        "ogd-pdf-header-enabled": "true",
                        "ogd-pdf-footer-enabled": "true",
                        "ogd-pdf-label-layout": "ogd-pdf-label-segmented-dual",
                        "ogd-pdf-header-text": "Prepared by",
                        "ogd-pdf-header-value": "Owen Graphite",
                        "ogd-pdf-header-text-2": "Reviewed by",
                        "ogd-pdf-header-value-2": "Design QA",
                    },
                    "bodyClasses": ["ogd-pdf-header-enabled", "ogd-pdf-footer-enabled", "ogd-pdf-label-segmented-dual"],
                },
                {
                    "id": "lp-pdf-parity-comfortable-visible",
                    "purpose": "LP/PDF parity fixture with the comfortable font preset.",
                    "theme": "light",
                    "media": "print",
                    "settings": {"ogd-pdf-font-size": "ogd-pdf-font-comfortable"},
                    "bodyClasses": ["ogd-pdf-font-comfortable"],
                },
            ]
        )
        payload = {
            "schema": "owen-graphite/style-settings-coverage-matrix/1",
            "version": version(),
            "functionalOptionCount": len(entries),
            "scenarioCount": len(scenarios),
            "coverage": coverage,
            "uncoveredSettings": [],
            "scenarios": scenarios,
        }
        out = ROOT / "dev" / "WIKI" / "effective-baseline" / f"v{version()}" / "style-settings-matrix.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"OK: wrote {out.relative_to(ROOT)} ({len(scenarios)} scenarios)")
        return 0
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
