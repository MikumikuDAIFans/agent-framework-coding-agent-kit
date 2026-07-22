# External-source drift maintenance

`tools/coding-agent-kit/knowledge/maintenance.py` is the repeatable Phase 9 entry point for link,
repository, version, license, archive, and API re-review signals. It never changes the source registry,
review files, or collection manifests. A coding agent or maintainer evaluates the report and applies the
approved review policy explicitly.

Use the repository Skill at `.agents/skills/maf-kit-maintainer` for the complete operating cycle: upstream
comparison, technology discovery, topic-coverage review, source re-review, retirement, validation, and
publication. The machine check remains deliberately read-only.

The active collection manifests are accompanied by `collection/archive.json`. When an adopted source is
retired, preserve its last active version, review, collection kind, retirement date, reason, and replacement
there before removing it from active lookup. A temporary outage or age threshold is only a re-review signal.

## Read-only discovery

`discovery.py` compares bounded Microsoft Learn, MAF developer-blog, and GitHub search observations with the
formal external registry and Learn index. It emits `known` and `new` candidates but never promotes them.

```powershell
python tools/coding-agent-kit/knowledge/discovery.py
python tools/coding-agent-kit/knowledge/discovery.py --network --timeout 20 --output <discovery-report.json>
```

Offline mode reports `not-run`. Network-surface failures remain `failed` and return nonzero. Treat all new
candidates as untrusted discovery evidence; resolve them to original sources and complete the approved review
before editing `sources.json` or collection manifests.

## Offline check

The default mode performs registry and collection-state checks without opening the network. Network-only
checks are emitted as `not-run`, and an all-offline report has overall status `not-run` rather than being
represented as successful.

```powershell
python tools/coding-agent-kit/knowledge/maintenance.py
```

Use an observation fixture to exercise the complete decision engine in an offline CI job:

```powershell
python tools/coding-agent-kit/knowledge/maintenance.py --fixture <observations.json> --all
```

Fixture schema:

```json
{
  "schema_version": 1,
  "sources": {
    "source-id": {
      "link": {"status_code": 200, "final_url": "https://example.com/final"},
      "github": {
        "archived": false,
        "default_branch": "main",
        "head_sha": "0123456789abcdef0123456789abcdef01234567",
        "license_spdx": "MIT",
        "pushed_at": "2026-07-17T00:00:00Z"
      },
      "api": {"compatible": true, "evidence": "local verifier and review artifact"}
    }
  }
}
```

`api` is optional and represents an explicit local comparison against the matching MAF exports,
implementation, samples, and tests. A repository head change without such evidence is reported as
`needs-review`; it is never inferred to be API-compatible.

## Controlled network smoke

Network access requires the explicit `--network` flag. Prefer one or a small number of source IDs in an
interactive run; `--all` is intended for a scheduled, rate-limit-aware job. HTTPS requests have a timeout
and bounded GitHub API response size. `GITHUB_TOKEN` or `GH_TOKEN` is used when already available but is
never required or printed.

```powershell
python tools/coding-agent-kit/knowledge/maintenance.py --network --source-id <source-id> --timeout 10
```

The smoke check verifies source reachability and, for GitHub repositories, archive state, default branch,
current head, and machine-detectable license. It compares the current head with `reviewed_commit` or the
immutable collection version. API compatibility still requires explicit reviewed evidence against the current
local MAF baseline, even when the external source has not moved. A moved head creates an additional API
re-review recommendation. Live network errors,
timeouts, malformed responses, and missing required GitHub metadata are `failed` and produce a nonzero
exit; they are not converted to `pass`.

## Output and re-review path

Stdout is a schema-versioned JSON report. `--output <path>` also writes the same report for CI artifacts.
Source and check states are:

- `pass`: the performed check matches its recorded baseline;
- `drift`: an observed link, archive, version, license, or API condition changed;
- `needs-review`: evidence is incomplete or a human/coding-agent API comparison is required;
- `failed`: the check could not obtain or validate required evidence;
- `not-run`: the offline invocation intentionally did not perform a network-only check.

`failed` and `drift` return exit code 1. `needs-review` remains machine-visible with exit code 0 so a
scheduled job can create a review queue without claiming that the source passed. For each recommendation:

1. inspect the source at its new immutable coordinate;
2. compare MAF dependencies and API calls with the local catalog, exports, implementation, and tests;
3. update the independent review and apply `REVIEW_POLICY.md`;
4. update the registry and collection through their existing controlled paths;
5. rerun collection, lookup, maintenance, and kit validation.
