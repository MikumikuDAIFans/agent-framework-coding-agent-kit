#!/usr/bin/env python3
"""Query the generated Microsoft Agent Framework reference catalog."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


def repository_root() -> Path:
    return Path(__file__).resolve().parents[3]


def tokenize(value: str) -> list[str]:
    return [token for token in re.findall(r"[a-zA-Z0-9_.-]+", value.lower()) if len(token) > 1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Task concepts, API symbols, or behavior to locate.")
    parser.add_argument("--root", type=Path, default=repository_root(), help="Reference repository root.")
    parser.add_argument("--topic", help="Limit to one topic ID.")
    parser.add_argument("--language", choices=["any", "python", "csharp", "declarative", "typescript", "language-neutral"], default="any")
    parser.add_argument("--role", choices=["any", "documentation", "design", "sample", "implementation", "test", "schema", "configuration"], default="any")
    parser.add_argument("--limit", type=int, default=20, help="Maximum file results.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    return parser.parse_args()


def load(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as stream:
        return json.load(stream)


def choose_topics(query_tokens: list[str], catalog: dict[str, Any], requested: str | None) -> list[dict[str, Any]]:
    topics = catalog["topics"]
    if requested:
        matches = [topic for topic in topics if topic["id"] == requested]
        if not matches:
            valid = ", ".join(topic["id"] for topic in topics)
            raise ValueError(f"Unknown topic '{requested}'. Valid topics: {valid}")
        return matches
    scored: list[tuple[int, dict[str, Any]]] = []
    for topic in topics:
        haystack = " ".join([topic["id"], topic["title"], topic["description"], *topic["keywords"]]).lower()
        score = sum(5 if token in topic["id"] else 2 for token in query_tokens if token in haystack)
        if score:
            scored.append((score, topic))
    scored.sort(key=lambda item: (-item[0], item[1]["id"]))
    return [topic for _, topic in scored[:3]]


def score_entry(entry: dict[str, Any], query_tokens: list[str], selected_topics: set[str]) -> int:
    path = entry["path"].lower()
    title = entry["title"].lower()
    symbols = " ".join(entry.get("symbols", [])).lower()
    score = 0
    for token in query_tokens:
        if token in path:
            score += 6
        if token in title:
            score += 5
        if token in symbols:
            score += 8
    score += 7 * len(selected_topics.intersection(entry["topics"]))
    if entry["role"] in {"design", "sample", "test"}:
        score += 1
    return score


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    catalog_dir = root / "docs/coding-agent-kit/catalog"
    catalog = load(catalog_dir / "catalog.json")
    learn = load(catalog_dir / "learn-index.json")
    query_tokens = tokenize(args.query)
    selected_topics = choose_topics(query_tokens, catalog, args.topic)
    selected_ids = {topic["id"] for topic in selected_topics}

    curated: list[dict[str, Any]] = []
    for topic in selected_topics:
        for item in topic.get("curated", []):
            if args.language != "any" and item["language"] not in {args.language, "any", "language-neutral"}:
                continue
            if args.role != "any" and item["role"] != args.role:
                continue
            curated.append({"topic": topic["id"], **item})

    ranked: list[tuple[int, dict[str, Any]]] = []
    for entry in catalog["entries"]:
        if args.language != "any" and entry["language"] not in {args.language, "language-neutral"}:
            continue
        if args.role != "any" and entry["role"] != args.role:
            continue
        score = score_entry(entry, query_tokens, selected_ids)
        if score:
            ranked.append((score, entry))
    ranked.sort(key=lambda item: (-item[0], item[1]["path"]))
    results = [{"score": score, **entry} for score, entry in ranked[: max(1, args.limit)]]

    learn_pages = [
        page
        for page in learn["pages"]
        if selected_ids.intersection(page["topics"])
        and any(token in " ".join([page["title"], page["doc_path"], *page["section_path"]]).lower() for token in query_tokens)
    ][:10]
    if not learn_pages:
        learn_pages = [page for page in learn["pages"] if selected_ids.intersection(page["topics"])][:8]

    output = {
        "query": args.query,
        "reference_root": str(root),
        "upstream_commit": catalog["upstream_commit"],
        "topics": [{"id": topic["id"], "title": topic["title"], "description": topic["description"]} for topic in selected_topics],
        "curated": curated,
        "official_docs": learn_pages,
        "results": results,
    }
    if args.json:
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return 0

    print(f"# MAF reference lookup: {args.query}")
    print(f"\nReference commit: `{catalog['upstream_commit']}`")
    if selected_topics:
        print("\nTopics: " + ", ".join(f"`{topic['id']}`" for topic in selected_topics))
    else:
        print("\nTopics: no strong automatic match; results use direct path/title/symbol matching.")

    print("\n## Curated starting points")
    if curated:
        for item in curated:
            print(f"- `{item['topic']}` `{item['role']}` `{item['language']}` — `{item['path']}` — {item['why']}")
    else:
        print("- No curated entry matched the requested filters.")

    print("\n## Official Microsoft Learn")
    if learn_pages:
        for page in learn_pages:
            section = " / ".join(page["section_path"])
            suffix = f" — {section}" if section else ""
            print(f"- [{page['title']}]({page['url']}){suffix}")
    else:
        print("- No normalized page matched; query Microsoft Learn MCP using the same terms.")

    print("\n## Ranked repository files")
    if results:
        for entry in results:
            symbol_text = f" — symbols: {', '.join(entry['symbols'][:5])}" if entry["symbols"] else ""
            print(
                f"- score {entry['score']:>2} · `{entry['role']}` · `{entry['language']}` · "
                f"`{entry['path']}` — {entry['title']}{symbol_text}"
            )
    else:
        print("- No file matched. Use `rg` with an exact API symbol or broaden the query.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as error:
        print(f"ERROR: {error}")
        raise SystemExit(2) from error
