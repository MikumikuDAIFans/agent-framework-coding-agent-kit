#!/usr/bin/env python3
"""Synchronize repository-scoped Skills into the plugin's required skills/ path."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = ROOT / ".agents/skills"
DESTINATION_ROOT = ROOT / "skills"
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

    skill_names = sorted(path.name for path in SOURCE_ROOT.iterdir() if path.is_dir() and (path / "SKILL.md").is_file())
    if not skill_names:
        raise SystemExit(f"No repository Skills found under {SOURCE_ROOT.relative_to(ROOT)}")

    if args.check:
        destination_names = sorted(
            path.name for path in DESTINATION_ROOT.iterdir() if path.is_dir() and (path / "SKILL.md").is_file()
        ) if DESTINATION_ROOT.exists() else []
        if skill_names != destination_names:
            print("Plugin Skill set is out of date. Run: python tools/coding-agent-kit/sync_skill.py")
            return 1
        for name in skill_names:
            if files_under(SOURCE_ROOT / name) != files_under(DESTINATION_ROOT / name):
                print(f"Plugin Skill copy is out of date: {name}. Run: python tools/coding-agent-kit/sync_skill.py")
                return 1
        print(f"Plugin Skill copies are synchronized: {', '.join(skill_names)}.")
        return 0

    if DESTINATION_ROOT.is_symlink() or DESTINATION_ROOT.resolve() != (ROOT / "skills").resolve():
        raise SystemExit(f"Refusing to replace unsafe destination root: {DESTINATION_ROOT}")
    DESTINATION_ROOT.mkdir(parents=True, exist_ok=True)
    for path in DESTINATION_ROOT.iterdir():
        if path.is_dir() and path.name not in skill_names and (path / "SKILL.md").is_file():
            shutil.rmtree(path)
    for name in skill_names:
        source = SOURCE_ROOT / name
        destination = DESTINATION_ROOT / name
        if destination.is_symlink():
            raise SystemExit(f"Refusing to replace unsafe destination: {destination}")
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(source, destination, ignore=shutil.ignore_patterns(*IGNORED_NAMES))
        print(f"Synchronized {source.relative_to(ROOT)} -> {destination.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
