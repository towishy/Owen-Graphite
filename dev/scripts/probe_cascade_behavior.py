"""Cascade behavior verification harness.

Tests four scenarios with Playwright Chromium:

1. CORE_UNLAYERED + THEME_UNLAYERED (status quo: file order wins)
2. CORE_UNLAYERED + THEME_LAYERED   (the v3 question: does theme lose to core?)
3. CORE_UNLAYERED + THEME_LAYERED_WITH_IMPORTANT
4. CORE_UNLAYERED + THEME_HIGHER_SPECIFICITY

The CSS Cascading and Inheritance Module Level 5 says:

> Note: declarations in named layers lose to declarations in the implicit
> "unlayered" group, when they have the same origin and importance.

This script empirically confirms or refutes that for our actual Chromium
target. If (2) shows core winning even when theme has higher specificity,
then `@layer` is unusable for our theme. If (4) shows specificity beating
layering, then the spec note is wrong (it is not — but the test exists
to surface it).
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "dev" / "v3" / "cascade-probe"


CORE_CSS = """
/* Pretend Obsidian core (unlayered). */
body { color: rgb(136, 136, 136); }
p { font-size: 12px; color: rgb(136, 136, 136); }
.cm-line p { font-size: 12px; color: rgb(136, 136, 136); }
"""

SCENARIOS = [
    # (id, theme_css)
    (
        "1-theme-unlayered-same-specificity",
        """
/* Theme: unlayered, same specificity, declared later. */
body { color: rgb(255, 0, 0); }
p { font-size: 20px; color: rgb(255, 0, 0); }
""",
    ),
    (
        "2-theme-layered-same-specificity",
        """
@layer theme;
@layer theme {
  body { color: rgb(255, 0, 0); }
  p { font-size: 20px; color: rgb(255, 0, 0); }
}
""",
    ),
    (
        "3-theme-layered-with-important",
        """
@layer theme;
@layer theme {
  body { color: rgb(255, 0, 0) !important; }
  p { font-size: 20px !important; color: rgb(255, 0, 0) !important; }
}
""",
    ),
    (
        "4-theme-layered-higher-specificity",
        """
@layer theme;
@layer theme {
  /* Higher specificity than the unlayered core selectors. */
  body.theme-light { color: rgb(255, 0, 0); }
  .cm-line p { color: rgb(255, 0, 0); font-size: 20px; }
}
""",
    ),
    (
        "5-theme-unlayered-equal-specificity-later",
        """
/* Same specificity as core's `.cm-line p`, declared later in cascade order.
   No @layer, no !important. This is the v2.30.14 / v3 default strategy. */
.cm-line p { color: rgb(255, 0, 0); font-size: 20px; }
""",
    ),
    (
        "6-theme-unlayered-higher-specificity",
        """
/* Higher specificity than core's `.cm-line p` (0,1,1 vs 0,2,1).
   Mirrors the `body.theme-light :is(.cm-line) p` pattern v2.30.14 uses. */
body.theme-light .cm-line p { color: rgb(255, 0, 0); font-size: 20px; }
""",
    ),
]

HTML_TEMPLATE = """\
<!doctype html>
<html>
<head>
<meta charset='utf-8'>
<link rel='stylesheet' href='./core.css'>
<link rel='stylesheet' href='./theme.css'>
</head>
<body class='theme-light'>
<div class='cm-line'><p id='target'>x</p></div>
</body>
</html>
"""


def main() -> int:
    try:
        from playwright.sync_api import sync_playwright
    except ModuleNotFoundError:
        print("ERROR: playwright not installed")
        return 2

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    results: list[tuple[str, str, str]] = []
    for scenario_id, theme_css in SCENARIOS:
        scenario_dir = OUT_DIR / scenario_id
        scenario_dir.mkdir(exist_ok=True)
        (scenario_dir / "core.css").write_text(CORE_CSS, encoding="utf-8")
        (scenario_dir / "theme.css").write_text(theme_css, encoding="utf-8")
        (scenario_dir / "index.html").write_text(HTML_TEMPLATE, encoding="utf-8")

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page()
        for scenario_id, _ in SCENARIOS:
            url = (OUT_DIR / scenario_id / "index.html").resolve().as_uri()
            page.goto(url, wait_until="networkidle")
            color = page.evaluate(
                "() => getComputedStyle(document.getElementById('target')).color"
            )
            size = page.evaluate(
                "() => getComputedStyle(document.getElementById('target')).fontSize"
            )
            results.append((scenario_id, color, size))
        browser.close()

    print(f"{'scenario':<48} {'color':<22} {'font-size':<10} {'verdict'}")
    print("-" * 100)
    THEME_RED = "rgb(255, 0, 0)"
    THEME_SIZE = "20px"
    for sid, color, size in results:
        theme_wins = color == THEME_RED and size == THEME_SIZE
        verdict = "THEME WINS" if theme_wins else "CORE WINS"
        print(f"{sid:<48} {color:<22} {size:<10} {verdict}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
