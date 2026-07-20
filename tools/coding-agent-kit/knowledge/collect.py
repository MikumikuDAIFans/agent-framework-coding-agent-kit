#!/usr/bin/env python3
"""Collect adopted external routes, link references, and redistributable documents."""

from __future__ import annotations

import argparse
import hashlib
import html
import ipaddress
import json
import re
import sys
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen


MAX_DOWNLOAD_BYTES = 5 * 1024 * 1024
ALLOWED_CONTENT_TYPES = {"text/html", "text/markdown", "text/plain", "application/xhtml+xml"}


def repository_root() -> Path:
    return Path(__file__).resolve().parents[3]


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as stream:
        return json.load(stream)


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def normalize_space(value: str) -> str:
    return " ".join(value.split())


def require_https(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError(f"Only absolute HTTPS URLs are allowed: {url}")
    hostname = parsed.hostname.lower().rstrip(".")
    if hostname == "localhost" or hostname.endswith(".localhost") or hostname.endswith(".local"):
        raise ValueError(f"Local network document URLs are not allowed: {url}")
    try:
        address = ipaddress.ip_address(hostname)
    except ValueError:
        return
    if not address.is_global:
        raise ValueError(f"Private or non-global document URLs are not allowed: {url}")


def require_iso_date(value: str) -> None:
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise ValueError(f"Expected an ISO date or datetime: {value}") from error


def require_immutable_version(value: str) -> None:
    if value.strip().lower() in {"main", "master", "head", "latest", "default"}:
        raise ValueError(f"Project version must be an immutable commit, tag, or release: {value}")


def fetch(url: str, timeout: int, max_bytes: int) -> tuple[bytes, str, str]:
    require_https(url)
    request = Request(url, headers={"User-Agent": "agent-framework-coding-agent-kit/1.0"})
    with urlopen(request, timeout=timeout) as response:  # noqa: S310 - HTTPS is checked before and after redirects
        final_url = response.geturl()
        require_https(final_url)
        content_type = response.headers.get_content_type().lower()
        if content_type not in ALLOWED_CONTENT_TYPES:
            raise ValueError(f"Unsupported document content type: {content_type}")
        declared = response.headers.get("Content-Length")
        if declared and int(declared) > max_bytes:
            raise ValueError(f"Document exceeds the {max_bytes}-byte limit.")
        payload = response.read(max_bytes + 1)
    if len(payload) > max_bytes:
        raise ValueError(f"Document exceeds the {max_bytes}-byte limit.")
    return payload, content_type, final_url


class MarkdownHTMLParser(HTMLParser):
    """Small deterministic HTML-to-Markdown converter for reviewed technical pages."""

    SKIP_TAGS = {"script", "style", "svg", "nav", "footer", "form"}

    def __init__(self, base_url: str) -> None:
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.parts: list[str] = []
        self.skip_depth = 0
        self.pre_depth = 0
        self.links: list[str | None] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        if tag in self.SKIP_TAGS:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        attributes = dict(attrs)
        if re.fullmatch(r"h[1-6]", tag):
            self.parts.append("\n\n" + "#" * int(tag[1]) + " ")
        elif tag in {"p", "div", "section", "article", "table", "tr"}:
            self.parts.append("\n\n")
        elif tag == "br":
            self.parts.append("\n")
        elif tag == "li":
            self.parts.append("\n- ")
        elif tag == "blockquote":
            self.parts.append("\n\n> ")
        elif tag == "pre":
            self.pre_depth += 1
            self.parts.append("\n\n```\n")
        elif tag == "code" and not self.pre_depth:
            self.parts.append("`")
        elif tag in {"strong", "b"}:
            self.parts.append("**")
        elif tag in {"em", "i"}:
            self.parts.append("*")
        elif tag == "a":
            href = attributes.get("href")
            if href:
                href = urljoin(self.base_url, href)
                if urlparse(href).scheme not in {"http", "https"}:
                    href = None
            self.links.append(href)
            self.parts.append("[")

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in self.SKIP_TAGS:
            if self.skip_depth:
                self.skip_depth -= 1
            return
        if self.skip_depth:
            return
        if tag == "pre" and self.pre_depth:
            self.pre_depth -= 1
            self.parts.append("\n```\n")
        elif tag == "code" and not self.pre_depth:
            self.parts.append("`")
        elif tag in {"strong", "b"}:
            self.parts.append("**")
        elif tag in {"em", "i"}:
            self.parts.append("*")
        elif tag == "a":
            href = self.links.pop() if self.links else None
            self.parts.append(f"]({href})" if href else "]")
        elif re.fullmatch(r"h[1-6]", tag) or tag in {"p", "article", "section"}:
            self.parts.append("\n\n")

    def handle_data(self, data: str) -> None:
        if self.skip_depth or not data:
            return
        if self.pre_depth:
            self.parts.append(data)
        else:
            self.parts.append(re.sub(r"\s+", " ", data))

    def markdown(self) -> str:
        value = html.unescape("".join(self.parts)).replace("\r\n", "\n")
        value = re.sub(r"[ \t]+\n", "\n", value)
        value = re.sub(r"\n{3,}", "\n\n", value)
        return value.strip() + "\n"


def to_markdown(payload: bytes, content_type: str, source_url: str) -> tuple[str, str]:
    text = payload.decode("utf-8", errors="replace").lstrip("\ufeff")
    if content_type == "text/markdown" or urlparse(source_url).path.lower().endswith((".md", ".markdown")):
        return text.replace("\r\n", "\n").strip() + "\n", "markdown-normalize"
    if content_type in {"text/html", "application/xhtml+xml"} or re.search(r"<html|<article|<main", text[:2048], re.I):
        parser = MarkdownHTMLParser(source_url)
        parser.feed(text)
        return parser.markdown(), "html-to-markdown"
    return text.replace("\r\n", "\n").strip() + "\n", "plain-text"


def source_map(root: Path) -> dict[str, dict[str, Any]]:
    path = root / "docs/coding-agent-kit/knowledge/external-sources/sources.json"
    return {item["id"]: item for item in load_json(path).get("items", [])}


def adopted_source(root: Path, source_id: str) -> dict[str, Any]:
    source = source_map(root).get(source_id)
    if not source:
        raise ValueError(f"Unknown external source: {source_id}")
    if source.get("review_status") != "adopted":
        raise ValueError(f"External source must be adopted before collection: {source_id}")
    if not source.get("review"):
        raise ValueError(f"Adopted source has no review artifact: {source_id}")
    return source


def collection_paths(root: Path) -> tuple[Path, Path, Path, Path]:
    base = root / "docs/coding-agent-kit/knowledge/collection"
    return (
        base / "project-routes.json",
        base / "link-references.json",
        base / "documents.json",
        base / "KNOWLEDGE_INDEX.md",
    )


def upsert(items: list[dict[str, Any]], entry: dict[str, Any]) -> None:
    items[:] = [item for item in items if item.get("id") != entry["id"]]
    items.append(entry)
    items.sort(key=lambda item: item["id"])


def table_cell(value: Any) -> str:
    return normalize_space(str(value)).replace("|", "\\|")


def render_index(projects: dict[str, Any], links: dict[str, Any], documents: dict[str, Any]) -> str:
    lines = [
        "# Adopted external knowledge",
        "",
        "> Generated by `tools/coding-agent-kit/knowledge/collect.py`. Do not edit by hand.",
        "",
        "## Project routes",
        "",
    ]
    if projects.get("items"):
        lines.extend(["| Project | Topics | Version | Route | Boundaries |", "| --- | --- | --- | --- | --- |"])
        for item in projects["items"]:
            lines.append(
                f"| [{table_cell(item['title'])}]({item['url']}) | {', '.join(item['topics'])} | `{item['version']}` | "
                f"{table_cell(item['route'])} {table_cell(item['design'])} | {table_cell(item['limitations'])} |"
            )
    else:
        lines.append("- No adopted project routes.")
    lines.extend(["", "## Link and annotation references", ""])
    if links.get("items"):
        lines.extend(["| Reference | Topics | Route | Annotation | Boundaries |", "| --- | --- | --- | --- | --- |"])
        for item in links["items"]:
            lines.append(
                f"| [{table_cell(item['title'])}]({item['url']}) | {', '.join(item['topics'])} | "
                f"{table_cell(item['route'])} | {table_cell(item['annotation'])} | {table_cell(item['limitations'])} |"
            )
    else:
        lines.append("- No adopted link-only references.")
    lines.extend(["", "## Collected documents", ""])
    if documents.get("items"):
        lines.extend(["| Document | Topics | Source | Retrieved | Route |", "| --- | --- | --- | --- | --- |"])
        for item in documents["items"]:
            lines.append(
                f"| [{table_cell(item['title'])}]({PurePosixPath(item['local_path']).relative_to('docs/coding-agent-kit/knowledge/collection').as_posix()}) | "
                f"{', '.join(item['topics'])} | [upstream]({item['source_url']}) | {item['retrieved_at']} | {table_cell(item['route'])} |"
            )
    else:
        lines.append("- No adopted documents.")
    return "\n".join(lines).rstrip() + "\n"


def rebuild_index(root: Path) -> None:
    projects_path, links_path, documents_path, index_path = collection_paths(root)
    index_path.write_text(
        render_index(load_json(projects_path), load_json(links_path), load_json(documents_path)),
        encoding="utf-8",
        newline="\n",
    )


def add_project(args: argparse.Namespace) -> None:
    root = args.root.resolve()
    source = adopted_source(root, args.source_id)
    if source["source_class"] not in {"official-repository", "community-repository"}:
        raise ValueError("Project routes require a repository source class.")
    require_immutable_version(args.version)
    projects_path, _, _, _ = collection_paths(root)
    registry = load_json(projects_path)
    entry = {
        "id": args.source_id,
        "source_id": args.source_id,
        "title": source["name"],
        "url": source["url"],
        "review": f"docs/coding-agent-kit/knowledge/external-sources/{source['review']}",
        "topics": source["topics"],
        "languages": source["languages"],
        "version": args.version,
        "route": normalize_space(args.route),
        "design": normalize_space(args.design),
        "limitations": normalize_space(args.limitations),
        "collected_at": utc_now(),
    }
    upsert(registry["items"], entry)
    write_json(projects_path, registry)
    rebuild_index(root)
    print(f"Registered project route: {args.source_id}")


def add_link(args: argparse.Namespace) -> None:
    """Register an adopted document/article as a URL plus original annotation only."""
    root = args.root.resolve()
    source = adopted_source(root, args.source_id)
    if source["source_class"] not in {"official-doc", "official-engineering", "community-article"}:
        raise ValueError("Link-only references require a documentation or article source class.")
    _, links_path, _, _ = collection_paths(root)
    registry = load_json(links_path)
    entry = {
        "id": args.source_id,
        "source_id": args.source_id,
        "title": source["name"],
        "url": source["url"],
        "review": f"docs/coding-agent-kit/knowledge/external-sources/{source['review']}",
        "source_class": source["source_class"],
        "topics": source["topics"],
        "languages": source["languages"],
        "route": normalize_space(args.route),
        "annotation": normalize_space(args.annotation),
        "limitations": normalize_space(args.limitations),
        "collected_at": utc_now(),
    }
    upsert(registry["items"], entry)
    write_json(links_path, registry)
    rebuild_index(root)
    print(f"Registered link-only reference: {args.source_id}")


def add_document(args: argparse.Namespace) -> None:
    root = args.root.resolve()
    source = adopted_source(root, args.source_id)
    if source["source_class"] not in {"official-doc", "official-engineering", "community-article"}:
        raise ValueError("Document collection requires a documentation or article source class.")
    if not args.redistribution_allowed:
        raise ValueError("Document retention requires an explicit --redistribution-allowed confirmation.")
    if normalize_space(args.license).lower() in {"", "unknown", "unspecified"}:
        raise ValueError("Document retention requires a verified redistribution license.")
    require_https(args.license_url)
    if args.timeout <= 0 or args.max_bytes <= 0:
        raise ValueError("Timeout and maximum response size must be positive.")

    source_url = args.content_url or source["url"]
    require_https(source_url)
    require_iso_date(args.published_at)
    if args.input:
        input_path = args.input.resolve()
        payload = input_path.read_bytes()
        content_type = args.content_type or ("text/markdown" if input_path.suffix.lower() in {".md", ".markdown"} else "text/html")
        final_url = source_url
    else:
        payload, content_type, final_url = fetch(source_url, args.timeout, args.max_bytes)
    if len(payload) > args.max_bytes:
        raise ValueError(f"Document exceeds the {args.max_bytes}-byte limit.")
    markdown, conversion = to_markdown(payload, content_type, final_url)
    if len(markdown.strip()) < 100:
        raise ValueError("Converted document is too short to retain as a technical source.")

    retrieved_at = utc_now()
    local_relative = PurePosixPath(f"docs/coding-agent-kit/knowledge/collection/documents/{args.source_id}.md")
    local_path = root / local_relative
    frontmatter = [
        "---",
        f"source_id: {json.dumps(args.source_id, ensure_ascii=False)}",
        f"source_url: {json.dumps(source['url'], ensure_ascii=False)}",
        f"content_url: {json.dumps(final_url, ensure_ascii=False)}",
        f"retrieved_at: {json.dumps(retrieved_at)}",
        f"license: {json.dumps(normalize_space(args.license), ensure_ascii=False)}",
        f"license_url: {json.dumps(args.license_url, ensure_ascii=False)}",
        f"source_sha256: {json.dumps(sha256_bytes(payload))}",
        f"conversion: {json.dumps(conversion)}",
        "---",
        "",
    ]
    stored = "\n".join(frontmatter) + markdown
    local_path.parent.mkdir(parents=True, exist_ok=True)
    local_path.write_text(stored, encoding="utf-8", newline="\n")

    _, _, documents_path, _ = collection_paths(root)
    registry = load_json(documents_path)
    entry = {
        "id": args.source_id,
        "source_id": args.source_id,
        "title": source["name"],
        "source_url": source["url"],
        "content_url": final_url,
        "review": f"docs/coding-agent-kit/knowledge/external-sources/{source['review']}",
        "local_path": local_relative.as_posix(),
        "topics": source["topics"],
        "languages": source["languages"],
        "license": normalize_space(args.license),
        "license_url": args.license_url,
        "published_at": args.published_at,
        "retrieved_at": retrieved_at,
        "source_sha256": sha256_bytes(payload),
        "stored_sha256": sha256_bytes(stored.encode("utf-8")),
        "conversion": conversion,
        "route": normalize_space(args.route),
    }
    upsert(registry["items"], entry)
    write_json(documents_path, registry)
    rebuild_index(root)
    print(f"Collected document: {local_relative.as_posix()}")


def check(root: Path) -> list[str]:
    failures: list[str] = []
    projects_path, links_path, documents_path, index_path = collection_paths(root)
    collection_root = projects_path.parent
    projects = load_json(projects_path)
    links = load_json(links_path)
    documents = load_json(documents_path)
    sources = source_map(root)
    topic_ids = {item["id"] for item in load_json(root / "tools/coding-agent-kit/indexer/topics.json")["topics"]}
    seen: set[str] = set()

    collection_source_ids: dict[str, str] = {}
    for kind, registry in (("project", projects), ("link", links), ("document", documents)):
        if registry.get("schema_version") != 1 or not isinstance(registry.get("items"), list):
            failures.append(f"Invalid {kind} collection registry schema.")
            continue
        for item in registry["items"]:
            source_id = item.get("source_id", "")
            if source_id in collection_source_ids:
                failures.append(
                    f"Adopted source {source_id} appears in multiple collection forms: "
                    f"{collection_source_ids[source_id]} and {kind}."
                )
            else:
                collection_source_ids[source_id] = kind
            item_id = f"{kind}:{item.get('id', '')}"
            if item_id in seen:
                failures.append(f"Duplicate collection id: {item_id}")
            seen.add(item_id)
            source = sources.get(source_id)
            if not source or source.get("review_status") != "adopted":
                failures.append(f"Collection entry {item_id} does not reference an adopted source.")
            elif item.get("url", item.get("source_url")) != source.get("url"):
                failures.append(f"Collection entry {item_id} does not preserve its registered source URL.")
            elif item.get("title") != source.get("name"):
                failures.append(f"Collection entry {item_id} does not preserve its registered title.")
            if source:
                if item.get("topics") != source.get("topics"):
                    failures.append(f"Collection entry {item_id} does not preserve its registered topics.")
                if item.get("languages") != source.get("languages"):
                    failures.append(f"Collection entry {item_id} does not preserve its registered languages.")
            review = root / item.get("review", "")
            if not item.get("review") or not review.is_file():
                failures.append(f"Collection entry {item_id} has no valid review artifact.")
            elif source:
                expected_review = PurePosixPath(
                    f"docs/coding-agent-kit/knowledge/external-sources/{source.get('review', '')}"
                ).as_posix()
                if PurePosixPath(item["review"]).as_posix() != expected_review:
                    failures.append(f"Collection entry {item_id} does not preserve its registered review path.")
                action_match = re.search(
                    r"(?m)^- Collection action: `([^`]+)`", review.read_text(encoding="utf-8")
                )
                expected_action = {
                    "project": "project route",
                    "link": "link and annotation only",
                    "document": "retained Markdown",
                }[kind]
                if not action_match or action_match.group(1) != expected_action:
                    failures.append(
                        f"Collection entry {item_id} conflicts with review collection action {expected_action}."
                    )
            unknown_topics = set(item.get("topics", [])) - topic_ids - {"all"}
            if unknown_topics:
                failures.append(f"Collection entry {item_id} has unknown topics: {sorted(unknown_topics)}")
            for key in ("route", "review"):
                if not item.get(key):
                    failures.append(f"Collection entry {item_id} is missing {key}.")
            if kind == "project" and ("local_path" in item or "content" in item):
                failures.append(f"Project route {item_id} must not contain copied project content.")
            if kind == "project":
                if source and source.get("source_class") not in {"official-repository", "community-repository"}:
                    failures.append(f"Project route {item_id} has an incompatible source class.")
                for key in ("url", "version", "design", "limitations"):
                    if not item.get(key):
                        failures.append(f"Project route {item_id} is missing {key}.")
                try:
                    require_https(item.get("url", ""))
                    require_immutable_version(item.get("version", ""))
                except ValueError as error:
                    failures.append(str(error))
                if source and item.get("version") != source.get("reviewed_commit"):
                    failures.append(f"Project route {item_id} version does not match reviewed_commit.")
            if kind == "link":
                if source and source.get("source_class") not in {"official-doc", "official-engineering", "community-article"}:
                    failures.append(f"Link reference {item_id} has an incompatible source class.")
                for key in ("url", "annotation", "limitations", "source_class"):
                    if not item.get(key):
                        failures.append(f"Link reference {item_id} is missing {key}.")
                try:
                    require_https(item.get("url", ""))
                except ValueError as error:
                    failures.append(str(error))
                if source and item.get("source_class") != source.get("source_class"):
                    failures.append(f"Link reference {item_id} does not preserve its registered source class.")
            if kind == "document" and source and source.get("source_class") not in {
                "official-doc",
                "official-engineering",
                "community-article",
            }:
                failures.append(f"Collected document {item_id} has an incompatible source class.")

    for item in documents.get("items", []):
        path_text = item.get("local_path", "")
        relative = PurePosixPath(path_text)
        expected_parent = PurePosixPath("docs/coding-agent-kit/knowledge/collection/documents")
        if ".." in relative.parts or expected_parent not in relative.parents or relative.suffix != ".md":
            failures.append(f"Document {item.get('id')} has an invalid local path: {path_text}")
            continue
        path = root / relative
        if not path.exists():
            failures.append(f"Collected document is missing: {path_text}")
            continue
        actual = sha256_bytes(path.read_bytes())
        if actual != item.get("stored_sha256"):
            failures.append(f"Collected document hash mismatch: {path_text}")
        if not item.get("license") or not item.get("license_url"):
            failures.append(f"Collected document {item.get('id')} lacks redistribution metadata.")
        for key in ("source_url", "content_url", "license_url"):
            try:
                require_https(item.get(key, ""))
            except ValueError as error:
                failures.append(str(error))
        try:
            require_iso_date(item.get("published_at", ""))
        except ValueError as error:
            failures.append(str(error))

    for source_id, source in sources.items():
        if source.get("review_status") == "adopted" and source_id not in collection_source_ids:
            failures.append(f"Adopted source {source_id} has no collection result.")
        if source.get("review_status") != "adopted" and source_id in collection_source_ids:
            failures.append(f"Non-adopted source {source_id} must not appear in the collection.")

    expected_index = render_index(projects, links, documents)
    actual_index = index_path.read_text(encoding="utf-8") if index_path.exists() else None
    if actual_index != expected_index:
        failures.append("Collected knowledge index is out of date.")

    allowed_root_files = {"README.md", "project-routes.json", "link-references.json", "documents.json", "KNOWLEDGE_INDEX.md"}
    for path in collection_root.rglob("*"):
        if not path.is_file():
            continue
        relative = PurePosixPath(path.relative_to(collection_root).as_posix())
        is_document = relative.parent == PurePosixPath("documents") and relative.suffix == ".md"
        if relative.as_posix() not in allowed_root_files and not is_document:
            failures.append(f"Unexpected file in external collection: {relative.as_posix()}")
    return failures


def add_common(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--root", type=Path, default=repository_root(), help="Compatible repository root.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    check_parser = subparsers.add_parser("check", help="Validate collection manifests and generated index.")
    add_common(check_parser)

    rebuild_parser = subparsers.add_parser("rebuild", help="Regenerate the collection knowledge index.")
    add_common(rebuild_parser)

    project = subparsers.add_parser("add-project", help="Register an adopted project link and route.")
    add_common(project)
    project.add_argument("--source-id", required=True)
    project.add_argument("--version", required=True, help="Immutable commit, tag, or release coordinate.")
    project.add_argument("--route", required=True)
    project.add_argument("--design", required=True)
    project.add_argument("--limitations", required=True)

    link = subparsers.add_parser("add-link", help="Register an adopted document/article as link and annotation only.")
    add_common(link)
    link.add_argument("--source-id", required=True)
    link.add_argument("--route", required=True)
    link.add_argument("--annotation", required=True)
    link.add_argument("--limitations", required=True)

    document = subparsers.add_parser("add-document", help="Download/convert an adopted document to Markdown.")
    add_common(document)
    document.add_argument("--source-id", required=True)
    document.add_argument("--content-url", help="Canonical raw/print URL; defaults to the registered source URL.")
    document.add_argument("--input", type=Path, help="Reviewed local HTML/Markdown instead of network retrieval.")
    document.add_argument("--content-type", choices=sorted(ALLOWED_CONTENT_TYPES))
    document.add_argument("--license", required=True)
    document.add_argument("--license-url", required=True)
    document.add_argument("--redistribution-allowed", action="store_true")
    document.add_argument("--published-at", required=True, help="ISO date or datetime from the source.")
    document.add_argument("--route", required=True)
    document.add_argument("--timeout", type=int, default=30)
    document.add_argument("--max-bytes", type=int, default=MAX_DOWNLOAD_BYTES)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.command == "add-project":
            add_project(args)
        elif args.command == "add-link":
            add_link(args)
        elif args.command == "add-document":
            add_document(args)
        elif args.command == "rebuild":
            rebuild_index(args.root.resolve())
            print("Rebuilt external knowledge index.")
        else:
            failures = check(args.root.resolve())
            if failures:
                for failure in failures:
                    print(f"ERROR: {failure}", file=sys.stderr)
                return 1
            print("External knowledge collection check passed.")
    except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
