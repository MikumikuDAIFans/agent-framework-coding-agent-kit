# Source review: `repo-dotnet-docs-maui`

## Snapshot

- Source: `dotnet/docs-maui` page `docs/ai/agent-framework.md`
- Canonical URL: https://github.com/dotnet/docs-maui/blob/main/docs/ai/agent-framework.md
- Source class: `official-repository`
- Owner/author: .NET/Microsoft documentation contributors.
- Reviewed commit, tag, or page date: repository commit `e75fa6a805d14c89b18a8a51199e05a007082b41` (2026-07-16); the page is pinned to that blob for review.
- Package/API coordinates: C#/.NET MAUI; `Microsoft.Agents.AI`/Workflows/Generators `1.0.0-rc3`, Hosting `1.0.0-preview.260304.1`, and `Microsoft.Maui.Essentials.AI 10.0.50-preview.1.26158.1`.
- License: repository documentation CC BY 4.0; code snippets governed by `LICENSE-CODE` (MIT).
- Reviewer and date: Codex, 2026-07-17.
- Policy version: `v1.1`
- Review track: `code-project`

## Direct Microsoft Agent Framework evidence

- Languages: C# documentation snippets.
- Package references/imports: explicit package references and snippets using `AddAIAgent`, `AsAIAgent`, typed workflow models/executors, `WorkflowBuilder`, conditional edges, workflow-agent run and streaming.
- Relevant files: only `docs/ai/agent-framework.md` in this source entry; it links a separate `dotnet/maui-samples` application.
- MAF topics demonstrated: on-device agents, typed sequential/conditional workflows, DI/keyed chat clients, streaming, and UI progress.
- Preview, experimental, deprecated, or provider-specific surfaces: Apple Intelligence and MAUI Essentials AI are preview/platform-specific; Android and Windows are explicitly unsupported. RC3/preview coordinates must not be mapped silently to target revision `5ab8877ba55b4778d778cf51450eafe483194708`.

## Design and implementation value

- Reusable decisions: typed stage contracts, narrow agents, keyed `IChatClient` instances, conditional workflow edges, and streaming UI progress are clearly explained.
- Sample shortcuts that must not be copied into production: snippets omit complete project context, tests, lifecycle/error handling, model availability checks, data retention, and fallback UX.
- State and data flow: typed travel-planning stages are clear; session/history persistence and app lifecycle recovery are not addressed.
- Tool and side-effect boundaries: no substantial side-effecting tool design is demonstrated.
- Failure, cancellation, retry, and concurrency behavior: cancellation is mentioned in streaming syntax, but failure/provider unavailability/retry/concurrency behavior is not tested in this source artifact.
- Security, identity, and data handling: on-device execution reduces some remote-data exposure; permission, local retention/deletion, untrusted prompt content, and device compromise boundaries remain unaddressed.
- Observability and evaluation: UI status events are described; telemetry/evaluation gates are absent.
- Hosting, deployment, and rollback: mobile platform prerequisites are documented; release, fallback, and rollback behavior is absent.

## Verification

- Commands documented by the source: package references and application composition snippets; no self-contained build command for this repository page.
- Checks reproduced locally: immutable blob, page front matter, package coordinates, API snippets, platform warning, and dual documentation/code licenses inspected through GitHub API.
- Test/eval coverage: the reviewed repository artifact contains no executable project or tests for these snippets; the linked sample is a different source and was not implicitly audited.
- Conflicts with local upstream source, tests, or Microsoft Learn: no direct conflict established; exact RC3/preview APIs remain version-sensitive against target `5ab8877...`.
- Unverified claims: Apple Intelligence runtime and linked sample are `not-run`; no compatible Apple runtime/project is in scope. Static page inspection is substitute evidence.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 3 | 15 | Clear typed on-device workflow guidance, narrow scope. |
| C-02 | Testing and verification | 25 | 0 | 0 | No executable project/tests in the reviewed source entry. |
| C-03 | Production depth | 20 | 1 | 4 | Platform prerequisites only; operational controls absent. |
| C-04 | Real MAF dependency | 10 | 4 | 8 | Exact packages and real API snippets, but not compiled here. |
| C-05 | Source/author credibility | 10 | 5 | 10 | Official .NET documentation repository. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable blob and exact RC/preview coordinates. |
| C-07 | Maintenance activity | 5 | 5 | 5 | Updated immediately before review. |
|  | **Total** | **100** |  | **47** |  |

### Hard gates

- Triggered gates: as a code-project-classified source, it has no verifiable executable dependency/API call—only snippets and a link to a separately owned sample.
- Result: reject under the project/code hard gate and score threshold. Official-document exemption is not applied because the registry class and assigned track are `official-repository`/`code-project`.
- Reviewer decision: `rejected`; the published Learn page or linked sample may be audited independently under the correct track.

## Decision

- State: `rejected`
- Approved use: none as a curated code-project route.
- Prohibited or unsafe use: do not claim snippets were compiled/tested; do not generalize Apple-only preview behavior to Android/Windows or other hosts.
- Topic-registry promotion proposal: none.
- Collection action: `none`
- Re-review trigger: reclassify/audit the published official documentation page or independently audit the linked executable sample.
- Residual risk: official prose can be mistaken for target-revision executable evidence.

## Re-review 2026-08-11

- New repository coordinate: `193868ac9559ce4a06f81fa2f82f03dcee61b4bd` (2026-08-10T08:46:12Z).
- The 15-commit delta is MAUI documentation and workflow maintenance; no MAF package, implementation, or test evidence changed.
- Decision unchanged: `rejected`, score 47. The source still fails the direct-MAF hard gate for this kit.
