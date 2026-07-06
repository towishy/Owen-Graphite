#!/usr/bin/env python3
"""Audit CSS compatibility and bundle budget guardrails."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
THEME = ROOT / "theme.css"
SRC_DIR = ROOT / "src"
MAX_THEME_LINES = 19_900
MAX_THEME_BYTES = 1_010_000
ALLOWED_SCROLLBAR_GUTTER_VALUE = "stable both-edges"
MAX_RAW_AQUA_RGBA = 182
RAW_AQUA_RGBA_PATTERNS = (
    re.compile(r"rgba\(125,\s*211,\s*252"),
    re.compile(r"rgba\(186,\s*230,\s*253"),
    re.compile(r"rgba\(56,\s*189,\s*248"),
    re.compile(r"rgba\(103,\s*232,\s*249"),
)

COMMENT_RE = re.compile(r"/\*.*?\*/", re.DOTALL)
DECL_RE = re.compile(r"(?P<prop>[a-zA-Z-]+)\s*:\s*(?P<value>[^;{}]+);")


def strip_comments(text: str) -> str:
    return COMMENT_RE.sub("", text)


def src_css_text() -> str:
    return "\n".join(path.read_text(encoding="utf-8") for path in sorted(SRC_DIR.rglob("*.css")))


def main() -> int:
    try:
        if not THEME.exists():
            raise FileNotFoundError("theme.css is missing")
        theme = THEME.read_text(encoding="utf-8")
        src = src_css_text()
        clean_theme = strip_comments(theme)
        clean_src = strip_comments(src)

        line_count = theme.count("\n") + 1
        byte_count = len(theme.encode("utf-8"))
        if line_count > MAX_THEME_LINES:
            raise AssertionError(f"theme.css line budget exceeded: {line_count} > {MAX_THEME_LINES}")
        if byte_count > MAX_THEME_BYTES:
            raise AssertionError(f"theme.css byte budget exceeded: {byte_count} > {MAX_THEME_BYTES}")

        if "!important" in clean_src:
            raise AssertionError("src/ contains declaration-level !important outside comments")
        if "@layer" in clean_src:
            raise AssertionError("src/ contains @layer outside comments; v3 must remain unlayered")
        if "@import" in clean_theme:
            raise AssertionError("theme.css still contains @import outside comments; bundle should inline imports")

        raw_aqua_rgba_count = sum(len(pattern.findall(clean_src)) for pattern in RAW_AQUA_RGBA_PATTERNS)
        if raw_aqua_rgba_count > MAX_RAW_AQUA_RGBA:
            raise AssertionError(
                f"raw aqua rgba budget exceeded: {raw_aqua_rgba_count} > {MAX_RAW_AQUA_RGBA}; "
                "prefer semantic --ogd-rim-* / --ogd-surface-tint-* tokens"
            )

        scrollbar_matches = [match.group("value").strip() for match in DECL_RE.finditer(clean_theme) if match.group("prop") == "scrollbar-gutter"]
        unexpected_scrollbar = [value for value in scrollbar_matches if value != ALLOWED_SCROLLBAR_GUTTER_VALUE]
        if unexpected_scrollbar:
            raise AssertionError("unexpected scrollbar-gutter values: " + ", ".join(unexpected_scrollbar))
        if len(scrollbar_matches) > 1:
            raise AssertionError(f"scrollbar-gutter exception budget exceeded: {len(scrollbar_matches)} > 1")

        unsupported_print_values: list[str] = []
        for match in DECL_RE.finditer(clean_theme):
            prop = match.group("prop")
            value = match.group("value").strip()
            if prop in {"break-before", "break-after"} and value == "avoid-page":
                unsupported_print_values.append(f"{prop}: {value}")
        if unsupported_print_values:
            raise AssertionError("unsupported print break values found: " + ", ".join(sorted(set(unsupported_print_values))))

        print(
            "OK: CSS compatibility budget passed "
            f"({line_count} lines, {byte_count} bytes, scrollbar-gutter exceptions={len(scrollbar_matches)}, "
            f"raw aqua rgba={raw_aqua_rgba_count}/{MAX_RAW_AQUA_RGBA})"
        )
        return 0
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
