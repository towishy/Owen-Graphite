#!/usr/bin/env python3
"""Fail on direct-owner and core-geometry violations in v3 CSS.

This guard exists to prevent the old pattern of adding late restore/final
override blocks after the real owner. High-risk selectors must either stay in
Obsidian core or live in their direct owner module.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from css_scan import iter_comments, iter_rule_blocks, line_for_offset, strip_comments


ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
RISK_REGISTRY = ROOT / "dev" / "WIKI" / "risk-accepted-registry.json"

OWEN_RISK_BEGIN = "owen-risk-accepted-begin: cm-table-widget"
OWEN_RISK_END = "owen-risk-accepted-end: cm-table-widget"

@dataclass(frozen=True)
class Rule:
    name: str
    pattern: re.Pattern[str]
    allowed_files: frozenset[str]
    message: str
    allow_if: tuple[str, ...] = ()


@dataclass(frozen=True)
class RiskRange:
    start: int
    end: int
    risk_id: str
    evidence: str


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



def css_files() -> list[Path]:
    return sorted(SRC.rglob("*.css"))


def load_risk_registry() -> dict[str, dict[str, object]]:
    if not RISK_REGISTRY.is_file():
        return {}
    payload = json.loads(RISK_REGISTRY.read_text(encoding="utf-8"))
    if payload.get("schema") != "owen-graphite/risk-accepted-registry/1":
        raise AssertionError(f"unexpected risk registry schema: {payload.get('schema')!r}")
    return {str(entry["id"]): dict(entry) for entry in payload.get("entries", [])}


def marker_value(text: str, key: str) -> str:
    match = re.search(rf"(?:^|;|\s){re.escape(key)}=([^;*\s]+)", text)
    return match.group(1).strip() if match else ""


def owen_risk_ranges(text: str, rel: str, registry: dict[str, dict[str, object]]) -> tuple[list[RiskRange], list[str]]:
    ranges: list[RiskRange] = []
    problems: list[str] = []
    comments = list(iter_comments(text))
    for index, comment in enumerate(comments):
        body = comment.group(0)
        if OWEN_RISK_BEGIN not in body:
            continue
        risk_id = marker_value(body, "id")
        evidence = marker_value(body, "evidence")
        if not risk_id:
            problems.append("owen risk marker missing id=...")
        if not evidence:
            problems.append("owen risk marker missing evidence=...")
        end = next((item for item in comments[index + 1:] if OWEN_RISK_END in item.group(0)), None)
        if end is None:
            problems.append("owen risk marker missing matching end marker")
            continue
        entry = registry.get(risk_id)
        if risk_id and not entry:
            problems.append(f"owen risk marker id not found in registry: {risk_id}")
        elif entry:
            if entry.get("module") != rel:
                problems.append(f"risk registry module mismatch for {risk_id}: {entry.get('module')} != {rel}")
            if evidence and evidence not in {str(item) for item in entry.get("evidence", [])}:
                problems.append(f"risk marker evidence not listed in registry for {risk_id}: {evidence}")
        ranges.append(RiskRange(comment.end(), end.start(), risk_id, evidence))
    return ranges, problems


def has_owen_risk_marker(text: str, offset: int, ranges: list[RiskRange]) -> bool:
    return any(item.start <= offset <= item.end for item in ranges)


def assert_risk_range_rules(text: str, rel: str, ranges: list[RiskRange], registry: dict[str, dict[str, object]], violations: list[str]) -> None:
    searchable = strip_comments(text)
    for risk_range in ranges:
        entry = registry.get(risk_range.risk_id)
        if not entry:
            continue
        allowed_properties = {str(item) for item in entry.get("allowedProperties", [])}
        selector_needles = [str(item) for item in entry.get("selectorContains", [])]
        for block in iter_rule_blocks(searchable, risk_range.start, risk_range.end):
            selectors = block.normalized_selectors
            if selector_needles and not any(needle in selectors for needle in selector_needles):
                line = line_for_offset(searchable, block.start)
                violations.append(f"{rel}:{line}: owen-risk-selector: {selectors} — selector is not listed in risk registry entry {risk_range.risk_id}")
            for prop, _value in block.declarations():
                if allowed_properties and prop not in allowed_properties:
                    line = line_for_offset(searchable, block.start)
                    violations.append(f"{rel}:{line}: owen-risk-property: {prop} — property is not listed in risk registry entry {risk_range.risk_id}")


def assert_no_callout_left_rails(text: str, rel: str, violations: list[str]) -> None:
    searchable = strip_comments(text)
    for block in iter_rule_blocks(searchable):
        selectors = block.normalized_selectors
        if ".callout" not in selectors:
            continue
        for prop, value in block.declarations():
            if "border-left" not in prop:
                continue
            value = value.strip().lower()
            if prop == "border-left-width" and value in {"0", "0px", "1px"}:
                continue
            if value in {"0", "0px", "transparent", "var(--ogd-surface-transparent, transparent)"}:
                continue
            line = line_for_offset(searchable, block.start)
            violations.append(f"{rel}:{line}: callout-left-rail: {selectors} — callout rules must not add left-only accent rails; use full border, icon, or surface state instead.")


def main() -> int:
    violations: list[str] = []
    registry = load_risk_registry()
    for path in css_files():
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        searchable = strip_comments(text)
        risk_ranges, risk_problems = owen_risk_ranges(text, rel, registry)
        for problem in risk_problems:
            violations.append(f"{rel}: {problem}")
        assert_risk_range_rules(text, rel, risk_ranges, registry, violations)
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
