"""Identify *truly safe* duplicate-selector merge candidates inside a single dev/ module.

Safe = same file, same selector (whitespace-normalised), same declaration body
(whitespace-normalised), same enclosing at-rule / media-query context.

These are pure no-op duplicates whose removal cannot change rendered styles.
The script only reports — it never edits files.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

DEV_DIR = Path(__file__).resolve().parent.parent / "dev"


def normalize_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def tokenize_blocks(css: str):
    """Yield (selector, body, at_context, line_no) for each top-level rule.

    Handles nested at-rules (`@media`, `@supports`, `@layer`, `@container`)
    by tracking the enclosing at-rule chain as `at_context`.
    """
    i = 0
    n = len(css)
    at_stack: list[str] = []
    line = 1

    def advance_lines(start: int, end: int) -> None:
        nonlocal line
        line += css.count("\n", start, end)

    while i < n:
        # skip comments
        if css.startswith("/*", i):
            j = css.find("*/", i + 2)
            if j == -1:
                return
            advance_lines(i, j + 2)
            i = j + 2
            continue
        ch = css[i]
        if ch.isspace():
            if ch == "\n":
                line += 1
            i += 1
            continue
        # @-rule
        if ch == "@":
            # Find next `{` or `;`
            depth = 0
            j = i
            while j < n:
                c = css[j]
                if c == "/" and css.startswith("/*", j):
                    end = css.find("*/", j + 2)
                    if end == -1:
                        return
                    j = end + 2
                    continue
                if c == "{":
                    break
                if c == ";":
                    break
                j += 1
            if j >= n:
                return
            header = normalize_ws(css[i:j])
            if css[j] == ";":
                # at-rule without block (e.g. @charset)
                advance_lines(i, j + 1)
                i = j + 1
                continue
            # at-rule with block — push context, recurse over contents
            at_stack.append(header)
            depth = 1
            advance_lines(i, j + 1)
            i = j + 1
            block_start = i
            while i < n and depth > 0:
                c = css[i]
                if c == "/" and css.startswith("/*", i):
                    end = css.find("*/", i + 2)
                    if end == -1:
                        return
                    advance_lines(i, end + 2)
                    i = end + 2
                    continue
                if c == "{":
                    depth += 1
                elif c == "}":
                    depth -= 1
                    if depth == 0:
                        break
                if c == "\n":
                    line += 1
                i += 1
            # Recurse into the block to capture inner rules
            inner = css[block_start:i]
            inner_line_offset = css.count("\n", 0, block_start) + 1
            for sel, body, inner_ctx, sub_line in tokenize_blocks(inner):
                full_ctx = " >> ".join(at_stack[:-1] + [header] + ([inner_ctx] if inner_ctx else []))
                yield sel, body, full_ctx, inner_line_offset + sub_line - 1
            at_stack.pop()
            i += 1  # past '}'
            continue
        # plain rule: selector { body }
        sel_start = i
        sel_line = line
        depth = 0
        j = i
        while j < n:
            c = css[j]
            if c == "/" and css.startswith("/*", j):
                end = css.find("*/", j + 2)
                if end == -1:
                    return
                advance_lines(j, end + 2)
                j = end + 2
                continue
            if c == "{":
                break
            if c == "}":
                # stray closing — skip
                break
            j += 1
        if j >= n or css[j] != "{":
            i = j + 1
            continue
        selector = css[sel_start:j].strip()
        advance_lines(i, j + 1)
        i = j + 1
        depth = 1
        body_start = i
        while i < n and depth > 0:
            c = css[i]
            if c == "/" and css.startswith("/*", i):
                end = css.find("*/", i + 2)
                if end == -1:
                    return
                advance_lines(i, end + 2)
                i = end + 2
                continue
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
        at_context = " >> ".join(at_stack)
        yield normalize_ws(selector), normalize_ws(body), at_context, sel_line
        i += 1  # past '}'


def scan_module(path: Path):
    css = path.read_text(encoding="utf-8")
    by_key: dict[tuple[str, str, str], list[int]] = defaultdict(list)
    for sel, body, ctx, line in tokenize_blocks(css):
        if not sel or not body:
            continue
        key = (sel, body, ctx)
        by_key[key].append(line)
    candidates = []
    for (sel, body, ctx), lines in by_key.items():
        if len(lines) > 1:
            candidates.append((sel, body, ctx, lines))
    return candidates


def main() -> int:
    total = 0
    files_with_dupes = 0
    for css_path in sorted(DEV_DIR.glob("*.css")):
        dupes = scan_module(css_path)
        if not dupes:
            continue
        files_with_dupes += 1
        print(f"\n=== {css_path.name} : {len(dupes)} safe duplicate group(s) ===")
        for sel, body, ctx, lines in sorted(dupes, key=lambda d: d[3][0]):
            ctx_note = f"  @ctx: {ctx}" if ctx else ""
            print(f"  lines {lines}  sel: {sel[:100]}{'…' if len(sel) > 100 else ''}{ctx_note}")
            print(f"    body: {body[:120]}{'…' if len(body) > 120 else ''}")
            total += len(lines) - 1  # extra copies that could be removed
    print(f"\nTotal removable extra copies (safe): {total}")
    print(f"Modules with safe duplicates: {files_with_dupes}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
