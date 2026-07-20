# Source review: `repo-microsoft-agent-framework`

## Snapshot

- Source: `microsoft/agent-framework`
- Canonical URL: https://github.com/microsoft/agent-framework
- Source class: `official-repository`; owner: Microsoft.
- Reviewed commit: `5ab8877ba55b4778d778cf51450eafe483194708` (2026-07-16T22:06:25Z).
- Package/API coordinates: canonical multi-package .NET and Python source, plus declarative schemas/designs.
- License: MIT; GitHub license metadata and repository LICENSE.
- Reviewer and date: Codex, 2026-07-17; policy `v1.1`; track `code-project`.

## Direct Microsoft Agent Framework evidence

- Languages: C#, Python, declarative/schema and documentation.
- This is the defining implementation: package manifests, public exports, providers, agents, sessions/context, middleware, workflows/orchestrations, hosting, protocols, evaluation and samples.
- Relevant evidence layers include `dotnet/src`, `dotnet/tests`, `dotnet/samples`, `python/packages`, `python/tests`, `python/samples`, `docs/decisions`, schemas and 20+ build/test/release workflows.
- Maturity is per-package/per-feature; preview/experimental attributes and package metadata must be checked at this commit.

## Design and implementation value

- Reusable: source, tests, decisions and samples permit a four-way evidence bundle for exact symbols.
- Production value includes identity/provider seams, middleware, telemetry, hosting, protocols, persistence and extensive negative/compatibility tests.
- Samples demonstrate composition but do not override implementation/tests or supply application-specific authorization, SLOs, retention, rollout and evaluation thresholds.
- State/data, failure/cancellation/concurrency and security behavior must be cited from the smallest matching package/test, not inferred repository-wide.

## Verification

- GitHub API verified immutable commit, date, ownership, MIT license, 5,186 tracked blobs and active maintenance.
- Tree inspection found dedicated .NET/Python build, unit/integration, sample-validation, coverage, CodeQL, formatting and release workflows.
- The kit's catalog/validator is the reusable local verification entry; cloud integration suites are separately credential-bound.
- Version boundary: all adopted external sources in this audit are compared to this exact commit.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 5 | 25 | Source, decisions, schemas and cross-language designs. |
| C-02 | Testing and verification | 25 | 5 | 25 | Extensive unit/integration/coverage/sample CI. |
| C-03 | Production depth | 20 | 5 | 20 | Hosting, telemetry, identity, protocols, durability. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | Canonical implementation itself. |
| C-05 | Source/author credibility | 10 | 5 | 10 | Microsoft canonical repository, MIT. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit and package/release history. |
| C-07 | Maintenance activity | 5 | 5 | 5 | Updated one day before review. |
|  | **Total** | **100** |  | **100** |  |

### Hard gates

- Triggered gates: none.
- Result: passes.
- Reviewer decision: `adopted` as primary source-observed authority.

## Decision

- State: `adopted`
- Approved use: exact-revision implementation, design, samples and tests through catalog routes.
- Prohibited or unsafe use: assuming all features are GA or samples are production defaults.
- Topic-registry promotion proposal: `all`; existing local catalog remains primary.
- Collection action: `project route`
- Re-review trigger: upstream baseline changes from `5ab8877...`.
- Residual risk: live main and published packages can diverge from this source snapshot.

