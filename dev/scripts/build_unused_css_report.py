#!/usr/bin/env python3
"""Build a conservative unused CSS candidate report.

This script measures selector coverage across the existing effective snapshot
fixtures and Style Settings body-class scenarios. It reports candidates only;
it does not delete CSS. Selectors tied to document semantics, Obsidian chrome,
plugins, style settings, tokens, responsive states, or dynamic pseudo-classes
are reserved for manual review even when they do not match the current fixture
matrix.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT / "src"
BUNDLE = ROOT / "dist" / "theme-v3.css"
MANIFEST = ROOT / "manifest.json"
DEFAULT_FIXTURE = ROOT / "dev" / "WIKI" / "DOCS" / "v3" / "research" / "golden-rig" / "obsidian-harness.html"
PRINT_FIXTURES = [
    ROOT / "dev" / "WIKI" / "DOCS" / "v3" / "research" / "table-callout-parity-fixture.html",
    ROOT / "dev" / "WIKI" / "DOCS" / "v3" / "research" / "pdf-marginalia-fixture.html",
    ROOT / "dev" / "WIKI" / "DOCS" / "v3" / "research" / "pdf-image-body-quality-fixture.html",
    ROOT / "dev" / "WIKI" / "DOCS" / "v3" / "research" / "live-preview-pdf-parity-fixture.html",
    ROOT / "dev" / "WIKI" / "DOCS" / "v3" / "research" / "code-font-clarity-fixture.html",
]
COVERAGE_FIXTURES = [
    ROOT / "dev" / "WIKI" / "DOCS" / "v3" / "research" / "coverage-priority-fixture.html",
]
MATRIX_TEMPLATE = ROOT / "dev" / "WIKI" / "effective-baseline" / "v{version}" / "style-settings-matrix.json"
OUT_JSON = ROOT / "dev" / "WIKI" / "MAP" / "unused-css-candidates.json"
OUT_MD = ROOT / "dev" / "WIKI" / "MAP" / "unused-css-candidates.md"

STATE_PSEUDOS = re.compile(
    r":(?:hover|active|focus|focus-visible|focus-within|target|visited|link|checked|disabled|enabled|placeholder-shown|modal|open)\b"
)
PSEUDO_ELEMENT_RE = re.compile(r"::[a-zA-Z0-9_-]+(?:\([^()]*\))?")
LEGACY_PSEUDO_ELEMENT_RE = re.compile(r":(?:before|after|first-line|first-letter)\b")
RISK_TEXT_RE = re.compile(
    r"(?:^|[.\[#\s:-])(is-|mod-|workspace|workspace-|setting-|nav-|menu|suggestion|popover|tooltip|modal|prompt|search|canvas|dataview|tasks|style-settings|cm-|HyperMD|ogd-|pdf-|print-|mobile|ribbon|status-bar|side-dock|theme-|markdown-|language-|token|line-|copy-code-button|table|callout|blockquote|heading|metadata|graph|kanban|calendar|bases|excalidraw|mermaid|toc|outline|tag)",
    re.I,
)
CONTENT_ELEMENT_RE = re.compile(
    r"(?:^|[\s>+~:(,])(?:body|main|article|section|figure|figcaption|p|ul|ol|li|h[1-6]|pre|code|kbd|mark|img|svg|table|thead|tbody|tr|th|td|blockquote)(?:$|[\s>+~).#[:,])",
    re.I,
)
RESERVED_CONTEXT_RE = re.compile(r"@(?:media|supports).*(?:forced-colors|prefers-|print|hover|pointer|color-gamut)", re.I)
RESERVED_MODULE_RE = re.compile(r"^src/(?:chrome|plugins|themes/51-|features/40-style-settings|tokens)/")
PLUGIN_RUNTIME_RE = re.compile(
    r"(?:canvas|dataview|tasks|kanban|calendar|bases|excalidraw|mermaid|graph|metadata|pickr|editingToolbar|cMenu|community)",
    re.I,
)
CHROME_RUNTIME_RE = re.compile(
    r"(?:workspace|nav-|tree-item|menu|suggestion|popover|tooltip|modal|prompt|search|ribbon|status-bar|side-dock|view-header|tab-header|empty-state)",
    re.I,
)
LIVE_PREVIEW_RE = re.compile(r"(?:markdown-source-view|cm-|HyperMD|CodeMirror|cm6)", re.I)
STYLE_SETTING_BODY_RE = re.compile(r"(?:^|\s)body(?:\.[\w-]+)*\.ogd-", re.I)
PRINT_PDF_RE = re.compile(r"(?:pdf|print|ogd-pdf|@media\s+print)", re.I)

BUCKET_LABELS = {
    "state-interaction": "State pseudo selectors (:hover/:focus/etc.) that static DOM coverage cannot fully prove.",
    "print-pdf-context": "Print/PDF and PDF Style Settings selectors reserved for print-specific validation.",
    "style-setting-class": "Body-class Style Settings variants that are valid only under selected settings.",
    "plugin-runtime": "Plugin/runtime DOM such as Canvas, Dataview, Mermaid, Graph, Bases, Pickr, or Editing Toolbar.",
    "obsidian-chrome-runtime": "Obsidian app chrome/runtime DOM such as workspace, nav, search, modal, menu, tooltip, or status surfaces.",
    "live-preview-runtime": "CodeMirror/Live Preview runtime DOM and editor-generated classes.",
    "document-content-fixture-gap": "Document/content semantics that need more purpose-built fixture DOM before removal review.",
    "token-variable": "Token or custom-property selectors that are not removal candidates.",
    "at-context-runtime": "Media/supports context selectors reserved for context-specific validation.",
    "reserved-static-other": "Reserved static no-match selectors that need manual review.",
}
BUCKET_RECIPES = {
    "state-interaction": "dev/WIKI/RECIPES/coverage-state-interaction.md",
    "plugin-runtime": "dev/WIKI/RECIPES/coverage-plugin-runtime.md",
    "print-pdf-context": "dev/WIKI/RECIPES/coverage-print-pdf-context.md",
    "document-content-fixture-gap": "dev/WIKI/RECIPES/coverage-document-content-fixture.md",
    "obsidian-chrome-runtime": "dev/WIKI/RECIPES/coverage-state-interaction.md",
    "live-preview-runtime": "dev/WIKI/RECIPES/live-preview-spacing.md",
}
BUCKET_DECISIONS = {
    "state-interaction": {
        "decision": "do-not-remove",
        "nextAction": "Validate through interactive state coverage or keep reserved.",
    },
    "print-pdf-context": {
        "decision": "do-not-remove",
        "nextAction": "Validate through PDF/print scenario coverage before any removal review.",
    },
    "style-setting-class": {
        "decision": "do-not-remove",
        "nextAction": "Keep reserved unless the Style Settings contract removes the class.",
    },
    "plugin-runtime": {
        "decision": "runtime-reserved",
        "nextAction": "Validate in Obsidian/plugin runtime or keep reserved.",
    },
    "obsidian-chrome-runtime": {
        "decision": "runtime-reserved",
        "nextAction": "Validate in Obsidian app chrome runtime or keep reserved.",
    },
    "live-preview-runtime": {
        "decision": "runtime-reserved",
        "nextAction": "Validate with CodeMirror/Live Preview runtime DOM or keep reserved.",
    },
    "document-content-fixture-gap": {
        "decision": "needs-purpose-built-fixture",
        "nextAction": "Add natural document fixture coverage when real document evidence exists; otherwise keep as coverage backlog.",
    },
    "token-variable": {
        "decision": "do-not-remove",
        "nextAction": "Keep token/custom-property selectors reserved.",
    },
    "at-context-runtime": {
        "decision": "context-reserved",
        "nextAction": "Validate in the matching media/supports context.",
    },
    "reserved-static-other": {
        "decision": "manual-review",
        "nextAction": "Inspect owner module and add targeted coverage before removal review.",
    },
}
INVALID_QUERY_LABELS = {
    "browser-query-error": "The browser rejected the generated query selector.",
    "pseudo-element-only-not-dom-queryable": "The selector targets a pseudo-element only, so it has no DOM element to count with querySelectorAll().",
    "at-rule-not-dom-queryable": "The selector part is an at-rule/context marker, not a DOM selector.",
    "empty-after-pseudo-stripping": "Pseudo-element stripping left no DOM selector to query.",
    "not-queryable-after-pseudo-stripping": "The selector could not be converted into a DOM query selector.",
}
COVERAGE_BACKLOG_POLICY = {
    "document-content-fixture-gap": "Keep as coverage backlog unless a natural Obsidian document fixture can represent the selector without synthetic DOM overreach.",
    "invalid-query": "Do not use invalid-query rows as deletion evidence; pseudo-element-only selectors and browser query limitations require manual or visual/context validation.",
}


def version() -> str:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))["version"]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_tokenizer():
    path = ROOT / "dev" / "scripts" / "v3_audit_duplicate_selectors.py"
    spec = importlib.util.spec_from_file_location("v3_audit_duplicate_selectors", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("unable to load v3_audit_duplicate_selectors.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.tokenize_blocks


def split_selector_list(selector: str) -> list[str]:
    parts: list[str] = []
    start = 0
    depth = 0
    quote: str | None = None
    for index, char in enumerate(selector):
        if quote:
            if char == quote and selector[index - 1:index] != "\\":
                quote = None
            continue
        if char in {'"', "'"}:
            quote = char
            continue
        if char in "([":
            depth += 1
            continue
        if char in ")]" and depth > 0:
            depth -= 1
            continue
        if char == "," and depth == 0:
            part = selector[start:index].strip()
            if part:
                parts.append(part)
            start = index + 1
    tail = selector[start:].strip()
    if tail:
        parts.append(tail)
    return parts


def to_query_selector(selector_part: str) -> str | None:
    query = PSEUDO_ELEMENT_RE.sub("", selector_part)
    query = LEGACY_PSEUDO_ELEMENT_RE.sub("", query)
    query = re.sub(r"\s+", " ", query).strip()
    if not query or query.startswith("@"):
        return None
    return query


def invalid_query_reason(row: dict[str, Any], invalid_queries: set[str]) -> str:
    query = row["querySelector"]
    if query in invalid_queries:
        return "browser-query-error"
    selector_part = str(row["selectorPart"]).strip()
    if selector_part.startswith("@"):
        return "at-rule-not-dom-queryable"
    if PSEUDO_ELEMENT_RE.fullmatch(selector_part) or LEGACY_PSEUDO_ELEMENT_RE.fullmatch(selector_part):
        return "pseudo-element-only-not-dom-queryable"
    if to_query_selector(selector_part) is None:
        return "empty-after-pseudo-stripping"
    return "not-queryable-after-pseudo-stripping"


def parse_rules() -> list[dict[str, Any]]:
    tokenize_blocks = load_tokenizer()
    rules: list[dict[str, Any]] = []
    for css_path in sorted(SRC_DIR.rglob("*.css")):
        rel = css_path.relative_to(ROOT).as_posix()
        css = css_path.read_text(encoding="utf-8")
        for selector, body, context, line in tokenize_blocks(css):
            if not selector or not body or "@keyframes" in context:
                continue
            for selector_part in split_selector_list(selector):
                rules.append(
                    {
                        "module": rel,
                        "line": line,
                        "selector": selector,
                        "selectorPart": selector_part,
                        "querySelector": to_query_selector(selector_part),
                        "atContext": context,
                    }
                )
    return rules


def load_style_scenarios(limit: int | None) -> list[dict[str, Any]]:
    path = Path(str(MATRIX_TEMPLATE).format(version=version()))
    if not path.is_file():
        return []
    payload = json.loads(path.read_text(encoding="utf-8"))
    seen: set[tuple[str, str, tuple[str, ...]]] = set()
    scenarios: list[dict[str, Any]] = []
    for item in payload.get("scenarios", []):
        body_classes = tuple(sorted(str(value) for value in item.get("bodyClasses", [])))
        if not body_classes:
            continue
        key = (str(item.get("theme", "light")), str(item.get("media", "screen")), body_classes)
        if key in seen:
            continue
        seen.add(key)
        scenarios.append(
            {
                "id": str(item.get("id", f"style-{len(scenarios) + 1}")),
                "fixture": DEFAULT_FIXTURE,
                "theme": key[0],
                "media": key[1],
                "bodyClasses": list(body_classes),
                "viewport": {"width": 1440, "height": 1400},
            }
        )
        if limit is not None and len(scenarios) >= limit:
            break
    return scenarios


def build_scenarios(style_limit: int | None) -> list[dict[str, Any]]:
    scenarios: list[dict[str, Any]] = [
        {"id": "harness-light-screen", "fixture": DEFAULT_FIXTURE, "theme": "light", "media": "screen", "bodyClasses": [], "viewport": {"width": 1440, "height": 1400}},
        {"id": "harness-dark-screen", "fixture": DEFAULT_FIXTURE, "theme": "dark", "media": "screen", "bodyClasses": [], "viewport": {"width": 1440, "height": 1400}},
        {"id": "harness-light-mobile", "fixture": DEFAULT_FIXTURE, "theme": "light", "media": "screen", "bodyClasses": ["is-mobile"], "viewport": {"width": 390, "height": 844}},
        {"id": "harness-light-print", "fixture": DEFAULT_FIXTURE, "theme": "light", "media": "print", "bodyClasses": [], "viewport": {"width": 1440, "height": 1400}},
    ]
    scenarios.extend(
        [
            {
                "id": "harness-light-pdf-compound",
                "fixture": DEFAULT_FIXTURE,
                "theme": "light",
                "media": "print",
                "bodyClasses": [
                    "ogd-pdf-preset-status-end",
                    "ogd-pdf-label-single",
                    "ogd-pdf-label-filled",
                    "ogd-pdf-segment-graphite",
                    "ogd-pdf-segment-key-graphite",
                    "ogd-pdf-font-comfortable",
                    "ogd-pdf-visibility",
                ],
                "viewport": {"width": 1440, "height": 1400},
            },
            {
                "id": "harness-dark-pdf-compound",
                "fixture": DEFAULT_FIXTURE,
                "theme": "dark",
                "media": "print",
                "bodyClasses": [
                    "ogd-pdf-label-filled",
                    "ogd-pdf-font-large",
                    "ogd-pdf-visibility",
                    "ogd-zebra-disabled-permanently",
                ],
                "viewport": {"width": 1440, "height": 1400},
            },
            {
                "id": "harness-light-heading-number-off",
                "fixture": DEFAULT_FIXTURE,
                "theme": "light",
                "media": "screen",
                "bodyClasses": ["ogd-no-h1-number"],
                "viewport": {"width": 1440, "height": 1400},
            },
            {
                "id": "harness-dark-chrome-compound",
                "fixture": DEFAULT_FIXTURE,
                "theme": "dark",
                "media": "screen",
                "bodyClasses": ["ogd-eye-care", "ogd-glass-reduced"],
                "viewport": {"width": 1440, "height": 1400},
            },
        ]
    )
    for body_class in [
        "ogd-pdf-segment-sky",
        "ogd-pdf-segment-mint",
        "ogd-pdf-segment-violet",
        "ogd-pdf-segment-teal",
        "ogd-pdf-segment-key-slate",
        "ogd-pdf-segment-key-sky",
        "ogd-pdf-segment-key-teal",
        "ogd-pdf-segment-key-mint",
        "ogd-pdf-segment-key-violet",
        "ogd-pdf-segment-key-rose",
        "ogd-pdf-segment-key-amber",
        "ogd-pdf-segment-value-graphite",
        "ogd-pdf-segment-value-slate",
        "ogd-pdf-segment-value-sky",
        "ogd-pdf-segment-value-teal",
        "ogd-pdf-segment-value-mint",
        "ogd-pdf-segment-value-violet",
        "ogd-pdf-segment-value-rose",
        "ogd-pdf-segment-value-amber",
        "ogd-report-mode",
    ]:
        scenarios.append(
            {
                "id": f"harness-light-{body_class}",
                "fixture": DEFAULT_FIXTURE,
                "theme": "light",
                "media": "screen",
                "bodyClasses": [body_class],
                "viewport": {"width": 1440, "height": 1400},
            }
        )
    scenarios.append(
        {
            "id": "harness-dark-report-mode",
            "fixture": DEFAULT_FIXTURE,
            "theme": "dark",
            "media": "screen",
            "bodyClasses": ["ogd-report-mode"],
            "viewport": {"width": 1440, "height": 1400},
        }
    )
    for body_class in ["ogd-glass-subtle", "ogd-glass-strong"]:
        scenarios.append(
            {
                "id": f"harness-dark-{body_class}",
                "fixture": DEFAULT_FIXTURE,
                "theme": "dark",
                "media": "screen",
                "bodyClasses": [body_class],
                "viewport": {"width": 1440, "height": 1400},
            }
        )
    for fixture in PRINT_FIXTURES:
        if fixture.is_file():
            scenarios.append({"id": f"{fixture.stem}-print-light", "fixture": fixture, "theme": "light", "media": "print", "bodyClasses": [], "viewport": {"width": 1440, "height": 1400}})
    for fixture in COVERAGE_FIXTURES:
        if fixture.is_file():
            scenarios.extend(
                [
                    {"id": f"{fixture.stem}-screen-light", "fixture": fixture, "theme": "light", "media": "screen", "bodyClasses": [], "viewport": {"width": 1440, "height": 1400}},
                    {"id": f"{fixture.stem}-screen-dark", "fixture": fixture, "theme": "dark", "media": "screen", "bodyClasses": ["ogd-glass-subtle"], "viewport": {"width": 1440, "height": 1400}},
                    {"id": f"{fixture.stem}-screen-dark-mobile", "fixture": fixture, "theme": "dark", "media": "screen", "bodyClasses": ["is-mobile"], "viewport": {"width": 390, "height": 844}},
                    {"id": f"{fixture.stem}-screen-light-relaxed", "fixture": fixture, "theme": "light", "media": "screen", "bodyClasses": ["ogd-spacing-relaxed", "ogd-zebra-disabled-permanently"], "viewport": {"width": 1440, "height": 1400}},
                    {"id": f"{fixture.stem}-screen-dark-relaxed", "fixture": fixture, "theme": "dark", "media": "screen", "bodyClasses": ["ogd-glass-subtle", "ogd-spacing-relaxed", "ogd-modern-tables", "ogd-zebra-disabled-permanently"], "viewport": {"width": 1440, "height": 1400}},
                    {"id": f"{fixture.stem}-print-light", "fixture": fixture, "theme": "light", "media": "print", "bodyClasses": ["ogd-report-mode", "ogd-pdf-visibility"], "viewport": {"width": 1440, "height": 1400}},
                    {"id": f"{fixture.stem}-print-pdf-compound", "fixture": fixture, "theme": "light", "media": "print", "bodyClasses": ["ogd-report-mode", "ogd-pdf-visibility", "ogd-pdf-compact", "ogd-pdf-screen-delivery", "ogd-pdf-header-enabled", "ogd-pdf-header-top-center", "ogd-pdf-label-segmented-dual", "ogd-pdf-header-dual-pair", "ogd-pdf-links-inline", "ogd-pdf-segment-value-violet", "ogd-pdf-segment-value-rose", "ogd-pdf-segment-value-amber"], "viewport": {"width": 1440, "height": 1400}},
                    {"id": f"{fixture.stem}-print-pdf-links-clean", "fixture": fixture, "theme": "light", "media": "print", "bodyClasses": ["ogd-report-mode", "ogd-pdf-visibility", "ogd-pdf-links-clean"], "viewport": {"width": 1440, "height": 1400}},
                ]
            )
    scenarios.extend(load_style_scenarios(style_limit))
    return scenarios


def risk_reasons(rule: dict[str, Any]) -> list[str]:
    selector_part = str(rule["selectorPart"])
    context = str(rule["atContext"])
    module = str(rule["module"])
    reasons: list[str] = []
    if STATE_PSEUDOS.search(selector_part):
        reasons.append("state-pseudo")
    if RISK_TEXT_RE.search(selector_part):
        reasons.append("obsidian-style-or-semantic-selector")
    if CONTENT_ELEMENT_RE.search(selector_part):
        reasons.append("document-content-selector")
    if RESERVED_MODULE_RE.search(module):
        reasons.append("reserved-module")
    if RESERVED_CONTEXT_RE.search(context):
        reasons.append("reserved-at-context")
    if ":root" in selector_part or "--ogd-" in f"{selector_part} {context}":
        reasons.append("token-or-variable")
    return sorted(set(reasons))


def reserved_bucket(row: dict[str, Any]) -> str | None:
    if row.get("classification") != "reserved":
        return None
    selector_part = str(row["selectorPart"])
    context = str(row["atContext"])
    module = str(row["module"])
    haystack = f"{selector_part} {context} {module}"
    risk_reasons_for_row = {str(reason) for reason in row["riskReasons"]}
    if "state-pseudo" in risk_reasons_for_row:
        return "state-interaction"
    if PRINT_PDF_RE.search(haystack):
        return "print-pdf-context"
    if STYLE_SETTING_BODY_RE.search(selector_part):
        return "style-setting-class"
    if module.startswith("src/plugins/") or PLUGIN_RUNTIME_RE.search(haystack):
        return "plugin-runtime"
    if module.startswith("src/chrome/") or CHROME_RUNTIME_RE.search(haystack):
        return "obsidian-chrome-runtime"
    if LIVE_PREVIEW_RE.search(haystack):
        return "live-preview-runtime"
    if "token-or-variable" in risk_reasons_for_row:
        return "token-variable"
    if "reserved-at-context" in risk_reasons_for_row:
        return "at-context-runtime"
    if "document-content-selector" in risk_reasons_for_row or "markdown-" in selector_part:
        return "document-content-fixture-gap"
    return "reserved-static-other"


def fixture_url(fixture: Path) -> str:
    url = fixture.resolve().as_uri()
    if fixture.resolve() == DEFAULT_FIXTURE.resolve():
        return f"{url}?build=v3"
    return url


def write_markdown(payload: dict[str, Any], out_path: Path) -> None:
    lines = [
        "# Unused CSS Candidate Report",
        "",
        f"Version: {payload['version']}",
        f"Bundle SHA256: `{payload['bundleSha256']}`",
        f"Coverage scenarios: {payload['scenarioCount']}",
        "",
        "## Summary",
        "",
        "| Classification | Count |",
        "| --- | ---: |",
    ]
    for key, value in payload["summary"].items():
        lines.append(f"| {key} | {value} |")
    lines.extend(["", "## Candidate Selectors", ""])
    candidates = [item for item in payload["selectors"] if item["classification"] == "candidate"]
    if candidates:
        lines.extend(["| Module | Line | Selector |", "| --- | ---: | --- |"])
        for item in candidates[:200]:
            selector = str(item["selectorPart"]).replace("|", "\\|")
            lines.append(f"| {item['module']} | {item['line']} | `{selector}` |")
    else:
        lines.append("No low-risk no-match selectors were found in the current coverage matrix.")
    lines.extend(["", "## Reserved No-Match Selectors", ""])
    reserved_count = payload["summary"].get("reserved", 0)
    lines.append(f"Reserved no-match selectors: {reserved_count}. These need purpose-built coverage before removal.")
    if payload["reservedReasonSummary"]:
        lines.extend(["", "### Reserved Reason Summary", "", "| Reason | Count |", "| --- | ---: |"])
        for reason, count in payload["reservedReasonSummary"].items():
            lines.append(f"| {reason} | {count} |")
    if payload.get("reservedBucketSummary"):
        lines.extend(["", "### Reserved Bucket Summary", "", "| Bucket | Count | Meaning | Recipe |", "| --- | ---: | --- | --- |"])
        for bucket, count in payload["reservedBucketSummary"].items():
            label = BUCKET_LABELS.get(bucket, "Reserved for manual review.").replace("|", "\\|")
            recipe = BUCKET_RECIPES.get(bucket, "OWNER-DECISION-TREE.md")
            lines.append(f"| {bucket} | {count} | {label} | `{recipe}` |")
    if payload.get("reservedDecisionPolicy"):
        lines.extend(["", "### Reserved Decision Policy", ""])
        lines.append(f"Current low-risk removal candidates: {payload['summary'].get('candidate', 0)}.")
        lines.append("Reserved selectors are not deletion approval; each bucket below defines the required next validation step.")
        lines.extend(["", "| Bucket | Decision | Next action |", "| --- | --- | --- |"])
        for bucket in payload.get("reservedBucketSummary", {}):
            policy = payload["reservedDecisionPolicy"].get(bucket, {})
            decision = str(policy.get("decision", "manual-review")).replace("|", "\\|")
            next_action = str(policy.get("nextAction", "Inspect before removal review.")).replace("|", "\\|")
            lines.append(f"| {bucket} | {decision} | {next_action} |")
    if payload.get("coverageBacklogPolicy"):
        lines.extend(["", "### Coverage Backlog Policy", ""])
        for key, text in payload["coverageBacklogPolicy"].items():
            lines.append(f"- `{key}`: {text}")
    if payload["coverageGapSummary"]:
        lines.extend(["", "### Coverage Gap Hotspots", "", "| Module | reserved | static | state | matched | Top buckets | Top reserved reasons |", "| --- | ---: | ---: | ---: | ---: | --- | --- |"])
        for item in payload["coverageGapSummary"][:12]:
            reasons = ", ".join(f"{entry['reason']}={entry['count']}" for entry in item["topReasons"])
            buckets = ", ".join(f"{entry['bucket']}={entry['count']}" for entry in item["topBuckets"])
            lines.append(f"| {item['module']} | {item['reserved']} | {item['staticReserved']} | {item['stateReserved']} | {item['matched']} | {buckets} | {reasons} |")
    if payload.get("reservedSamples"):
        lines.extend(["", "### Reserved Selector Samples", ""])
        lines.append("Representative no-match selectors from the largest hotspots. Static no-match selectors are shown before state-only hover/focus examples. These are examples for coverage planning, not removal approval.")
        for group in payload["reservedSamples"]:
            lines.extend(["", f"#### {group['module']}", "", "| Line | Bucket | Selector part | Reasons |", "| ---: | --- | --- | --- |"])
            for item in group["items"]:
                selector = str(item["selectorPart"]).replace("|", "\\|")
                reasons = ", ".join(item["riskReasons"])
                lines.append(f"| {item['line']} | {item['reservedBucket']} | `{selector}` | {reasons} |")
    if payload["invalidQueries"] or payload["invalidSelectorParts"]:
        lines.extend(["", "### Invalid Query Selectors", ""])
        lines.append("Invalid-query rows are query-coverage exclusions, not CSS syntax failures and not deletion evidence.")
    if payload.get("invalidQuerySummary"):
        lines.extend(["", "| Reason | Count | Meaning |", "| --- | ---: | --- |"])
        for reason, count in payload["invalidQuerySummary"].items():
            meaning = INVALID_QUERY_LABELS.get(reason, "The selector is not usable as direct DOM query coverage.").replace("|", "\\|")
            lines.append(f"| {reason} | {count} | {meaning} |")
    if payload["invalidQueries"]:
        lines.append("")
        lines.extend(["| Query selector |", "| --- |"])
        for query in payload["invalidQueries"]:
            escaped_query = str(query).replace("|", "\\|")
            lines.append(f"| `{escaped_query}` |")
    if payload["invalidSelectorParts"]:
        if payload["invalidQueries"]:
            lines.append("")
        lines.extend(["", "| Module | Line | Selector part | Reason | Meaning |", "| --- | ---: | --- | --- | --- |"])
        for item in payload["invalidSelectorParts"]:
            selector = str(item["selectorPart"]).replace("|", "\\|")
            meaning = str(item.get("meaning", "The selector is not usable as direct DOM query coverage.")).replace("|", "\\|")
            lines.append(f"| {item['module']} | {item['line']} | `{selector}` | {item['reason']} | {meaning} |")
    lines.extend(["", "## Module Summary", "", "| Module | candidate | reserved | invalid-query | matched |", "| --- | ---: | ---: | ---: | ---: |"])
    for module, counts in payload["moduleSummary"].items():
        lines.append(f"| {module} | {counts.get('candidate', 0)} | {counts.get('reserved', 0)} | {counts.get('invalid-query', 0)} | {counts.get('matched', 0)} |")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def reserved_reason_summary(rows: list[dict[str, Any]]) -> dict[str, int]:
    counter: Counter[str] = Counter()
    for row in rows:
        if row["classification"] != "reserved":
            continue
        counter.update(str(reason) for reason in row["riskReasons"])
    return dict(counter.most_common())


def reserved_bucket_summary(rows: list[dict[str, Any]]) -> dict[str, int]:
    counter: Counter[str] = Counter()
    for row in rows:
        if row["classification"] != "reserved":
            continue
        counter[str(row["reservedBucket"])] += 1
    return dict(counter.most_common())


def reserved_decision_summary(bucket_summary: dict[str, int]) -> dict[str, int]:
    counter: Counter[str] = Counter()
    for bucket, count in bucket_summary.items():
        decision = BUCKET_DECISIONS.get(bucket, {"decision": "manual-review"})["decision"]
        counter[str(decision)] += int(count)
    return dict(counter.most_common())


def invalid_query_summary(rows: list[dict[str, Any]], invalid_queries: set[str]) -> dict[str, int]:
    counter: Counter[str] = Counter()
    for row in rows:
        if row["classification"] == "invalid-query":
            counter[invalid_query_reason(row, invalid_queries)] += 1
    return dict(counter.most_common())


def coverage_gap_summary(rows: list[dict[str, Any]], module_summary: dict[str, dict[str, int]]) -> list[dict[str, Any]]:
    reason_by_module: dict[str, Counter[str]] = defaultdict(Counter)
    bucket_by_module: dict[str, Counter[str]] = defaultdict(Counter)
    static_reserved_by_module: Counter[str] = Counter()
    state_reserved_by_module: Counter[str] = Counter()
    for row in rows:
        if row["classification"] != "reserved":
            continue
        module = str(row["module"])
        risk_reasons_for_row = [str(reason) for reason in row["riskReasons"]]
        reason_by_module[module].update(risk_reasons_for_row)
        bucket_by_module[module].update([str(row["reservedBucket"])])
        if "state-pseudo" in risk_reasons_for_row:
            state_reserved_by_module[module] += 1
        else:
            static_reserved_by_module[module] += 1
    gaps: list[dict[str, Any]] = []
    for module, counts in sorted(module_summary.items()):
        reserved = counts.get("reserved", 0)
        if not reserved:
            continue
        gaps.append(
            {
                "module": module,
                "reserved": reserved,
                "staticReserved": static_reserved_by_module[module],
                "stateReserved": state_reserved_by_module[module],
                "matched": counts.get("matched", 0),
                "invalidQuery": counts.get("invalid-query", 0),
                "topReasons": [
                    {"reason": reason, "count": count}
                    for reason, count in reason_by_module[module].most_common(4)
                ],
                "topBuckets": [
                    {"bucket": bucket, "count": count}
                    for bucket, count in bucket_by_module[module].most_common(4)
                ],
            }
        )
    gaps.sort(key=lambda item: (-int(item["reserved"]), int(item["matched"]), item["module"]))
    return gaps


def reserved_samples(rows: list[dict[str, Any]], gaps: list[dict[str, Any]], per_module: int = 8) -> list[dict[str, Any]]:
    samples: list[dict[str, Any]] = []
    rows_by_module: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        if row["classification"] == "reserved":
            rows_by_module[str(row["module"])].append(row)
    for gap in gaps[:12]:
        module = str(gap["module"])
        items = []
        ordered_rows = sorted(
            rows_by_module.get(module, []),
            key=lambda row: (
                str(row["reservedBucket"]) == "state-interaction",
                str(row["reservedBucket"]) in {"plugin-runtime", "obsidian-chrome-runtime", "live-preview-runtime"},
                int(row["line"]),
                str(row["selectorPart"]),
            ),
        )
        for row in ordered_rows[:per_module]:
            items.append(
                {
                    "line": row["line"],
                    "selectorPart": row["selectorPart"],
                    "querySelector": row["querySelector"],
                    "atContext": row["atContext"],
                    "reservedBucket": row["reservedBucket"],
                    "riskReasons": row["riskReasons"],
                }
            )
        if items:
            samples.append({"module": module, "items": items})
    return samples


def invalid_selector_parts(rows: list[dict[str, Any]], invalid_queries: set[str]) -> list[dict[str, Any]]:
    invalid: list[dict[str, Any]] = []
    for row in rows:
        if row["classification"] != "invalid-query":
            continue
        query = row["querySelector"]
        reason = invalid_query_reason(row, invalid_queries)
        invalid.append(
            {
                "module": row["module"],
                "line": row["line"],
                "selectorPart": row["selectorPart"],
                "querySelector": query,
                "reason": reason,
                "meaning": INVALID_QUERY_LABELS.get(reason, "The selector is not usable as direct DOM query coverage."),
            }
        )
    invalid.sort(key=lambda item: (str(item["module"]), int(item["line"]), str(item["selectorPart"])))
    return invalid


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--style-limit", type=int, default=None, help="Limit unique Style Settings class scenarios for faster exploratory runs.")
    args = parser.parse_args()
    try:
        from playwright.sync_api import sync_playwright
    except ModuleNotFoundError:
        print("FAIL: Playwright is not installed", file=sys.stderr)
        return 2
    if not BUNDLE.is_file():
        print("FAIL: dist/theme-v3.css missing; run dev/scripts/bundle_v3.py", file=sys.stderr)
        return 1

    rules = parse_rules()
    query_selectors = sorted({rule["querySelector"] for rule in rules if rule["querySelector"]})
    scenarios = build_scenarios(args.style_limit)
    style_class_pool = sorted({body_class for scenario in scenarios for body_class in scenario["bodyClasses"]})
    counts: dict[str, int] = defaultdict(int)
    invalid_queries: set[str] = set()
    scenario_totals: list[dict[str, Any]] = []
    collect_js = r"""
    ({selectors}) => {
      const counts = {};
      const invalid = [];
      for (const selector of selectors) {
        try { counts[selector] = document.querySelectorAll(selector).length; }
        catch (error) { counts[selector] = 0; invalid.push(selector); }
      }
      return {counts, invalid};
    }
    """
    replace_css_js = r"""
    async (href) => {
      const links = Array.from(document.querySelectorAll('link[rel="stylesheet"]'))
        .filter((link) => /(?:^|\/)theme\.css(?:$|[?#])/.test(link.getAttribute('href') || link.href));
      const targets = links.length ? links : [document.head.appendChild(document.createElement('link'))];
      await Promise.all(targets.map((link) => new Promise((resolve, reject) => {
        link.rel = 'stylesheet'; link.onload = resolve; link.onerror = reject; link.href = href;
      })));
    }
    """
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        pages: dict[tuple[str, int, int, str], Any] = {}
        for scenario in scenarios:
            fixture = Path(scenario["fixture"]).resolve()
            viewport = scenario["viewport"]
            page_key = (str(fixture), int(viewport["width"]), int(viewport["height"]), str(scenario["media"]))
            page = pages.get(page_key)
            if page is None:
                page = browser.new_page(viewport=viewport, device_scale_factor=1)
                page.goto(fixture_url(fixture), wait_until="networkidle")
                if fixture != DEFAULT_FIXTURE.resolve():
                    page.evaluate(replace_css_js, BUNDLE.as_uri())
                if scenario["media"] == "print":
                    page.emulate_media(media="print")
                pages[page_key] = page
            page.evaluate(
                """
                ({theme, bodyClasses, styleClassPool}) => {
                  document.body.classList.remove('theme-light', 'theme-dark');
                  for (const name of styleClassPool) document.body.classList.remove(name);
                  document.body.classList.add(theme === 'dark' ? 'theme-dark' : 'theme-light');
                  for (const name of bodyClasses) document.body.classList.add(name);
                }
                """,
                {"theme": scenario["theme"], "bodyClasses": scenario["bodyClasses"], "styleClassPool": style_class_pool},
            )
            result = page.evaluate(collect_js, {"selectors": query_selectors})
            matched = 0
            for selector, count in result["counts"].items():
                count = int(count)
                if count:
                    matched += 1
                counts[selector] += count
            invalid_queries.update(result["invalid"])
            scenario_totals.append({"id": scenario["id"], "matchedQuerySelectors": matched, "invalidQuerySelectors": len(result["invalid"])})
        for page in pages.values():
            page.close()
        browser.close()

    rows: list[dict[str, Any]] = []
    summary: dict[str, int] = defaultdict(int)
    module_summary: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for rule in rules:
        query = rule["querySelector"]
        reasons = risk_reasons(rule)
        match_count = 0 if query is None else counts.get(str(query), 0)
        if query is None or query in invalid_queries:
            classification = "invalid-query"
            reasons = ["invalid-query"]
        elif match_count:
            classification = "matched"
        elif reasons:
            classification = "reserved"
        else:
            classification = "candidate"
        summary[classification] += 1
        module_summary[str(rule["module"])][classification] += 1
        row = {**rule, "classification": classification, "matchCount": match_count, "riskReasons": reasons}
        row["reservedBucket"] = reserved_bucket(row)
        rows.append(row)

    rows.sort(key=lambda item: (item["classification"], item["module"], item["line"], item["selectorPart"]))
    gaps = coverage_gap_summary(rows, {module: dict(counts) for module, counts in module_summary.items()})
    bucket_summary = reserved_bucket_summary(rows)
    payload = {
        "schema": "owen-graphite/unused-css-candidates/2",
        "version": version(),
        "bundle": BUNDLE.relative_to(ROOT).as_posix(),
        "bundleSha256": sha256(BUNDLE),
        "scenarioCount": len(scenarios),
        "querySelectorCount": len(query_selectors),
        "sourceSelectorPartCount": len(rules),
        "summary": dict(sorted(summary.items())),
        "reservedReasonSummary": reserved_reason_summary(rows),
        "reservedBucketSummary": bucket_summary,
        "reservedBucketLabels": BUCKET_LABELS,
        "reservedBucketRecipes": BUCKET_RECIPES,
        "reservedDecisionPolicy": BUCKET_DECISIONS,
        "reservedDecisionSummary": reserved_decision_summary(bucket_summary),
        "coverageBacklogPolicy": COVERAGE_BACKLOG_POLICY,
        "coverageGapSummary": gaps,
        "reservedSamples": reserved_samples(rows, gaps),
        "invalidQueries": sorted(invalid_queries),
        "invalidQueryLabels": INVALID_QUERY_LABELS,
        "invalidQuerySummary": invalid_query_summary(rows, invalid_queries),
        "invalidSelectorParts": invalid_selector_parts(rows, invalid_queries),
        "scenarios": [
            {
                "id": scenario["id"],
                "fixture": Path(scenario["fixture"]).relative_to(ROOT).as_posix(),
                "theme": scenario["theme"],
                "media": scenario["media"],
                "bodyClasses": scenario["bodyClasses"],
                **scenario_totals[index],
            }
            for index, scenario in enumerate(scenarios)
        ],
        "moduleSummary": {module: dict(counts) for module, counts in sorted(module_summary.items())},
        "selectors": rows,
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(payload, OUT_MD)
    print(
        f"OK: wrote {OUT_JSON.relative_to(ROOT)} and {OUT_MD.relative_to(ROOT)} "
        f"({len(scenarios)} scenarios, {summary.get('candidate', 0)} candidates, {summary.get('reserved', 0)} reserved no-match)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
