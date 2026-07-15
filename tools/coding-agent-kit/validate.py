#!/usr/bin/env python3
"""Validate the coding-agent kit without external Python dependencies."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FAILURES: list[str] = []


def require(path: str) -> Path:
    target = ROOT / path
    if not target.exists():
        FAILURES.append(f"Missing required path: {path}")
    return target


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as error:  # validation should report all useful failures
        FAILURES.append(f"Invalid JSON {path.relative_to(ROOT)}: {error}")
        return {}


def run(command: list[str]) -> None:
    result = subprocess.run(command, cwd=ROOT, text=True)
    if result.returncode:
        FAILURES.append(f"Command failed ({result.returncode}): {' '.join(command)}")


def main() -> int:
    required = [
        "AGENTS.md",
        ".codex-plugin/plugin.json",
        ".mcp.json",
        ".agents/skills/maf-expert/SKILL.md",
        "skills/maf-expert/SKILL.md",
        ".agents/skills/maf-expert/agents/openai.yaml",
        "docs/coding-agent-kit/README.md",
        "docs/coding-agent-kit/catalog/catalog.json",
        "docs/coding-agent-kit/catalog/learn-index.json",
        "docs/coding-agent-kit/catalog/CATALOG.md",
        "docs/coding-agent-kit/knowledge/external-sources/README.md",
        "docs/coding-agent-kit/knowledge/external-sources/REVIEW_QUEUE.md",
        "docs/coding-agent-kit/knowledge/external-sources/review-template.md",
        "docs/coding-agent-kit/knowledge/external-sources/sources.json",
        "tools/coding-agent-kit/indexer/topics.json",
        "tools/coding-agent-kit/indexer/upstream-base.json",
        "tools/coding-agent-kit/indexer/build_catalog.py",
        "tools/coding-agent-kit/indexer/lookup.py",
        "tools/coding-agent-kit/install.py",
    ]
    paths = {path: require(path) for path in required}

    if (ROOT / ".codex/config.toml").exists():
        FAILURES.append("Project .codex/config.toml must not be part of this kit.")

    plugin = load_json(paths[".codex-plugin/plugin.json"])
    if plugin.get("name") != "agent-framework-coding-agent-kit":
        FAILURES.append("Plugin name is missing or unexpected.")
    if plugin.get("skills") != "./skills/":
        FAILURES.append("Plugin skills path must be ./skills/.")
    if plugin.get("mcpServers") != "./.mcp.json":
        FAILURES.append("Plugin MCP path must be ./.mcp.json.")

    mcp = load_json(paths[".mcp.json"])
    learn_url = mcp.get("mcpServers", {}).get("microsoft_learn", {}).get("url")
    if learn_url != "https://learn.microsoft.com/api/mcp":
        FAILURES.append("Microsoft Learn MCP URL is missing or unexpected.")

    skill = paths[".agents/skills/maf-expert/SKILL.md"].read_text(encoding="utf-8") if paths[".agents/skills/maf-expert/SKILL.md"].exists() else ""
    if not re.search(r"(?m)^name: maf-expert$", skill):
        FAILURES.append("Skill name frontmatter is missing.")
    if "Do not trigger for generic AI" not in skill:
        FAILURES.append("Skill negative trigger boundary is missing.")
    if ".codex/config.toml" not in skill:
        FAILURES.append("Skill must explicitly state that project Codex config is not required.")

    catalog = load_json(paths["docs/coding-agent-kit/catalog/catalog.json"])
    entry_count = int(catalog.get("entry_count", 0))
    classified_count = int(catalog.get("classified_entry_count", 0))
    if entry_count < 4000:
        FAILURES.append(f"Catalog coverage unexpectedly low: {entry_count} repository files.")
    if not entry_count or classified_count / entry_count < 0.9:
        FAILURES.append(f"Catalog topic classification below 90%: {classified_count}/{entry_count}.")
    topics = catalog.get("topics", [])
    if len(topics) < 15:
        FAILURES.append(f"Catalog has too few topics: {len(topics)}.")
    for topic in topics:
        if len(topic.get("curated", [])) < 3:
            FAILURES.append(f"Topic {topic.get('id')} has fewer than three curated references.")
        if not topic.get("entry_counts"):
            FAILURES.append(f"Topic {topic.get('id')} has no indexed repository coverage.")

    learn = load_json(paths["docs/coding-agent-kit/catalog/learn-index.json"])
    if int(learn.get("page_count", 0)) < 100:
        FAILURES.append(f"Microsoft Learn metadata coverage unexpectedly low: {learn.get('page_count', 0)} pages.")

    external = load_json(paths["docs/coding-agent-kit/knowledge/external-sources/sources.json"])
    external_items = external.get("items", [])
    if len(external_items) < 50:
        FAILURES.append(f"External source discovery coverage unexpectedly low: {len(external_items)} sources.")
    allowed_classes = {
        "official-doc",
        "official-engineering",
        "official-repository",
        "community-repository",
        "community-article",
        "meta-index",
    }
    allowed_states = {"discovered", "queued", "in-review", "adopted", "context-only", "quarantined", "rejected"}
    allowed_priorities = {"P0", "P1", "P2", "P3"}
    seen_ids: set[str] = set()
    seen_urls: set[str] = set()
    required_external_fields = {
        "id",
        "name",
        "url",
        "source_class",
        "authority",
        "topics",
        "languages",
        "review_status",
        "priority",
        "why",
    }
    for item in external_items:
        missing = required_external_fields - item.keys()
        source_id = item.get("id", "<missing-id>")
        if missing:
            FAILURES.append(f"External source {source_id} is missing fields: {', '.join(sorted(missing))}.")
        if source_id in seen_ids:
            FAILURES.append(f"Duplicate external source id: {source_id}.")
        seen_ids.add(source_id)
        url = item.get("url", "")
        if url in seen_urls:
            FAILURES.append(f"Duplicate external source URL: {url}.")
        seen_urls.add(url)
        if not url.startswith("https://"):
            FAILURES.append(f"External source {source_id} must use an HTTPS URL.")
        if item.get("source_class") not in allowed_classes:
            FAILURES.append(f"External source {source_id} has an unknown class: {item.get('source_class')}.")
        if item.get("review_status") not in allowed_states:
            FAILURES.append(f"External source {source_id} has an unknown review state: {item.get('review_status')}.")
        if item.get("priority") not in allowed_priorities:
            FAILURES.append(f"External source {source_id} has an unknown priority: {item.get('priority')}.")
        if not item.get("topics") or not item.get("languages"):
            FAILURES.append(f"External source {source_id} must declare topics and languages.")
        if item.get("review_status") in {"adopted", "context-only", "quarantined", "rejected"}:
            review_path = item.get("review")
            if not review_path:
                FAILURES.append(f"Reviewed external source {source_id} must point to its review artifact.")
            elif not (paths["docs/coding-agent-kit/knowledge/external-sources/sources.json"].parent / review_path).exists():
                FAILURES.append(f"External source {source_id} review artifact does not exist: {review_path}.")
            score = item.get("review_score")
            if not isinstance(score, int) or not 0 <= score <= 40:
                FAILURES.append(f"Reviewed external source {source_id} must have an integer review score from 0 to 40.")

    scan_roots = [ROOT / ".agents", ROOT / ".codex-plugin", ROOT / "docs/coding-agent-kit", ROOT / "tools/coding-agent-kit"]
    machine_path = re.compile(r"(?:[A-Za-z]:\\Users\\|/home/[^/]+/|/Users/[^/]+/)")
    for scan_root in scan_roots:
        if not scan_root.exists():
            continue
        for path in scan_root.rglob("*"):
            if path.resolve() == Path(__file__).resolve():
                continue
            if path.is_file() and path.suffix.lower() in {".md", ".json", ".py", ".ps1", ".yaml", ".yml"}:
                text = path.read_text(encoding="utf-8", errors="replace")
                if machine_path.search(text):
                    FAILURES.append(f"Machine-specific absolute path found: {path.relative_to(ROOT)}")

    markdown_roots = [ROOT / "docs/coding-agent-kit", ROOT / ".agents/skills/maf-expert"]
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for markdown_root in markdown_roots:
        for path in markdown_root.rglob("*.md"):
            text = path.read_text(encoding="utf-8", errors="replace")
            for raw_target in link_pattern.findall(text):
                target = raw_target.strip().split("#", 1)[0]
                if not target or target.startswith(("http://", "https://", "mailto:")):
                    continue
                resolved = (path.parent / target).resolve()
                if not resolved.exists():
                    FAILURES.append(f"Broken local Markdown link in {path.relative_to(ROOT)}: {raw_target}")

    run([sys.executable, "tools/coding-agent-kit/sync_skill.py", "--check"])
    run([sys.executable, "tools/coding-agent-kit/indexer/build_catalog.py", "--check"])
    run([sys.executable, "-m", "unittest", "discover", "tools/coding-agent-kit/indexer/tests"])
    run([sys.executable, "tools/coding-agent-kit/install.py", "--scope", "user", "--dry-run"])

    if FAILURES:
        print("Coding-agent kit validation failed:")
        for failure in FAILURES:
            print(f"- {failure}")
        return 1
    print("Coding-agent kit validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
