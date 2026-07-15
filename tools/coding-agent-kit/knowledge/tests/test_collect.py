from __future__ import annotations

import argparse
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "collect.py"
SPEC = importlib.util.spec_from_file_location("collect", MODULE_PATH)
assert SPEC and SPEC.loader
collect = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(collect)


class CollectionTests(unittest.TestCase):
    def test_html_conversion_removes_script_and_preserves_code(self) -> None:
        payload = b"<html><script>bad()</script><article><h1>Agent</h1><p>Use <code>Agent</code>.</p></article></html>"
        markdown, method = collect.to_markdown(payload, "text/html", "https://example.com/doc")
        self.assertEqual(method, "html-to-markdown")
        self.assertIn("# Agent", markdown)
        self.assertIn("`Agent`", markdown)
        self.assertNotIn("bad()", markdown)

    def test_html_conversion_resolves_relative_links(self) -> None:
        payload = b'<article><p><a href="../api">API</a></p></article>'
        markdown, _ = collect.to_markdown(payload, "text/html", "https://example.com/guide/page")
        self.assertIn("[API](https://example.com/api)", markdown)

    def test_non_https_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            collect.require_https("http://example.com/doc")

    def test_private_url_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            collect.require_https("https://127.0.0.1/doc")

    def test_moving_project_version_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            collect.require_immutable_version("main")

    def test_invalid_publication_date_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            collect.require_iso_date("recently")

    def test_table_cells_are_escaped(self) -> None:
        self.assertEqual(collect.table_cell("a | b\n c"), "a \\| b c")

    def test_project_registration_never_downloads_content(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_root(Path(directory), "official-repository")
            args = argparse.Namespace(
                root=root,
                source_id="source",
                version="abc123",
                route="Use for workflow design.",
                design="Shows explicit state.",
                limitations="Not production guidance.",
            )
            collect.add_project(args)
            registry = collect.load_json(root / "docs/coding-agent-kit/knowledge/collection/project-routes.json")
            self.assertNotIn("local_path", registry["items"][0])
            self.assertFalse((root / "docs/coding-agent-kit/knowledge/collection/documents/source.md").exists())
            self.assertEqual(collect.check(root), [])

    def test_document_requires_redistribution_permission(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_root(Path(directory), "official-doc")
            source_file = root / "source.md"
            source_file.write_text("# Title\n\n" + "Useful content. " * 20, encoding="utf-8")
            args = argparse.Namespace(
                root=root,
                source_id="source",
                content_url=None,
                input=source_file,
                content_type="text/markdown",
                license="CC-BY-4.0",
                license_url="https://example.com/license",
                redistribution_allowed=False,
                published_at="2026-07-01",
                route="Use for agents.",
                timeout=1,
                max_bytes=1024,
            )
            with self.assertRaises(ValueError):
                collect.add_document(args)

    def test_document_manifest_and_hash_are_validated(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_root(Path(directory), "official-doc")
            source_file = root / "source.md"
            source_file.write_text("# Title\n\n" + "Useful content. " * 20, encoding="utf-8")
            args = argparse.Namespace(
                root=root,
                source_id="source",
                content_url=None,
                input=source_file,
                content_type="text/markdown",
                license="CC-BY-4.0",
                license_url="https://example.com/license",
                redistribution_allowed=True,
                published_at="2026-07-01",
                route="Use for agents.",
                timeout=1,
                max_bytes=1024,
            )
            collect.add_document(args)
            self.assertEqual(collect.check(root), [])
            retained = root / "docs/coding-agent-kit/knowledge/collection/documents/source.md"
            retained.write_text(retained.read_text(encoding="utf-8") + "tampered", encoding="utf-8")
            self.assertTrue(any("hash mismatch" in failure for failure in collect.check(root)))

    def test_collection_rejects_project_source_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_root(Path(directory), "official-repository")
            copied = root / "docs/coding-agent-kit/knowledge/collection/copied.py"
            copied.write_text("print('copied')", encoding="utf-8")
            self.assertTrue(any("Unexpected file" in failure for failure in collect.check(root)))

    @staticmethod
    def make_root(root: Path, source_class: str) -> Path:
        external = root / "docs/coding-agent-kit/knowledge/external-sources"
        collection = root / "docs/coding-agent-kit/knowledge/collection"
        topics = root / "tools/coding-agent-kit/indexer"
        external.mkdir(parents=True)
        collection.mkdir(parents=True)
        topics.mkdir(parents=True)
        (external / "reviews").mkdir()
        (external / "reviews/source.md").write_text("review", encoding="utf-8")
        (external / "sources.json").write_text(
            json.dumps(
                {
                    "items": [
                        {
                            "id": "source",
                            "name": "Source",
                            "url": "https://example.com/source",
                            "source_class": source_class,
                            "topics": ["agents"],
                            "languages": ["python"],
                            "review_status": "adopted",
                            "review": "reviews/source.md",
                        }
                    ]
                }
            ),
            encoding="utf-8",
        )
        (collection / "project-routes.json").write_text('{"schema_version":1,"items":[]}', encoding="utf-8")
        (collection / "documents.json").write_text('{"schema_version":1,"items":[]}', encoding="utf-8")
        (collection / "KNOWLEDGE_INDEX.md").write_text(
            collect.render_index({"items": []}, {"items": []}), encoding="utf-8"
        )
        (topics / "topics.json").write_text(
            json.dumps({"topics": [{"id": "agents"}]}), encoding="utf-8"
        )
        return root


if __name__ == "__main__":
    unittest.main()
