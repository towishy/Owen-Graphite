#!/usr/bin/env python3
"""Audit computed styles for Live Preview / PDF parity fixtures."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TABLE_CALLOUT_FIXTURE = ROOT / "docs" / "v3" / "research" / "table-callout-parity-fixture.html"
CODE_FONT_FIXTURE = ROOT / "docs" / "v3" / "research" / "code-font-clarity-fixture.html"


SCREEN_TABLE_SELECTORS = {
    "lp_table": '[data-check="lp-table-widget-cell"]',
    "lp_html_table": '[data-check="lp-html-table-cell"]',
}

SCREEN_CALLOUT_SELECTORS = {
    "lp_callout": '[data-check="lp-callout-content"]',
}

READING_SELECTORS = {
    "reading_table": '[data-check="reading-table-cell"]',
    "reading_callout": '[data-check="reading-callout-content"]',
}

PRINT_SELECTORS = {
    "pdf_body_text": '[data-check="pdf-body-text"]',
    "pdf_table_baseline": '[data-check="pdf-table-font-baseline"]',
    "pdf_table_cell": '[data-check="pdf-table-cell"]',
    "pdf_table_code": '[data-check="pdf-table-code"]',
    "pdf_callout": '[data-check="pdf-callout-widget"]',
    "pdf_callout_content": '[data-check="pdf-callout-content"]',
}

PRINT_CODE_SELECTORS = {
    "pdf_code_block": '[data-check="pdf-code-clarity"] code',
}


def px(value: str) -> float:
    if not value.endswith("px"):
        raise AssertionError(f"expected px value, got {value!r}")
    return float(value[:-2])


def assert_close(name: str, observed: float, expected: float, tolerance: float = 0.75) -> None:
    if abs(observed - expected) > tolerance:
        raise AssertionError(f"{name}: expected {expected:.2f}px +/- {tolerance:.2f}, got {observed:.2f}px")


def assert_equal_style(group: str, samples: dict[str, dict[str, str]], properties: tuple[str, ...]) -> None:
    baseline_name = next(iter(samples))
    baseline = samples[baseline_name]
    for name, style in samples.items():
        for prop in properties:
            if style[prop] != baseline[prop]:
                raise AssertionError(
                    f"{group}.{prop}: {name}={style[prop]!r} differs from {baseline_name}={baseline[prop]!r}"
        )


def assert_close_style(group: str, samples: dict[str, dict[str, str]], properties: tuple[str, ...], tolerance: float = 0.75) -> None:
    baseline_name = next(iter(samples))
    baseline = samples[baseline_name]
    for name, style in samples.items():
        for prop in properties:
            assert_close(f"{group}.{prop}.{name}", px(style[prop]), px(baseline[prop]), tolerance=tolerance)


def assert_between(name: str, observed: float, minimum: float, maximum: float) -> None:
    if observed < minimum or observed > maximum:
        raise AssertionError(f"{name}: expected {minimum:.2f}px..{maximum:.2f}px, got {observed:.2f}px")


def audit_with_playwright(require_playwright: bool) -> int:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        message = "SKIP: playwright is not installed; computed-style audit not run"
        print(message)
        return 2 if require_playwright else 0

    if not TABLE_CALLOUT_FIXTURE.exists():
        raise FileNotFoundError(f"missing fixture: {TABLE_CALLOUT_FIXTURE}")
    if not CODE_FONT_FIXTURE.exists():
        raise FileNotFoundError(f"missing fixture: {CODE_FONT_FIXTURE}")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 1100})
        page.goto(TABLE_CALLOUT_FIXTURE.as_uri(), wait_until="networkidle")

        screen_table = {name: get_style(page, selector) for name, selector in SCREEN_TABLE_SELECTORS.items()}
        assert_close_style("screen_table", screen_table, ("paddingTop", "paddingLeft", "fontSize", "lineHeight"))

        screen_callout = {name: get_style(page, selector) for name, selector in SCREEN_CALLOUT_SELECTORS.items()}
        assert_close_style("screen_callout", screen_callout, ("fontSize", "lineHeight"))

        reading = {name: get_style(page, selector) for name, selector in READING_SELECTORS.items()}
        assert_between("reading table font-size", px(reading["reading_table"]["fontSize"]), 12.0, 16.5)
        assert_between("reading table padding-left", px(reading["reading_table"]["paddingLeft"]), 5.0, 10.0)
        assert_between("reading callout font-size", px(reading["reading_callout"]["fontSize"]), 12.0, 16.5)

        page.emulate_media(media="print")
        print_styles = {name: get_style(page, selector) for name, selector in PRINT_SELECTORS.items()}

        pdf_document_h1 = get_style(page, '[data-check="pdf-table-callout"] > h1:first-of-type')
        if pdf_document_h1["display"] != "none":
            raise AssertionError(f"pdf document H1 should be hidden, got display={pdf_document_h1['display']!r}")

        page.evaluate(
                        """
                        () => {
                            const pdfArticle = document.querySelector('[data-check="pdf-table-callout"]');
                            const bodyHeading = document.createElement('h1');
                            bodyHeading.dataset.check = 'pdf-first-body-h1';
                            bodyHeading.textContent = 'First visible body heading';
                            pdfArticle.insertBefore(bodyHeading, pdfArticle.children[1]);
                        }
                        """
        )
        pdf_first_body_h1 = get_style(page, '[data-check="pdf-first-body-h1"]')
        if pdf_first_body_h1["display"] == "none":
            raise AssertionError("pdf first body H1 should remain visible")
        assert_between("pdf first body H1 font-size", px(pdf_first_body_h1["fontSize"]), 48.0, 58.0)

        page.evaluate(
                        """
                        () => {
                            const inlineTitle = document.createElement('div');
                            inlineTitle.className = 'inline-title';
                            inlineTitle.dataset.check = 'pdf-inline-title';
                            inlineTitle.textContent = 'Obsidian inline title';
                            document.body.appendChild(inlineTitle);
                        }
                        """
        )
        inline_title = get_style(page, '[data-check="pdf-inline-title"]')
        if inline_title["display"] != "none":
            raise AssertionError(f"pdf inline title should be hidden, got display={inline_title['display']!r}")

        lp_table = screen_table["lp_table"]
        pdf_table_baseline = print_styles["pdf_table_baseline"]
        pdf_table = print_styles["pdf_table_cell"]
        assert_close("print table font-size follows baseline", px(pdf_table["fontSize"]), px(pdf_table_baseline["fontSize"]), tolerance=0.35)
        assert_close("print table padding-top follows LP", px(pdf_table["paddingTop"]), px(lp_table["paddingTop"]), tolerance=1.0)
        assert_close("print table padding-left follows LP", px(pdf_table["paddingLeft"]), px(lp_table["paddingLeft"]), tolerance=1.0)
        assert_close("print table line-height follows baseline", px(pdf_table["lineHeight"]), px(pdf_table_baseline["lineHeight"]), tolerance=0.75)

        lp_callout = screen_callout["lp_callout"]
        pdf_callout_content = print_styles["pdf_callout_content"]
        assert_close("print body font-size follows table", px(print_styles["pdf_body_text"]["fontSize"]), px(pdf_table_baseline["fontSize"]), tolerance=0.35)
        assert_close("print callout font-size follows table", px(pdf_callout_content["fontSize"]), px(pdf_table_baseline["fontSize"]), tolerance=0.35)
        assert_close("print callout line-height follows table", px(pdf_callout_content["lineHeight"]), px(pdf_table_baseline["lineHeight"]), tolerance=0.75)

        page.evaluate(
                        """
                        () => {
                            const barePreview = document.createElement('section');
                            barePreview.className = 'markdown-preview-view';
                            barePreview.innerHTML = '<div class="el-p"><p data-check="pdf-body-bare-preview-text">Bare preview PDF body text</p></div>';
                            document.body.appendChild(barePreview);
                        }
                        """
        )
        bare_preview_text = get_style(page, '[data-check="pdf-body-bare-preview-text"]')
        assert_close("bare preview print body font-size follows table", px(bare_preview_text["fontSize"]), px(pdf_table_baseline["fontSize"]), tolerance=0.35)
        assert_close("bare preview print body line-height follows table", px(bare_preview_text["lineHeight"]), px(pdf_table_baseline["lineHeight"]), tolerance=0.75)

        table_code = print_styles["pdf_table_code"]
        if table_code["whiteSpace"] == "nowrap":
            raise AssertionError("pdf table code should wrap, but computed white-space is nowrap")
        if table_code["overflowWrap"] not in {"anywhere", "break-word"}:
            raise AssertionError(f"pdf table code should allow wrapping, got overflow-wrap={table_code['overflowWrap']!r}")

        callout = print_styles["pdf_callout"]
        if callout["borderLeftWidth"] != callout["borderRightWidth"]:
            raise AssertionError(
                "pdf callout should not reintroduce a left rail: "
                f"left={callout['borderLeftWidth']}, right={callout['borderRightWidth']}"
            )

        page.evaluate("document.body.classList.add('ogd-pdf-compact')")
        compact_styles = {name: get_style(page, selector) for name, selector in PRINT_SELECTORS.items()}
        compact_baseline = compact_styles["pdf_table_baseline"]
        assert_close("compact print body font-size follows table", px(compact_styles["pdf_body_text"]["fontSize"]), px(compact_baseline["fontSize"]), tolerance=0.35)
        assert_close("compact print body line-height follows table", px(compact_styles["pdf_body_text"]["lineHeight"]), px(compact_baseline["lineHeight"]), tolerance=0.75)
        assert_close("compact print table font-size follows baseline", px(compact_styles["pdf_table_cell"]["fontSize"]), px(compact_baseline["fontSize"]), tolerance=0.35)
        assert_close("compact print callout font-size follows table", px(compact_styles["pdf_callout_content"]["fontSize"]), px(compact_baseline["fontSize"]), tolerance=0.35)
        page.evaluate("document.body.classList.remove('ogd-pdf-compact')")

        header_value = get_pseudo_style(page, ".fixture-print.markdown-rendered", "::before")
        header_key = get_pseudo_style(page, ".fixture-print.markdown-rendered", "::after")
        for name, style in {"header_value": header_value, "header_key": header_key}.items():
            if style["display"] not in {"flex", "inline-flex"}:
                raise AssertionError(f"{name} should use flex centering, got display={style['display']!r}")
            if style["alignItems"] != "center" or style["justifyContent"] != "center":
                raise AssertionError(
                    f"{name} should center text inside the segment box, "
                    f"got align-items={style['alignItems']!r}, justify-content={style['justifyContent']!r}"
        )
        assert_close("header pair-1 key/value height", px(header_key["height"]), px(header_value["height"]), tolerance=0.35)

        header_pair2_anchor = "body"
        header_pair2_key = get_pseudo_style(page, header_pair2_anchor, "::before")
        header_pair2_value = get_pseudo_style(page, header_pair2_anchor, "::after")
        expected_pair2_content = {
            "header_pair2_key": '"Reviewed by"',
            "header_pair2_value": '"Graphite QA"',
        }
        for name, style in {"header_pair2_key": header_pair2_key, "header_pair2_value": header_pair2_value}.items():
            if style["display"] not in {"flex", "inline-flex"}:
                raise AssertionError(f"{name} should use flex centering, got display={style['display']!r}")
            if style["content"] != expected_pair2_content[name]:
                raise AssertionError(f"{name} content mismatch: got {style['content']!r}")
            height = px(style["height"])
            if height < 20 or height > 34:
                raise AssertionError(f"{name} should keep compact segment height, got height={style['height']!r}")
        assert_close("header pair-1/pair-2 key height", px(header_key["height"]), px(header_pair2_key["height"]), tolerance=0.35)
        assert_close("header pair-1/pair-2 value height", px(header_value["height"]), px(header_pair2_value["height"]), tolerance=0.35)
        ordered_lefts = [
            ("header_pair1_key", px(header_key["left"])),
            ("header_pair1_value", px(header_value["left"])),
            ("header_pair2_key", px(header_pair2_key["left"])),
            ("header_pair2_value", px(header_pair2_value["left"])),
        ]
        for (left_name, left_value), (right_name, right_value) in zip(ordered_lefts, ordered_lefts[1:]):
            if left_value >= right_value:
                raise AssertionError(
                    "dual header order should be pair-1 key/value then pair-2 key/value, "
                    f"but {left_name} left={left_value:.2f}px >= {right_name} left={right_value:.2f}px"
        )
        if header_pair2_key["backgroundColor"] == header_key["backgroundColor"]:
            raise AssertionError("header pair-2 key should support an independent palette from pair-1 key")
        if header_pair2_value["backgroundColor"] == header_value["backgroundColor"]:
            raise AssertionError("header pair-2 value should support an independent palette from pair-1 value")

        page.goto(CODE_FONT_FIXTURE.as_uri(), wait_until="networkidle")
        page.emulate_media(media="print")
        code_styles = {name: get_style(page, selector) for name, selector in PRINT_CODE_SELECTORS.items()}
        assert_close("print codeblock font-size follows table", px(code_styles["pdf_code_block"]["fontSize"]), px(pdf_table_baseline["fontSize"]), tolerance=0.35)
        assert_close("print codeblock line-height follows table", px(code_styles["pdf_code_block"]["lineHeight"]), px(pdf_table_baseline["lineHeight"]), tolerance=0.75)

        browser.close()

    print("OK: LP/PDF computed style parity audit")
    return 0


def get_style(page, selector: str) -> dict[str, str]:
    count = page.locator(selector).count()
    if count < 1:
        raise AssertionError(f"selector not found: {selector}")
    return page.eval_on_selector(
        selector,
        """
        (el) => {
          const style = getComputedStyle(el);
          return {
            display: style.display,
            paddingTop: style.paddingTop,
            paddingLeft: style.paddingLeft,
            fontSize: style.fontSize,
            lineHeight: style.lineHeight,
            whiteSpace: style.whiteSpace,
            overflowWrap: style.overflowWrap,
            wordBreak: style.wordBreak,
            color: style.color,
            backgroundColor: style.backgroundColor,
            borderLeftWidth: style.borderLeftWidth,
            borderRightWidth: style.borderRightWidth,
          };
        }
        """,
    )


def get_pseudo_style(page, selector: str, pseudo: str) -> dict[str, str]:
        count = page.locator(selector).count()
        if count < 1:
                raise AssertionError(f"selector not found: {selector}")
        return page.eval_on_selector(
                selector,
                """
                (el, pseudo) => {
                    const style = getComputedStyle(el, pseudo);
                    return {
                        display: style.display,
                        alignItems: style.alignItems,
                        justifyContent: style.justifyContent,
                        textAlign: style.textAlign,
                        height: style.height,
                        minHeight: style.minHeight,
                        left: style.left,
                        right: style.right,
                        width: style.width,
                        backgroundColor: style.backgroundColor,
                        content: style.content,
                    };
                }
                """,
                pseudo,
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-playwright", action="store_true", help="fail when Playwright is not installed")
    args = parser.parse_args()

    try:
        return audit_with_playwright(args.require_playwright)
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
