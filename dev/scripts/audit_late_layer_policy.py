#!/usr/bin/env python3
"""Audit the late polish layer freeze policy.

The protected `src/polish/*` modules are allowed to contain the current
baseline debt, but new selectors or new properties on existing selectors must
be declared as explicit exceptions. This keeps direct-owner migrations from
quietly accumulating another late override layer.

Usage:
    python dev/scripts/audit_late_layer_policy.py --write-baseline
    python dev/scripts/audit_late_layer_policy.py
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
POLICY_PATH = ROOT / "dev" / "MAP" / "late-layer-policy.json"


def normalize_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def strip_comments(css: str) -> str:
    def replace(match: re.Match[str]) -> str:
        return "\n" * match.group(0).count("\n")

    return re.sub(r"/\*.*?\*/", replace, css, flags=re.S)


def tokenize_blocks(css: str):
    css = strip_comments(css)
    index = 0
    length = len(css)
    line_number = 1
    at_stack: list[str] = []

    while index < length:
        ch = css[index]
        if ch.isspace():
            if ch == "\n":
                line_number += 1
            index += 1
            continue
        if ch == "@":
            header_start = index
            while index < length and css[index] not in "{;":
                if css[index] == "\n":
                    line_number += 1
                index += 1
            if index >= length:
                return
            if css[index] == ";":
                index += 1
                continue
            header = normalize_ws(css[header_start:index])
            at_stack.append(header)
            block_start = index + 1
            index = block_start
            depth = 1
            while index < length and depth > 0:
                if css[index] == "{":
                    depth += 1
                elif css[index] == "}":
                    depth -= 1
                    if depth == 0:
                        break
                if css[index] == "\n":
                    line_number += 1
                index += 1
            inner = css[block_start:index]
            inner_start_line = css.count("\n", 0, block_start) + 1
            for selector, body, ctx, sub_line in tokenize_blocks(inner):
                context = " >> ".join([*at_stack, *([ctx] if ctx else [])])
                yield selector, body, context, inner_start_line + sub_line - 1
            at_stack.pop()
            index += 1
            continue
        selector_start = index
        while index < length and css[index] not in "{}":
            index += 1
        if index >= length or css[index] != "{":
            index += 1
            continue
        selector = normalize_ws(css[selector_start:index])
        body_start = index + 1
        index = body_start
        depth = 1
        while index < length and depth > 0:
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
            yield selector, body, " >> ".join(at_stack), line_number
        index += 1


def declarations(body: str) -> dict[str, str]:
    parsed: dict[str, str] = {}
    for raw in body.split(";"):
        if ":" not in raw:
            continue
        prop, _, value = raw.partition(":")
        parsed[prop.strip().lower()] = value.strip()
    return parsed


def read_policy() -> dict[str, Any]:
    return json.loads(POLICY_PATH.read_text(encoding="utf-8"))


def snapshot(policy: dict[str, Any]) -> dict[str, Any]:
    modules: dict[str, Any] = {}
    for rel in policy["protectedModules"]:
        path = ROOT / rel
        if not path.is_file():
            raise FileNotFoundError(f"protected module missing: {rel}")
        selectors: dict[str, Any] = {}
        for selector, body, at_context, line in tokenize_blocks(path.read_text(encoding="utf-8")):
            key = f"{at_context} :: {selector}" if at_context else selector
            entry = selectors.setdefault(key, {"selector": selector, "atContext": at_context, "lines": [], "properties": {}})
            entry["lines"].append(line)
            for prop, value in declarations(body).items():
                entry["properties"].setdefault(prop, value)
        modules[rel] = {"selectorCount": len(selectors), "selectors": selectors}
    return {"schema": "owen-graphite/late-layer-baseline/1", "modules": modules}


def exception_keys(policy: dict[str, Any]) -> set[tuple[str, str, str]]:
    path = ROOT / policy["exceptions"]
    payload = json.loads(path.read_text(encoding="utf-8"))
    keys: set[tuple[str, str, str]] = set()
    for index, item in enumerate(payload.get("exceptions", []), start=1):
        missing = [key for key in ("module", "selector", "property", "reason", "owner", "expiresWhen") if not item.get(key)]
        if missing:
            raise AssertionError(f"exception #{index} missing required fields: {', '.join(missing)}")
        keys.add((str(item["module"]), str(item["selector"]), str(item["property"]).lower()))
    return keys


def audit(policy: dict[str, Any]) -> int:
    baseline_path = ROOT / policy["baseline"]
    if not baseline_path.is_file():
        raise FileNotFoundError(f"missing late-layer baseline: {baseline_path.relative_to(ROOT)}; run --write-baseline")
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    current = snapshot(policy)
    exceptions = exception_keys(policy)
    failures: list[str] = []

    for module, module_payload in current["modules"].items():
        base_selectors = baseline.get("modules", {}).get(module, {}).get("selectors", {})
        current_selectors = module_payload["selectors"]
        for selector_key, selector_payload in current_selectors.items():
            if selector_key not in base_selectors:
                if (module, selector_key, "*") not in exceptions:
                    failures.append(f"new late selector in {module}: {selector_key}")
                continue
            base_props = set(base_selectors[selector_key].get("properties", {}))
            current_props = set(selector_payload.get("properties", {}))
            for prop in sorted(current_props - base_props):
                if (module, selector_key, prop) not in exceptions and (module, selector_key, "*") not in exceptions:
                    failures.append(f"new late property in {module}: {selector_key} :: {prop}")

    if failures:
        print(f"FAIL: late layer policy violations ({len(failures)})")
        for failure in failures[:80]:
            print(f"  - {failure}")
        if len(failures) > 80:
            print(f"  ... (+{len(failures) - 80} more)")
        return 1
    protected_count = len(policy["protectedModules"])
    selector_count = sum(int(module["selectorCount"]) for module in current["modules"].values())
    print(f"OK: late layer policy clean ({protected_count} modules, {selector_count} baseline selectors)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-baseline", action="store_true", help="Write the current protected modules as the frozen baseline.")
    args = parser.parse_args()
    try:
        policy = read_policy()
        if args.write_baseline:
            baseline = snapshot(policy)
            path = ROOT / policy["baseline"]
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(baseline, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            selector_count = sum(int(module["selectorCount"]) for module in baseline["modules"].values())
            print(f"OK: wrote {path.relative_to(ROOT)} ({selector_count} selectors)")
            return 0
        return audit(policy)
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())