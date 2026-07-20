from __future__ import annotations

import importlib.util
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch


MODULE_PATH = Path(__file__).resolve().parents[1] / "lookup.py"
SPEC = importlib.util.spec_from_file_location("lookup", MODULE_PATH)
assert SPEC and SPEC.loader
lookup = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(lookup)


class ExternalLookupTests(unittest.TestCase):
    def test_external_route_scores_topic_and_annotation(self) -> None:
        entry = {
            "title": "Workflow reference",
            "route": "Use for durable workflow recovery",
            "design": "Explicit checkpoints",
            "limitations": "Python only",
            "version": "abc123",
            "topics": ["workflows", "durability"],
        }
        score = lookup.score_external(entry, ["recovery"], {"durability"})
        self.assertEqual(score, 14)

    def test_external_language_filter(self) -> None:
        self.assertTrue(lookup.external_language_matches({"languages": ["any"]}, "python"))
        self.assertFalse(lookup.external_language_matches({"languages": ["csharp"]}, "python"))

    def test_link_reference_annotation_is_searchable(self) -> None:
        entry = {
            "title": "A2A protocol reference",
            "route": "Use for protocol hosting",
            "annotation": "Explains cross-platform agent cards",
            "limitations": "Moving documentation",
            "topics": ["protocols"],
        }
        self.assertGreater(lookup.score_external(entry, ["cross-platform"], {"protocols"}), 8)

    def test_main_returns_link_only_reference_in_json(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            catalog_dir = root / "docs/coding-agent-kit/catalog"
            collection_dir = root / "docs/coding-agent-kit/knowledge/collection"
            catalog_dir.mkdir(parents=True)
            collection_dir.mkdir(parents=True)
            (catalog_dir / "catalog.json").write_text(
                json.dumps(
                    {
                        "upstream_commit": "a" * 40,
                        "topics": [
                            {
                                "id": "protocols",
                                "title": "Protocols",
                                "description": "A2A and AG-UI protocols",
                                "keywords": ["a2a", "ag-ui"],
                                "curated": [],
                            }
                        ],
                        "entries": [],
                    }
                ),
                encoding="utf-8",
            )
            (catalog_dir / "learn-index.json").write_text('{"pages":[]}', encoding="utf-8")
            (collection_dir / "project-routes.json").write_text('{"items":[]}', encoding="utf-8")
            (collection_dir / "documents.json").write_text('{"items":[]}', encoding="utf-8")
            (collection_dir / "link-references.json").write_text(
                json.dumps(
                    {
                        "items": [
                            {
                                "id": "a2a-doc",
                                "title": "A2A hosting",
                                "url": "https://example.com/a2a",
                                "route": "Use for A2A protocol hosting.",
                                "annotation": "Agent card and transport design.",
                                "limitations": "Recheck moving APIs.",
                                "topics": ["protocols"],
                                "languages": ["any"],
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            output = io.StringIO()
            argv = ["lookup.py", "A2A hosting", "--root", str(root), "--json"]
            with patch.object(sys, "argv", argv), redirect_stdout(output):
                self.assertEqual(lookup.main(), 0)
            result = json.loads(output.getvalue())
            self.assertEqual(result["external_link_references"][0]["id"], "a2a-doc")


if __name__ == "__main__":
    unittest.main()
