"""Extract CSS custom property (--ogd-*) inventory from the v2.30.14 bundle.

Produces docs/v3/token-inventory.md and docs/v3/token-inventory.json:
- list of every `--ogd-*` token defined in dev/*.css
- where each token is defined (file, line, selector context)
- where each token is consumed (var(--ogd-*) reference)
- light-default value (root scope)
- dark-default value (.theme-dark scope when present)

Read-only. Never mutates source. Used as the v3 token contract: the
v3-rewrite must declare exactly the same token names and resolve to
identical default values so the existing dev/* output is reproducible.
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEV = ROOT / "dev"
OUT_DIR = ROOT / "docs" / "v3"
OUT_DIR.mkdir(parents=True, exist_ok=True)


TOKEN_RE = re.compile(r"--ogd-[a-z0-9-]+", re.IGNORECASE)
DECL_RE = re.compile(
    r"(--ogd-[a-z0-9-]+)\s*:\s*([^;{}]+?)\s*(?:!important)?\s*;",
    re.IGNORECASE,
)


def iter_blocks(css: str):
    """Yield (selector, body, line) blocks at depth 0 (ignoring @-rule nesting).

    For token inventory we only care about declaration context, so this
    simplified walker is enough.
    """
    i = 0
    n = len(css)
    line = 1
    while i < n:
        if css.startswith("/*", i):
            j = css.find("*/", i + 2)
            if j == -1:
                return
            line += css.count("\n", i, j + 2)
            i = j + 2
            continue
        ch = css[i]
        if ch.isspace():
            if ch == "\n":
                line += 1
            i += 1
            continue
        if ch == "@":
            # Skip the at-rule header up to `{` or `;` keeping the depth tracker simple
            j = i
            while j < n and css[j] not in ";{":
                if css[j] == "\n":
                    line += 1
                j += 1
            if j >= n:
                return
            if css[j] == ";":
                i = j + 1
                continue
            # at-rule with block — open it, walk inside, close
            depth = 1
            line += css.count("\n", i, j + 1)
            i = j + 1
            block_start = i
            while i < n and depth > 0:
                if css.startswith("/*", i):
                    end = css.find("*/", i + 2)
                    if end == -1:
                        return
                    line += css.count("\n", i, end + 2)
                    i = end + 2
                    continue
                c = css[i]
                if c == "{":
                    depth += 1
                elif c == "}":
                    depth -= 1
                    if depth == 0:
                        break
                if c == "\n":
                    line += 1
                i += 1
            inner = css[block_start:i]
            for sub_sel, sub_body, sub_line in iter_blocks(inner):
                yield sub_sel, sub_body, sub_line
            i += 1
            continue
        # plain selector { body }
        sel_start = i
        sel_line = line
        while i < n and css[i] != "{":
            if css.startswith("/*", i):
                end = css.find("*/", i + 2)
                if end == -1:
                    return
                line += css.count("\n", i, end + 2)
                i = end + 2
                continue
            if css[i] == "\n":
                line += 1
            elif css[i] == "}":
                # stray
                i += 1
                continue
            i += 1
        if i >= n:
            return
        selector = " ".join(css[sel_start:i].split())
        i += 1  # past {
        body_start = i
        depth = 1
        while i < n and depth > 0:
            if css.startswith("/*", i):
                end = css.find("*/", i + 2)
                if end == -1:
                    return
                line += css.count("\n", i, end + 2)
                i = end + 2
                continue
            c = css[i]
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    break
            if c == "\n":
                line += 1
            i += 1
        body = css[body_start:i]
        yield selector, body, sel_line
        i += 1


def main() -> None:
    definitions: dict[str, list[dict]] = defaultdict(list)
    usages: dict[str, list[dict]] = defaultdict(list)
    light_default: dict[str, str] = {}
    dark_default: dict[str, str] = {}

    for css_path in sorted(DEV.glob("*.css")):
        text = css_path.read_text(encoding="utf-8")
        # Token definitions
        for selector, body, line in iter_blocks(text):
            for m in DECL_RE.finditer(body):
                name = m.group(1)
                value = " ".join(m.group(2).split())
                definitions[name].append(
                    {
                        "file": css_path.name,
                        "line": line,
                        "selector": selector[:160],
                        "value": value,
                    }
                )
                if selector == ":root" and name not in light_default:
                    light_default[name] = value
                if (
                    ".theme-dark" in selector
                    and "html" not in selector
                    and name not in dark_default
                ):
                    dark_default[name] = value
        # Token usages (var references)
        for m in TOKEN_RE.finditer(text):
            name = m.group(0)
            line_no = text.count("\n", 0, m.start()) + 1
            # heuristic: usages are when token name appears inside `var(...)` or
            # as part of a value other than a declaration LHS
            # We accept any non-declaration occurrence as a usage signal
            window = text[max(0, m.start() - 4): m.end() + 1]
            if not window.startswith(("--ogd",)):
                usages[name].append({"file": css_path.name, "line": line_no})

    all_tokens = sorted(set(definitions) | set(usages))

    inventory = []
    for name in all_tokens:
        defs = definitions.get(name, [])
        uses = usages.get(name, [])
        inventory.append(
            {
                "token": name,
                "definitions": defs,
                "usage_count": len(uses),
                "light_default": light_default.get(name),
                "dark_default": dark_default.get(name),
                "first_usage": uses[0] if uses else None,
            }
        )

    json_out = OUT_DIR / "token-inventory.json"
    json_out.write_text(
        json.dumps(inventory, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    md_lines = [
        "# v3 Token Inventory (extracted from v2.30.14)",
        "",
        "이 문서는 `scripts/extract_token_inventory.py`가 자동 생성합니다.",
        "v3-rewrite는 아래 모든 토큰 이름을 동일하게 선언하고, light/dark default 값이 일치해야 합니다.",
        "",
        f"- 총 토큰: **{len(all_tokens)}**",
        f"- light(`:root`) default 정의: **{len(light_default)}**",
        f"- dark(`.theme-dark`) default 정의: **{len(dark_default)}**",
        "",
        "## 카테고리 분류",
        "",
        "| prefix | 추정 책임 |",
        "| --- | --- |",
        "| `--ogd-glass-*` | Liquid Glass surface (rest/hover/active/disabled) |",
        "| `--ogd-table-*` | 표 surface tokens |",
        "| `--ogd-callout-*` | callout surface tokens |",
        "| `--ogd-text-*` | 텍스트 색 토큰 |",
        "| `--ogd-line-*`, `--ogd-border-*` | 분리선·테두리 |",
        "| `--ogd-radius-*` | radius scale |",
        "| `--ogd-shadow-*` | shadow scale |",
        "| `--ogd-last-page-footer-*` | PDF 마지막 페이지 footer |",
        "| 기타 `--ogd-*` | feature-specific |",
        "",
        "## 토큰 목록 (light default | dark default | 사용 횟수 | 정의 위치 수)",
        "",
        "| token | light default | dark default | uses | defs |",
        "| --- | --- | --- | ---: | ---: |",
    ]
    for item in inventory:
        light = item["light_default"] or "—"
        dark = item["dark_default"] or "—"
        if len(light) > 80:
            light = light[:77] + "…"
        if len(dark) > 80:
            dark = dark[:77] + "…"
        md_lines.append(
            f"| `{item['token']}` | `{light}` | `{dark}` | {item['usage_count']} | {len(item['definitions'])} |"
        )

    md_out = OUT_DIR / "token-inventory.md"
    md_out.write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    print(f"Wrote {md_out.relative_to(ROOT)} ({len(all_tokens)} tokens)")
    print(f"Wrote {json_out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
