#!/usr/bin/env python3
"""Fail on direct-owner and core-geometry violations in v3 CSS.

This guard exists to prevent the old pattern of adding late restore/final
override blocks after the real owner. High-risk selectors must either stay in
Obsidian core or live in their direct owner module.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"

COMMENT_RE = re.compile(r"/\*.*?\*/", re.DOTALL)
OWEN_RISK_MARKER = "owen-risk-accepted: cm-table-widget"

@dataclass(frozen=True)
class Rule:
    name: str
    pattern: re.Pattern[str]
    allowed_files: frozenset[str]
    message: str
    allow_if: tuple[str, ...] = ()


RULES = [
    Rule(
        name="cm-table-widget-core-geometry",
        pattern=re.compile(r"(?<!not\()\.(?:cm-table-widget)\b|\btable\.cm-table\b"),
        allowed_files=frozenset(),
        message=(
            "Markdown Live Preview table widgets are owned by Obsidian core. "
            "Do not style .cm-table-widget/table.cm-table in theme CSS; use "
            "rendered tables or HTML embed table selectors instead."
        ),
    ),
    Rule(
        name="generic-lp-table-selector",
        pattern=re.compile(r"\.markdown-source-view\.mod-cm6[^{}]*(?<![A-Za-z0-9_-])table[^{}]*"),
        allowed_files=frozenset(),
        allow_if=(":not(.cm-table-widget)", ":not(.cm-table)"),
        message=(
            "Generic Live Preview table selectors can hit Obsidian markdown table widgets. "
            "Scope them to HTML/embed tables with :not(.cm-table-widget) and :not(.cm-table)."
        ),
    ),
    Rule(
        name="pdf-header-owner",
        pattern=re.compile(r"\bbody\.ogd-pdf-header-enabled\b"),
        allowed_files=frozenset({"src/features/41-feature-presets.css"}),
        message="PDF header selectors are owned by src/features/41-feature-presets.css.",
    ),
    Rule(
        name="pdf-footer-owner",
        pattern=re.compile(r"\bbody\.ogd-pdf-footer-enabled\b"),
        allowed_files=frozenset({"src/features/41-feature-presets.css"}),
        message="PDF footer selectors are owned by src/features/41-feature-presets.css.",
    ),
]


def strip_comments(text: str) -> str:
    return COMMENT_RE.sub(lambda match: "".join("\n" if char == "\n" else " " for char in match.group(0)), text)


def line_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def css_files() -> list[Path]:
    return sorted(SRC.rglob("*.css"))


def has_owen_risk_marker(text: str, offset: int) -> bool:
    prefix = text[max(0, offset - 8000):offset]
    return OWEN_RISK_MARKER in prefix


def main() -> int:
    violations: list[str] = []
    for path in css_files():
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        searchable = strip_comments(text)
        for rule in RULES:
            if rel in rule.allowed_files:
                continue
            for match in rule.pattern.finditer(searchable):
                snippet = searchable[match.start():match.end()]
                if rule.name in {"cm-table-widget-core-geometry", "generic-lp-table-selector"} and has_owen_risk_marker(text, match.start()):
                    continue
                if rule.allow_if and all(token in snippet for token in rule.allow_if):
                    continue
                # Negative lookbehind cannot express :not(.cm-table) for table.cm-table.
                prefix = searchable[max(0, match.start() - 8):match.start()]
                if prefix.endswith(":not("):
                    continue
                line = line_for_offset(searchable, match.start())
                violations.append(f"{rel}:{line}: {rule.name}: {snippet} — {rule.message}")

    if violations:
        print("FAIL: direct-owner/core-geometry guard violations:")
        for item in violations:
            print(f"  - {item}")
        return 1

    print("OK: direct-owner/core-geometry guard clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
