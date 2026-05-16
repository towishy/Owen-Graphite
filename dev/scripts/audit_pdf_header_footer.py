#!/usr/bin/env python3
"""Audit the PDF header/footer marginalia contract.

This guard codifies the v3.1.32+ PDF marginalia design: print-only, two
anchor pseudos, no Chromium-fragile margin boxes/string-set/list tricks, and
stable Style Settings + token plumbing.

Exits with code 1 if any contract violation is detected, 0 otherwise.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT / "src"
STYLE_SETTINGS = SRC_DIR / "features" / "40-style-settings.css"
PDF_OWNER = SRC_DIR / "features" / "41-feature-presets.css"
PAGE_OWNER = SRC_DIR / "features" / "43-print-base.css"
LIGHT_TOKENS = SRC_DIR / "tokens" / "00-light-tokens.css"
DARK_TOKENS = SRC_DIR / "tokens" / "01-dark-tokens.css"

REQUIRED_SETTING_IDS = (
    "ogd-settings-pdf-marginalia",
    "ogd-pdf-marginalia-preset",
    "ogd-pdf-label-layout",
    "ogd-pdf-header-enabled",
    "ogd-pdf-header-text",
    "ogd-pdf-header-value",
    "ogd-pdf-footer-enabled",
    "ogd-pdf-footer-text",
    "ogd-pdf-footer-value",
    "ogd-pdf-marginalia-accent",
    "ogd-pdf-marginalia-style",
    "ogd-pdf-header-key-palette",
    "ogd-pdf-header-value-palette",
    "ogd-pdf-footer-key-palette",
    "ogd-pdf-footer-value-palette",
    "ogd-pdf-marginalia-size",
    "ogd-pdf-header-position",
)
REQUIRED_SETTING_VALUES = (
    "ogd-pdf-preset-custom",
    "ogd-pdf-preset-prepared-confidential",
    "ogd-pdf-preset-draft-internal",
    "ogd-pdf-preset-final-end",
    "ogd-pdf-label-single",
    "ogd-pdf-label-segmented",
    "ogd-pdf-label-minimal",
    "ogd-pdf-label-bordered",
    "ogd-pdf-label-filled",
    "ogd-pdf-label-badge",
    "ogd-pdf-header-key-graphite",
    "ogd-pdf-header-key-slate",
    "ogd-pdf-header-key-sky",
    "ogd-pdf-header-key-teal",
    "ogd-pdf-header-key-mint",
    "ogd-pdf-header-key-violet",
    "ogd-pdf-header-key-rose",
    "ogd-pdf-header-key-amber",
    "ogd-pdf-header-value-graphite",
    "ogd-pdf-header-value-slate",
    "ogd-pdf-header-value-sky",
    "ogd-pdf-header-value-teal",
    "ogd-pdf-header-value-mint",
    "ogd-pdf-header-value-violet",
    "ogd-pdf-header-value-rose",
    "ogd-pdf-header-value-amber",
    "ogd-pdf-footer-key-graphite",
    "ogd-pdf-footer-key-slate",
    "ogd-pdf-footer-key-sky",
    "ogd-pdf-footer-key-teal",
    "ogd-pdf-footer-key-mint",
    "ogd-pdf-footer-key-violet",
    "ogd-pdf-footer-key-rose",
    "ogd-pdf-footer-key-amber",
    "ogd-pdf-footer-value-graphite",
    "ogd-pdf-footer-value-slate",
    "ogd-pdf-footer-value-sky",
    "ogd-pdf-footer-value-teal",
    "ogd-pdf-footer-value-mint",
    "ogd-pdf-footer-value-violet",
    "ogd-pdf-footer-value-rose",
    "ogd-pdf-footer-value-amber",
    "ogd-pdf-label-compact",
    "ogd-pdf-label-standard",
    "ogd-pdf-header-top-right",
    "ogd-pdf-header-top-center",
)
REQUIRED_IMPLEMENTED_CLASSES = (
    "ogd-pdf-preset-prepared-confidential",
    "ogd-pdf-preset-draft-internal",
    "ogd-pdf-preset-final-end",
    "ogd-pdf-label-minimal",
    "ogd-pdf-label-filled",
    "ogd-pdf-label-badge",
    "ogd-pdf-header-key-graphite",
    "ogd-pdf-header-key-slate",
    "ogd-pdf-header-key-sky",
    "ogd-pdf-header-key-teal",
    "ogd-pdf-header-key-mint",
    "ogd-pdf-header-key-violet",
    "ogd-pdf-header-key-rose",
    "ogd-pdf-header-key-amber",
    "ogd-pdf-header-value-graphite",
    "ogd-pdf-header-value-slate",
    "ogd-pdf-header-value-sky",
    "ogd-pdf-header-value-teal",
    "ogd-pdf-header-value-mint",
    "ogd-pdf-header-value-violet",
    "ogd-pdf-header-value-rose",
    "ogd-pdf-header-value-amber",
    "ogd-pdf-footer-key-graphite",
    "ogd-pdf-footer-key-slate",
    "ogd-pdf-footer-key-sky",
    "ogd-pdf-footer-key-teal",
    "ogd-pdf-footer-key-mint",
    "ogd-pdf-footer-key-violet",
    "ogd-pdf-footer-key-rose",
    "ogd-pdf-footer-key-amber",
    "ogd-pdf-footer-value-graphite",
    "ogd-pdf-footer-value-slate",
    "ogd-pdf-footer-value-sky",
    "ogd-pdf-footer-value-teal",
    "ogd-pdf-footer-value-mint",
    "ogd-pdf-footer-value-violet",
    "ogd-pdf-footer-value-rose",
    "ogd-pdf-footer-value-amber",
    "ogd-pdf-label-compact",
    "ogd-pdf-header-top-center",
)
REQUIRED_LIGHT_TOKENS = (
    "--ogd-pdf-header-text",
    "--ogd-pdf-header-value",
    "--ogd-pdf-footer-text",
    "--ogd-pdf-footer-value",
    "--ogd-pdf-marginalia-accent",
    "--ogd-pdf-marginalia-bg",
    "--ogd-pdf-marginalia-border",
    "--ogd-pdf-marginalia-shadow",
    "--ogd-pdf-header-top",
    "--ogd-pdf-header-right",
    "--ogd-pdf-header-left",
    "--ogd-pdf-header-transform",
    "--ogd-pdf-header-font-size",
    "--ogd-pdf-footer-font-size",
    "--ogd-pdf-label-letter-spacing",
    "--ogd-pdf-label-line-height",
    "--ogd-pdf-label-radius",
    "--ogd-pdf-header-pad-y",
    "--ogd-pdf-header-pad-x",
    "--ogd-pdf-footer-pad-y",
    "--ogd-pdf-footer-pad-x",
    "--ogd-pdf-footer-reserve",
    "--ogd-pdf-footer-offset",
    "--ogd-pdf-footer-max-width",
    "--ogd-pdf-segment-key-width",
    "--ogd-pdf-segment-value-width",
    "--ogd-pdf-segment-half-width",
    "--ogd-pdf-segment-key-bg",
    "--ogd-pdf-segment-key-text",
    "--ogd-pdf-segment-key-border",
    "--ogd-pdf-segment-value-bg",
    "--ogd-pdf-segment-value-text",
    "--ogd-pdf-segment-value-border",
    "--ogd-pdf-header-segment-key-bg",
    "--ogd-pdf-header-segment-key-text",
    "--ogd-pdf-header-segment-key-border",
    "--ogd-pdf-header-segment-value-bg",
    "--ogd-pdf-header-segment-value-text",
    "--ogd-pdf-header-segment-value-border",
    "--ogd-pdf-footer-segment-key-bg",
    "--ogd-pdf-footer-segment-key-text",
    "--ogd-pdf-footer-segment-key-border",
    "--ogd-pdf-footer-segment-value-bg",
    "--ogd-pdf-footer-segment-value-text",
    "--ogd-pdf-footer-segment-value-border",
)
REQUIRED_DARK_TOKENS = (
    "--ogd-pdf-marginalia-accent",
    "--ogd-pdf-marginalia-bg",
    "--ogd-pdf-marginalia-border",
    "--ogd-pdf-marginalia-shadow",
    "--ogd-pdf-segment-key-bg",
    "--ogd-pdf-segment-key-text",
    "--ogd-pdf-segment-key-border",
    "--ogd-pdf-segment-value-bg",
    "--ogd-pdf-segment-value-text",
    "--ogd-pdf-segment-value-border",
    "--ogd-pdf-header-segment-key-bg",
    "--ogd-pdf-header-segment-key-text",
    "--ogd-pdf-header-segment-key-border",
    "--ogd-pdf-header-segment-value-bg",
    "--ogd-pdf-header-segment-value-text",
    "--ogd-pdf-header-segment-value-border",
    "--ogd-pdf-footer-segment-key-bg",
    "--ogd-pdf-footer-segment-key-text",
    "--ogd-pdf-footer-segment-key-border",
    "--ogd-pdf-footer-segment-value-bg",
    "--ogd-pdf-footer-segment-value-text",
    "--ogd-pdf-footer-segment-value-border",
)
MARGIN_BOX_RE = re.compile(r"^@(top|bottom|left|right)(?:-|$)", re.I)
VIEWPORT_UNIT_RE = re.compile(r"(?:^|[^a-zA-Z-])-?\d*\.?\d+v(?:h|w|min|max)\b", re.I)


@dataclass(frozen=True)
class CssRule:
    path: Path
    selector: str
    body: str
    at_context: str
    line: int


@dataclass(frozen=True)
class AtBlock:
    path: Path
    header: str
    at_context: str
    line: int


def normalize_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def strip_comments(css: str) -> str:
    def replace(match: re.Match[str]) -> str:
        return "\n" * match.group(0).count("\n")

    return re.sub(r"/\*.*?\*/", replace, css, flags=re.S)


def declarations(body: str) -> dict[str, str]:
    parsed: dict[str, str] = {}
    for raw_declaration in body.split(";"):
        if ":" not in raw_declaration:
            continue
        property_name, _, value = raw_declaration.partition(":")
        parsed[property_name.strip().lower()] = value.strip()
    return parsed


def tokenize_css(path: Path, css: str) -> tuple[list[CssRule], list[AtBlock]]:
    rules: list[CssRule] = []
    at_blocks: list[AtBlock] = []

    def walk(fragment: str, line_offset: int, at_stack: list[str]) -> None:
        index = 0
        line_number = 1
        css_length = len(fragment)
        while index < css_length:
            if fragment.startswith("/*", index):
                comment_end = fragment.find("*/", index + 2)
                if comment_end == -1:
                    return
                line_number += fragment.count("\n", index, comment_end + 2)
                index = comment_end + 2
                continue
            current_char = fragment[index]
            if current_char.isspace():
                if current_char == "\n":
                    line_number += 1
                index += 1
                continue
            if current_char == "@":
                header_start = index
                while index < css_length and fragment[index] not in "{;":
                    if fragment[index] == "\n":
                        line_number += 1
                    index += 1
                if index >= css_length:
                    return
                if fragment[index] == ";":
                    index += 1
                    continue
                header = normalize_ws(fragment[header_start:index])
                absolute_line = line_offset + line_number - 1
                at_blocks.append(AtBlock(path, header, " >> ".join(at_stack), absolute_line))
                block_start = index + 1
                index = block_start
                depth = 1
                while index < css_length and depth > 0:
                    if fragment.startswith("/*", index):
                        comment_end = fragment.find("*/", index + 2)
                        if comment_end == -1:
                            return
                        line_number += fragment.count("\n", index, comment_end + 2)
                        index = comment_end + 2
                        continue
                    if fragment[index] == "{":
                        depth += 1
                    elif fragment[index] == "}":
                        depth -= 1
                        if depth == 0:
                            break
                    if fragment[index] == "\n":
                        line_number += 1
                    index += 1
                inner_css = fragment[block_start:index]
                inner_line_offset = line_offset + fragment.count("\n", 0, block_start)
                walk(inner_css, inner_line_offset, [*at_stack, header])
                index += 1
                continue
            selector_start = index
            while index < css_length:
                if fragment.startswith("/*", index):
                    comment_end = fragment.find("*/", index + 2)
                    if comment_end == -1:
                        return
                    line_number += fragment.count("\n", index, comment_end + 2)
                    index = comment_end + 2
                    continue
                if fragment[index] in "{}":
                    break
                index += 1
            if index >= css_length or fragment[index] != "{":
                index += 1
                continue
            selector = normalize_ws(fragment[selector_start:index])
            rule_line = line_offset + line_number - 1
            body_start = index + 1
            index = body_start
            depth = 1
            while index < css_length and depth > 0:
                if fragment.startswith("/*", index):
                    comment_end = fragment.find("*/", index + 2)
                    if comment_end == -1:
                        return
                    line_number += fragment.count("\n", index, comment_end + 2)
                    index = comment_end + 2
                    continue
                if fragment[index] == "{":
                    depth += 1
                elif fragment[index] == "}":
                    depth -= 1
                    if depth == 0:
                        break
                if fragment[index] == "\n":
                    line_number += 1
                index += 1
            body = normalize_ws(fragment[body_start:index])
            if selector and body:
                rules.append(CssRule(path, selector, body, " >> ".join(at_stack), rule_line))
            index += 1

    walk(css, 1, [])
    return rules, at_blocks


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def location(path: Path, line: int) -> str:
    return f"{rel(path)}:{line}"


def has_body_class(selector: str, class_name: str) -> bool:
    return re.search(rf"\bbody(?=[^{{,]*\.{re.escape(class_name)}\b)", selector) is not None


def require_substring(failures: list[str], text: str, token: str, label: str) -> None:
    if token not in text:
        failures.append(f"missing {label}: `{token}`")


def audit_settings_and_tokens(failures: list[str]) -> None:
    settings_text = STYLE_SETTINGS.read_text(encoding="utf-8")
    owner_text = PDF_OWNER.read_text(encoding="utf-8")
    light_text = LIGHT_TOKENS.read_text(encoding="utf-8")
    dark_text = DARK_TOKENS.read_text(encoding="utf-8")
    for setting_id in REQUIRED_SETTING_IDS:
        if not re.search(rf"\bid:\s*{re.escape(setting_id)}\b", settings_text):
            failures.append(f"missing Style Settings id `{setting_id}` in {rel(STYLE_SETTINGS)}")
    for setting_value in REQUIRED_SETTING_VALUES:
        if not re.search(rf"\bvalue:\s*{re.escape(setting_value)}\b", settings_text):
            failures.append(f"missing Style Settings value `{setting_value}` in {rel(STYLE_SETTINGS)}")
    for class_name in REQUIRED_IMPLEMENTED_CLASSES:
        if not re.search(rf"\bbody(?:\.[\w-]+)*\.{re.escape(class_name)}\b", owner_text):
            failures.append(f"missing PDF marginalia implementation class `body.{class_name}` in {rel(PDF_OWNER)}")
    for token in REQUIRED_LIGHT_TOKENS:
        require_substring(failures, light_text, token, f"light token in {rel(LIGHT_TOKENS)}")
    for token in REQUIRED_DARK_TOKENS:
        require_substring(failures, dark_text, token, f"dark token in {rel(DARK_TOKENS)}")


def audit_at_rules(failures: list[str], at_blocks: list[AtBlock], uncommented_sources: dict[Path, str]) -> None:
    for block in at_blocks:
        header = block.header.lower()
        if header.startswith("@page"):
            if block.path != PAGE_OWNER:
                failures.append(f"{location(block.path, block.line)}: @page is owned by {rel(PAGE_OWNER)}")
            if "@media print" not in block.at_context.lower():
                failures.append(f"{location(block.path, block.line)}: @page must be nested under @media print")
        if MARGIN_BOX_RE.match(header):
            failures.append(f"{location(block.path, block.line)}: forbidden @page margin box `{block.header}`")
    for path, css in uncommented_sources.items():
        for pattern, label in (
            (r"\bstring-set\b", "string-set"),
            (r"\bcontent\s*\(", "CSS content() function"),
        ):
            match = re.search(pattern, css, flags=re.I)
            if match:
                line = css.count("\n", 0, match.start()) + 1
                failures.append(f"{location(path, line)}: forbidden PDF-fragile primitive `{label}`")


def audit_pdf_rules(failures: list[str], rules: list[CssRule]) -> None:
    header_rules: list[CssRule] = []
    header_segment_rules: list[CssRule] = []
    header_value_rules: list[CssRule] = []
    footer_rules: list[CssRule] = []
    footer_segment_rules: list[CssRule] = []
    footer_value_rules: list[CssRule] = []
    footer_reserve_rules: list[CssRule] = []
    for rule in rules:
        selector = rule.selector
        body = rule.body
        mentions_header_toggle = has_body_class(selector, "ogd-pdf-header-enabled")
        mentions_footer_toggle = has_body_class(selector, "ogd-pdf-footer-enabled")
        mentions_pdf_toggle = mentions_header_toggle or mentions_footer_toggle
        mentions_pdf_token = "--ogd-pdf-" in body or "--ogd-pdf-" in selector
        if mentions_pdf_toggle and rule.path != PDF_OWNER:
            failures.append(f"{location(rule.path, rule.line)}: PDF marginalia selector is owned by {rel(PDF_OWNER)}")
        if mentions_pdf_toggle and "@media print" not in rule.at_context.lower():
            failures.append(f"{location(rule.path, rule.line)}: PDF marginalia selector must be inside @media print")
        if "markdown-source-view.mod-cm6" in selector and (mentions_pdf_toggle or mentions_pdf_token):
            failures.append(f"{location(rule.path, rule.line)}: PDF marginalia must not target Live Preview / CM6")
        if mentions_pdf_toggle:
            declarations_map = declarations(body)
            if "!important" in body:
                failures.append(f"{location(rule.path, rule.line)}: !important is forbidden in PDF marginalia")
            if VIEWPORT_UNIT_RE.search(body):
                failures.append(f"{location(rule.path, rule.line)}: viewport units are forbidden in PDF marginalia")
            if re.search(r"::(?:first-line|marker)\b", selector):
                failures.append(f"{location(rule.path, rule.line)}: forbidden pseudo in PDF marginalia selector")
            for property_name, value in declarations_map.items():
                if property_name in ("backdrop-filter", "-webkit-backdrop-filter"):
                    failures.append(f"{location(rule.path, rule.line)}: backdrop-filter is forbidden in PDF output")
                if property_name == "position" and value.split()[0].lower() == "fixed":
                    failures.append(f"{location(rule.path, rule.line)}: position: fixed is forbidden in PDF marginalia")
                if property_name == "display" and "list-item" in value:
                    failures.append(f"{location(rule.path, rule.line)}: list-item trick is forbidden in PDF marginalia")
                if property_name.startswith("list-style"):
                    failures.append(f"{location(rule.path, rule.line)}: list-style trick is forbidden in PDF marginalia")
                if property_name == "content" and "\\A" in value:
                    failures.append(f"{location(rule.path, rule.line)}: multiline generated content is forbidden in PDF marginalia")
            if mentions_header_toggle and "::before" in selector and "content" in declarations_map:
                if "--ogd-pdf-header-value" in declarations_map.get("content", ""):
                    header_value_rules.append(rule)
                else:
                    header_rules.append(rule)
            if mentions_header_toggle and "::after" in selector and "content" in declarations_map:
                header_segment_rules.append(rule)
            if mentions_footer_toggle and "::after" in selector and "content" in declarations_map:
                if "--ogd-pdf-footer-value" in declarations_map.get("content", ""):
                    footer_value_rules.append(rule)
                else:
                    footer_rules.append(rule)
            if mentions_footer_toggle and "::before" in selector and "content" in declarations_map:
                footer_segment_rules.append(rule)
            if mentions_footer_toggle and "::before" not in selector and "::after" not in selector:
                footer_reserve_rules.append(rule)

    if len(header_rules) != 1:
        failures.append(f"expected exactly one PDF header anchor pseudo; found {len(header_rules)}")
    else:
        require_anchor_contract(failures, header_rules[0], "--ogd-pdf-header-text")
    if len(footer_rules) != 1:
        failures.append(f"expected exactly one PDF footer anchor pseudo; found {len(footer_rules)}")
    else:
        require_anchor_contract(failures, footer_rules[0], "--ogd-pdf-footer-text")
    if len(footer_reserve_rules) != 1:
        failures.append(f"expected exactly one PDF footer reserve rule; found {len(footer_reserve_rules)}")
    else:
        reserve_declarations = declarations(footer_reserve_rules[0].body)
        margin_bottom = reserve_declarations.get("margin-bottom", "")
        if "mm" not in margin_bottom:
            failures.append(f"{location(footer_reserve_rules[0].path, footer_reserve_rules[0].line)}: footer reserve must use mm margin-bottom")
    if len(header_segment_rules) != 1:
        failures.append(f"expected exactly one PDF header segmented key pseudo; found {len(header_segment_rules)}")
    else:
        require_anchor_contract(failures, header_segment_rules[0], "--ogd-pdf-header-text", check_geometry=False)
    if len(header_value_rules) != 1:
        failures.append(f"expected exactly one PDF header segmented value override; found {len(header_value_rules)}")
    if len(footer_segment_rules) != 1:
        failures.append(f"expected exactly one PDF footer segmented key pseudo; found {len(footer_segment_rules)}")
    else:
        require_anchor_contract(failures, footer_segment_rules[0], "--ogd-pdf-footer-text", check_geometry=False)
    if len(footer_value_rules) != 1:
        failures.append(f"expected exactly one PDF footer segmented value override; found {len(footer_value_rules)}")


def require_anchor_contract(failures: list[str], rule: CssRule, text_token: str, check_geometry: bool = True) -> None:
    decl = declarations(rule.body)
    expected_exact = {
        "position": "absolute",
        "pointer-events": "none",
        "display": "inline-block",
        "white-space": "nowrap",
        "overflow": "hidden",
        "text-overflow": "ellipsis",
        "font-style": "normal",
    }
    for property_name, expected_value in expected_exact.items():
        actual = decl.get(property_name, "").split()[0].lower() if decl.get(property_name) else ""
        if actual != expected_value:
            failures.append(f"{location(rule.path, rule.line)}: expected `{property_name}: {expected_value}`")
    content = decl.get("content", "")
    if normalize_ws(content) != f'var({text_token}, "")':
        failures.append(f"{location(rule.path, rule.line)}: content must be `var({text_token}, \"\")`")
    if "exact" not in decl.get("print-color-adjust", "") or "exact" not in decl.get("-webkit-print-color-adjust", ""):
        failures.append(f"{location(rule.path, rule.line)}: both print-color-adjust properties must be exact")
    if not check_geometry:
        return
    if text_token == "--ogd-pdf-header-text":
        expected_header_values = {
            "top": "var(--ogd-pdf-header-top, 11mm)",
            "right": "var(--ogd-pdf-header-right, 13mm)",
            "left": "var(--ogd-pdf-header-left, auto)",
            "transform": "var(--ogd-pdf-header-transform, none)",
        }
        for property_name, expected_value in expected_header_values.items():
            if normalize_ws(decl.get(property_name, "")) != expected_value:
                failures.append(f"{location(rule.path, rule.line)}: header must keep `{property_name}: {expected_value}`")
    if text_token == "--ogd-pdf-footer-text":
        expected_footer_values = {
            "left": "50%",
            "bottom": "var(--ogd-pdf-footer-offset, -22mm)",
            "transform": "translateX(-50%)",
            "max-width": "var(--ogd-pdf-footer-max-width, 90%)",
        }
        for property_name, expected_value in expected_footer_values.items():
            if normalize_ws(decl.get(property_name, "")) != expected_value:
                failures.append(f"{location(rule.path, rule.line)}: footer must keep `{property_name}: {expected_value}`")


def main() -> int:
    failures: list[str] = []
    rules: list[CssRule] = []
    at_blocks: list[AtBlock] = []
    uncommented_sources: dict[Path, str] = {}
    for css_path in sorted(SRC_DIR.rglob("*.css")):
        css = css_path.read_text(encoding="utf-8")
        module_rules, module_at_blocks = tokenize_css(css_path, css)
        rules.extend(module_rules)
        at_blocks.extend(module_at_blocks)
        uncommented_sources[css_path] = strip_comments(css)

    audit_settings_and_tokens(failures)
    audit_at_rules(failures, at_blocks, uncommented_sources)
    audit_pdf_rules(failures, rules)

    if failures:
        print("FAIL: PDF header/footer contract violations:")
        for failure in failures:
            print(f"  - {failure}")
        return 1
    print("OK: PDF header/footer contract clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())