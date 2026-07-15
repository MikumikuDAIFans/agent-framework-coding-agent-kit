from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path, PurePosixPath


MODULE_PATH = Path(__file__).resolve().parents[1] / "build_catalog.py"
SPEC = importlib.util.spec_from_file_location("build_catalog", MODULE_PATH)
assert SPEC and SPEC.loader
build_catalog = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(build_catalog)


class CatalogClassificationTests(unittest.TestCase):
    def test_roles_are_path_sensitive(self) -> None:
        self.assertEqual(build_catalog.classify_role(PurePosixPath("python/samples/02-agents/demo.py")), "sample")
        self.assertEqual(build_catalog.classify_role(PurePosixPath("dotnet/tests/Core.UnitTests/Test.cs")), "test")
        self.assertEqual(build_catalog.classify_role(PurePosixPath("docs/decisions/0001-agent.md")), "design")
        self.assertEqual(build_catalog.classify_role(PurePosixPath("python/packages/core/module.py")), "implementation")

    def test_language_detection(self) -> None:
        self.assertEqual(build_catalog.detect_language(PurePosixPath("dotnet/src/Agent.cs")), "csharp")
        self.assertEqual(build_catalog.detect_language(PurePosixPath("python/packages/agent.py")), "python")
        self.assertEqual(build_catalog.detect_language(PurePosixPath("schemas/state.json")), "declarative")

    def test_path_pattern_outweighs_generic_keywords(self) -> None:
        topics = [
            {"id": "agents", "keywords": ["agent"], "path_patterns": []},
            {"id": "middleware", "keywords": ["middleware"], "path_patterns": ["*/middleware/*"]},
        ]
        scores = build_catalog.score_topics(
            "python/samples/02-agents/middleware/agent_logging.py",
            "Agent logging middleware",
            [],
            topics,
        )
        self.assertEqual(scores[0][0], "middleware")

    def test_learn_import_rejects_non_microsoft_urls(self) -> None:
        manifest = {
            "source": "https://learn.microsoft.com/agent-framework/",
            "generated_at": "2026-01-01T00:00:00Z",
            "results": [
                {
                    "status": "ok",
                    "title": "Unsafe",
                    "section_path": [],
                    "url": "https://example.com/not-official",
                    "markdown_url": "https://example.com/not-official.md",
                    "file": "unsafe.md",
                }
            ],
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.json"
            path.write_text(json.dumps(manifest), encoding="utf-8")
            with self.assertRaises(ValueError):
                build_catalog.import_learn_manifest(path)


if __name__ == "__main__":
    unittest.main()
