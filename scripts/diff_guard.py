#!/usr/bin/env python3
"""Run hit-routing / Live Preview guards on the *changes* introduced by
the current branch (or the staged diff for pre-commit).

Why:
  `validate_theme.py --ci` audits the entire bundle, but during patch
  authoring we want a fast, focused signal that says "this patch added
  a new violation". This script pulls only the *added* lines from
  `git diff` (default: against `origin/main`), reconstructs the new CSS
  rules they belong to, and runs the same hit-routing audit functions
  the full validator uses.

Usage:
  python scripts/diff_guard.py                    # diff vs origin/main
  python scripts/diff_guard.py --base HEAD~1
  python scripts/diff_guard.py --staged           # pre-commit mode
  python scripts/diff_guard.py --files dev/05-live-preview.css

Pre-commit hook:
  Add to `.git/hooks/pre-commit`:
      #!/bin/sh
      exec python scripts/diff_guard.py --staged
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

# Reuse the audit primitives from the main validator.
from validate_theme import (  # type: ignore
    _RULE_RE,
    _declares_any,
    _declares_pair,
    _has_nonzero_vertical_box,
    _selector_targets_token_directly,
    LIVE_PREVIEW_HYPERMD_DIRECT_TOKENS,
    LIVE_PREVIEW_WIDGET_DIRECT_TOKENS,
)


def _git(args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True, text=True, check=False
    )
    return result.stdout


def _changed_css_files(base: str | None, staged: bool) -> list[Path]:
    if staged:
        out = _git(["diff", "--name-only", "--cached", "--diff-filter=ACMR"])
    else:
        ref = base or "origin/main"
        out = _git(["diff", "--name-only", f"{ref}...HEAD", "--diff-filter=ACMR"])
    return [
        ROOT / line.strip()
        for line in out.splitlines()
        if line.strip().endswith(".css") and (ROOT / line.strip()).is_file()
    ]


def _added_line_numbers(file: Path, base: str | None, staged: bool) -> set[int]:
    """Return 1-based line numbers in the *current* file that were added by
    this diff (excluding context lines)."""
    rel = file.relative_to(ROOT).as_posix()
    if staged:
        out = _git(["diff", "--unified=0", "--cached", "--", rel])
    else:
        ref = base or "origin/main"
        out = _git(["diff", "--unified=0", f"{ref}...HEAD", "--", rel])
    added: set[int] = set()
    new_line = 0
    hunk_re = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@")
    for raw in out.splitlines():
        m = hunk_re.match(raw)
        if m:
            new_line = int(m.group(1))
            continue
        if raw.startswith("+++") or raw.startswith("---"):
            continue
        if raw.startswith("+"):
            added.add(new_line)
            new_line += 1
        elif raw.startswith("-"):
            continue
        else:
            new_line += 1
    return added


def _audit_rule(selectors: str, body: str) -> list[str]:
    """Return human-readable failures for a single CSS rule, or []."""
    failures: list[str] = []
    if "markdown-source-view.mod-cm6" not in selectors:
        return failures
    margin_props = (
        "margin", "margin-top", "margin-bottom", "margin-block",
        "margin-block-start", "margin-block-end",
    )
    margin_padding_props = margin_props + (
        "padding", "padding-top", "padding-bottom", "padding-block",
        "padding-block-start", "padding-block-end",
    )
    for token in LIVE_PREVIEW_WIDGET_DIRECT_TOKENS:
        if _selector_targets_token_directly(selectors, token):
            offender = _has_nonzero_vertical_box(body, margin_props)
            if offender:
                failures.append(
                    f"non-zero vertical margin on block widget ({token}): `{offender}`"
                )
            break
    for token in LIVE_PREVIEW_HYPERMD_DIRECT_TOKENS:
        if _selector_targets_token_directly(selectors, token):
            offender = _has_nonzero_vertical_box(body, margin_padding_props)
            if offender:
                failures.append(
                    f"non-zero vertical margin/padding on HyperMD-* cm-line ({token}): `{offender}`"
                )
            break
    for token in (".cm-active.cm-line", ".cm-active .cm-line"):
        if _selector_targets_token_directly(selectors, token):
            bad = _declares_any(
                body,
                ("outline", "box-shadow", "transform",
                 "padding", "padding-top", "padding-bottom"),
            )
            if bad:
                failures.append(f"forbidden visual on active line ({token}): `{bad}`")
            break
    for token in (".cm-embed-block", ".cm-html-embed"):
        if _selector_targets_token_directly(selectors, token):
            if _declares_pair(body, "overflow-x", "auto") and \
                    _declares_pair(body, "max-width", "100%"):
                failures.append(
                    f"lethal BFC pair on embed wrapper ({token}): "
                    f"overflow-x:auto + max-width:100%"
                )
            break
    for token in (".cm-content", ".cm-line"):
        if _selector_targets_token_directly(selectors, token):
            if re.search(r"pointer-events\s*:\s*none\b", body):
                failures.append(f"pointer-events:none on rendered text ({token})")
            break
    return failures


def _audit_file(file: Path, added_lines: set[int]) -> list[str]:
    """Return failure messages for rules whose body intersects `added_lines`."""
    text = file.read_text(encoding="utf-8")
    # Build line-number index: for each char offset, what line is it on?
    line_starts = [0]
    for i, ch in enumerate(text):
        if ch == "\n":
            line_starts.append(i + 1)

    def char_to_line(offset: int) -> int:
        # Binary search would be faster; linear is fine for theme size.
        import bisect
        return bisect.bisect_right(line_starts, offset)

    failures: list[str] = []
    for match in _RULE_RE.finditer(text):
        start_line = char_to_line(match.start())
        end_line = char_to_line(match.end())
        rule_lines = set(range(start_line, end_line + 1))
        if not rule_lines.intersection(added_lines):
            continue
        rule_failures = _audit_rule(match.group(1), match.group(2))
        for f in rule_failures:
            failures.append(f"{file.relative_to(ROOT).as_posix()}:{start_line}: {f}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", help="git ref to diff against (default: origin/main)")
    parser.add_argument("--staged", action="store_true", help="audit staged changes (pre-commit)")
    parser.add_argument("--files", nargs="*", help="explicit file list (skip git diff)")
    args = parser.parse_args()

    if args.files:
        files = [ROOT / f for f in args.files if (ROOT / f).is_file()]
        # When --files is given, treat the entire file as 'added'.
        all_failures: list[str] = []
        for f in files:
            all_lines = set(range(1, f.read_text(encoding="utf-8").count("\n") + 2))
            all_failures.extend(_audit_file(f, all_lines))
    else:
        files = _changed_css_files(args.base, args.staged)
        if not files:
            print("diff_guard: no changed CSS files")
            return 0
        all_failures = []
        for f in files:
            added = _added_line_numbers(f, args.base, args.staged)
            if not added:
                continue
            all_failures.extend(_audit_file(f, added))

    if all_failures:
        print("diff_guard: FAIL — hit-routing regressions in this patch:", file=sys.stderr)
        for line in all_failures:
            print(f"  - {line}", file=sys.stderr)
        print(
            "\nSee dev/MAP/cm6-hit-routing-contract.md for the rule set.",
            file=sys.stderr,
        )
        return 1
    print(f"diff_guard: OK ({len(files)} CSS file(s) inspected)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
