#!/usr/bin/env python3
"""Audit all PDF heading templates against the UI Foundation print contract."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "dev" / "WIKI" / "DOCS" / "v3" / "research" / "pdf-heading-template-fixture.html"
PRINT_BASE = ROOT / "src" / "features" / "43-print-base.css"
OUT_DIR = ROOT / "dev" / "temp" / "pdf-heading-templates"
TEMPLATE_SPECS = (
    ("ogd-heading-printclean", "01-print-clean", "프린트 클린 / Print Clean"),
    ("ogd-heading-keyline", "02-cobalt-keyline", "코발트 키라인 / Cobalt Keyline"),
    ("ogd-heading-bracket", "03-bracket-chapter", "브래킷 챕터 / Bracket Chapter"),
    ("ogd-heading-quiet-ledger", "04-quiet-ledger", "조용한 장부 / Quiet Ledger"),
    ("ogd-heading-focus-bar", "05-focus-bar", "포커스 바 / Focus Bar"),
    ("ogd-heading-double-rule", "06-double-rule-classic", "더블룰 클래식 / Double Rule Classic"),
    ("ogd-heading-tag-ribbon", "07-tag-ribbon", "태그 리본 / Tag Ribbon"),
    ("ogd-heading-number-stamp", "08-number-stamp", "넘버 스탬프 / Number Stamp"),
    ("ogd-heading-grid-index", "09-grid-index", "그리드 인덱스 / Grid Index"),
)
TEMPLATES = tuple(template for template, _, _ in TEMPLATE_SPECS)
H1_LABEL_FREE_TEMPLATES = {
    "ogd-heading-bracket",
    "ogd-heading-focus-bar",
    "ogd-heading-number-stamp",
    "ogd-heading-grid-index",
}
SELECTORS = {
    "h1": '[data-check="pdf-template-h1"]',
    "h2": '[data-check="pdf-template-h2"]',
    "h3": '[data-check="pdf-template-h3"]',
    "h4": '[data-check="pdf-template-h4"]',
}
DOCUMENT_TITLE_SELECTOR = '[data-check="pdf-heading-template-article"] > h1:first-of-type'
METADATA_SELECTOR = ".fixture-template-meta"


def alpha(color: str) -> float:
    if color == "rgba(0, 0, 0, 0)":
        return 0.0
    if color.startswith("rgba("):
        return float(color.removesuffix(")").split(",")[-1].strip())
    return 1.0


def px(value: str) -> float:
    if not value.endswith("px"):
        raise AssertionError(f"expected px value, got {value!r}")
    return float(value[:-2])


def select_template(page: object, template: str, label: str) -> None:
    page.evaluate(
        """([templates, selected, selectedLabel]) => {
            document.body.classList.remove(...templates);
            document.body.classList.add(selected);
            document.documentElement.dataset.pdfTemplate = selected;
            document.title = `Owen Graphite PDF - ${selectedLabel}`;
            const label = document.querySelector('[data-check="pdf-template-name"]');
            if (label) label.textContent = selectedLabel;
        }""",
        [TEMPLATES, template, label],
    )


def render_outputs(page: object) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    outputs: list[dict[str, object]] = []

    for template, slug, label in TEMPLATE_SPECS:
        select_template(page, template, label)
        pdf_path = OUT_DIR / f"{slug}.pdf"
        preview_path = OUT_DIR / f"{slug}.png"
        page.pdf(
            path=str(pdf_path),
            format="A4",
            print_background=True,
            prefer_css_page_size=True,
        )
        page.screenshot(path=str(preview_path), full_page=True)
        if pdf_path.stat().st_size < 10_000:
            raise AssertionError(f"{template}: rendered PDF is unexpectedly small")
        if preview_path.stat().st_size < 20_000:
            raise AssertionError(f"{template}: rendered preview is unexpectedly small")
        outputs.append(
            {
                "order": len(outputs) + 1,
                "class": template,
                "label": label,
                "pdf": pdf_path.relative_to(ROOT).as_posix(),
                "preview": preview_path.relative_to(ROOT).as_posix(),
                "pdfBytes": pdf_path.stat().st_size,
                "previewBytes": preview_path.stat().st_size,
            }
        )
        print(f"OK: rendered {pdf_path.relative_to(ROOT)}")
        print(f"OK: rendered {preview_path.relative_to(ROOT)}")

    manifest = {
        "schema": "owen-graphite/pdf-heading-template-results/1",
        "fixture": FIXTURE.relative_to(ROOT).as_posix(),
        "count": len(outputs),
        "outputs": outputs,
    }
    manifest_path = OUT_DIR / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"OK: wrote {manifest_path.relative_to(ROOT)}")


def audit_readability_preset(page: object) -> None:
    print_base = PRINT_BASE.read_text(encoding="utf-8")
    if "@page ogd-pdf-readability" in print_base:
        raise AssertionError("PDF readability preset must not define a fixed named page")

    page.evaluate(
        """() => {
            document.body.classList.add('ogd-pdf-readability');
            const caption = document.createElement('figcaption');
            caption.dataset.check = 'pdf-readability-caption';
            caption.textContent = 'PDF readability caption';
            document.querySelector('[data-check="pdf-heading-template-article"]').append(caption);
        }"""
    )
    styles = page.evaluate(
        """() => {
            const read = (selector) => {
                const style = getComputedStyle(document.querySelector(selector));
                return {
                    fontFamily: style.fontFamily,
                    fontSize: style.fontSize,
                    fontWeight: style.fontWeight,
                    lineHeight: style.lineHeight,
                };
            };
            return {
                page: getComputedStyle(document.body).page,
                h1: read('[data-check="pdf-template-h1"]'),
                h2: read('[data-check="pdf-template-h2"]'),
                body: read('[data-check="pdf-template-h2"] + p'),
                caption: read('[data-check="pdf-readability-caption"]'),
            };
        }"""
    )
    expected = {
        "h1": {"fontSize": "36px", "fontWeight": "700", "lineHeight": "43.2px"},
        "h2": {"fontSize": "18px", "fontWeight": "700", "lineHeight": "24.3px"},
        "body": {"fontSize": "16px", "fontWeight": "400", "lineHeight": "24.96px"},
        "caption": {"fontSize": "14px", "fontWeight": "400", "lineHeight": "21px"},
    }
    if styles["page"] != "ogd-pdf-a4-portrait":
        raise AssertionError(f"PDF readability must preserve the selected paper size: {styles['page']!r}")
    for role, expected_style in expected.items():
        actual_style = styles[role]
        if not actual_style["fontFamily"].startswith("Pretendard"):
            raise AssertionError(f"PDF readability {role} must use Pretendard first")
        for property_name, expected_value in expected_style.items():
            if actual_style[property_name] != expected_value:
                raise AssertionError(
                    f"PDF readability {role} {property_name} {actual_style[property_name]!r} != {expected_value!r}"
                )
    print("OK: PDF readability preset preserves paper size and computed typography")


def audit(render: bool = False) -> int:
    from playwright.sync_api import sync_playwright

    if not FIXTURE.exists():
        raise FileNotFoundError(f"missing fixture: {FIXTURE}")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={"width": 1240, "height": 1400})
        page.goto(FIXTURE.as_uri(), wait_until="networkidle")
        page.emulate_media(media="print")

        for template, _, label in TEMPLATE_SPECS:
            select_template(page, template, label)
            metadata = page.eval_on_selector(
                METADATA_SELECTOR,
                """(element) => {
                    const style = getComputedStyle(element);
                    const first = element.firstElementChild.getBoundingClientRect();
                    const last = element.lastElementChild.getBoundingClientRect();
                    const rect = element.getBoundingClientRect();
                    return {
                        display: style.display,
                        itemGap: last.left - first.right,
                        rightInset: rect.right - last.right,
                    };
                }""",
            )
            styles = {
                level: page.eval_on_selector(
                    selector,
                    """(element) => {
                        const style = getComputedStyle(element);
                        const before = getComputedStyle(element, "::before");
                        const rect = element.getBoundingClientRect();
                        return {
                            display: style.display,
                            fontSize: style.fontSize,
                            beforeContent: before.content,
                            backgroundColor: style.backgroundColor,
                            borderRadius: style.borderRadius,
                            borderLeftWidth: style.borderLeftWidth,
                            boxShadow: style.boxShadow,
                            backdropFilter: style.backdropFilter,
                            overflowX: element.scrollWidth - element.clientWidth,
                            left: rect.left,
                            right: rect.right,
                        };
                    }""",
                )
                for level, selector in SELECTORS.items()
            }

            document_title_display = page.eval_on_selector(
                DOCUMENT_TITLE_SELECTOR,
                "element => getComputedStyle(element).display",
            )
            if document_title_display != "none":
                raise AssertionError(f"{template}: document title H1 must stay hidden in PDF")
            if metadata["display"] != "flex":
                raise AssertionError(f"{template}: fixture metadata must use flex layout")
            if metadata["itemGap"] < 20:
                raise AssertionError(f"{template}: fixture metadata values must remain separated")
            if abs(metadata["rightInset"]) > 1:
                raise AssertionError(f"{template}: fixture metadata date must remain right-aligned")
            if any(style["display"] == "none" for style in styles.values()):
                raise AssertionError(f"{template}: H1-H4 must remain visible")
            if not (px(styles["h1"]["fontSize"]) > px(styles["h2"]["fontSize"]) > px(styles["h3"]["fontSize"]) >= px(styles["h4"]["fontSize"])):
                raise AssertionError(f"{template}: heading typography hierarchy is not descending")
            for level, style in styles.items():
                if style["overflowX"] > 1:
                    raise AssertionError(f"{template}.{level}: horizontal overflow {style['overflowX']}px")
                if style["backdropFilter"] != "none":
                    raise AssertionError(f"{template}.{level}: print surface must not use backdrop-filter")
                if level in {"h1", "h2"} and style["boxShadow"] != "none":
                    raise AssertionError(f"{template}.{level}: print heading must not use shadow")
                if level in {"h1", "h2"} and any(px(radius) > 0 for radius in style["borderRadius"].split()):
                    raise AssertionError(f"{template}.{level}: rounded accent geometry is forbidden")

            if template in H1_LABEL_FREE_TEMPLATES and styles["h1"]["beforeContent"] != "none":
                raise AssertionError(f"{template}.h1: numeric label must remain removed")

            if template == "ogd-heading-focus-bar":
                if alpha(styles["h2"]["backgroundColor"]) == 0:
                    raise AssertionError("ogd-heading-focus-bar.h2: configured print background is not consumed")
                if px(styles["h2"]["borderLeftWidth"]) == 0:
                    raise AssertionError("ogd-heading-focus-bar.h2: configured print focus rule is not consumed")
            if template == "ogd-heading-grid-index" and alpha(styles["h2"]["backgroundColor"]) == 0:
                raise AssertionError("ogd-heading-grid-index.h2: configured print background is not consumed")

        if render:
            render_outputs(page)

        audit_readability_preset(page)

        browser.close()

    print(f"OK: PDF heading template UI Foundation audit ({len(TEMPLATES)} templates)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--render", action="store_true", help="render one PDF and print-media PNG per heading template")
    args = parser.parse_args()
    try:
        return audit(render=args.render)
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())