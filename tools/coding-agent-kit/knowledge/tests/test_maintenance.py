from __future__ import annotations

import argparse
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


MODULE_PATH = Path(__file__).resolve().parents[1] / "maintenance.py"
SPEC = importlib.util.spec_from_file_location("maintenance", MODULE_PATH)
assert SPEC and SPEC.loader
maintenance = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(maintenance)


class MaintenanceTests(unittest.TestCase):
    def test_github_coordinates_support_deep_links(self) -> None:
        self.assertEqual(
            maintenance.github_coordinates("https://github.com/microsoft/agent-framework/tree/main/python"),
            ("microsoft", "agent-framework"),
        )
        self.assertIsNone(maintenance.github_coordinates("https://learn.microsoft.com/agent-framework"))

    def test_offline_mode_never_calls_network(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_root(Path(directory), reviewed_commit="abc")
            args = self.args(root)
            with patch.object(maintenance, "network_observation", side_effect=AssertionError("network used")):
                report, exit_code = maintenance.run(args)
            self.assertEqual(exit_code, 0)
            self.assertEqual(report["mode"], "offline")
            self.assertEqual(report["status"], "not-run")
            self.assertEqual(report["sources"][0]["status"], "not-run")
            self.assertTrue(any(check["status"] == "not-run" for check in report["sources"][0]["checks"]))

    def test_fixture_reports_version_and_api_drift(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_root(Path(directory), reviewed_commit="a" * 40)
            fixture = root / "fixture.json"
            fixture.write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "sources": {
                            "source": {
                                "link": {"status_code": 200, "final_url": "https://github.com/org/repo"},
                                "github": {
                                    "archived": False,
                                    "default_branch": "main",
                                    "head_sha": "b" * 40,
                                    "license_spdx": "MIT",
                                },
                            }
                        },
                    }
                ),
                encoding="utf-8",
            )
            args = self.args(root, fixture=fixture)
            report, exit_code = maintenance.run(args)
            self.assertEqual(exit_code, 1)
            self.assertEqual(report["status"], "drift")
            checks = {check["id"]: check["status"] for check in report["sources"][0]["checks"]}
            self.assertEqual(checks["version_drift"], "drift")
            self.assertEqual(checks["api_drift"], "needs-review")

    def test_fixture_reports_archived_and_license_drift(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_root(Path(directory), reviewed_commit="a" * 40, license_name="Apache-2.0")
            fixture = root / "fixture.json"
            fixture.write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "sources": {
                            "source": {
                                "link": {"status_code": 200},
                                "github": {
                                    "archived": True,
                                    "default_branch": "main",
                                    "head_sha": "a" * 40,
                                    "license_spdx": "MIT",
                                },
                                "api": {"compatible": True, "evidence": "offline verifier"},
                            }
                        },
                    }
                ),
                encoding="utf-8",
            )
            report, exit_code = maintenance.run(self.args(root, fixture=fixture))
            self.assertEqual(exit_code, 1)
            checks = {check["id"]: check["status"] for check in report["sources"][0]["checks"]}
            self.assertEqual(checks["repository_state"], "drift")
            self.assertEqual(checks["license_drift"], "drift")
            self.assertEqual(checks["api_drift"], "pass")

    def test_unchanged_repository_still_requires_current_maf_api_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_root(Path(directory), reviewed_commit="a" * 40)
            fixture = root / "fixture.json"
            fixture.write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "sources": {
                            "source": {
                                "link": {"status_code": 200},
                                "github": {
                                    "archived": False,
                                    "default_branch": "main",
                                    "head_sha": "a" * 40,
                                    "license_spdx": "MIT",
                                },
                            }
                        },
                    }
                ),
                encoding="utf-8",
            )
            report, exit_code = maintenance.run(self.args(root, fixture=fixture))
            self.assertEqual(exit_code, 0)
            self.assertEqual(report["status"], "needs-review")
            checks = {check["id"]: check["status"] for check in report["sources"][0]["checks"]}
            self.assertEqual(checks["version_drift"], "pass")
            self.assertEqual(checks["api_drift"], "needs-review")

    def test_network_failure_is_failed_not_pass(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_root(Path(directory), reviewed_commit="abc")
            args = self.args(root, network=True)
            with patch.object(maintenance, "network_observation", side_effect=TimeoutError("timed out")):
                report, exit_code = maintenance.run(args)
            self.assertEqual(exit_code, 1)
            self.assertEqual(report["status"], "failed")
            self.assertEqual(report["sources"][0]["status"], "failed")

    def test_private_network_target_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            maintenance.require_public_https("https://127.0.0.1/source")

    def test_review_marker_without_link_manifest_fails_collection_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_root(Path(directory), reviewed_commit="abc")
            collection = root / "docs/coding-agent-kit/knowledge/collection/project-routes.json"
            collection.write_text(json.dumps({"schema_version": 1, "items": []}), encoding="utf-8")
            reviews = root / "docs/coding-agent-kit/knowledge/external-sources/reviews"
            reviews.mkdir(parents=True)
            (reviews / "source.md").write_text(
                "# Source review: `source`\n\n- Collection action: `link and annotation only`\n",
                encoding="utf-8",
            )

            report, exit_code = maintenance.run(self.args(root))

            self.assertEqual(exit_code, 1)
            checks = {check["id"]: check for check in report["sources"][0]["checks"]}
            self.assertEqual(checks["collection_route"]["status"], "failed")
            self.assertIn("lookup manifest entry is missing", checks["collection_route"]["detail"])

    def test_link_manifest_satisfies_collection_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_root(Path(directory), reviewed_commit="abc")
            collection = root / "docs/coding-agent-kit/knowledge/collection"
            (collection / "project-routes.json").write_text(
                json.dumps({"schema_version": 1, "items": []}), encoding="utf-8"
            )
            (collection / "link-references.json").write_text(
                json.dumps({"schema_version": 1, "items": [{"id": "source", "source_id": "source"}]}),
                encoding="utf-8",
            )

            report, exit_code = maintenance.run(self.args(root))

            self.assertEqual(exit_code, 0)
            checks = {check["id"]: check for check in report["sources"][0]["checks"]}
            self.assertEqual(checks["collection_route"]["status"], "pass")

    def test_link_only_network_fixture_does_not_require_redistribution_license(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_root(Path(directory), reviewed_commit="abc")
            external = root / "docs/coding-agent-kit/knowledge/external-sources/sources.json"
            external.write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "items": [
                            {
                                "id": "source",
                                "url": "https://learn.microsoft.com/agent-framework",
                                "source_class": "official-doc",
                                "review_status": "adopted",
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            collection = root / "docs/coding-agent-kit/knowledge/collection"
            (collection / "project-routes.json").write_text('{"schema_version":1,"items":[]}', encoding="utf-8")
            (collection / "link-references.json").write_text(
                '{"schema_version":1,"items":[{"id":"source","source_id":"source"}]}', encoding="utf-8"
            )
            fixture = root / "fixture.json"
            fixture.write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "sources": {
                            "source": {
                                "link": {"status_code": 200},
                                "api": {"compatible": True, "evidence": "local comparison"},
                            }
                        },
                    }
                ),
                encoding="utf-8",
            )

            report, exit_code = maintenance.run(self.args(root, fixture=fixture))

            self.assertEqual(exit_code, 0)
            self.assertEqual(report["status"], "pass")
            checks = {check["id"]: check["status"] for check in report["sources"][0]["checks"]}
            self.assertEqual(checks["license_drift"], "pass")

    def test_invalid_fixture_is_a_machine_readable_failure(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_root(Path(directory), reviewed_commit="abc")
            fixture = root / "fixture.json"
            fixture.write_text('{"sources": []}', encoding="utf-8")
            report, exit_code = maintenance.run(self.args(root, fixture=fixture))
            self.assertEqual(exit_code, 1)
            self.assertEqual(report["status"], "failed")
            self.assertTrue(report["errors"])

    @staticmethod
    def args(root: Path, fixture: Path | None = None, network: bool = False) -> argparse.Namespace:
        return argparse.Namespace(
            root=root,
            fixture=fixture,
            network=network,
            all=False,
            source_id=None,
            timeout=1.0,
            output=None,
        )

    @staticmethod
    def make_root(root: Path, reviewed_commit: str, license_name: str | None = None) -> Path:
        external = root / "docs/coding-agent-kit/knowledge/external-sources"
        collection = root / "docs/coding-agent-kit/knowledge/collection"
        external.mkdir(parents=True)
        collection.mkdir(parents=True)
        source = {
            "id": "source",
            "url": "https://github.com/org/repo",
            "source_class": "community-repository",
            "review_status": "adopted",
            "reviewed_commit": reviewed_commit,
        }
        (external / "sources.json").write_text(
            json.dumps({"schema_version": 1, "items": [source]}), encoding="utf-8"
        )
        route = {"id": "source", "source_id": "source", "version": reviewed_commit}
        if license_name:
            route["license"] = license_name
        (collection / "project-routes.json").write_text(
            json.dumps({"schema_version": 1, "items": [route]}), encoding="utf-8"
        )
        (collection / "link-references.json").write_text(
            json.dumps({"schema_version": 1, "items": []}), encoding="utf-8"
        )
        (collection / "documents.json").write_text(
            json.dumps({"schema_version": 1, "items": []}), encoding="utf-8"
        )
        return root


if __name__ == "__main__":
    unittest.main()
