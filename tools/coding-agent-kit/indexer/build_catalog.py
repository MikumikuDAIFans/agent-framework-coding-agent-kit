#!/usr/bin/env python3
"""Build deterministic Microsoft Agent Framework reference catalogs.

The generator uses only the Python standard library. It indexes repository paths,
lightweight titles/symbols, curated topic metadata, and normalized Microsoft Learn
page metadata. It never downloads or stores Microsoft Learn page bodies.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path, PurePosixPath
from typing import Any, Iterable
from urllib.parse import urlparse


SUPPORTED_SUFFIXES = {
    ".cs",
    ".csproj",
    ".json",
    ".js",
    ".jsx",
    ".md",
    ".py",
    ".pyi",
    ".toml",
    ".ts",
    ".tsx",
    ".yaml",
    ".yml",
}
SKIP_PARTS = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "bin",
    "node_modules",
    "obj",
}
GENERATED_DIR = PurePosixPath("docs/coding-agent-kit/catalog")


def repository_root() -> Path:
    return Path(__file__).resolve().parents[3]


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as stream:
        return json.load(stream)


def validate_upstream_commit(root: Path, commit: str) -> None:
    subprocess.run(
        ["git", "cat-file", "-e", f"{commit}^{{commit}}"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )


def iter_source_files(root: Path, source_roots: Iterable[str]) -> Iterable[Path]:
    for source_root in source_roots:
        base = root / source_root
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in SUPPORTED_SUFFIXES:
                continue
            relative = PurePosixPath(path.relative_to(root).as_posix())
            if any(part in SKIP_PARTS for part in relative.parts):
                continue
            if relative == GENERATED_DIR or GENERATED_DIR in relative.parents:
                continue
            if PurePosixPath("docs/coding-agent-kit") in relative.parents:
                continue
            yield path


def classify_role(relative: PurePosixPath) -> str:
    lower_parts = [part.lower() for part in relative.parts]
    lower_path = relative.as_posix().lower()
    if "samples" in lower_parts or "sample" in lower_parts:
        return "sample"
    if "tests" in lower_parts or "test" in lower_parts or "integrationtests" in lower_path or "unittests" in lower_path:
        return "test"
    if lower_parts[0] == "docs":
        if "decisions" in lower_parts or "design" in lower_parts or "specs" in lower_parts or "features" in lower_parts:
            return "design"
        return "documentation"
    if lower_parts[0] == "schemas":
        return "schema"
    if lower_parts[0] == "declarative-agents":
        return "sample"
    if "src" in lower_parts or "packages" in lower_parts:
        return "implementation"
    return "configuration"


def detect_language(relative: PurePosixPath) -> str:
    suffix = relative.suffix.lower()
    if suffix in {".cs", ".csproj"} or relative.parts[0] == "dotnet":
        return "csharp"
    if suffix in {".py", ".pyi", ".toml"} or relative.parts[0] == "python":
        return "python"
    if suffix in {".yaml", ".yml", ".json"} or relative.parts[0] in {"schemas", "declarative-agents"}:
        return "declarative"
    if suffix in {".ts", ".tsx", ".js", ".jsx"}:
        return "typescript"
    return "language-neutral"


def read_prefix(path: Path, limit: int = 32768) -> str:
    try:
        with path.open("r", encoding="utf-8", errors="replace") as stream:
            return stream.read(limit)
    except OSError:
        return ""


def humanize_stem(stem: str) -> str:
    value = re.sub(r"[_-]+", " ", stem)
    value = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", value)
    return " ".join(value.split()).strip() or stem


def extract_title_and_symbols(path: Path, relative: PurePosixPath) -> tuple[str, list[str]]:
    title = humanize_stem(path.stem)
    symbols: list[str] = []
    if path.suffix.lower() == ".md":
        text = read_prefix(path)
        heading = re.search(r"(?m)^#\s+(.+?)\s*$", text)
        if heading:
            title = heading.group(1).strip()
    elif path.suffix.lower() == ".cs":
        # Public .NET files conventionally use the primary type as the filename.
        # Avoid opening thousands of source/sample files during every catalog check.
        if path.stem.lower() not in {"program", "assemblyinfo", "globalusings"}:
            symbols = [path.stem]
    elif path.suffix.lower() in {".py", ".pyi"}:
        # Python module names are retained as deterministic search hints. Exact
        # public symbols are verified with rg after the catalog narrows the route.
        if path.stem not in {"__init__", "conftest"}:
            symbols = [path.stem]
    elif path.suffix.lower() in {".json", ".yaml", ".yml"}:
        title = humanize_stem(relative.stem)
    return title[:240], sorted(set(symbols), key=symbols.index)


def score_topics(
    searchable_path: str,
    title: str,
    symbols: Iterable[str],
    topics: list[dict[str, Any]],
) -> list[tuple[str, int]]:
    path_lower = searchable_path.lower()
    text_lower = " ".join([searchable_path, title, *symbols]).lower()
    scores: list[tuple[str, int]] = []
    for topic in topics:
        score = 0
        for pattern in topic.get("path_patterns", []):
            if fnmatch.fnmatch(path_lower, pattern.lower()):
                score += 12
        for keyword in topic.get("keywords", []):
            keyword_lower = keyword.lower()
            if keyword_lower in path_lower:
                score += 4 + keyword_lower.count(" ")
            elif keyword_lower in text_lower:
                score += 2 + keyword_lower.count(" ")
        if score:
            scores.append((topic["id"], score))
    if not scores:
        return []
    scores.sort(key=lambda item: (-item[1], item[0]))
    threshold = max(4, int(scores[0][1] * 0.6))
    return [item for item in scores if item[1] >= threshold][:3]


def build_source_entries(root: Path, config: dict[str, Any]) -> list[dict[str, Any]]:
    topics = config["topics"]
    entries: list[dict[str, Any]] = []
    for path in sorted(iter_source_files(root, config["source_roots"]), key=lambda item: item.as_posix().lower()):
        relative = PurePosixPath(path.relative_to(root).as_posix())
        title, symbols = extract_title_and_symbols(path, relative)
        scored_topics = score_topics(relative.as_posix(), title, symbols, topics)
        entries.append(
            {
                "path": relative.as_posix(),
                "title": title,
                "role": classify_role(relative),
                "language": detect_language(relative),
                "topics": [topic for topic, _ in scored_topics],
                "symbols": symbols,
            }
        )
    return entries


def import_learn_manifest(path: Path) -> dict[str, Any]:
    raw = load_json(path)
    pages: list[dict[str, Any]] = []
    for result in raw.get("results", []):
        if result.get("status") != "ok":
            continue
        url = str(result.get("url", ""))
        if urlparse(url).hostname != "learn.microsoft.com":
            raise ValueError(f"Learn manifest contains a non-Microsoft URL: {url}")
        pages.append(
            {
                "title": str(result.get("title", "")).strip(),
                "section_path": [str(item) for item in result.get("section_path", [])],
                "url": url,
                "markdown_url": str(result.get("markdown_url", "")),
                "doc_path": str(result.get("file", "")).replace("\\", "/"),
            }
        )
    pages.sort(key=lambda item: (item["section_path"], item["title"], item["url"]))
    return {
        "schema_version": 1,
        "source": raw.get("source", "https://learn.microsoft.com/agent-framework/"),
        "source_generated_at": raw.get("generated_at", "unknown"),
        "pages": pages,
    }


def build_learn_index(data: dict[str, Any], topics: list[dict[str, Any]]) -> dict[str, Any]:
    pages: list[dict[str, Any]] = []
    for page in data.get("pages", []):
        searchable = " ".join([page.get("doc_path", ""), *page.get("section_path", [])])
        scored = score_topics(searchable, page.get("title", ""), [], topics)
        pages.append({**page, "topics": [topic for topic, _ in scored]})
    return {
        "schema_version": 1,
        "source": data.get("source"),
        "source_generated_at": data.get("source_generated_at"),
        "page_count": len(pages),
        "pages": pages,
    }


def validate_curated_paths(root: Path, topics: list[dict[str, Any]]) -> None:
    missing: list[str] = []
    for topic in topics:
        for entry in topic.get("curated", []):
            if not (root / entry["path"]).exists():
                missing.append(f"{topic['id']}: {entry['path']}")
    if missing:
        raise FileNotFoundError("Curated paths do not exist:\n- " + "\n- ".join(missing))


def count_by_topic(entries: list[dict[str, Any]]) -> dict[str, Counter[tuple[str, str]]]:
    counts: dict[str, Counter[tuple[str, str]]] = defaultdict(Counter)
    for entry in entries:
        for topic in entry["topics"]:
            counts[topic][(entry["role"], entry["language"])] += 1
    return counts


def build_catalog_json(
    root: Path,
    commit: str,
    config: dict[str, Any],
    entries: list[dict[str, Any]],
    learn_index: dict[str, Any],
) -> dict[str, Any]:
    counts = count_by_topic(entries)
    learn_counts = Counter(topic for page in learn_index["pages"] for topic in page["topics"])
    topics_output: list[dict[str, Any]] = []
    for topic in config["topics"]:
        topic_counts = [
            {"role": role, "language": language, "count": count}
            for (role, language), count in sorted(counts[topic["id"]].items())
        ]
        topics_output.append(
            {
                "id": topic["id"],
                "title": topic["title"],
                "description": topic["description"],
                "keywords": topic["keywords"],
                "curated": topic.get("curated", []),
                "learn_page_count": learn_counts[topic["id"]],
                "entry_counts": topic_counts,
            }
        )
    return {
        "schema_version": 1,
        "upstream_repository": "https://github.com/microsoft/agent-framework",
        "upstream_commit": commit,
        "entry_count": len(entries),
        "classified_entry_count": sum(bool(entry["topics"]) for entry in entries),
        "topics": topics_output,
        "entries": entries,
    }


def markdown_link(path: str, catalog_dir: Path, root: Path) -> str:
    target = root / path
    try:
        relative = target.relative_to(catalog_dir)
    except ValueError:
        relative = Path("../../..") / path
    return relative.as_posix()


def render_markdown(
    root: Path,
    commit: str,
    config: dict[str, Any],
    entries: list[dict[str, Any]],
    learn_index: dict[str, Any],
) -> str:
    catalog_dir = root / "docs/coding-agent-kit/catalog"
    by_topic: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in entries:
        for topic in entry["topics"]:
            by_topic[topic].append(entry)
    learn_by_topic: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for page in learn_index["pages"]:
        for topic in page["topics"]:
            learn_by_topic[topic].append(page)

    lines = [
        "# Microsoft Agent Framework reference catalog",
        "",
        "> Generated by `tools/coding-agent-kit/indexer/build_catalog.py`. Do not edit by hand.",
        "",
        f"- Upstream commit: `{commit}`",
        f"- Indexed repository files: `{len(entries)}`",
        f"- Microsoft Learn metadata pages: `{len(learn_index['pages'])}`",
        "",
        "Use `python tools/coding-agent-kit/indexer/lookup.py \"<query>\"` for ranked task-specific results.",
        "",
        "## Topic index",
        "",
    ]
    for topic in config["topics"]:
        lines.append(f"- [{topic['title']}](#{topic['id']}) (`{topic['id']}`)")
    lines.append("")

    for topic in config["topics"]:
        topic_id = topic["id"]
        lines.extend(
            [
                f"## {topic['title']}",
                f"<a id=\"{topic_id}\"></a>",
                "",
                topic["description"],
                "",
                f"Query: `python tools/coding-agent-kit/indexer/lookup.py \"{' '.join(topic['keywords'][:3])}\" --topic {topic_id}`",
                "",
                "### Curated starting points",
                "",
                "| Role | Language | Reference | Why |",
                "| --- | --- | --- | --- |",
            ]
        )
        for item in topic.get("curated", []):
            link = markdown_link(item["path"], catalog_dir, root)
            lines.append(f"| {item['role']} | {item['language']} | [`{item['path']}`]({link}) | {item['why']} |")

        pages = sorted(learn_by_topic[topic_id], key=lambda item: (item["section_path"], item["title"]))[:8]
        lines.extend(["", "### Official Microsoft Learn", ""])
        if pages:
            for page in pages:
                section = " / ".join(page["section_path"])
                suffix = f" — {section}" if section else ""
                lines.append(f"- [{page['title']}]({page['url']}){suffix}")
        else:
            lines.append("- No page matched automatically; use Microsoft Learn MCP with the topic keywords.")

        topic_entries = sorted(by_topic[topic_id], key=lambda item: (item["role"], item["language"], item["path"]))
        counts = Counter((item["role"], item["language"]) for item in topic_entries)
        lines.extend(["", "### Indexed coverage", "", "| Role | Language | Files |", "| --- | --- | ---: |"])
        for (role, language), count in sorted(counts.items()):
            lines.append(f"| {role} | {language} | {count} |")

        lines.extend(["", "### Additional high-signal files", ""])
        chosen: list[dict[str, Any]] = []
        for role in ("design", "sample", "implementation", "test", "schema"):
            for language in ("python", "csharp", "declarative", "language-neutral"):
                matches = [item for item in topic_entries if item["role"] == role and item["language"] == language]
                chosen.extend(matches[:2])
        seen: set[str] = set()
        for item in chosen:
            if item["path"] in seen:
                continue
            seen.add(item["path"])
            link = markdown_link(item["path"], catalog_dir, root)
            lines.append(f"- `{item['role']}` / `{item['language']}` — [{item['title']}]({link}) (`{item['path']}`)")
        if not seen:
            lines.append("- No automatically classified files.")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def json_text(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=False) + "\n"


def write_or_check(path: Path, content: str, check: bool) -> bool:
    if check:
        existing = path.read_text(encoding="utf-8") if path.exists() else None
        if existing != content:
            print(f"OUT OF DATE: {path}", file=sys.stderr)
            return False
        return True
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")
    print(f"WROTE: {path}")
    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=repository_root(), help="Repository root to index.")
    parser.add_argument("--learn-manifest", type=Path, help="Import a local Microsoft Learn mirror manifest.")
    parser.add_argument("--check", action="store_true", help="Fail if committed generated files are out of date.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    indexer_dir = root / "tools/coding-agent-kit/indexer"
    config = load_json(indexer_dir / "topics.json")
    validate_curated_paths(root, config["topics"])

    learn_data_path = indexer_dir / "data/learn-pages.json"
    if args.learn_manifest:
        learn_data = import_learn_manifest(args.learn_manifest.resolve())
        if not args.check:
            learn_data_path.parent.mkdir(parents=True, exist_ok=True)
            learn_data_path.write_text(json_text(learn_data), encoding="utf-8", newline="\n")
            print(f"WROTE: {learn_data_path}")
    elif learn_data_path.exists():
        learn_data = load_json(learn_data_path)
    else:
        learn_data = {"schema_version": 1, "source": "https://learn.microsoft.com/agent-framework/", "source_generated_at": "unknown", "pages": []}

    upstream_base = load_json(indexer_dir / "upstream-base.json")
    commit = str(upstream_base["commit"])
    validate_upstream_commit(root, commit)
    entries = build_source_entries(root, config)
    learn_index = build_learn_index(learn_data, config["topics"])
    catalog = build_catalog_json(root, commit, config, entries, learn_index)
    catalog_dir = root / "docs/coding-agent-kit/catalog"

    checks = [
        write_or_check(catalog_dir / "catalog.json", json_text(catalog), args.check),
        write_or_check(catalog_dir / "learn-index.json", json_text(learn_index), args.check),
        write_or_check(catalog_dir / "CATALOG.md", render_markdown(root, commit, config, entries, learn_index), args.check),
    ]
    if not all(checks):
        return 1
    print(
        f"Catalog {'check' if args.check else 'generation'} passed: "
        f"{len(entries)} repository files, {len(learn_index['pages'])} Learn pages, {len(config['topics'])} topics."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
