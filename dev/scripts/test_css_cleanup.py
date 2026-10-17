"""Regression contracts for the behavior-preserving CSS owner cleanup."""

from __future__ import annotations

import unittest
from pathlib import Path

from rcssmin import cssmin

import bundle_v3
import css_scan
import dedup_v3


ROOT = Path(__file__).resolve().parents[2]
READING = ":is(.markdown-rendered, .markdown-preview-view, .markdown-reading-view)"
HTML_HEADER = (
    ".markdown-source-view.mod-cm6 "
    ":is(.cm-html-embed, .cm-embed-block:not(.cm-callout):not(.cm-table-widget)) "
    "table:not(.cm-table):not(.cm-table-widget) thead th"
)


def rule_bodies(css: str, selector: str) -> list[str]:
    target = cssmin(selector + "{}")
    return [
        rule.body
        for rule in css_scan.iter_rule_blocks(css)
        if cssmin(rule.selectors.strip() + "{}") == target
    ]


def property_names(body: str) -> list[str]:
    return [
        text.partition(":")[0].strip()
        for kind, text in dedup_v3._split_declarations(body)
        if kind == "decl"
    ]


class CssCleanupTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        source = bundle_v3.resolve_imports(bundle_v3.ENTRY, set())
        cls.bundled, _ = dedup_v3.dedup_scope(source)
        cls.callouts = (ROOT / "src" / "surfaces" / "21-reading-callouts-lists.css").read_text(encoding="utf-8")

    def test_callout_geometry_has_one_direct_owner_rule(self) -> None:
        bodies = rule_bodies(self.callouts, f"{READING} .callout")
        self.assertEqual(1, len(bodies))
        properties = property_names(bodies[0])
        self.assertIn("box-sizing", properties)
        self.assertIn("margin", properties)
        self.assertNotIn("margin-left", properties)
        self.assertNotIn("margin-right", properties)

    def test_callout_icon_geometry_has_one_direct_owner_rule(self) -> None:
        bodies = rule_bodies(self.callouts, f"{READING} .callout-icon")
        self.assertEqual(1, len(bodies))
        properties = property_names(bodies[0])
        self.assertIn("justify-self", properties)
        self.assertIn("background", properties)

    def test_marked_list_note_has_one_effective_margin_rule(self) -> None:
        selector = f"{READING} :is(ol, ul):not(.contains-task-list) + p:has(> mark:first-child)"
        bodies = rule_bodies(self.callouts, f"body {selector}")
        self.assertEqual(1, len(bodies))
        self.assertEqual(
            [("margin-inline-start", "0")],
            list(css_scan.CssRuleBlock("", bodies[0], 0, 0, 1).declarations()),
        )

    def test_callout_icon_background_has_no_shadowed_color(self) -> None:
        bodies = rule_bodies(self.bundled, f"{READING} .callout-icon")
        self.assertEqual(1, len(bodies))
        self.assertNotIn("background-color", property_names(bodies[0]))

    def test_static_callout_backgrounds_do_not_repeat_the_same_color(self) -> None:
        for rule in css_scan.iter_rule_blocks(self.callouts):
            with self.subTest(selector=rule.normalized_selectors):
                declarations = dict(rule.declarations())
                background = declarations.get("background")
                color = declarations.get("background-color")
                if background and color:
                    self.assertNotEqual(background, color)

    def test_view_title_background_has_no_shadowed_clip(self) -> None:
        selector = "body:not(.is-mobile) .mod-root .view-header .view-header-title"
        bodies = rule_bodies(self.bundled, selector)
        self.assertEqual(1, len(bodies))
        self.assertNotIn("background-clip", property_names(bodies[0]))
        self.assertIn("background", property_names(bodies[0]))

    def test_html_header_divider_has_no_shadowed_color(self) -> None:
        for prefix in ("body", "body.theme-dark"):
            with self.subTest(prefix=prefix):
                bodies = rule_bodies(self.bundled, f"{prefix} {HTML_HEADER}")
                self.assertEqual(1, len(bodies))
                properties = property_names(bodies[0])
                self.assertIn("border-bottom", properties)
                self.assertNotIn("border-bottom-color", properties)


if __name__ == "__main__":
    unittest.main()
