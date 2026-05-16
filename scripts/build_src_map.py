#!/usr/bin/env python3
"""Build source-adjacent MAP artifacts for the Owen Graphite src/ tree.

The MAP lives under dev/MAP so investigation artifacts stay separate from the
shipping src/ CSS modules while still mapping directly back to src/entry.css.
"""

from __future__ import annotations

import html
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / "src"
ENTRY = SRC_DIR / "entry.css"
MAP_DIR = ROOT / "dev" / "MAP"
MANIFEST = ROOT / "manifest.json"

IMPORT_RE = re.compile(r"@import\s+url\(\s*['\"]?([^'\")]+)['\"]?\s*\)\s*;", re.I)
LEGACY_RE = re.compile(r"/\*\s*([^*]+?)\s*->\s*([^*]+?)\s*\*/")
RULE_RE = re.compile(r"([^{}]+?)\{([^{}]*)\}", re.S)


@dataclass(frozen=True)
class CssRule:
    selector: str
    body: str
    at_context: str
    line: int


def normalize_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def manifest_version() -> str:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))["version"]


def import_order() -> list[dict[str, object]]:
    modules: list[dict[str, object]] = []
    pending_legacy = ""
    for line_number, raw_line in enumerate(ENTRY.read_text(encoding="utf-8").splitlines(), start=1):
        legacy_match = LEGACY_RE.search(raw_line)
        if legacy_match:
            pending_legacy = normalize_ws(legacy_match.group(1))
            continue
        import_match = IMPORT_RE.search(raw_line)
        if not import_match:
            continue
        relative_import = import_match.group(1)
        module_path = (ENTRY.parent / relative_import).resolve()
        modules.append(
            {
                "import_index": len(modules) + 1,
                "entry_line": line_number,
                "legacy_id": pending_legacy,
                "module": module_path.relative_to(ROOT).as_posix(),
            }
        )
        pending_legacy = ""
    return modules


def tokenize_blocks(css: str) -> list[CssRule]:
    rules: list[CssRule] = []
    at_stack: list[str] = []
    index = 0
    line_number = 1
    css_length = len(css)

    while index < css_length:
        if css.startswith("/*", index):
            comment_end = css.find("*/", index + 2)
            if comment_end == -1:
                return rules
            line_number += css.count("\n", index, comment_end + 2)
            index = comment_end + 2
            continue
        current_char = css[index]
        if current_char.isspace():
            if current_char == "\n":
                line_number += 1
            index += 1
            continue
        if current_char == "@":
            header_start = index
            while index < css_length and css[index] not in "{;":
                if css[index] == "\n":
                    line_number += 1
                index += 1
            if index >= css_length:
                return rules
            if css[index] == ";":
                index += 1
                continue
            header = normalize_ws(css[header_start:index])
            at_stack.append(header)
            block_start = index + 1
            index = block_start
            depth = 1
            while index < css_length and depth > 0:
                if css.startswith("/*", index):
                    comment_end = css.find("*/", index + 2)
                    if comment_end == -1:
                        return rules
                    line_number += css.count("\n", index, comment_end + 2)
                    index = comment_end + 2
                    continue
                if css[index] == "{":
                    depth += 1
                elif css[index] == "}":
                    depth -= 1
                    if depth == 0:
                        break
                if css[index] == "\n":
                    line_number += 1
                index += 1
            inner_css = css[block_start:index]
            inner_start_line = css.count("\n", 0, block_start) + 1
            for inner_rule in tokenize_blocks(inner_css):
                context = " >> ".join(at_stack + ([inner_rule.at_context] if inner_rule.at_context else []))
                rules.append(
                    CssRule(
                        selector=inner_rule.selector,
                        body=inner_rule.body,
                        at_context=context,
                        line=inner_start_line + inner_rule.line - 1,
                    )
                )
            at_stack.pop()
            index += 1
            continue
        selector_start = index
        while index < css_length:
            if css.startswith("/*", index):
                comment_end = css.find("*/", index + 2)
                if comment_end == -1:
                    return rules
                line_number += css.count("\n", index, comment_end + 2)
                index = comment_end + 2
                continue
            if css[index] in "{}":
                break
            index += 1
        if index >= css_length or css[index] != "{":
            index += 1
            continue
        selector = normalize_ws(css[selector_start:index])
        body_start = index + 1
        index = body_start
        depth = 1
        while index < css_length and depth > 0:
            if css.startswith("/*", index):
                comment_end = css.find("*/", index + 2)
                if comment_end == -1:
                    return rules
                line_number += css.count("\n", index, comment_end + 2)
                index = comment_end + 2
                continue
            if css[index] == "{":
                depth += 1
            elif css[index] == "}":
                depth -= 1
                if depth == 0:
                    break
            if css[index] == "\n":
                line_number += 1
            index += 1
        body = normalize_ws(css[body_start:index])
        if selector and body:
            rules.append(CssRule(selector=selector, body=body, at_context=" >> ".join(at_stack), line=line_number))
        index += 1
    return rules


def scan_structural_issues(css: str) -> list[dict[str, object]]:
    issues: list[dict[str, object]] = []
    depth = 0
    line_number = 1
    index = 0
    css_length = len(css)
    while index < css_length:
        if css.startswith("/*", index):
            comment_end = css.find("*/", index + 2)
            if comment_end == -1:
                issues.append({"severity": "critical", "line": line_number, "message": "unterminated comment"})
                return issues
            line_number += css.count("\n", index, comment_end + 2)
            index = comment_end + 2
            continue
        current_char = css[index]
        if current_char == "\n":
            line_number += 1
        elif current_char == "{":
            depth += 1
        elif current_char == "}":
            if depth == 0:
                issues.append({"severity": "critical", "line": line_number, "message": "orphan closing brace"})
            else:
                depth -= 1
        index += 1
    if depth:
        issues.append({"severity": "critical", "line": line_number, "message": f"unclosed block depth={depth}"})
    return issues


def declarations(body: str) -> list[tuple[str, str]]:
    parsed: list[tuple[str, str]] = []
    for raw_declaration in body.split(";"):
        if ":" not in raw_declaration:
            continue
        property_name, _, value = raw_declaration.partition(":")
        parsed.append((property_name.strip().lower(), value.strip()))
    return parsed


def specificity(selector: str) -> tuple[int, int, int]:
    selector_without_strings = re.sub(r"(['\"]).*?\1", "", selector)
    ids = len(re.findall(r"#[\w-]+", selector_without_strings))
    classes = len(re.findall(r"\.[\w-]+|\[[^\]]+\]|:(?!:)[\w-]+(?:\([^)]*\))?", selector_without_strings))
    elements = len(re.findall(r"(?<![#.:-])\b[a-zA-Z][\w-]*\b", selector_without_strings))
    elements -= len(re.findall(r":{1,2}[\w-]+", selector_without_strings))
    return ids, max(classes, 0), max(elements, 0)


def severity_for_score(score: int, critical_count: int) -> str:
    if critical_count:
        return "critical"
    if score >= 30:
        return "high"
    if score >= 12:
        return "medium"
    if score > 0:
        return "low"
    return "info"


def severity_rank(severity: object) -> int:
    order = {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4}
    return order.get(str(severity), 5)


def analyze_module(module_info: dict[str, object]) -> tuple[dict[str, object], list[dict[str, object]], dict[str, dict[str, object]]]:
    module_path = ROOT / str(module_info["module"])
    css = module_path.read_text(encoding="utf-8")
    rules = tokenize_blocks(css)
    structural_issues = scan_structural_issues(css)
    findings: list[dict[str, object]] = []
    selector_entries: dict[str, dict[str, object]] = {}

    important_count = 0
    has_count = 0
    high_specificity_count = 0
    live_preview_sensitive_count = 0
    max_specificity = (0, 0, 0)
    property_counter: Counter[str] = Counter()
    selector_counter: Counter[str] = Counter()

    for issue in structural_issues:
        findings.append(
            {
                "severity": issue["severity"],
                "category": "css-structure",
                "module": module_info["module"],
                "line": issue["line"],
                "message": issue["message"],
            }
        )

    for rule in rules:
        selector_counter[rule.selector] += 1
        selector_specificity = specificity(rule.selector)
        max_specificity = max(max_specificity, selector_specificity)
        if selector_specificity >= (0, 8, 0):
            high_specificity_count += 1
            findings.append(
                {
                    "severity": "medium",
                    "category": "high-specificity",
                    "module": module_info["module"],
                    "line": rule.line,
                    "selector": rule.selector,
                    "message": f"specificity={selector_specificity}",
                }
            )
        if ":has(" in rule.selector:
            has_count += rule.selector.count(":has(")
            findings.append(
                {
                    "severity": "low",
                    "category": "has-selector",
                    "module": module_info["module"],
                    "line": rule.line,
                    "selector": rule.selector,
                    "message": ":has() selector; keep narrowly scoped",
                }
            )
        if "markdown-source-view.mod-cm6" in rule.selector:
            sensitive_props = {"margin", "margin-top", "margin-bottom", "padding", "padding-top", "padding-bottom", "outline", "transform"}
            declared_props = {property_name for property_name, _ in declarations(rule.body)}
            if declared_props & sensitive_props:
                live_preview_sensitive_count += 1
                findings.append(
                    {
                        "severity": "medium",
                        "category": "cm6-hit-routing-sensitive",
                        "module": module_info["module"],
                        "line": rule.line,
                        "selector": rule.selector,
                        "message": "CM6 rule declares vertical box or overlay-sensitive properties",
                    }
                )
        for property_name, value in declarations(rule.body):
            property_counter[property_name] += 1
            if "!important" in value:
                important_count += 1
                findings.append(
                    {
                        "severity": "high",
                        "category": "important",
                        "module": module_info["module"],
                        "line": rule.line,
                        "selector": rule.selector,
                        "message": f"{property_name}: {value}",
                    }
                )
        selector_entries[f"{module_info['module']}::{rule.selector}::{rule.line}"] = {
            "module": module_info["module"],
            "selector": rule.selector,
            "line": rule.line,
            "at_context": rule.at_context,
            "specificity": selector_specificity,
            "declarations": len(declarations(rule.body)),
        }

    repeated_in_file = sum(count - 1 for count in selector_counter.values() if count > 1)
    score = (
        len(structural_issues) * 100
        + important_count * 15
        + high_specificity_count * 3
        + live_preview_sensitive_count * 3
        + has_count * 2
        + repeated_in_file
    )
    reasons: list[str] = []
    if structural_issues:
        reasons.append("css-structure")
    if important_count:
        reasons.append("important")
    if high_specificity_count:
        reasons.append("high-specificity")
    if live_preview_sensitive_count:
        reasons.append("cm6-hit-routing-sensitive")
    if has_count:
        reasons.append("has-selector")
    if repeated_in_file:
        reasons.append("repeated-selector-in-file")

    module_record = {
        **module_info,
        "line_count": css.count("\n") + 1,
        "selector_count": len(rules),
        "declaration_count": sum(property_counter.values()),
        "important_count": important_count,
        "has_selector_count": has_count,
        "high_specificity_selector_count": high_specificity_count,
        "live_preview_sensitive_rule_count": live_preview_sensitive_count,
        "repeated_selector_extra_count": repeated_in_file,
        "max_specificity": max_specificity,
        "top_properties": property_counter.most_common(12),
        "risk_score": score,
        "severity": severity_for_score(score, len(structural_issues)),
        "risk_reasons": reasons,
    }
    return module_record, findings, selector_entries


def cross_file_selector_groups(selector_entries: dict[str, dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for entry in selector_entries.values():
        grouped[str(entry["selector"])].append(entry)
    groups: list[dict[str, object]] = []
    for selector, entries in grouped.items():
        modules = sorted({str(entry["module"]) for entry in entries})
        if len(modules) < 2:
            continue
        groups.append(
            {
                "selector": selector,
                "occurrences": len(entries),
                "modules": modules,
                "lines": [{"module": entry["module"], "line": entry["line"]} for entry in entries],
            }
        )
    return sorted(groups, key=lambda group: (-int(group["occurrences"]), str(group["selector"])))


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def markdown_report(payload: dict[str, object]) -> str:
    summary = payload["summary"]
    finding_counts = summary["finding_severity_counts"]
    module_counts = summary["module_severity_counts"]
    module_rows = []
    for module in payload["source_modules"]:
        module_rows.append(
            "| {severity} | {score} | `{module}` | {selectors} | {important} | {has_count} | {reasons} |".format(
                severity=module["severity"],
                score=module["risk_score"],
                module=module["module"],
                selectors=module["selector_count"],
                important=module["important_count"],
                has_count=module["has_selector_count"],
                reasons=", ".join(module["risk_reasons"]) or "-",
            )
        )
    finding_rows = []
    for finding in payload["findings"][:80]:
        finding_rows.append(
            "| {severity} | {category} | `{module}:{line}` | {message} |".format(
                severity=finding["severity"],
                category=finding["category"],
                module=finding["module"],
                line=finding["line"],
                message=str(finding["message"]).replace("|", "\\|"),
            )
        )
    return "\n".join(
        [
            "# Source MAP Risk Classification",
            "",
            "Canonical MAP location: `dev/MAP`.",
            "",
            "## Summary",
            "",
            f"- Version: `{payload['version']}`",
            f"- Source: `{payload['source']}`",
            f"- Modules: {summary['module_count']}",
            f"- Selectors: {summary['selector_count']}",
            f"- Findings: {summary['finding_count']}",
            f"- Finding severity counts: critical={finding_counts.get('critical', 0)}, high={finding_counts.get('high', 0)}, medium={finding_counts.get('medium', 0)}, low={finding_counts.get('low', 0)}, info={finding_counts.get('info', 0)}",
            f"- Module severity counts: critical={module_counts.get('critical', 0)}, high={module_counts.get('high', 0)}, medium={module_counts.get('medium', 0)}, low={module_counts.get('low', 0)}, info={module_counts.get('info', 0)}",
            "",
            "## Module Risk Table",
            "",
            "| Severity | Score | Module | Selectors | !important | :has | Reasons |",
            "|---|---:|---|---:|---:|---:|---|",
            *module_rows,
            "",
            "## Findings",
            "",
            "| Severity | Category | Location | Message |",
            "|---|---|---|---|",
            *(finding_rows or ["| info | none | - | No structural findings. |"]),
            "",
        ]
    )


def checklist(payload: dict[str, object]) -> str:
    finding_counts = payload["summary"]["finding_severity_counts"]
    module_counts = payload["summary"]["module_severity_counts"]
    return "\n".join(
        [
            "# Source MAP Stabilization Checklist",
            "",
            "## Gates",
            "",
            "- Finding `critical = 0`: no orphan braces, unclosed blocks, or unterminated comments.",
            "- Finding `high` must not increase unless a release note explains the Obsidian core conflict.",
            "- CM6 hit-routing sensitive findings must be reviewed against `dev/MAP/cm6-hit-routing-contract.md`.",
            "- Top chrome/icon changes must be reviewed against `dev/MAP/top-chrome-icon-background-contract.md`.",
            "",
            "## Current Finding Baseline",
            "",
            f"- critical={finding_counts.get('critical', 0)}",
            f"- high={finding_counts.get('high', 0)}",
            f"- medium={finding_counts.get('medium', 0)}",
            f"- low={finding_counts.get('low', 0)}",
            f"- info={finding_counts.get('info', 0)}",
            "",
            "## Current Module Baseline",
            "",
            f"- critical={module_counts.get('critical', 0)}",
            f"- high={module_counts.get('high', 0)}",
            f"- medium={module_counts.get('medium', 0)}",
            f"- low={module_counts.get('low', 0)}",
            f"- info={module_counts.get('info', 0)}",
            "",
            "## Regenerate",
            "",
            "```powershell",
            r".\.venv\Scripts\python.exe scripts\build_src_map.py",
            "```",
            "",
        ]
    )


def html_report(payload: dict[str, object]) -> str:
    rows = []
    for module in payload["source_modules"]:
        rows.append(
            "<tr><td><span class='badge {severity}'>{severity}</span></td><td>{score}</td><td><code>{module}</code></td><td>{selectors}</td><td>{reasons}</td></tr>".format(
                severity=html.escape(str(module["severity"])),
                score=module["risk_score"],
                module=html.escape(str(module["module"])),
                selectors=module["selector_count"],
                reasons=html.escape(", ".join(module["risk_reasons"]) or "-"),
            )
        )
    finding_counts = payload["summary"]["finding_severity_counts"]
    return f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Owen Graphite Source MAP Risk Map</title>
  <style>
    body {{ margin:0; background:#f8fafc; color:#111827; font:14px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; }}
    main {{ max-width:1180px; margin:0 auto; padding:28px 20px 48px; }}
    h1 {{ margin:0 0 8px; font-size:28px; letter-spacing:0; }}
    p {{ margin:0 0 18px; color:#64748b; }}
    .summary {{ display:grid; grid-template-columns:repeat(5,minmax(0,1fr)); gap:10px; margin:18px 0; }}
    .metric, table {{ background:rgba(255,255,255,.9); border:1px solid #dbe3ef; border-radius:8px; box-shadow:0 8px 24px rgba(15,23,42,.06); }}
    .metric {{ padding:12px; }} .metric b {{ display:block; font-size:24px; }} .metric span {{ color:#64748b; font-size:12px; font-weight:700; text-transform:uppercase; }}
    table {{ width:100%; border-collapse:separate; border-spacing:0; overflow:hidden; }}
    th, td {{ text-align:left; vertical-align:top; padding:9px 10px; border-bottom:1px solid #edf2f7; }} th {{ background:#eef2f7; color:#334155; font-size:12px; }} tr:last-child td {{ border-bottom:0; }}
    code {{ font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; font-size:.92em; }}
    .badge {{ display:inline-block; min-width:64px; text-align:center; border-radius:999px; padding:2px 8px; color:white; font-weight:700; font-size:12px; }}
    .critical {{ background:#b91c1c; }} .high {{ background:#c2410c; }} .medium {{ background:#a16207; }} .low {{ background:#2563eb; }} .info {{ background:#475569; }}
    @media (max-width: 760px) {{ .summary {{ grid-template-columns:1fr; }} }}
  </style>
</head>
<body>
<main>
  <h1>Owen Graphite Source MAP Risk Map</h1>
    <p>Canonical MAP root: <code>dev/MAP</code>. Source: <code>{html.escape(str(payload['source']))}</code>. Version: <code>{html.escape(str(payload['version']))}</code>.</p>
  <section class="summary">
    <div class="metric"><b>{payload['summary']['module_count']}</b><span>modules</span></div>
    <div class="metric"><b>{payload['summary']['selector_count']}</b><span>selectors</span></div>
    <div class="metric"><b>{payload['summary']['finding_count']}</b><span>findings</span></div>
    <div class="metric"><b>{finding_counts.get('critical', 0)}</b><span>critical findings</span></div>
    <div class="metric"><b>{finding_counts.get('high', 0)}</b><span>high findings</span></div>
  </section>
  <table>
    <thead><tr><th>Severity</th><th>Score</th><th>Module</th><th>Selectors</th><th>Reasons</th></tr></thead>
    <tbody>{''.join(rows)}</tbody>
  </table>
</main>
</body>
</html>
"""


def main() -> int:
    MAP_DIR.mkdir(parents=True, exist_ok=True)
    modules = import_order()
    module_records: list[dict[str, object]] = []
    all_findings: list[dict[str, object]] = []
    selector_entries: dict[str, dict[str, object]] = {}
    for module_info in modules:
        module_record, findings, module_selector_entries = analyze_module(module_info)
        module_records.append(module_record)
        all_findings.extend(findings)
        selector_entries.update(module_selector_entries)
    cross_file_groups = cross_file_selector_groups(selector_entries)
    finding_severity_counts = Counter(str(finding["severity"]) for finding in all_findings)
    module_severity_counts = Counter(str(module["severity"]) for module in module_records)
    payload: dict[str, object] = {
        "source": ENTRY.relative_to(ROOT).as_posix(),
        "map_root": MAP_DIR.relative_to(ROOT).as_posix(),
        "version": manifest_version(),
        "module_order": modules,
        "summary": {
            "module_count": len(module_records),
            "selector_count": sum(int(module["selector_count"]) for module in module_records),
            "finding_count": len(all_findings),
            "cross_file_selector_group_count": len(cross_file_groups),
            "finding_severity_counts": dict(sorted(finding_severity_counts.items(), key=lambda item: severity_rank(item[0]))),
            "module_severity_counts": dict(sorted(module_severity_counts.items(), key=lambda item: severity_rank(item[0]))),
        },
        "source_modules": module_records,
        "findings": sorted(all_findings, key=lambda finding: (severity_rank(finding["severity"]), str(finding["module"]), int(finding["line"]))),
        "cross_file_selectors": cross_file_groups[:120],
    }
    write_json(MAP_DIR / "theme-css-risk-map.json", payload)
    write_json(MAP_DIR / "selector-provenance.json", selector_entries)
    (MAP_DIR / "map-info-classification.md").write_text(markdown_report(payload), encoding="utf-8")
    (MAP_DIR / "css-stabilization-checklist.md").write_text(checklist(payload), encoding="utf-8")
    (MAP_DIR / "theme-css-risk-map.html").write_text(html_report(payload), encoding="utf-8")
    print(
        "OK: built dev/MAP "
        f"({len(module_records)} modules, {payload['summary']['selector_count']} selectors, "
        f"{len(all_findings)} findings, {len(cross_file_groups)} cross-file selector groups)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())