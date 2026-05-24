#!/usr/bin/env python3
"""Build a coverage priority plan from unused CSS coverage buckets."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "dev" / "WIKI" / "MAP" / "unused-css-candidates.json"
OUT_MD = ROOT / "dev" / "WIKI" / "MAP" / "coverage-priority-plan.md"

STATE_BUCKETS = {"state-interaction", "obsidian-chrome-runtime", "live-preview-runtime"}
PLUGIN_BUCKETS = {"plugin-runtime"}
PDF_BUCKETS = {"print-pdf-context"}
DOCUMENT_BUCKETS = {"document-content-fixture-gap"}

OWNER_BY_PREFIX = {
    "src/chrome/37-tabs-file-explorer-search.css": "src/chrome/37-tabs-file-explorer-search.css",
    "src/chrome/36-floating-ui-glass-system.css": "src/chrome/36-floating-ui-glass-system.css",
    "src/chrome/35-editing-menu-tooltip-glass.css": "src/chrome/35-editing-menu-tooltip-glass.css",
    "src/chrome/33-settings-controls.css": "src/chrome/33-settings-controls.css",
    "src/chrome/32-overlay-popover-dataview.css": "src/chrome/32-overlay-popover-dataview.css",
    "src/chrome/31-navigation-tasks-search.css": "src/chrome/31-navigation-tasks-search.css",
    "src/chrome/30-workspace.css": "src/chrome/30-workspace.css",
    "src/plugins/60-canvas-graph-link-panes.css": "src/plugins/60-canvas-graph-link-panes.css",
    "src/plugins/61-live-preview-mobile-plugin.css": "src/plugins/61-live-preview-mobile-plugin.css",
    "src/features/41-feature-presets.css": "src/features/41-feature-presets.css",
    "src/features/42-report-print-polish.css": "src/features/42-report-print-polish.css",
    "src/surfaces/23-liquid-glass-core.css": "src/surfaces/23-liquid-glass-core.css",
}


def bucket_counts(item: dict[str, Any]) -> dict[str, int]:
    return {str(row["bucket"]): int(row["count"]) for row in item.get("topBuckets", [])}


def score(item: dict[str, Any], buckets: set[str]) -> int:
    counts = bucket_counts(item)
    return sum(counts.get(bucket, 0) for bucket in buckets)


def slug_module(module: str) -> str:
    return module.replace("src/", "").replace(".css", "").replace("/", "-")


def evidence_command(module: str, surface: str, state: str = "hovered") -> str:
    owner = OWNER_BY_PREFIX.get(module, module)
    return (
        f".\\.venv\\Scripts\\python.exe dev\\scripts\\new_runtime_evidence.py "
        f"--surface {surface} --name {slug_module(module)} --state {state} --owner {owner}"
    )


def top_modules(payload: dict[str, Any], buckets: set[str], limit: int) -> list[dict[str, Any]]:
    rows = [item for item in payload.get("coverageGapSummary", []) if score(item, buckets) > 0]
    rows.sort(key=lambda item: (-score(item, buckets), -int(item.get("reserved", 0)), str(item.get("module", ""))))
    return rows[:limit]


def table_for(rows: list[dict[str, Any]], buckets: set[str], surface: str, state: str) -> list[str]:
    lines = ["| Module | Priority Count | Reserved | Matched | Evidence scaffold |", "| --- | ---: | ---: | ---: | --- |"]
    for item in rows:
        module = str(item["module"])
        lines.append(
            f"| `{module}` | {score(item, buckets)} | {item['reserved']} | {item['matched']} | "
            f"`{evidence_command(module, surface, state)}` |"
        )
    return lines


def build_markdown(payload: dict[str, Any]) -> str:
    state_rows = top_modules(payload, STATE_BUCKETS, 8)
    plugin_rows = top_modules(payload, PLUGIN_BUCKETS, 6)
    pdf_rows = top_modules(payload, PDF_BUCKETS, 5)
    document_rows = top_modules(payload, DOCUMENT_BUCKETS, 5)
    summary = payload.get("summary", {})
    bucket_summary = payload.get("reservedBucketSummary", {})

    lines = [
        "# Coverage Priority Plan",
        "",
        "Generated from `dev/WIKI/MAP/unused-css-candidates.json`.",
        "",
        "## Summary",
        "",
        f"- Matched selector parts: {summary.get('matched', 0)}",
        f"- Reserved no-match selector parts: {summary.get('reserved', 0)}",
        f"- State interaction backlog: {bucket_summary.get('state-interaction', 0)}",
        f"- Plugin runtime backlog: {bucket_summary.get('plugin-runtime', 0)}",
        f"- Print/PDF context backlog: {bucket_summary.get('print-pdf-context', 0)}",
        f"- Document fixture backlog: {bucket_summary.get('document-content-fixture-gap', 0)}",
        "",
        "## P0 State And Chrome Runtime",
        "",
        "Capture resting and active runtime states before changing or deleting these selectors.",
        "",
        *table_for(state_rows, STATE_BUCKETS, "chrome", "hovered"),
        "",
        "## P1 Plugin Runtime",
        "",
        "Prefer real plugin DOM. If unavailable, mark the capture as an approximation and keep the selector reserved.",
        "",
        *table_for(plugin_rows, PLUGIN_BUCKETS, "plugin", "rendered"),
        "",
        "## P2 Print And PDF Context",
        "",
        "Validate print media, report mode, header/footer state, and customer-delivery visibility before changing selector status.",
        "",
        *table_for(pdf_rows, PDF_BUCKETS, "pdf", "print"),
        "",
        "## P3 Document Content Fixtures",
        "",
        "Add natural Markdown fixtures before treating these selectors as removal candidates.",
        "",
        *table_for(document_rows, DOCUMENT_BUCKETS, "table", "rendered"),
        "",
        "## Required Checks",
        "",
        "```powershell",
        ".\\.venv\\Scripts\\python.exe dev\\scripts\\build_unused_css_report.py",
        ".\\.venv\\Scripts\\python.exe dev\\scripts\\build_coverage_priority_plan.py --check",
        ".\\.venv\\Scripts\\python.exe dev\\scripts\\audit_runtime_evidence_requirements.py --strict",
        ".\\.venv\\Scripts\\python.exe dev\\scripts\\audit_docs_assets.py",
        "```",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if the generated plan is stale.")
    args = parser.parse_args()

    try:
        payload = json.loads(INPUT.read_text(encoding="utf-8"))
        content = build_markdown(payload)
        if args.check:
            if not OUT_MD.is_file() or OUT_MD.read_text(encoding="utf-8") != content:
                raise AssertionError(f"{OUT_MD.relative_to(ROOT)} is stale; run dev/scripts/build_coverage_priority_plan.py")
            print("OK: coverage priority plan is fresh")
            return 0
        OUT_MD.write_text(content, encoding="utf-8")
        print(f"OK: wrote {OUT_MD.relative_to(ROOT)}")
        return 0
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())