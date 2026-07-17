from __future__ import annotations

import importlib.util
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


INSTALL_PATH = Path(__file__).resolve().parents[1] / "install.py"


def load_install_module():
    spec = importlib.util.spec_from_file_location("coding_agent_kit_install", INSTALL_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load installer from {INSTALL_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class InstallTests(unittest.TestCase):
    def setUp(self) -> None:
        self.install = load_install_module()

    def test_user_destination_is_absolute_and_resolved(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            codex_home = Path(temp_dir) / "nested" / ".." / "codex-home"
            args = self.install.argparse.Namespace(scope="user", target=None)

            with patch.dict(os.environ, {"CODEX_HOME": str(codex_home)}):
                destination = self.install.destination(args)

            self.assertTrue(destination.is_absolute())
            self.assertEqual(destination, (Path(temp_dir) / "codex-home" / "skills" / "maf-expert").resolve())

    def test_refuses_to_install_over_kit_skill_source(self) -> None:
        reference_root = self.install.ROOT
        argv = [
            str(INSTALL_PATH),
            "--scope",
            "repo",
            "--target",
            str(reference_root),
            "--dry-run",
        ]

        with patch.object(sys, "argv", argv):
            with self.assertRaisesRegex(SystemExit, "Refusing to install onto the kit's own Skill source"):
                self.install.main()

    def test_force_install_avoids_existing_backup_names(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "source"
            (source / "references").mkdir(parents=True)
            (source / "SKILL.md").write_text("test skill\n", encoding="utf-8")

            reference_root = root / "reference"
            catalog = reference_root / "docs" / "coding-agent-kit" / "catalog" / "catalog.json"
            catalog.parent.mkdir(parents=True)
            catalog.write_text("{}\n", encoding="utf-8")

            target_repo = root / "target-repo"
            target = target_repo / ".agents" / "skills" / "maf-expert"
            target.mkdir(parents=True)
            (target / "old.txt").write_text("old\n", encoding="utf-8")

            stamp = "20260717-120000-123456"
            target.with_name(f"maf-expert.backup-{stamp}").mkdir()
            target.with_name(f"maf-expert.backup-{stamp}-1").mkdir()

            argv = [
                str(INSTALL_PATH),
                "--scope",
                "repo",
                "--target",
                str(target_repo),
                "--reference-root",
                str(reference_root),
                "--force",
            ]
            with (
                patch.object(self.install, "SOURCE", source),
                patch.object(self.install, "datetime") as datetime_mock,
                patch.object(sys, "argv", argv),
            ):
                datetime_mock.now.return_value.strftime.return_value = stamp
                self.assertEqual(self.install.main(), 0)

            backup = target.with_name(f"maf-expert.backup-{stamp}-2")
            self.assertEqual((backup / "old.txt").read_text(encoding="utf-8"), "old\n")
            self.assertEqual((target / "SKILL.md").read_text(encoding="utf-8"), "test skill\n")
            marker = target / "references" / "local-reference-root.txt"
            self.assertEqual(marker.read_text(encoding="utf-8"), str(reference_root.resolve()) + "\n")


if __name__ == "__main__":
    unittest.main()
