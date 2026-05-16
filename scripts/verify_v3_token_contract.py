#!/usr/bin/env python3
"""Verify that the v3 token contract is satisfied by src/tokens/.

Compares the set of `--ogd-*` tokens declared globally in v3 src/tokens/
against the v2.30.14 set declared globally in dev/*.css. "Globally" means
inside `:root` (light) or a non-descendant selector that mentions
`.theme-dark` (dark). Descendant-context dark overrides (inside `.callout`,
table cells, etc.) belong to later steps and are not compared here.

Exits with code 0 when the contract holds, 1 otherwise.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEV = ROOT / "dev"
SRC_TOKENS = ROOT / "src" / "tokens"

DECL_RE = re.compile(
    r"(--ogd-[a-z0-9-]+)\s*:\s*([^;{}]+?)\s*(?:!important)?\s*;",
    re.IGNORECASE | re.DOTALL,
)


def normalize_value(value: str) -> str:
    return " ".join(value.split())


def is_global_light_root(selector: str) -> bool:
    return selector.strip() == ":root"


def is_global_theme_dark(selector: str) -> bool:
    s = selector.strip()
    if not s or any(ch.isspace() for ch in s):
        return False
    if any(ch in s for ch in (">", "+", "~")):
        return False
    return ".theme-dark" in s


def iter_blocks(css: str):
    i = 0
    n = len(css)
    while i < n:
        if css.startswith("/*", i):
            j = css.find("*/", i + 2)
            if j == -1:
                return
            i = j + 2
            continue
        ch = css[i]
        if ch.isspace():
            i += 1
            continue
        if ch == "@":
            j = i
            while j < n and css[j] not in ";{":
                j += 1
            if j >= n:
                return
            if css[j] == ";":
                i = j + 1
                continue
            depth = 1
            i = j + 1
            block_start = i
            while i < n and depth > 0:
                if css.startswith("/*", i):
                    end = css.find("*/", i + 2)
                    if end == -1:
                        return
                    i = end + 2
                    continue
                c = css[i]
                if c == "{":
                    depth += 1
                elif c == "}":
                    depth -= 1
                    if depth == 0:
                        break
                i += 1
            inner = css[block_start:i]
            for s, b in iter_blocks(inner):
                yield s, b
            i += 1
            continue
        sel_start = i
        while i < n and css[i] != "{":
            if css.startswith("/*", i):
                end = css.find("*/", i + 2)
                if end == -1:
                    return
                i = end + 2
                continue
            if css[i] == "}":
                i += 1
                continue
            i += 1
        if i >= n:
            return
        selector = " ".join(css[sel_start:i].split())
        i += 1
        body_start = i
        depth = 1
        while i < n and depth > 0:
            if css.startswith("/*", i):
                end = css.find("*/", i + 2)
                if end == -1:
                    return
                i = end + 2
                continue
            c = css[i]
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    break
            i += 1
        yield selector, css[body_start:i]
        i += 1


def split_selector_list(selector: str) -> list[str]:
    parts: list[str] = []
    depth = 0
    current: list[str] = []
    for ch in selector:
        if ch == "(":
            depth += 1
            current.append(ch)
        elif ch == ")":
            depth = max(0, depth - 1)
            current.append(ch)
        elif ch == "," and depth == 0:
            parts.append("".join(current).strip())
            current = []
        else:
            current.append(ch)
    if current:
        parts.append("".join(current).strip())
    return [p for p in parts if p]


def collect_v3_defaults() -> tuple[dict[str, str], dict[str, str]]:
    return collect_global_defaults(sorted(SRC_TOKENS.glob("*.css")))


def collect_baseline_defaults() -> tuple[dict[str, str], dict[str, str]]:
    return collect_global_defaults(sorted(DEV.glob("*.css")))


def collect_global_defaults(css_paths: list[Path]) -> tuple[dict[str, str], dict[str, str]]:
    light: dict[str, str] = {}
    dark: dict[str, str] = {}
    for css_path in css_paths:
        text = css_path.read_text(encoding="utf-8")
        for raw_selector, body in iter_blocks(text):
            for sub in split_selector_list(raw_selector):
                if is_global_light_root(sub):
                    for m in DECL_RE.finditer(body):
                        name = m.group(1)
                        if name not in light:
                            light[name] = normalize_value(m.group(2))
                elif is_global_theme_dark(sub):
                    for m in DECL_RE.finditer(body):
                        name = m.group(1)
                        if name not in dark:
                            dark[name] = normalize_value(m.group(2))
    return light, dark


def main() -> int:
    baseline_light, baseline_dark = collect_baseline_defaults()
    v3_light, v3_dark = collect_v3_defaults()
    v3_all = set(v3_light) | set(v3_dark)

    failures: list[str] = []
    light_missing = sorted(set(baseline_light) - set(v3_light))
    light_changed = sorted(
        name for name in set(baseline_light) & set(v3_light)
        if baseline_light[name] != v3_light[name]
    )
    dark_missing = sorted(set(baseline_dark) - set(v3_dark))
    dark_changed = sorted(
        name for name in set(baseline_dark) & set(v3_dark)
        if baseline_dark[name] != v3_dark[name]
    )

    for name in light_missing:
        failures.append(f"LIGHT MISSING: {name}  (baseline: {baseline_light[name]!r})")
    for name in light_changed:
        failures.append(
            f"LIGHT CHANGED: {name}\n  baseline: {baseline_light[name]!r}\n  v3:       {v3_light[name]!r}"
        )
    for name in dark_missing:
        failures.append(f"DARK MISSING: {name}  (baseline: {baseline_dark[name]!r})")
    for name in dark_changed:
        failures.append(
            f"DARK CHANGED: {name}\n  baseline: {baseline_dark[name]!r}\n  v3:       {v3_dark[name]!r}"
        )

    print(f"v2.30.14 baseline tokens (light defaults): {len(baseline_light)}")
    print(f"v2.30.14 baseline tokens (dark defaults):  {len(baseline_dark)}")
    print(f"v3 src/tokens light defaults:              {len(v3_light)}")
    print(f"v3 src/tokens dark defaults:               {len(v3_dark)}")

    if failures:
        print(f"FAIL: {len(failures)} contract violations")
        for f in failures[:60]:
            print(f)
        if len(failures) > 60:
            print(f"... (+{len(failures) - 60} more) ...")
        return 1
    print("OK: v3 src/tokens contract satisfied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
