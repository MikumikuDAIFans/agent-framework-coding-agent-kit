#!/usr/bin/env python3
"""Discover current MAF documentation and project candidates without mutating registries."""

from __future__ import annotations

import argparse
import ipaddress
import json
import os
import re
import sys
from datetime import datetime, timezone
from html import unescape
from pathlib import Path
from typing import Any
from urllib.parse import quote, urljoin, urlparse, urlunparse
from urllib.request import Request, urlopen
from xml.etree import ElementTree


USER_AGENT = "agent-framework-coding-agent-kit-discovery/1.0"
LEARN_HUB = "https://learn.microsoft.com/en-us/agent-framework/"
BLOG_FEED = "https://devblogs.microsoft.com/agent-framework/feed/"
GITHUB_QUERIES = (
    '"Microsoft Agent Framework" in:name,description,readme archived:false',
    '"Microsoft.Agents.AI" in:readme archived:false',
    '"agent_framework" in:readme archived:false',
)
PINNED_DISCOVERY_SOURCES = (
    (
        "https://github.com/microsoft/agent-framework-go",
        "microsoft/agent-framework-go",
        "official-repository",
        "official-ecosystem-seed",
    ),
    (
        "https://github.com/microsoft/Agent-Framework-Samples",
        "microsoft/Agent-Framework-Samples",
        "official-repository",
        "official-ecosystem-seed",
    ),
    (
        "https://github.com/microsoft/skills",
        "microsoft/skills",
        "official-repository",
        "official-ecosystem-seed",
    ),
    (
        "https://docs.github.com/en/copilot/how-tos/copilot-sdk/integrations/microsoft-agent-framework",
        "GitHub Copilot SDK integration with Microsoft Agent Framework",
        "official-doc",
        "official-ecosystem-seed",
    ),
    (
        "https://github.com/rwjdk/AgentFrameworkToolkit",
        "rwjdk/AgentFrameworkToolkit",
        "repository-candidate",
        "curated-community-seed",
    ),
)


def repository_root() -> Path:
    return Path(__file__).resolve().parents[3]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"Expected a JSON object: {path}")
    return value


def require_public_https(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError(f"Only absolute HTTPS URLs are allowed: {url}")
    hostname = parsed.hostname.lower().rstrip(".")
    if hostname == "localhost" or hostname.endswith((".localhost", ".local")):
        raise ValueError(f"Local network URLs are not allowed: {url}")
    try:
        address = ipaddress.ip_address(hostname)
    except ValueError:
        return
    if not address.is_global:
        raise ValueError(f"Private or non-global URLs are not allowed: {url}")


def canonical_url(url: str) -> str:
    """Normalize URLs for duplicate detection without changing the retained source URL."""
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower()
    path = re.sub(r"/{2,}", "/", parsed.path).rstrip("/")
    if host == "learn.microsoft.com":
        path = re.sub(r"^/[a-z]{2}-[a-z]{2}(?=/)", "", path, flags=re.IGNORECASE)
    if host in {"github.com", "www.github.com"}:
        host = "github.com"
        parts = [part for part in path.split("/") if part]
        if len(parts) >= 2:
            path = "/" + "/".join(parts[:2])
    return urlunparse(("https", host, path.lower(), "", "", ""))


def fetch_bytes(url: str, timeout: float, token: str | None = None, accept: str | None = None) -> bytes:
    require_public_https(url)
    headers = {"User-Agent": USER_AGENT}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    if accept:
        headers["Accept"] = accept
    request = Request(url, headers=headers)
    with urlopen(request, timeout=timeout) as response:  # noqa: S310 - fixed HTTPS discovery surfaces
        payload = response.read(4 * 1024 * 1024 + 1)
    if len(payload) > 4 * 1024 * 1024:
        raise ValueError(f"Discovery response exceeded 4 MiB: {url}")
    return payload


def candidate(url: str, title: str, source_class: str, discovered_via: str, **extra: Any) -> dict[str, Any]:
    require_public_https(url)
    result = {
        "url": url,
        "title": title.strip() or url,
        "source_class": source_class,
        "discovered_via": discovered_via,
    }
    result.update({key: value for key, value in extra.items() if value is not None})
    return result


def discover_learn(timeout: float) -> list[dict[str, Any]]:
    text = fetch_bytes(LEARN_HUB, timeout, accept="text/html").decode("utf-8", errors="replace")
    results: list[dict[str, Any]] = []
    for href, body in re.findall(r'<a\b[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', text, flags=re.I | re.S):
        url = urljoin(LEARN_HUB, unescape(href))
        parsed = urlparse(url)
        if parsed.hostname != "learn.microsoft.com" or "/agent-framework" not in parsed.path:
            continue
        clean = urlunparse(("https", parsed.hostname, parsed.path, "", "", ""))
        title = re.sub(r"<[^>]+>", " ", body)
        title = re.sub(r"\s+", " ", unescape(title)).strip()
        results.append(candidate(clean, title, "official-doc", "microsoft-learn-hub"))
    return results


def discover_blog(timeout: float) -> list[dict[str, Any]]:
    root = ElementTree.fromstring(fetch_bytes(BLOG_FEED, timeout, accept="application/rss+xml"))
    results: list[dict[str, Any]] = []
    for item in root.findall("./channel/item"):
        link = (item.findtext("link") or "").strip()
        title = (item.findtext("title") or link).strip()
        published = (item.findtext("pubDate") or "").strip()
        if link:
            results.append(candidate(link, title, "official-engineering", "maf-developer-blog", published_at=published))
    return results


def discover_github(timeout: float, token: str | None, limit: int) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for query in GITHUB_QUERIES:
        url = f"https://api.github.com/search/repositories?q={quote(query)}&sort=updated&order=desc&per_page={limit}"
        value = json.loads(fetch_bytes(url, timeout, token, "application/vnd.github+json"))
        for item in value.get("items", []):
            if not isinstance(item, dict) or not item.get("html_url"):
                continue
            results.append(
                candidate(
                    item["html_url"],
                    item.get("full_name") or item["html_url"],
                    "repository-candidate",
                    f"github-search:{query}",
                    description=item.get("description"),
                    pushed_at=item.get("pushed_at"),
                    archived=item.get("archived"),
                    stars=item.get("stargazers_count"),
                    license=(item.get("license") or {}).get("spdx_id"),
                )
            )
    return results


def known_urls(root: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    registry = load_json(root / "docs/coding-agent-kit/knowledge/external-sources/sources.json")
    for item in registry.get("items", []):
        if isinstance(item, dict) and isinstance(item.get("url"), str):
            result[canonical_url(item["url"])] = f"external-source:{item.get('id')}"
    learn = load_json(root / "docs/coding-agent-kit/catalog/learn-index.json")
    for item in learn.get("pages", []):
        if isinstance(item, dict) and isinstance(item.get("url"), str):
            result.setdefault(canonical_url(item["url"]), f"learn-index:{item.get('doc_path', item.get('title'))}")
    return result


def build_report(root: Path, raw_candidates: list[dict[str, Any]], mode: str, errors: list[str]) -> dict[str, Any]:
    known = known_urls(root)
    unique: dict[str, dict[str, Any]] = {}
    for item in raw_candidates:
        key = canonical_url(item["url"])
        if key not in unique:
            unique[key] = item
        elif item["discovered_via"] not in unique[key]["discovered_via"]:
            unique[key]["discovered_via"] += f"; {item['discovered_via']}"
    candidates = []
    for key, item in sorted(unique.items(), key=lambda pair: pair[0]):
        candidates.append({**item, "status": "known" if key in known else "new", "known_as": known.get(key)})
    counts = {
        "total": len(candidates),
        "known": sum(item["status"] == "known" for item in candidates),
        "new": sum(item["status"] == "new" for item in candidates),
        "errors": len(errors),
    }
    return {
        "schema_version": 1,
        "generated_at": utc_now(),
        "mode": mode,
        "status": "failed" if errors else ("not-run" if mode == "offline" else "observed"),
        "counts": counts,
        "errors": errors,
        "candidates": candidates,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--network", action="store_true", help="Query bounded official and GitHub HTTPS discovery surfaces.")
    parser.add_argument("--fixture", type=Path, help="Load candidate observations from a deterministic JSON fixture.")
    parser.add_argument("--output", type=Path, help="Write the JSON report to this path.")
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--github-limit", type=int, default=20)
    args = parser.parse_args()
    if args.network and args.fixture:
        parser.error("Choose either --network or --fixture, not both.")
    if not 1 <= args.github_limit <= 50:
        parser.error("--github-limit must be between 1 and 50.")

    root = repository_root()
    raw: list[dict[str, Any]] = []
    errors: list[str] = []
    mode = "offline"
    if args.fixture:
        mode = "fixture"
        fixture = load_json(args.fixture)
        if fixture.get("schema_version") != 1 or not isinstance(fixture.get("candidates"), list):
            raise SystemExit("Fixture must use schema_version 1 and a candidates array.")
        raw = [item for item in fixture["candidates"] if isinstance(item, dict)]
        for item in raw:
            require_public_https(item.get("url", ""))
    elif args.network:
        mode = "network"
        token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
        raw.extend(candidate(*source) for source in PINNED_DISCOVERY_SOURCES)
        for name, operation in (
            ("microsoft-learn-hub", lambda: discover_learn(args.timeout)),
            ("maf-developer-blog", lambda: discover_blog(args.timeout)),
            ("github-search", lambda: discover_github(args.timeout, token, args.github_limit)),
        ):
            try:
                raw.extend(operation())
            except Exception as error:  # keep independent discovery surfaces observable
                errors.append(f"{name}: {type(error).__name__}: {error}")

    report = build_report(root, raw, mode, errors)
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    print(rendered, end="")
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
