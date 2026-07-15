from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


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


if __name__ == "__main__":
    unittest.main()
