from __future__ import annotations

import importlib.util
import json
import io
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "discovery.py"
SPEC = importlib.util.spec_from_file_location("kit_discovery", MODULE_PATH)
assert SPEC and SPEC.loader
discovery = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(discovery)


class DiscoveryTests(unittest.TestCase):
    def test_canonical_learn_urls_ignore_locale_and_trailing_slash(self) -> None:
        first = discovery.canonical_url("https://learn.microsoft.com/en-us/agent-framework/agents/skills/")
        second = discovery.canonical_url("https://learn.microsoft.com/zh-cn/agent-framework/agents/skills")
        self.assertEqual(first, second)

    def test_canonical_github_urls_route_to_repository(self) -> None:
        first = discovery.canonical_url("https://github.com/microsoft/agent-framework/tree/main/python")
        second = discovery.canonical_url("https://github.com/Microsoft/Agent-Framework/")
        self.assertEqual(first, second)

    def test_fixture_report_marks_known_and_new_candidates(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = root / "docs/coding-agent-kit/knowledge/external-sources"
            catalog = root / "docs/coding-agent-kit/catalog"
            registry.mkdir(parents=True)
            catalog.mkdir(parents=True)
            (registry / "sources.json").write_text(
                json.dumps({"items": [{"id": "known", "url": "https://github.com/microsoft/agent-framework"}]}),
                encoding="utf-8",
            )
            (catalog / "learn-index.json").write_text(json.dumps({"pages": []}), encoding="utf-8")
            raw = [
                discovery.candidate(
                    "https://github.com/microsoft/agent-framework/tree/main/python",
                    "known",
                    "repository-candidate",
                    "fixture",
                ),
                discovery.candidate(
                    "https://github.com/microsoft/agent-framework-go",
                    "new",
                    "repository-candidate",
                    "fixture",
                ),
            ]
            report = discovery.build_report(root, raw, "fixture", [])
            self.assertEqual(report["counts"], {"total": 2, "known": 1, "new": 1, "errors": 0})

    def test_private_network_url_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            discovery.require_public_https("https://127.0.0.1/source")

    def test_unicode_candidate_report_is_json_serializable(self) -> None:
        report = {"title": "Agent 🧰"}
        rendered = json.dumps(report, ensure_ascii=False)
        stream = io.TextIOWrapper(io.BytesIO(), encoding="utf-8")
        stream.write(rendered)
        stream.flush()
        self.assertIn("🧰", rendered)


if __name__ == "__main__":
    unittest.main()
