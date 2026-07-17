#!/usr/bin/env python3
"""Install the MAF expert Skill without changing Codex configuration."""

from __future__ import annotations

import argparse
import os
import shutil
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / ".agents/skills/maf-expert"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scope", choices=["user", "repo"], default="user")
    parser.add_argument("--target", type=Path, help="Target repository for --scope repo; defaults to the current directory.")
    parser.add_argument("--reference-root", type=Path, default=ROOT, help="Checkout containing the generated catalog and upstream source.")
    parser.add_argument("--force", action="store_true", help="Back up and replace an existing maf-expert Skill.")
    parser.add_argument("--dry-run", action="store_true", help="Show the destination without writing files.")
    return parser.parse_args()


def destination(args: argparse.Namespace) -> Path:
    if args.scope == "user":
        codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
        return (codex_home / "skills/maf-expert").resolve()
    target = (args.target or Path.cwd()).resolve()
    return (target / ".agents/skills/maf-expert").resolve()


def main() -> int:
    args = parse_args()
    target = destination(args)
    reference_root = args.reference_root.resolve()
    catalog = reference_root / "docs/coding-agent-kit/catalog/catalog.json"
    if not SOURCE.exists():
        raise SystemExit(f"Skill source is missing: {SOURCE}")
    if not catalog.exists():
        raise SystemExit(f"Reference root does not contain the generated catalog: {catalog}")
    if target == SOURCE.resolve():
        raise SystemExit("Refusing to install onto the kit's own Skill source.")

    print(f"Skill source: {SOURCE}")
    print(f"Destination: {target}")
    print(f"Reference root: {reference_root}")
    if args.dry_run:
        print("Dry run completed; no files changed.")
        return 0

    if target.exists():
        if not args.force:
            raise SystemExit("Destination exists. Review it, then rerun with --force to preserve a backup and replace it.")
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
        backup = target.with_name(f"{target.name}.backup-{stamp}")
        suffix = 1
        while backup.exists():
            backup = target.with_name(f"{target.name}.backup-{stamp}-{suffix}")
            suffix += 1
        target.rename(backup)
        print(f"Preserved existing Skill: {backup}")

    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SOURCE, target)
    marker = target / "references/local-reference-root.txt"
    marker.write_text(str(reference_root) + "\n", encoding="utf-8")
    print("Installed maf-expert without modifying Codex config or permissions.")
    print("Restart Codex or open a new task if the Skill does not appear automatically.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
