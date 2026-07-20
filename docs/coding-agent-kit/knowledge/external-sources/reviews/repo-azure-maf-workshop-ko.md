# Source review: `repo-azure-maf-workshop-ko`

## Snapshot

- Source: `Azure-Samples/maf-workshop-in-a-day-ko`
- Canonical URL: https://github.com/Azure-Samples/maf-workshop-in-a-day-ko
- Source class: `official-repository`; owner: Azure-Samples/Microsoft.
- Reviewed commit: `8c79b3c6552e5271f80e834e28cf40565e93d4f1` (2026-05-06T14:33:50Z).
- Package/API coordinates: centrally versioned .NET MAF core, DevUI, Hosting, AG-UI, OpenAI and Workflows packages across save-points.
- License: MIT.
- Reviewer and date: Codex, 2026-07-17; policy `v1.1`; track `code-project`.

## Direct Microsoft Agent Framework evidence

- Languages: C# and Korean documentation.
- Progressive start/complete save-points cover agent creation, UI/protocol hosting, workflows, Aspire and an MCP todo server; 18 project files directly reference MAF packages.
- Tree inspection found no GitHub Actions workflow and no test path.
- Regional language and workshop provenance are explicit; technical authority still depends on exact commit/package mapping.

## Design and implementation value

- Reusable: incremental save-point pedagogy and complete application topology can clarify how agent, workflow, MCP and UI pieces accumulate.
- Limits: duplication across start/complete snapshots, no automated verification, no evaluation set, incomplete failure/replay/security/identity/SLO/rollback evidence.
- Start save-points are intentionally incomplete and may contain transient APIs or unsafe teaching shortcuts.

## Verification

- GitHub API verified commit/date/license, 539 blobs, direct dependencies and absence of detected tests/workflows.
- No build/cloud/model execution was run; exact centrally managed versions and compatibility with target `5ab8877ba55b4778d778cf51450eafe483194708` remain static-review boundaries.
- Korean instructional accuracy was not independently language-reviewed beyond structural evidence.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 4 | 20 | Useful progressive full-stack teaching route. |
| C-02 | Testing and verification | 25 | 0 | 0 | No tests or CI found. |
| C-03 | Production depth | 20 | 2 | 8 | Hosting/Aspire shape, little operational proof. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | Direct MAF packages throughout. |
| C-05 | Source/author credibility | 10 | 5 | 10 | Azure-Samples, Microsoft, MIT. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable review commit. |
| C-07 | Maintenance activity | 5 | 4 | 4 | Recent 2026 update. |
|  | **Total** | **100** |  | **57** |  |

### Hard gates

- Triggered gates: none.
- Result: score requires quarantine.
- Reviewer decision: `quarantined`.

## Decision

- State: `quarantined`
- Approved use: none in collection; retain review for future evidence refresh.
- Prohibited or unsafe use: routing start save-points or claiming production/readiness from workshop completion.
- Topic-registry promotion proposal: none while quarantined.
- Collection action: `none`
- Re-review trigger: tested CI, reproducible package coordinates and current API mapping are added.
- Residual risk: translation and duplicated save-points can drift independently.
