#!/usr/bin/env python3
"""Audit selector owner cheatsheet references against owner registry files."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CHEATSHEET = ROOT / "dev" / "WIKI" / "SELECTOR-OWNER-CHEATSHEET.md"
REGISTRY = ROOT / "dev" / "WIKI" / "MAP" / "owner-registry.json"

REQUIRED_TERMS = [
    ".cm-table-widget",
    "table.cm-table",
    ".markdown-rendered table",
    "dataview",
    "mermaid",
    "ogd-pdf-header-*",
    ".workspace-tab-header",
]


def fail(message: str) -> None:
    raise AssertionError(message)


def markdown_code_paths(text: str) -> set[str]:
    return {match.group(1) for match in re.finditer(r"`((?:src|dev/WIKI)/[^`]+?)`", text)}


def main() -> int:
    try:
        text = CHEATSHEET.read_text(encoding="utf-8")
        registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
        low = text.lower()
        missing_terms = [term for term in REQUIRED_TERMS if term.lower() not in low]
        if missing_terms:
            fail("selector cheatsheet missing required terms: " + ", ".join(missing_terms))

        missing_paths: list[str] = []
        for path in markdown_code_paths(text):
            if "*" in path or path.endswith("/*"):
                continue
            if not (ROOT / path).exists():
                missing_paths.append(path)
        if missing_paths:
            fail("selector cheatsheet references missing files: " + ", ".join(sorted(missing_paths)))

        registry_modules = {
            module
            for surface in registry["surfaces"]
            for key in ("ownerModules", "allowedLateModules")
            for module in surface.get(key, [])
            if module.startswith("src/")
        }
        important_modules = {
            "src/base/13-live-preview.css",
            "src/surfaces/20-reading-tables-code.css",
            "src/chrome/32-overlay-popover-dataview.css",
            "src/plugins/61-live-preview-mobile-plugin.css",
            "src/features/41-feature-presets.css",
        }
        missing_modules = sorted(module for module in important_modules if module in registry_modules and module not in text)
        if missing_modules:
            fail("selector cheatsheet missing important registered owners: " + ", ".join(missing_modules))

        print("OK: selector owner cheatsheet audit clean")
        return 0
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())