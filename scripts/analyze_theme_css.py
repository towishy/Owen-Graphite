#!/usr/bin/env python3
"""Generate an Owen Graphite CSS risk map for Obsidian core chrome."""

from __future__ import annotations

import argparse
import html
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CSS = ROOT / "theme.css"
DEFAULT_OUTPUT_DIR = ROOT / "docs" / "MAP"
DEFAULT_HTML = DEFAULT_OUTPUT_DIR / "theme-css-risk-map.html"
DEFAULT_JSON = DEFAULT_OUTPUT_DIR / "theme-css-risk-map.json"

CORE_SELECTOR_PATTERNS = [
    ("[role=tab]", re.compile(r"\[\s*role\s*=\s*['\"]?tab['\"]?\s*\]", re.I), 10),
    (".workspace-tabs", re.compile(r"\.workspace-tabs\b"), 7),
    (".workspace-tab-header-container", re.compile(r"\.workspace-tab-header-container\b"), 8),
    (".workspace-tab-header", re.compile(r"\.workspace-tab-header\b"), 8),
    (".workspace-tab-container", re.compile(r"\.workspace-tab-container\b"), 6),
    (".titlebar", re.compile(r"\.titlebar\b"), 7),
    (".titlebar-button", re.compile(r"\.titlebar-button\b"), 8),
    (".sidebar-toggle-button", re.compile(r"\.sidebar-toggle-button\b"), 8),
    (".workspace-ribbon", re.compile(r"\.workspace-ribbon\b"), 8),
    (".workspace-ribbon-collapse-btn", re.compile(r"\.workspace-ribbon-collapse-btn\b"), 8),
    (".side-dock-ribbon", re.compile(r"\.side-dock-ribbon\b"), 7),
    (".clickable-icon", re.compile(r"\.clickable-icon\b"), 5),
]

RISK_PROPERTIES = {
    "display": 8,
    "visibility": 8,
    "opacity": 7,
    "height": 7,
    "width": 7,
    "min-height": 6,
    "max-height": 6,
    "min-width": 6,
    "max-width": 6,
    "overflow": 6,
    "overflow-x": 5,
    "overflow-y": 5,
    "position": 7,
    "top": 5,
    "right": 5,
    "bottom": 5,
    "left": 5,
    "inset": 5,
    "z-index": 7,
    "transform": 7,
    "translate": 6,
    "scale": 6,
    "pointer-events": 8,
    "flex": 5,
    "flex-direction": 7,
    "flex-basis": 5,
    "flex-grow": 5,
    "flex-shrink": 5,
    "order": 7,
    "grid-area": 5,
}

DECORATIVE_PROPERTIES = {
    "background",
    "background-color",
    "background-image",
    "border",
    "border-color",
    "border-radius",
    "box-shadow",
    "color",
    "filter",
    "font-weight",
    "outline",
    "text-shadow",
}

CRITICAL_VALUES = {
    "display": re.compile(r"\bnone\b", re.I),
    "visibility": re.compile(r"\bhidden\b|\bcollapse\b", re.I),
    "opacity": re.compile(r"^(?:0(?:\.0+)?|0?\.0\d+)(?![\d.])"),
    "height": re.compile(r"^0(?:px|rem|em|%)?\b", re.I),
    "width": re.compile(r"^0(?:px|rem|em|%)?\b", re.I),
    "max-height": re.compile(r"^0(?:px|rem|em|%)?\b", re.I),
    "max-width": re.compile(r"^0(?:px|rem|em|%)?\b", re.I),
    "overflow": re.compile(r"\bhidden\b", re.I),
    "pointer-events": re.compile(r"\bnone\b", re.I),
}

VERSION_PATTERN = re.compile(r"\bv\d+(?:\.\d+){1,2}\b", re.I)


@dataclass(frozen=True)
class Declaration:
    property_name: str
    value: str
    line: int


@dataclass(frozen=True)
class Rule:
    selector: str
    declarations: list[Declaration]
    line: int
    context: str


@dataclass(frozen=True)
class Finding:
    severity: str
    score: int
    line: int
    selector: str
    context: str
    block: str
    matched_selectors: list[str]
    risky_properties: list[str]
    critical_properties: list[str]
    decorative_properties: list[str]
    summary: str


def line_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def mask_comments(text: str) -> str:
    def replace(match: re.Match[str]) -> str:
        return "".join("\n" if char == "\n" else " " for char in match.group(0))

    return re.sub(r"/\*[\s\S]*?\*/", replace, text)


def find_matching_brace(text: str, open_index: int) -> int:
    depth = 0
    quote = ""
    escape = False
    for index in range(open_index, len(text)):
        char = text[index]
        if quote:
            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif char == quote:
                quote = ""
            continue
        if char in {'"', "'"}:
            quote = char
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return index
    return -1


def extract_version_blocks(source: str) -> list[tuple[int, str]]:
    blocks = [(1, "Base stylesheet")]
    for match in re.finditer(r"/\*([\s\S]*?)\*/", source):
        comment = match.group(1)
        if not VERSION_PATTERN.search(comment):
            continue
        lines = [line.strip(" *=-") for line in comment.splitlines() if line.strip(" *=-")]
        title = next((line for line in lines if VERSION_PATTERN.search(line)), lines[0] if lines else "Version block")
        blocks.append((line_for_offset(source, match.start()), title[:120]))
    blocks.sort(key=lambda item: item[0])
    return blocks


def block_for_line(blocks: list[tuple[int, str]], line: int) -> str:
    current = blocks[0][1]
    for block_line, title in blocks:
        if block_line > line:
            break
        current = title
    return current


def parse_declarations(source: str, body_start: int, body: str) -> list[Declaration]:
    declarations = []
    for match in re.finditer(r"(?P<property>-{0,2}[\w-]+)\s*:\s*(?P<value>[^;{}]+)", body):
        property_name = match.group("property").strip().lower()
        value = " ".join(match.group("value").strip().split())
        declarations.append(Declaration(property_name, value, line_for_offset(source, body_start + match.start())))
    return declarations


def parse_rules(source: str, masked: str | None = None, start: int = 0, end: int | None = None, context: str = "") -> list[Rule]:
    if masked is None:
        masked = mask_comments(source)
    if end is None:
        end = len(masked)
    rules: list[Rule] = []
    cursor = start
    while cursor < end:
        open_index = masked.find("{", cursor, end)
        if open_index == -1:
            break
        close_index = find_matching_brace(masked, open_index)
        if close_index == -1 or close_index > end:
            break
        prelude = " ".join(masked[cursor:open_index].strip().split())
        body_start = open_index + 1
        body = source[body_start:close_index]
        masked_body = masked[body_start:close_index]
        if not prelude:
            cursor = close_index + 1
            continue
        if prelude.startswith("@") and "{" in masked_body and not prelude.lower().startswith("@keyframes"):
            nested_context = f"{context} / {prelude}" if context else prelude
            rules.extend(parse_rules(source, masked, body_start, close_index, nested_context))
        elif not prelude.startswith("@"):
            declarations = parse_declarations(source, body_start, body)
            if declarations:
                rules.append(Rule(prelude, declarations, line_for_offset(source, open_index), context or "root"))
        cursor = close_index + 1
    return rules


def matched_core_selectors(selector: str) -> list[tuple[str, int]]:
    matches = []
    for label, pattern, weight in CORE_SELECTOR_PATTERNS:
        if pattern.search(selector):
            matches.append((label, weight))
    return matches


def classify_findings(rules: list[Rule], blocks: list[tuple[int, str]]) -> list[Finding]:
    findings = []
    for rule in rules:
        selector_matches = matched_core_selectors(rule.selector)
        is_pseudo = "::before" in rule.selector or "::after" in rule.selector
        is_print_context = "@media print" in rule.context
        risky = []
        critical = []
        decorative = []
        property_score = 0
        for declaration in rule.declarations:
            property_name = declaration.property_name
            if property_name in RISK_PROPERTIES:
                risky.append(f"{property_name}: {declaration.value}")
                property_score += RISK_PROPERTIES[property_name]
                value_pattern = CRITICAL_VALUES.get(property_name)
                if value_pattern and value_pattern.search(declaration.value) and not is_pseudo and not is_print_context:
                    critical.append(f"{property_name}: {declaration.value}")
                    property_score += 10
            elif property_name in DECORATIVE_PROPERTIES:
                decorative.append(property_name)
        if not selector_matches:
            continue
        selector_score = max(weight for _, weight in selector_matches)
        score = selector_score + property_score + min(len(selector_matches), 4)
        if any(label == "[role=tab]" for label, _ in selector_matches):
            score += 12
        if is_pseudo and not critical:
            score = min(score, 17)
        if is_print_context and not critical:
            score = min(score, 14)
        if not risky:
            severity = "info"
            score = selector_score + len(decorative)
        elif critical:
            severity = "critical"
        elif score >= 28:
            severity = "high"
        elif score >= 18:
            severity = "medium"
        else:
            severity = "low"
        touched_properties = risky or decorative
        property_names = ", ".join(item.split(":", 1)[0] for item in touched_properties[:5])
        selector_names = ", ".join(label for label, _ in selector_matches)
        findings.append(
            Finding(
                severity=severity,
                score=score,
                line=rule.line,
                selector=rule.selector,
                context=rule.context,
                block=block_for_line(blocks, rule.line),
                matched_selectors=[label for label, _ in selector_matches],
                risky_properties=risky,
                critical_properties=critical,
                decorative_properties=sorted(set(decorative)),
                summary=f"{selector_names} touched by {property_names}",
            )
        )
    findings.sort(key=lambda finding: (finding.score, -finding.line), reverse=True)
    return findings


def severity_counts(findings: list[Finding]) -> Counter[str]:
    return Counter(finding.severity for finding in findings)


def top_blocks(findings: list[Finding], limit: int = 14) -> list[tuple[str, int, int]]:
    scores: dict[str, int] = defaultdict(int)
    counts: dict[str, int] = defaultdict(int)
    for finding in findings:
        scores[finding.block] += finding.score
        counts[finding.block] += 1
    return sorted(((block, scores[block], counts[block]) for block in scores), key=lambda item: item[1], reverse=True)[:limit]


def finding_to_dict(finding: Finding) -> dict[str, object]:
    return {
        "severity": finding.severity,
        "score": finding.score,
        "line": finding.line,
        "selector": finding.selector,
        "context": finding.context,
        "block": finding.block,
        "matched_selectors": finding.matched_selectors,
        "risky_properties": finding.risky_properties,
        "critical_properties": finding.critical_properties,
        "decorative_properties": finding.decorative_properties,
        "summary": finding.summary,
    }


def render_chips(items: list[str]) -> str:
    if not items:
        return '<span class="muted">None</span>'
    return "".join(f'<span class="chip">{html.escape(item)}</span>' for item in items)


def render_html(findings: list[Finding], rules: list[Rule], css_path: Path, json_path: Path) -> str:
    counts = severity_counts(findings)
    blocks = top_blocks(findings)
    selector_counts = Counter(label for finding in findings for label in finding.matched_selectors)
    property_counts = Counter(
        item.split(":", 1)[0]
        for finding in findings
        for item in (finding.risky_properties or finding.decorative_properties)
    )
    max_block_score = max((score for _, score, _ in blocks), default=1)
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    finding_rows = []
    for finding in findings[:100]:
        finding_rows.append(
            "<tr>"
            f'<td><span class="badge {finding.severity}">{finding.severity}</span></td>'
            f"<td>{finding.score}</td>"
            f"<td>{finding.line}</td>"
            f"<td><code>{html.escape(finding.selector)}</code><small>{html.escape(finding.context)}</small></td>"
            f"<td>{render_chips(finding.matched_selectors)}</td>"
            f"<td>{render_chips((finding.risky_properties or finding.decorative_properties)[:8])}</td>"
            f"<td>{html.escape(finding.block)}</td>"
            "</tr>"
        )
    block_rows = []
    for block, score, count in blocks:
        width = max(4, int(score / max_block_score * 100))
        block_rows.append(
            "<div class=\"block-row\">"
            f"<div class=\"block-title\">{html.escape(block)}</div>"
            f"<div class=\"bar\"><span style=\"width:{width}%\"></span></div>"
            f"<div class=\"block-meta\">score {score} / {count} findings</div>"
            "</div>"
        )
    selector_items = "".join(f"<li><code>{html.escape(name)}</code><strong>{count}</strong></li>" for name, count in selector_counts.most_common())
    property_items = "".join(f"<li><code>{html.escape(name)}</code><strong>{count}</strong></li>" for name, count in property_counts.most_common(16))
    css_label = html.escape(str(css_path.relative_to(ROOT)))
    json_label = html.escape(str(json_path.relative_to(ROOT)))
    return f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Owen Graphite Theme CSS Risk Map</title>
  <style>
    :root {{ color-scheme: light; --bg:#f8fafc; --panel:rgba(255,255,255,.88); --ink:#111827; --muted:#64748b; --line:#dbe3ef; --critical:#b91c1c; --high:#c2410c; --medium:#a16207; --low:#2563eb; }}
    body {{ margin:0; background:var(--bg); color:var(--ink); font:14px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; }}
    main {{ max-width:1200px; margin:0 auto; padding:28px 20px 48px; }}
    header {{ display:grid; gap:10px; margin-bottom:20px; }}
    h1 {{ margin:0; font-size:28px; letter-spacing:0; }}
    h2 {{ margin:28px 0 12px; font-size:18px; letter-spacing:0; }}
    p {{ margin:0; color:var(--muted); }}
    code {{ font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; font-size:.92em; }}
    .summary {{ display:grid; grid-template-columns:repeat(6,minmax(0,1fr)); gap:10px; margin:18px 0; }}
    .metric {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:12px; box-shadow:0 8px 24px rgba(15,23,42,.06); }}
    .metric b {{ display:block; font-size:24px; line-height:1.1; }}
    .metric span {{ color:var(--muted); font-size:12px; text-transform:uppercase; font-weight:700; }}
    .grid {{ display:grid; grid-template-columns:1.15fr .85fr; gap:14px; align-items:start; }}
    .panel {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:14px; box-shadow:0 8px 24px rgba(15,23,42,.06); }}
    .block-row {{ display:grid; grid-template-columns:minmax(220px,1fr) 220px 136px; gap:10px; align-items:center; padding:8px 0; border-bottom:1px solid #edf2f7; }}
    .block-row:last-child {{ border-bottom:0; }}
    .block-title {{ overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }}
    .block-meta {{ color:var(--muted); font-size:12px; text-align:right; }}
    .bar {{ height:9px; background:#e5e7eb; border-radius:999px; overflow:hidden; }}
    .bar span {{ display:block; height:100%; background:linear-gradient(90deg,#0f766e,#f59e0b,#b91c1c); border-radius:inherit; }}
    ul.compact {{ list-style:none; padding:0; margin:0; display:grid; gap:7px; }}
    ul.compact li {{ display:flex; justify-content:space-between; gap:12px; border-bottom:1px solid #edf2f7; padding-bottom:6px; }}
    table {{ width:100%; border-collapse:separate; border-spacing:0; background:var(--panel); border:1px solid var(--line); border-radius:8px; overflow:hidden; box-shadow:0 8px 24px rgba(15,23,42,.06); }}
    th, td {{ text-align:left; vertical-align:top; padding:9px 10px; border-bottom:1px solid #edf2f7; }}
    th {{ background:#eef2f7; font-size:12px; color:#334155; position:sticky; top:0; }}
    tr:last-child td {{ border-bottom:0; }}
    td small {{ display:block; margin-top:4px; color:var(--muted); }}
    .badge {{ display:inline-block; min-width:64px; text-align:center; border-radius:999px; padding:2px 8px; color:white; font-weight:700; font-size:12px; }}
    .critical {{ background:var(--critical); }} .high {{ background:var(--high); }} .medium {{ background:var(--medium); }} .low {{ background:var(--low); }} .info {{ background:#475569; }}
    .chip {{ display:inline-block; margin:0 4px 4px 0; padding:2px 6px; border:1px solid #c7d2fe; border-radius:6px; background:#eef2ff; font:12px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; }}
    .muted {{ color:var(--muted); }}
    .note {{ margin-top:12px; padding:12px; border:1px solid #bae6fd; background:#eff6ff; border-radius:8px; color:#075985; }}
    @media (max-width: 880px) {{ .summary, .grid {{ grid-template-columns:1fr; }} .block-row {{ grid-template-columns:1fr; }} th:nth-child(5), td:nth-child(5), th:nth-child(7), td:nth-child(7) {{ display:none; }} }}
  </style>
</head>
<body>
  <main>
    <header>
      <h1>Owen Graphite Theme CSS Risk Map</h1>
      <p>Generated {generated}. Source: <code>{css_label}</code>. Machine data: <code>{json_label}</code>. Parsed rules: {len(rules)}.</p>
    </header>
        <section class="summary">
            <div class="metric"><b>{len(findings)}</b><span>total</span></div>
            <div class="metric"><b>{counts.get('critical', 0)}</b><span>critical</span></div>
            <div class="metric"><b>{counts.get('high', 0)}</b><span>high</span></div>
            <div class="metric"><b>{counts.get('medium', 0)}</b><span>medium</span></div>
            <div class="metric"><b>{counts.get('low', 0)}</b><span>low</span></div>
            <div class="metric"><b>{counts.get('info', 0)}</b><span>info</span></div>
    </section>
    <div class="note">This report is a triage map, not a failure gate. Review findings that combine core chrome selectors with structural properties before shipping a Windows test ZIP.</div>
    <section class="grid">
      <div class="panel">
        <h2>Patch Block Heatmap</h2>
        {''.join(block_rows) if block_rows else '<p>No core chrome findings.</p>'}
      </div>
      <div class="panel">
        <h2>Selector Hits</h2>
        <ul class="compact">{selector_items}</ul>
        <h2>Risky Properties</h2>
        <ul class="compact">{property_items}</ul>
      </div>
    </section>
    <section>
      <h2>Top Findings</h2>
      <table>
        <thead><tr><th>Severity</th><th>Score</th><th>Line</th><th>Selector</th><th>Matched</th><th>Risky Properties</th><th>Block</th></tr></thead>
        <tbody>{''.join(finding_rows) if finding_rows else '<tr><td colspan="7">No findings.</td></tr>'}</tbody>
      </table>
    </section>
  </main>
</body>
</html>
"""


def write_outputs(css_path: Path, html_path: Path, json_path: Path) -> list[Finding]:
    source = css_path.read_text(encoding="utf-8")
    blocks = extract_version_blocks(source)
    rules = parse_rules(source)
    findings = classify_findings(rules, blocks)
    html_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "source": str(css_path.relative_to(ROOT)),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "rule_count": len(rules),
        "finding_count": len(findings),
        "severity_counts": dict(severity_counts(findings)),
        "findings": [finding_to_dict(finding) for finding in findings],
    }
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    html_path.write_text(render_html(findings, rules, css_path, json_path), encoding="utf-8")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--css", type=Path, default=DEFAULT_CSS, help="CSS file to analyze")
    parser.add_argument("--html", type=Path, default=DEFAULT_HTML, help="HTML report output path")
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON, help="JSON report output path")
    parser.add_argument("--top", type=int, default=12, help="Number of console findings to print")
    args = parser.parse_args()

    css_path = args.css.resolve()
    html_path = args.html.resolve()
    json_path = args.json.resolve()
    findings = write_outputs(css_path, html_path, json_path)
    counts = severity_counts(findings)
    print(f"OK: wrote {html_path.relative_to(ROOT)}")
    print(f"OK: wrote {json_path.relative_to(ROOT)}")
    print(
        "OK: CSS risk map findings="
        f"{len(findings)} critical={counts.get('critical', 0)} "
        f"high={counts.get('high', 0)} medium={counts.get('medium', 0)} "
        f"low={counts.get('low', 0)} info={counts.get('info', 0)}"
    )
    for finding in findings[:args.top]:
        print(f"{finding.severity.upper()}: line {finding.line}: score={finding.score}: {finding.summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())