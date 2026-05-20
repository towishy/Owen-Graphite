#!/usr/bin/env python3
"""Audit Live Preview / Reading / PDF selector ownership in src CSS.

The audit follows src/entry.css import order, classifies each source rule into
surface buckets, and blocks unapproved vertical box changes on direct
`.cm-line.HyperMD-*` selectors. Current exceptions are limited to existing
frontmatter box and quote rhythm rules.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from audit_v3_hit_routing import _has_nonzero_vertical_box
from build_src_map import CssRule, declarations, import_order, tokenize_blocks


ROOT = Path(__file__).resolve().parents[2]
SURFACE_ORDER = ("lp-source", "lp-widget", "reading", "pdf-print", "shared-token")
TRACKED_TOKEN_PREFIXES = (
    "--ogd-code-",
    "--ogd-codeblock-",
    "--ogd-table-",
    "--ogd-pdf-",
    "--ogd-img-",
    "--ogd-figure-",
)
LP_WIDGET_TOKENS = (
    ".cm-preview-code-block",
    ".cm-hmd-codeblock",
    ".cm-callout",
    ".cm-table-widget",
    "table.cm-table",
    ".cm-html-embed",
    ".cm-embed-block",
)
READING_TOKENS = (
    ".markdown-rendered",
    ".markdown-preview-view",
    ".markdown-reading-view",
)
LP_SOURCE_TOKENS = (
    ".markdown-source-view.mod-cm6",
    ".HyperMD-",
    ".cm-line",
    ".cm-content",
    ".cm-active",
)
PDF_PRINT_TOKENS = (
    "ogd-pdf",
    "ogd-print",
    "pdf-",
    "print-",
    "@page",
)
VERTICAL_BOX_PROPERTIES = (
    "margin",
    "margin-top",
    "margin-bottom",
    "margin-block",
    "margin-block-start",
    "margin-block-end",
    "padding",
    "padding-top",
    "padding-bottom",
    "padding-block",
    "padding-block-start",
    "padding-block-end",
)
APPROVED_HYPERMD_VERTICAL_BOX = (
    ".cm-line.HyperMD-frontmatter-1",
    ".cm-line.HyperMD-frontmatter-end",
    ".cm-line.HyperMD-quote",
)
HYPERMD_DIRECT_RE = re.compile(r"\.cm-line(?:\.[\w-]+)*\.HyperMD-[\w-]+")


@dataclass(frozen=True)
class RuleRecord:
    import_index: int
    module: str
    line: int
    selector: str
    at_context: str
    surfaces: tuple[str, ...]
    token_refs: tuple[str, ...]


def normalize_token_refs(rule: CssRule) -> tuple[str, ...]:
    refs: set[str] = set()
    for property_name, value in declarations(rule.body):
        if property_name.startswith(TRACKED_TOKEN_PREFIXES):
            refs.add(property_name)
        for token in re.findall(r"var\((--ogd-[\w-]+)", value):
            if token.startswith(TRACKED_TOKEN_PREFIXES):
                refs.add(token)
    for token in re.findall(r"var\((--ogd-[\w-]+)", rule.selector):
        if token.startswith(TRACKED_TOKEN_PREFIXES):
            refs.add(token)
    return tuple(sorted(refs))


def classify_surfaces(module: str, rule: CssRule, token_refs: tuple[str, ...]) -> tuple[str, ...]:
    selector = rule.selector
    body = rule.body
    context = rule.at_context.lower()
    combined = f"{selector} {body}".lower()
    surfaces: set[str] = set()

    if ".markdown-source-view.mod-cm6" in selector and any(token in selector for token in LP_SOURCE_TOKENS[1:]):
        surfaces.add("lp-source")
    elif ".markdown-source-view.mod-cm6" in selector and ".cm-" in selector:
        surfaces.add("lp-source")

    if any(token in selector for token in LP_WIDGET_TOKENS):
        surfaces.add("lp-widget")
    if any(token in selector for token in READING_TOKENS):
        surfaces.add("reading")
    if "@media print" in context or any(token in combined for token in PDF_PRINT_TOKENS):
        surfaces.add("pdf-print")
    if module.startswith("src/tokens/") or token_refs:
        surfaces.add("shared-token")

    return tuple(surface for surface in SURFACE_ORDER if surface in surfaces)


def is_approved_hypermd_vertical_box(selector: str) -> bool:
    return any(token in selector for token in APPROVED_HYPERMD_VERTICAL_BOX)


def audit_hypermd_vertical_box(records: list[RuleRecord], rules_by_location: dict[tuple[str, int, str], CssRule]) -> list[str]:
    failures: list[str] = []
    for record in records:
        if "lp-source" not in record.surfaces:
            continue
        if not HYPERMD_DIRECT_RE.search(record.selector):
            continue
        if is_approved_hypermd_vertical_box(record.selector):
            continue
        rule = rules_by_location[(record.module, record.line, record.selector)]
        offender = _has_nonzero_vertical_box(rule.body, VERTICAL_BOX_PROPERTIES)
        if offender:
            failures.append(
                f"{record.module}:{record.line} direct HyperMD cm-line declares vertical box `{offender}` in `{record.selector}`"
            )
    return failures


def collect_records() -> tuple[list[RuleRecord], dict[tuple[str, int, str], CssRule]]:
    records: list[RuleRecord] = []
    rules_by_location: dict[tuple[str, int, str], CssRule] = {}
    for module_info in import_order():
        module = str(module_info["module"])
        module_path = ROOT / module
        css = module_path.read_text(encoding="utf-8")
        for rule in tokenize_blocks(css):
            token_refs = normalize_token_refs(rule)
            surfaces = classify_surfaces(module, rule, token_refs)
            if not surfaces:
                continue
            record = RuleRecord(
                import_index=int(module_info["import_index"]),
                module=module,
                line=rule.line,
                selector=rule.selector,
                at_context=rule.at_context,
                surfaces=surfaces,
                token_refs=token_refs,
            )
            records.append(record)
            rules_by_location[(module, rule.line, rule.selector)] = rule
    return records, rules_by_location


def grouped_records(records: list[RuleRecord]) -> dict[str, list[dict[str, object]]]:
    grouped: dict[str, list[dict[str, object]]] = {surface: [] for surface in SURFACE_ORDER}
    for record in records:
        item = {
            "importIndex": record.import_index,
            "module": record.module,
            "line": record.line,
            "selector": record.selector,
            "atContext": record.at_context,
            "surfaces": list(record.surfaces),
            "tokenRefs": list(record.token_refs),
        }
        for surface in record.surfaces:
            grouped[surface].append(item)
    return grouped


def print_summary(records: list[RuleRecord]) -> None:
    grouped = grouped_records(records)
    print("Selector ownership surface counts:")
    for surface in SURFACE_ORDER:
        modules = {str(item["module"]) for item in grouped[surface]}
        print(f"  - {surface}: {len(grouped[surface])} selectors across {len(modules)} modules")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json-output", type=Path, help="Optional path for grouped selector ownership JSON.")
    args = parser.parse_args()

    try:
        records, rules_by_location = collect_records()
        failures = audit_hypermd_vertical_box(records, rules_by_location)
        if args.json_output:
            payload = {
                "surfaces": grouped_records(records),
                "surfaceOrder": list(SURFACE_ORDER),
                "trackedTokenPrefixes": list(TRACKED_TOKEN_PREFIXES),
                "approvedHypermdVerticalBox": list(APPROVED_HYPERMD_VERTICAL_BOX),
            }
            output_path = args.json_output if args.json_output.is_absolute() else ROOT / args.json_output
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(f"Wrote {output_path.relative_to(ROOT)}")

        if failures:
            print("FAIL: LP/PDF selector ownership violations:", file=sys.stderr)
            for failure in failures:
                print(f"  - {failure}", file=sys.stderr)
            return 1

        print_summary(records)
        print("OK: LP/PDF selector ownership audit clean")
        return 0
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
