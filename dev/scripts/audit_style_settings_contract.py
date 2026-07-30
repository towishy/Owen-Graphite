#!/usr/bin/env python3
"""Audit Style Settings metadata against the recorded v3 contract JSON."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
STYLE_SETTINGS = ROOT / "src" / "features" / "40-style-settings.css"
CONTRACT = ROOT / "dev" / "WIKI" / "DOCS" / "v3" / "style-settings-contract.json"
FUNCTIONAL_TYPES = {"class-toggle", "class-select", "variable-color", "variable-number-slider", "variable-select", "variable-text"}


SETTING_BLOCK_RE = re.compile(r"/\*\s*@settings(?P<body>.*?)\*/", re.DOTALL)
FIELD_RE = re.compile(r"^\s{4}(id|title|title\.ko|description|description\.ko|type|default):\s*(.*)\s*$")
LABEL_RE = re.compile(r"^\s{8}label:\s*(.*)\s*$")
VALUE_RE = re.compile(r"^\s{8}value:\s*(.*)\s*$")
HANGUL_RE = re.compile(r"[가-힣]")


def normalize(value: object) -> str:
    text = str(value).strip()
    if len(text) >= 2 and text[0] == text[-1] and text[0] in {'"', "'"}:
        text = text[1:-1]
    return text


def parse_settings() -> list[dict[str, object]]:
    text = STYLE_SETTINGS.read_text(encoding="utf-8")
    match = SETTING_BLOCK_RE.search(text)
    if not match:
        raise AssertionError("missing /* @settings ... */ block")

    entries: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    for line in match.group("body").splitlines():
        if line.startswith("  -") and not line.startswith("      -"):
            if current is not None:
                entries.append(current)
            current = {"labels": [], "values": []}
            continue
        if current is None:
            continue

        field = FIELD_RE.match(line)
        if field:
            key, value = field.groups()
            if key in {"title", "title.ko", "description", "description.ko"} and ": " in value and not value.startswith(("'", '"')):
                raise AssertionError(f"{current.get('id', '<unknown>')} {key} contains an unquoted YAML mapping colon")
            current[key] = normalize(value)
            continue

        label = LABEL_RE.match(line)
        if label:
            current.setdefault("labels", []).append(normalize(label.group(1)))
            continue

        value = VALUE_RE.match(line)
        if value:
            current.setdefault("values", []).append(normalize(value.group(1)))

    if current is not None:
        entries.append(current)
    return entries


def main() -> int:
    try:
        contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
        entries = parse_settings()
        functional = [entry for entry in entries if entry.get("type") in FUNCTIONAL_TYPES]
        contract_options = contract["options"]

        if contract.get("schema_name") != "Owen Graphite":
            raise AssertionError("contract schema_name drifted")
        if contract.get("schema_id") != "owen-graphite-document":
            raise AssertionError("contract schema_id drifted")
        if len(entries) != int(contract["total_entries"]):
            raise AssertionError(f"settings entry count {len(entries)} != contract {contract['total_entries']}")
        if len(functional) != int(contract["functional_options"]):
            raise AssertionError(f"functional option count {len(functional)} != contract {contract['functional_options']}")
        if len(functional) != len(contract_options):
            raise AssertionError(f"functional list count {len(functional)} != contract options {len(contract_options)}")

        for entry in entries:
            setting_id = entry.get("id", "<missing>")
            if not entry.get("title") or not entry.get("title.ko"):
                raise AssertionError(f"{setting_id} must define both title and title.ko")
            if bool(entry.get("description")) != bool(entry.get("description.ko")):
                raise AssertionError(f"{setting_id} must define description and description.ko together")
            for label in entry.get("labels", []):
                if HANGUL_RE.search(str(label)) and " / " not in str(label):
                    raise AssertionError(f"{setting_id} Korean option label must be bilingual: {label!r}")

        entries_by_id = {str(entry.get("id")): entry for entry in entries}
        language = entries_by_id.get("ogd-style-settings-language")
        if not language:
            raise AssertionError("missing Owen Graphite language selector")
        if language.get("default") != "ogd-language-auto":
            raise AssertionError("language selector default must remain ogd-language-auto")
        if language.get("values") != ["ogd-language-auto", "ogd-language-ko", "ogd-language-en"]:
            raise AssertionError("language selector values must preserve auto/ko/en compatibility")

        for index, (entry, expected) in enumerate(zip(functional, contract_options), start=1):
            for key in ("id", "title", "type", "default"):
                actual_value = normalize(entry.get(key, ""))
                expected_value = normalize(expected.get(key, ""))
                if actual_value != expected_value:
                    raise AssertionError(
                        f"option #{index} {entry.get('id', '<missing>')} {key} {actual_value!r} != contract {expected_value!r}"
                    )

            if entry.get("type") == "class-select":
                values = [normalize(value) for value in entry.get("values", [])]
                default = normalize(entry.get("default", ""))
                if default not in values:
                    raise AssertionError(f"class-select {entry['id']} default {default!r} is not in options")
                if len(values) != len(set(values)):
                    raise AssertionError(f"class-select {entry['id']} has duplicate option values")

        localized_descriptions = sum(bool(entry.get("description")) for entry in entries)
        print(
            f"OK: Style Settings contract matches ({len(entries)} entries, {len(functional)} functional options, "
            f"{len(entries)} localized titles, {localized_descriptions} localized descriptions)"
        )
        return 0
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
