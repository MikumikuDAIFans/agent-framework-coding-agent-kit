#!/usr/bin/env python3
"""Detect structural and external-source drift for the coding-agent kit.

The default command is deliberately offline. Network access is available only
with ``--network`` and uses bounded HTTPS requests. A JSON observation fixture
can exercise the same drift rules deterministically in CI.
"""

from __future__ import annotations

import argparse
import ipaddress
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlparse
from urllib.request import Request, urlopen


USER_AGENT = "agent-framework-coding-agent-kit-maintenance/1.0"
GITHUB_HOSTS = {"github.com", "www.github.com"}
TERMINAL_STATES = {"adopted", "context-only", "quarantined", "rejected"}
REPOSITORY_CLASSES = {"official-repository", "community-repository"}


def repository_root() -> Path:
    return Path(__file__).resolve().parents[3]


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as stream:
        value = json.load(stream)
    if not isinstance(value, dict):
        raise ValueError(f"Expected a JSON object: {path}")
    return value


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def github_coordinates(url: str) -> tuple[str, str] | None:
    parsed = urlparse(url)
    if parsed.hostname not in GITHUB_HOSTS:
        return None
    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) < 2:
        return None
    repo = parts[1][:-4] if parts[1].endswith(".git") else parts[1]
    return parts[0], repo


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


def request_json(url: str, timeout: float, token: str | None) -> dict[str, Any]:
    headers = {"Accept": "application/vnd.github+json", "User-Agent": USER_AGENT}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(url, headers=headers)
    with urlopen(request, timeout=timeout) as response:  # noqa: S310 - caller constructs HTTPS GitHub API URLs
        payload = response.read(2 * 1024 * 1024 + 1)
    if len(payload) > 2 * 1024 * 1024:
        raise ValueError("GitHub API response exceeded the 2 MiB limit")
    value = json.loads(payload)
    if not isinstance(value, dict):
        raise ValueError("GitHub API returned a non-object response")
    return value


def probe_link(url: str, timeout: float) -> dict[str, Any]:
    require_public_https(url)
    request = Request(url, headers={"User-Agent": USER_AGENT}, method="HEAD")
    try:
        with urlopen(request, timeout=timeout) as response:  # noqa: S310 - registry validation requires HTTPS
            final_url = response.geturl()
            require_public_https(final_url)
            return {"status_code": response.status, "final_url": final_url}
    except HTTPError as error:
        # Some documentation servers reject HEAD even though GET is supported.
        if error.code not in {405, 501}:
            return {"status_code": error.code, "final_url": error.geturl()}
    request = Request(url, headers={"User-Agent": USER_AGENT, "Range": "bytes=0-0"})
    with urlopen(request, timeout=timeout) as response:  # noqa: S310 - registry validation requires HTTPS
        response.read(1)
        final_url = response.geturl()
        require_public_https(final_url)
        return {"status_code": response.status, "final_url": final_url}


def probe_github(url: str, timeout: float, token: str | None) -> dict[str, Any] | None:
    coordinates = github_coordinates(url)
    if not coordinates:
        return None
    owner, repo = coordinates
    base = f"https://api.github.com/repos/{quote(owner)}/{quote(repo)}"
    metadata = request_json(base, timeout, token)
    default_branch = metadata.get("default_branch")
    head_sha = None
    if isinstance(default_branch, str) and default_branch:
        branch = request_json(f"{base}/commits/{quote(default_branch, safe='')}", timeout, token)
        head_sha = branch.get("sha")
    license_value = metadata.get("license")
    return {
        "archived": metadata.get("archived"),
        "default_branch": default_branch,
        "head_sha": head_sha,
        "license_spdx": license_value.get("spdx_id") if isinstance(license_value, dict) else None,
        "pushed_at": metadata.get("pushed_at"),
    }


def network_observation(
    source: dict[str, Any], collection: dict[str, Any] | None, timeout: float, token: str | None
) -> dict[str, Any]:
    observation = {"link": probe_link(source["url"], timeout)}
    github = probe_github(source["url"], timeout, token)
    if github is not None:
        observation["github"] = github
    if collection and collection.get("license_url"):
        observation["license_link"] = probe_link(collection["license_url"], timeout)
    return observation


def load_fixture(path: Path) -> dict[str, dict[str, Any]]:
    value = load_json(path)
    if value.get("schema_version") != 1 or not isinstance(value.get("sources"), dict):
        raise ValueError("Observation fixture must have schema_version 1 and a sources object")
    observations: dict[str, dict[str, Any]] = {}
    for source_id, observation in value["sources"].items():
        if not isinstance(source_id, str) or not isinstance(observation, dict):
            raise ValueError("Fixture source observations must be JSON objects keyed by source id")
        observations[source_id] = observation
    return observations


def find_collection_entry(root: Path, source_id: str) -> dict[str, Any] | None:
    base = root / "docs/coding-agent-kit/knowledge/collection"
    for name in ("project-routes.json", "link-references.json", "documents.json"):
        for item in load_json(base / name).get("items", []):
            if item.get("source_id") == source_id:
                return {**item, "_collection_kind": name}
    return None


def review_uses_link_annotation_only(root: Path, source_id: str) -> bool:
    review = root / "docs/coding-agent-kit/knowledge/external-sources/reviews" / f"{source_id}.md"
    if not review.is_file():
        return False
    text = review.read_text(encoding="utf-8")
    return bool(
        re.search(
            r"^- Collection action:\s*`?link(?:\s+and|-and-)\s+annotation\s+only`?\s*$",
            text,
            flags=re.IGNORECASE | re.MULTILINE,
        )
    )


def expected_version(source: dict[str, Any], collection: dict[str, Any] | None) -> str | None:
    value = source.get("reviewed_commit")
    if not value and collection:
        value = collection.get("version")
    return value if isinstance(value, str) and value else None


def make_check(check_id: str, status: str, detail: str, observed: Any = None, expected: Any = None) -> dict[str, Any]:
    result: dict[str, Any] = {"id": check_id, "status": status, "detail": detail}
    if observed is not None:
        result["observed"] = observed
    if expected is not None:
        result["expected"] = expected
    return result


def evaluate_source(
    root: Path, source: dict[str, Any], observation: dict[str, Any] | None, observation_mode: str
) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    recommendations: list[str] = []
    url = source.get("url")
    try:
        require_public_https(url if isinstance(url, str) else "")
    except ValueError as error:
        checks.append(make_check("registry_url", "failed", str(error), url))
    else:
        checks.append(make_check("registry_url", "pass", "Source URL is structurally valid."))

    collection = find_collection_entry(root, source["id"])
    if source.get("review_status") == "adopted" and collection is None:
        detail = "Adopted source has no project route, link-reference manifest entry, or retained document."
        if review_uses_link_annotation_only(root, source["id"]):
            detail += " Its review requests link-and-annotation-only collection, but the lookup manifest entry is missing."
        checks.append(make_check("collection_route", "failed", detail))
        recommendations.append("Add the adopted source to the matching collection manifest or downgrade it pending collection.")
    else:
        checks.append(make_check("collection_route", "pass", "Collection state matches the current review state."))

    if observation is None:
        checks.append(make_check("link", "not-run", f"No {observation_mode} observation was supplied."))
        if source.get("source_class") in REPOSITORY_CLASSES:
            checks.extend(
                [
                    make_check("repository_state", "not-run", "No repository observation was supplied."),
                    make_check("version_drift", "not-run", "No repository head observation was supplied."),
                    make_check("license_drift", "not-run", "No repository license observation was supplied."),
                    make_check("api_drift", "not-run", "API compatibility needs a version observation or reviewed evidence."),
                ]
            )
        elif source.get("review_status") == "adopted":
            checks.extend(
                [
                    make_check("license_drift", "not-run", "No license-link observation was supplied."),
                    make_check("api_drift", "not-run", "Document API compatibility requires reviewed evidence."),
                ]
            )
        return {"id": source["id"], "status": source_status(checks), "checks": checks, "re_review": recommendations}

    link = observation.get("link")
    if not isinstance(link, dict) or not isinstance(link.get("status_code"), int):
        checks.append(make_check("link", "failed", "Observation has no numeric link status code."))
    elif 200 <= link["status_code"] < 400:
        checks.append(make_check("link", "pass", "Source link is reachable.", link["status_code"]))
    else:
        checks.append(make_check("link", "drift", "Source link is not reachable.", link["status_code"]))
        recommendations.append("Re-review the source URL and replace or retire the route.")

    if source.get("source_class") in REPOSITORY_CLASSES:
        github = observation.get("github")
        if not isinstance(github, dict):
            checks.append(make_check("repository_state", "failed", "GitHub repository metadata is missing."))
            checks.append(make_check("version_drift", "failed", "Repository head cannot be compared."))
            checks.append(make_check("license_drift", "failed", "Repository license cannot be checked."))
            checks.append(make_check("api_drift", "failed", "API drift cannot be bounded without repository metadata."))
        else:
            archived = github.get("archived")
            if archived is True:
                checks.append(make_check("repository_state", "drift", "Repository is archived.", archived, False))
                recommendations.append("Re-review production suitability and quarantine the route while archived.")
            elif archived is False and github.get("default_branch"):
                checks.append(
                    make_check(
                        "repository_state",
                        "pass",
                        "Repository is active and exposes a default branch.",
                        {"archived": archived, "default_branch": github.get("default_branch")},
                    )
                )
            else:
                checks.append(make_check("repository_state", "failed", "Archive or default-branch metadata is incomplete."))

            pinned = expected_version(source, collection)
            observed_head = github.get("head_sha")
            if not pinned:
                checks.append(make_check("version_drift", "needs-review", "No immutable reviewed version is recorded."))
                recommendations.append("Record an immutable reviewed commit/tag before adoption.")
            elif not isinstance(observed_head, str) or not observed_head:
                checks.append(make_check("version_drift", "failed", "Repository head SHA is missing.", expected=pinned))
            elif observed_head == pinned:
                checks.append(make_check("version_drift", "pass", "Repository remains at the reviewed commit.", observed_head, pinned))
            else:
                checks.append(make_check("version_drift", "drift", "Default branch moved beyond the reviewed commit.", observed_head, pinned))
                recommendations.append("Inspect dependency and MAF API changes since the reviewed commit.")

            license_spdx = github.get("license_spdx")
            expected_license = collection.get("license") if collection else None
            if expected_license:
                if license_spdx == expected_license:
                    checks.append(make_check("license_drift", "pass", "License matches the collection baseline.", license_spdx, expected_license))
                else:
                    checks.append(make_check("license_drift", "drift", "License differs from the collection baseline.", license_spdx, expected_license))
                    recommendations.append("Re-verify redistribution and attribution rights before reuse.")
            elif license_spdx and license_spdx != "NOASSERTION":
                checks.append(make_check("license_drift", "pass", "Repository currently reports a license.", license_spdx))
            else:
                checks.append(make_check("license_drift", "needs-review", "Repository has no machine-detectable license."))
                recommendations.append("Re-check repository license and keep content link-only until resolved.")

            api = observation.get("api")
            if isinstance(api, dict) and isinstance(api.get("compatible"), bool):
                if api["compatible"]:
                    checks.append(make_check("api_drift", "pass", "Fixture records a completed API compatibility check.", api))
                else:
                    checks.append(make_check("api_drift", "drift", "Fixture records incompatible or removed MAF API usage.", api))
                    recommendations.append("Re-review against the current local MAF exports, implementation, samples, and tests.")
            elif pinned and observed_head == pinned:
                checks.append(
                    make_check(
                        "api_drift",
                        "needs-review",
                        "Source is unchanged, but no explicit compatibility evidence targets the current local MAF baseline.",
                    )
                )
                recommendations.append("Confirm reviewed MAF API calls against the current local catalog and tests.")
            else:
                checks.append(make_check("api_drift", "needs-review", "Version movement requires an API evidence refresh."))
    elif source.get("review_status") == "adopted":
        license_link = observation.get("license_link")
        if collection and collection.get("_collection_kind") == "link-references.json":
            checks.append(
                make_check(
                    "license_drift",
                    "pass",
                    "Source body is not retained; the collection preserves only its URL and original annotation.",
                )
            )
        elif not collection or not collection.get("license") or not collection.get("license_url"):
            checks.append(make_check("license_drift", "failed", "Adopted document has no retained license baseline."))
            recommendations.append("Re-verify the document license; retain only a link if redistribution is not allowed.")
        elif not isinstance(license_link, dict) or not isinstance(license_link.get("status_code"), int):
            checks.append(make_check("license_drift", "failed", "License-link observation is missing."))
        elif 200 <= license_link["status_code"] < 400:
            checks.append(make_check("license_drift", "pass", "Recorded license link is reachable.", license_link["status_code"]))
        else:
            checks.append(make_check("license_drift", "drift", "Recorded license link is not reachable.", license_link["status_code"]))
            recommendations.append("Re-verify the document's redistribution license before retaining its body.")

        api = observation.get("api")
        if isinstance(api, dict) and isinstance(api.get("compatible"), bool):
            status = "pass" if api["compatible"] else "drift"
            checks.append(make_check("api_drift", status, "Document API compatibility observation was evaluated.", api))
            if not api["compatible"]:
                recommendations.append("Re-review the document against current MAF APIs and maturity labels.")
        else:
            checks.append(make_check("api_drift", "needs-review", "Link reachability alone cannot prove current API compatibility."))
    return {"id": source["id"], "status": source_status(checks), "checks": checks, "re_review": recommendations}


def source_status(checks: list[dict[str, Any]]) -> str:
    statuses = {check["status"] for check in checks}
    if "failed" in statuses:
        return "failed"
    if "drift" in statuses:
        return "drift"
    if "needs-review" in statuses:
        return "needs-review"
    if statuses == {"pass"}:
        return "pass"
    return "not-run"


def run(args: argparse.Namespace) -> tuple[dict[str, Any], int]:
    root = args.root.resolve()
    sources_path = root / "docs/coding-agent-kit/knowledge/external-sources/sources.json"
    try:
        registry = load_json(sources_path)
        if registry.get("schema_version") != 1 or not isinstance(registry.get("items"), list):
            raise ValueError("Source registry must have schema_version 1 and an items array")
        observations = load_fixture(args.fixture.resolve()) if args.fixture else {}
    except (OSError, ValueError, json.JSONDecodeError) as error:
        report = {
            "schema_version": 1,
            "generated_at": utc_now(),
            "mode": "offline-fixture" if args.fixture else "offline",
            "status": "failed",
            "errors": [str(error)],
            "sources": [],
        }
        return report, 1

    mode = "network" if args.network else ("offline-fixture" if args.fixture else "offline")
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    selected: list[dict[str, Any]] = []
    requested_ids = set(args.source_id or [])
    for source in registry["items"]:
        if requested_ids and source.get("id") not in requested_ids:
            continue
        if source.get("source_class") == "meta-index":
            continue
        if args.all or requested_ids or source.get("review_status") in TERMINAL_STATES:
            selected.append(source)

    unknown_ids = requested_ids - {source.get("id") for source in registry["items"]}
    errors = [f"Unknown source id: {source_id}" for source_id in sorted(unknown_ids)]
    results: list[dict[str, Any]] = []
    for source in selected:
        observation = observations.get(source["id"])
        if args.network:
            try:
                observation = network_observation(source, find_collection_entry(root, source["id"]), args.timeout, token)
            except (HTTPError, URLError, TimeoutError, OSError, ValueError, json.JSONDecodeError) as error:
                results.append(
                    {
                        "id": source["id"],
                        "status": "failed",
                        "checks": [make_check("network", "failed", f"Network observation failed: {error}")],
                        "re_review": ["Retry the controlled smoke check; do not treat this source as freshly verified."],
                    }
                )
                continue
        results.append(evaluate_source(root, source, observation, mode))

    counts = {status: sum(result["status"] == status for result in results) for status in ("pass", "drift", "needs-review", "failed", "not-run")}
    status = (
        "failed"
        if errors or counts["failed"]
        else "drift"
        if counts["drift"]
        else "needs-review"
        if counts["needs-review"]
        else "not-run"
        if counts["not-run"]
        else "pass"
    )
    report = {
        "schema_version": 1,
        "generated_at": utc_now(),
        "mode": mode,
        "status": status,
        "selected_count": len(selected),
        "counts": counts,
        "errors": errors,
        "sources": results,
    }
    return report, 1 if status in {"failed", "drift"} else 0


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser(description=__doc__)
    value.add_argument("--root", type=Path, default=repository_root())
    value.add_argument("--fixture", type=Path, help="Replay a schema-v1 observation fixture without network access.")
    value.add_argument("--network", action="store_true", help="Explicitly opt in to bounded live link and GitHub API checks.")
    value.add_argument("--all", action="store_true", help="Check all reviewable sources instead of terminal-state sources.")
    value.add_argument("--source-id", action="append", help="Check one source id; repeat to check a controlled subset.")
    value.add_argument("--timeout", type=float, default=10.0)
    value.add_argument("--output", type=Path, help="Write the JSON report to this path as well as stdout.")
    return value


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    if args.network and args.fixture:
        print("--network and --fixture are mutually exclusive", file=sys.stderr)
        return 2
    if args.timeout <= 0:
        print("--timeout must be positive", file=sys.stderr)
        return 2
    report, exit_code = run(args)
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8", newline="\n")
    sys.stdout.write(rendered)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
