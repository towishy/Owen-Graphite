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
OWEN_RISK_BEGIN = "owen-risk-accepted-begin: cm-table-widget"
OWEN_RISK_END = "owen-risk-accepted-end: cm-table-widget"
BLOCK_RE = re.compile(r"(?P<selectors>[^{}]+)\{(?P<body>[^{}]*)\}", re.DOTALL)

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


def owen_risk_ranges(text: str) -> tuple[list[tuple[int, int]], list[str]]:
    ranges: list[tuple[int, int]] = []
    problems: list[str] = []
    comments = list(COMMENT_RE.finditer(text))
    for index, comment in enumerate(comments):
        body = comment.group(0)
        if OWEN_RISK_BEGIN not in body:
            continue
        if "evidence=" not in body:
            problems.append("owen risk marker missing evidence=...")
        end = next((item for item in comments[index + 1:] if OWEN_RISK_END in item.group(0)), None)
        if end is None:
            problems.append("owen risk marker missing matching end marker")
            continue
        ranges.append((comment.end(), end.start()))
    return ranges, problems


def has_owen_risk_marker(text: str, offset: int, ranges: list[tuple[int, int]]) -> bool:
    if any(start <= offset <= end for start, end in ranges):
        return True
    prefix = text[max(0, offset - 320):offset]
    return OWEN_RISK_MARKER in prefix and "evidence=" in prefix


def assert_no_callout_left_rails(text: str, rel: str, violations: list[str]) -> None:
    searchable = strip_comments(text)
    for block in BLOCK_RE.finditer(searchable):
        selectors = " ".join(block.group("selectors").split())
        if ".callout" not in selectors:
            continue
        body = block.group("body")
        for declaration in body.split(";"):
            if "border-left" not in declaration:
                continue
            prop, _, value = declaration.partition(":")
            prop = prop.strip()
            value = value.strip().lower()
            if prop == "border-left-width" and value in {"0", "0px", "1px"}:
                continue
            if value in {"0", "0px", "transparent", "var(--ogd-surface-transparent, transparent)"}:
                continue
            line = line_for_offset(searchable, block.start())
            violations.append(f"{rel}:{line}: callout-left-rail: {selectors} — callout rules must not add left-only accent rails; use full border, icon, or surface state instead.")


def main() -> int:
    violations: list[str] = []
    for path in css_files():
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        searchable = strip_comments(text)
        risk_ranges, risk_problems = owen_risk_ranges(text)
        for problem in risk_problems:
            violations.append(f"{rel}: {problem}")
        assert_no_callout_left_rails(text, rel, violations)
        for rule in RULES:
            if rel in rule.allowed_files:
                continue
            for match in rule.pattern.finditer(searchable):
                snippet = searchable[match.start():match.end()]
                if rule.name in {"cm-table-widget-core-geometry", "generic-lp-table-selector"} and has_owen_risk_marker(text, match.start(), risk_ranges):
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
