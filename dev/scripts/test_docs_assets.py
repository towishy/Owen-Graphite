import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from audit_docs_assets import managed_design_documents


class ManagedDesignDocumentsTests(unittest.TestCase):
    def fixture(self, root: Path, relative: str, content: str = "Shared design"):
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        manifest = root / "docs" / "wiki-design" / ".sync-state.json"
        manifest.parent.mkdir(parents=True, exist_ok=True)
        manifest.write_text(json.dumps({
            "schemaVersion": 1,
            "owner": "wiki-project-design-guides",
            "files": {relative: hashlib.sha256(path.read_bytes()).hexdigest()},
        }), encoding="utf-8")
        return path

    def test_absent_manifest_keeps_the_normal_link_audit(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(managed_design_documents(Path(directory)), set())

    def test_verified_mirror_has_a_separate_upstream_link_boundary(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = self.fixture(root, "docs/wiki-design/DESIGN.md", "[Source](D:/wiki/source.md)")
            self.assertEqual(managed_design_documents(root), {path.resolve()})

    def test_modified_mirror_is_not_exempt(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = self.fixture(root, "docs/wiki-design/DESIGN.md")
            path.write_text("Unexpected change", encoding="utf-8")
            with self.assertRaisesRegex(AssertionError, "differs"):
                managed_design_documents(root)

    def test_product_docs_cannot_be_exempted_by_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.fixture(root, "README.md")
            with self.assertRaisesRegex(AssertionError, "unexpected"):
                managed_design_documents(root)

    def test_missing_mirror_fails_explicitly(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = self.fixture(root, "docs/wiki-design/DESIGN.md")
            path.unlink()
            with self.assertRaises(FileNotFoundError):
                managed_design_documents(root)
