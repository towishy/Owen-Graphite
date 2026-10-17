"""Regression tests for deterministic, metadata-preserving CSS packaging."""

from __future__ import annotations

import tempfile
import json
import unittest
from pathlib import Path
from unittest.mock import patch

import bundle_v3
import capture_provenance_snapshot


class BundlePackagingTests(unittest.TestCase):
    def test_compacts_public_bundle_without_rewriting_css_values(self) -> None:
        settings = "/* @settings\nname: Example\nid: example\nsettings:\n  - id: demo\n    title: Demo\n    type: class-toggle\n*/"
        rules = "\n".join(
            f'.example-{index} {{\n    content: "two  spaces";\n    width: calc(100% - 2em);\n    color: #aabbcc;\n}}\n'
            for index in range(100)
        )
        source = settings + "\n" + rules
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            entry = root / "entry.css"
            output = root / "bundle.css"
            entry.write_text(source, encoding="utf-8")
            with patch.object(bundle_v3, "ROOT", root):
                self.assertEqual(bundle_v3.bundle(entry, output, dedup=False), 0)
            result = output.read_text(encoding="utf-8")
            self.assertNotIn(b"\r\n", output.read_bytes())
            self.assertIn(settings, result)
            self.assertIn('"two  spaces"', result)
            self.assertIn("calc(100% - 2em)", result)
            self.assertLess(len(result.encode()), len(source.encode()) * 0.9)

    def test_module_markers_remain_on_separate_lines(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "src").mkdir()
            entry = root / "src" / "entry.css"
            child = root / "src" / "child.css"
            entry.write_text('@import url("child.css");', encoding="utf-8")
            child.write_text('.child { content: "quoted /* not a comment */"; }', encoding="utf-8")
            output = root / "bundle.css"
            with patch.object(bundle_v3, "ROOT", root):
                self.assertEqual(bundle_v3.bundle(entry, output, dedup=False), 0)
            lines = output.read_text(encoding="utf-8").splitlines()
            self.assertIn("/* >>> src/child.css */", lines)
            self.assertIn("/* <<< src/child.css */", lines)
            self.assertIn('"quoted /* not a comment */"', "\n".join(lines))

    def test_readable_output_is_available_without_changing_source(self) -> None:
        source = ".example {\n    color: #aabbcc;\n}\n"
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            entry = root / "entry.css"
            entry.write_text(source, encoding="utf-8")
            output = root / "readable.css"
            with patch.object(bundle_v3, "ROOT", root):
                self.assertEqual(bundle_v3.bundle(entry, output, dedup=False, readable=True), 0)
            self.assertIn(source, output.read_text(encoding="utf-8"))
            self.assertEqual(source, entry.read_text(encoding="utf-8"))

    def test_freshness_check_does_not_overwrite_stale_output(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            entry = root / "entry.css"
            output = root / "bundle.css"
            entry.write_text(".example { color: red; }", encoding="utf-8")
            with patch.object(bundle_v3, "ROOT", root):
                bundle_v3.bundle(entry, output, dedup=False)
                expected = output.read_bytes()
                self.assertEqual(bundle_v3.bundle(entry, output, dedup=False, check=True), 0)
                entry.write_text(".example { color: blue; }", encoding="utf-8")
                self.assertEqual(bundle_v3.bundle(entry, output, dedup=False, check=True), 1)
            self.assertEqual(expected, output.read_bytes())

    def test_compact_provenance_does_not_invent_original_line_numbers(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            target = root / "dev" / "WIKI" / "MAP" / "effective-source-map.json"
            target.parent.mkdir(parents=True)
            target.write_text(json.dumps({
                "lineMapping": "module-only",
                "ranges": [{"module": "src/example.css", "bundleStartLine": 10, "bundleEndLine": 12, "sourceStartLine": 1}],
            }), encoding="utf-8")
            with patch.object(capture_provenance_snapshot, "ROOT", root):
                mapping = capture_provenance_snapshot.load_line_map("0.0.0")
            self.assertEqual("src/example.css", mapping[10]["module"])
            self.assertIsNone(mapping[10]["module_line"])


if __name__ == "__main__":
    unittest.main()
