# Source review: `repo-microsoft-agent-framework-samples`

## Snapshot

- Source: `microsoft/Agent-Framework-Samples`
- Canonical URL: https://github.com/microsoft/Agent-Framework-Samples
- Source class: `official-repository`; owner: Microsoft.
- Reviewed commit: `5b854b7e1c3838f17f41bcf2412ef79d7662db37` (2026-06-06T03:29:15Z).
- Package/API coordinates: mixed source-main, minimum/unbounded Python dependencies, preview packages and developer-path .NET references.
- License: MIT.
- Reviewer and date: Codex, 2026-07-17; policy `v1.1`; track `code-project`.

## Direct Microsoft Agent Framework evidence

- Languages: Python, C#, notebooks and frontend/infrastructure fragments.
- 346 blobs cover agents, tools, providers, RAG, workflows, DevUI, OpenTelemetry, AG-UI and hosted agents.
- Direct imports/references are abundant, but the corpus has no single reproducible MAF coordinate.
- Representative symbols map to target `5ab8877ba55b4778d778cf51450eafe483194708`; per-sample compatibility is not established.

## Design and implementation value

- Useful for broad scenario discovery and side-by-side learning.
- All observed `.csproj` samples use placeholder/developer-machine source references; Python commonly installs moving GitHub main or minimum-only versions.
- No repository-wide CI; test-like Python files are mostly manual integration diagnostics. One diagnostic prints a GitHub token suffix and is an explicit unsafe pattern.
- Workflow, telemetry and hosting examples omit a common state/replay, authorization, idempotency, retry, evaluation, deployment and rollback contract.

## Verification

- Immutable commit/license/tree and dependency/reference inventory verified through GitHub API and prior local static review.
- Prior AST parsing passed 86 Python files; a sample .NET build was blocked by .NET 10 and placeholder references.
- Cloud/model tests were not run because they require credentials/resources.
- No GitHub Actions workflow exists beyond dependency metadata.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 4 | 20 | Broad compositions, weak common architecture. |
| C-02 | Testing and verification | 25 | 1 | 5 | No CI/assertion suite; static checks only. |
| C-03 | Production depth | 20 | 1 | 4 | Integrations shown; production controls absent. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | Many direct imports/references/API calls. |
| C-05 | Source/author credibility | 10 | 5 | 10 | Microsoft organization and MIT license. |
| C-06 | Version traceability | 5 | 5 | 5 | Review commit pinned, though dependencies move. |
| C-07 | Maintenance activity | 5 | 4 | 4 | Recent work, not current target date. |
|  | **Total** | **100** |  | **58** |  |

### Hard gates

- Triggered gates: none; direct MAF usage exists.
- Result: score requires quarantine.
- Reviewer decision: `quarantined` until individual samples gain reproducible dependencies and verification.

## Decision

- State: `quarantined`
- Approved use: none in coding-agent collection; maintainers may use it to discover candidates for separate review.
- Prohibited or unsafe use: project references, moving installs, credential diagnostics or production defaults.
- Topic-registry promotion proposal: none while quarantined.
- Collection action: `none`
- Re-review trigger: pinned packages, portable projects and CI/tests are added.
- Residual risk: a sample can be incompatible even when its symbol names still exist.
