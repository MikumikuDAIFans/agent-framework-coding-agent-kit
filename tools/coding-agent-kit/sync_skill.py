#!/usr/bin/env python3
"""Synchronize the repository-scoped Skill into the plugin's required skills/ path."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / ".agents/skills/maf-expert"
DESTINATION = ROOT / "skills/maf-expert"
IGNORED_NAMES = {"local-reference-root.txt", "__pycache__"}


def files_under(root: Path) -> dict[str, bytes]:
    result: dict[str, bytes] = {}
    if not root.exists():
        return result
    for path in root.rglob("*"):
        if not path.is_file() or any(part in IGNORED_NAMES for part in path.parts):
            continue
        result[path.relative_to(root).as_posix()] = path.read_bytes()
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail when the plugin copy differs from the repository Skill.")
    args = parser.parse_args()

    if args.check:
        if files_under(SOURCE) != files_under(DESTINATION):
            print("Plugin Skill copy is out of date. Run: python tools/coding-agent-kit/sync_skill.py")
            return 1
        print("Plugin Skill copy is synchronized.")
        return 0

    expected_parent = (ROOT / "skills").resolve()
    if DESTINATION.parent.resolve() != expected_parent or DESTINATION.is_symlink():
        raise SystemExit(f"Refusing to replace unsafe destination: {DESTINATION}")
    if DESTINATION.exists():
        shutil.rmtree(DESTINATION)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SOURCE, DESTINATION, ignore=shutil.ignore_patterns(*IGNORED_NAMES))
    print(f"Synchronized {SOURCE.relative_to(ROOT)} -> {DESTINATION.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
