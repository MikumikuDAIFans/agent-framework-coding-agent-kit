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
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    if result.returncode:
        FAILURES.append(f"Command failed ({result.returncode}): {' '.join(command)}")
        output = "\n".join(part.strip() for part in (result.stdout, result.stderr) if part.strip())
        if output:
            FAILURES.append(output)


def validate_review_policy(path: Path) -> None:
    """Check the approved dual-track policy without judging evidence quality."""
    text = path.read_text(encoding="utf-8")
    if not re.search(r"(?m)^- Approval status: `approved`$", text):
        FAILURES.append("External source review policy is not approved.")
    if not re.search(r"(?m)^- Version: `v1\.1`$", text):
        FAILURES.append("External source review policy must use the autonomous collection rules in v1.1.")

    expected = {
        "C": {"C-01": 25, "C-02": 25, "C-03": 20, "C-04": 10, "C-05": 10, "C-06": 5, "C-07": 5},
        "A": {"A-01": 30, "A-02": 25, "A-03": 15, "A-04": 15, "A-05": 15},
    }
    rows = {
        match.group(1): int(match.group(2))
        for match in re.finditer(r"(?m)^\| ((?:C|A)-\d{2}) \|[^\n]*?\| (\d+) \|", text)
    }
    for track, weights in expected.items():
        actual = {key: rows.get(key) for key in weights}
        if actual != weights:
            FAILURES.append(f"Review policy {track}-track weights are missing or unexpected: {actual}.")
        if sum(value for value in actual.values() if value is not None) != 100:
            FAILURES.append(f"Review policy {track}-track weights must total 100.")

    required_rules = [
        "技术文章的真实 Demo 等级低于 `3`",
        "技术文章超过 24 个月",
        "Coding Agent 可独立完成候选发现、事实核对、评分、状态决定和收录",
        "vendor 外部项目代码",
        "文档不得保存正文",
    ]
    for rule in required_rules:
        if rule not in text:
            FAILURES.append(f"Review policy is missing required rule: {rule}")


def main() -> int:
    required = [
        "AGENTS.md",
        ".codex-plugin/plugin.json",
        ".mcp.json",
        ".agents/skills/maf-expert/SKILL.md",
        "skills/maf-expert/SKILL.md",
        ".agents/skills/maf-expert/agents/openai.yaml",
        ".agents/skills/maf-kit-maintainer/SKILL.md",
        "skills/maf-kit-maintainer/SKILL.md",
        ".agents/skills/maf-kit-maintainer/agents/openai.yaml",
        "docs/coding-agent-kit/README.md",
        "docs/coding-agent-kit/catalog/catalog.json",
        "docs/coding-agent-kit/catalog/learn-index.json",
        "docs/coding-agent-kit/catalog/CATALOG.md",
        "docs/coding-agent-kit/knowledge/external-sources/README.md",
        "docs/coding-agent-kit/knowledge/external-sources/REVIEW_POLICY.md",
        "docs/coding-agent-kit/knowledge/external-sources/REVIEW_QUEUE.md",
        "docs/coding-agent-kit/knowledge/external-sources/review-template.md",
        "docs/coding-agent-kit/knowledge/external-sources/sources.json",
        "docs/coding-agent-kit/knowledge/collection/README.md",
        "docs/coding-agent-kit/knowledge/collection/project-routes.json",
        "docs/coding-agent-kit/knowledge/collection/link-references.json",
        "docs/coding-agent-kit/knowledge/collection/documents.json",
        "docs/coding-agent-kit/knowledge/collection/archive.json",
        "docs/coding-agent-kit/knowledge/collection/documents/README.md",
        "docs/coding-agent-kit/knowledge/collection/KNOWLEDGE_INDEX.md",
        "tools/coding-agent-kit/indexer/topics.json",
        "tools/coding-agent-kit/indexer/upstream-base.json",
        "tools/coding-agent-kit/indexer/build_catalog.py",
        "tools/coding-agent-kit/indexer/lookup.py",
        "tools/coding-agent-kit/knowledge/collect.py",
        "tools/coding-agent-kit/knowledge/maintenance.py",
        "tools/coding-agent-kit/knowledge/discovery.py",
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

    maintainer_skill = paths[".agents/skills/maf-kit-maintainer/SKILL.md"].read_text(encoding="utf-8")
    if not re.search(r"(?m)^name: maf-kit-maintainer$", maintainer_skill):
        FAILURES.append("Maintenance Skill name frontmatter is missing.")
    for required_phrase in ("docs/coding-agent-kit", "Never push to it", "not-run", "archive"):
        if required_phrase not in maintainer_skill:
            FAILURES.append(f"Maintenance Skill is missing required boundary: {required_phrase}.")

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

    archive = load_json(paths["docs/coding-agent-kit/knowledge/collection/archive.json"])
    if archive.get("schema_version") != 1 or not isinstance(archive.get("items"), list):
        FAILURES.append("Collection archive must use schema_version 1 and an items array.")
    archive_ids: set[str] = set()
    for item in archive.get("items", []):
        required_archive_fields = {
            "source_id", "retired_at", "reason", "previous_status", "previous_version", "review", "collection_kind"
        }
        missing = required_archive_fields - item.keys()
        source_id = item.get("source_id", "<missing-id>")
        if missing:
            FAILURES.append(f"Archive item {source_id} is missing fields: {', '.join(sorted(missing))}.")
        if source_id in archive_ids:
            FAILURES.append(f"Duplicate collection archive source id: {source_id}.")
        archive_ids.add(source_id)

    external = load_json(paths["docs/coding-agent-kit/knowledge/external-sources/sources.json"])
    validate_review_policy(paths["docs/coding-agent-kit/knowledge/external-sources/REVIEW_POLICY.md"])
    if external.get("policy") != "REVIEW_POLICY.md":
        FAILURES.append("External source registry must point to REVIEW_POLICY.md.")
    external_items = external.get("items", [])
    if len(external_items) < 65:
        FAILURES.append(f"External source registry lost approved coverage: found {len(external_items)}, expected at least 65.")
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
    terminal_states = {"adopted", "context-only", "quarantined", "rejected"}
    state_counts: dict[str, int] = {state: 0 for state in allowed_states}
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
        else:
            state_counts[item["review_status"]] += 1
        if item.get("source_class") == "meta-index" and item.get("review_status") != "discovered":
            FAILURES.append(f"Discovery-only meta index {source_id} must remain in discovered state.")
        if item.get("source_class") != "meta-index" and item.get("review_status") not in terminal_states:
            FAILURES.append(f"Reviewable external source {source_id} must be terminal, not {item.get('review_status')}.")
        if item.get("priority") not in allowed_priorities:
            FAILURES.append(f"External source {source_id} has an unknown priority: {item.get('priority')}.")
        if not item.get("topics") or not item.get("languages"):
            FAILURES.append(f"External source {source_id} must declare topics and languages.")
        if item.get("review_status") in {"in-review", "adopted", "context-only", "quarantined", "rejected"}:
            review_path = item.get("review")
            if not review_path:
                FAILURES.append(f"Reviewed external source {source_id} must point to its review artifact.")
            elif not (paths["docs/coding-agent-kit/knowledge/external-sources/sources.json"].parent / review_path).exists():
                FAILURES.append(f"External source {source_id} review artifact does not exist: {review_path}.")
            else:
                review_file = paths["docs/coding-agent-kit/knowledge/external-sources/sources.json"].parent / review_path
                review_text = review_file.read_text(encoding="utf-8")
                for heading in (
                    "## Snapshot",
                    "## Direct Microsoft Agent Framework evidence",
                    "## Verification",
                    "### Hard gates",
                    "## Decision",
                ):
                    if heading not in review_text:
                        FAILURES.append(f"Review {review_path} is missing required section: {heading}.")
                state_match = re.search(r"(?m)^- State: `([^`]+)`", review_text)
                if not state_match:
                    FAILURES.append(f"Review {review_path} has no parseable decision state.")
                elif state_match.group(1) != item.get("review_status"):
                    FAILURES.append(
                        f"External source {source_id} registry/review state mismatch: "
                        f"{item.get('review_status')} != {state_match.group(1)}."
                    )
                action_match = re.search(r"(?m)^- Collection action: `([^`]+)`", review_text)
                if not action_match:
                    FAILURES.append(f"Review {review_path} has no parseable collection action.")
                elif action_match.group(1) != item.get("collection_action"):
                    FAILURES.append(
                        f"External source {source_id} registry/review collection action mismatch: "
                        f"{item.get('collection_action')} != {action_match.group(1)}."
                    )
                reviewed_at = item.get("reviewed_at", "")
                if not re.fullmatch(r"20\d{2}-\d{2}-\d{2}", reviewed_at) or reviewed_at not in review_text:
                    FAILURES.append(f"External source {source_id} must preserve its review date in reviewed_at.")
                if item.get("review_status") == "adopted":
                    allowed_actions = (
                        {"project route"}
                        if item.get("source_class") in {"official-repository", "community-repository"}
                        else {"retained Markdown", "link and annotation only"}
                    )
                    if item.get("collection_action") not in allowed_actions:
                        FAILURES.append(
                            f"Adopted source {source_id} has incompatible collection action: "
                            f"{item.get('collection_action')}."
                        )
                if item.get("source_class") in {"official-repository", "community-repository"}:
                    reviewed_commit = item.get("reviewed_commit", "")
                    if not re.fullmatch(r"[0-9a-f]{40}", reviewed_commit):
                        FAILURES.append(f"Repository source {source_id} must record a 40-character reviewed_commit.")
                    elif reviewed_commit not in review_text:
                        FAILURES.append(f"Repository source {source_id} reviewed_commit is absent from its review.")
                total_match = re.search(
                    r"(?m)^\|[^\n]*?\*\*Total\*\*\s*\|\s*\*\*100\*\*\s*\|\s*\|\s*\*\*(\d+)\*\*",
                    review_text,
                )
                if item.get("source_class") != "official-doc":
                    if not total_match:
                        FAILURES.append(f"Scored review {review_path} has no parseable total.")
                    elif item.get("review_score") != int(total_match.group(1)):
                        FAILURES.append(
                            f"External source {source_id} review_score does not match review total {total_match.group(1)}."
                        )
                elif "review_score" in item:
                    FAILURES.append(f"Official-doc source {source_id} must use the direct-adoption check, not review_score.")

    meta_indexes = [item for item in external_items if item.get("source_class") == "meta-index"]
    if len(meta_indexes) != 1 or state_counts["discovered"] != 1:
        FAILURES.append("Exactly one discovery-only meta index must remain discovered.")
    if len(external_items) - len(meta_indexes) < 64:
        FAILURES.append("External source registry must retain at least 64 independently reviewable sources.")
    if state_counts["queued"] or state_counts["in-review"]:
        FAILURES.append("No reviewable external source may remain queued or in-review.")

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
    run([sys.executable, "-m", "unittest", "discover", "tools/coding-agent-kit/knowledge/tests"])
    run([sys.executable, "-m", "unittest", "discover", "tools/coding-agent-kit/tests"])
    run([sys.executable, "tools/coding-agent-kit/knowledge/collect.py", "check"])
    run([sys.executable, "tools/coding-agent-kit/knowledge/maintenance.py"])
    run([sys.executable, "tools/coding-agent-kit/knowledge/discovery.py"])
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
