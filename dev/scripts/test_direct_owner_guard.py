#!/usr/bin/env python3
"""Negative tests for direct-owner guard exceptions."""

from __future__ import annotations

import unittest

import audit_direct_owner_guard as guard

RISK_ID = "cm-table-widget-test"
EVIDENCE = "dev/TEMP/runtime-evidence/fragments/test.json"
REGISTRY = {
    RISK_ID: {
        "id": RISK_ID,
        "module": "src/base/13-live-preview.css",
        "selectorContains": [".cm-table-widget.markdown-rendered table.table-editor"],
        "allowedProperties": ["background-color", "color"],
        "evidence": [EVIDENCE],
    }
}


def risk_css(body: str, *, marker: str | None = None) -> str:
    marker_text = marker or f"/* owen-risk-accepted-begin: cm-table-widget; id={RISK_ID}; evidence={EVIDENCE} */"
    return f"""
{marker_text}
{body}
/* owen-risk-accepted-end: cm-table-widget */
"""


class DirectOwnerGuardTests(unittest.TestCase):
    def test_registry_backed_risk_range_allows_registered_selector_and_property(self) -> None:
        css = risk_css("body .markdown-source-view.mod-cm6 .cm-table-widget.markdown-rendered table.table-editor { background-color: #fff; }")
        ranges, problems = guard.owen_risk_ranges(css, "src/base/13-live-preview.css", REGISTRY)
        violations: list[str] = []
        guard.assert_risk_range_rules(css, "src/base/13-live-preview.css", ranges, REGISTRY, violations)
        self.assertEqual([], problems)
        self.assertEqual([], violations)
        self.assertTrue(guard.has_owen_risk_marker(css, css.index(".cm-table-widget"), ranges))

    def test_risk_marker_requires_registry_id(self) -> None:
        css = risk_css(
            "body .markdown-source-view.mod-cm6 .cm-table-widget.markdown-rendered table.table-editor { background-color: #fff; }",
            marker=f"/* owen-risk-accepted-begin: cm-table-widget; evidence={EVIDENCE} */",
        )
        _, problems = guard.owen_risk_ranges(css, "src/base/13-live-preview.css", REGISTRY)
        self.assertIn("owen risk marker missing id=...", problems)

    def test_risk_range_rejects_unregistered_property(self) -> None:
        css = risk_css("body .markdown-source-view.mod-cm6 .cm-table-widget.markdown-rendered table.table-editor { padding: 8px; }")
        ranges, _ = guard.owen_risk_ranges(css, "src/base/13-live-preview.css", REGISTRY)
        violations: list[str] = []
        guard.assert_risk_range_rules(css, "src/base/13-live-preview.css", ranges, REGISTRY, violations)
        self.assertTrue(any("owen-risk-property: padding" in item for item in violations))

    def test_risk_range_rejects_unregistered_selector(self) -> None:
        css = risk_css("body .markdown-source-view.mod-cm6 .cm-table-widget table.cm-table { background-color: #fff; }")
        ranges, _ = guard.owen_risk_ranges(css, "src/base/13-live-preview.css", REGISTRY)
        violations: list[str] = []
        guard.assert_risk_range_rules(css, "src/base/13-live-preview.css", ranges, REGISTRY, violations)
        self.assertTrue(any("owen-risk-selector" in item for item in violations))

    def test_callout_left_rail_is_rejected(self) -> None:
        css = ".callout[data-callout='info'] { border-left-color: red; }"
        violations: list[str] = []
        guard.assert_no_callout_left_rails(css, "src/test.css", violations)
        self.assertTrue(any("callout-left-rail" in item for item in violations))


if __name__ == "__main__":
    unittest.main()
