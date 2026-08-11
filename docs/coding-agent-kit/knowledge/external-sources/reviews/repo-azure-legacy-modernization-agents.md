# Source review: `repo-azure-legacy-modernization-agents`

## Snapshot

- Source: `Azure-Samples/Legacy-Modernization-Agents`
- Canonical URL: https://github.com/Azure-Samples/Legacy-Modernization-Agents
- Source class: `official-repository`; owner: Azure-Samples.
- Reviewed commit: `3511138b890cb5b385ef417b2092018cb82263aa` (observed 2026-08-11).
- Claimed coordinates: README claims MAF preview packages; current project manifests inspected do not declare them.
- License: MIT.
- Reviewer and date: Codex, 2026-08-11; policy `v1.1`; track `code-project`.

## Direct Microsoft Agent Framework evidence

- The README describes a multi-provider MAF modernization workflow, but inspected .NET project manifests declare Azure/OpenAI/MEAI/Copilot dependencies without `Microsoft.Agents.AI` packages.
- The tree has 245 files, 29 tests, and six agentic documentation workflows; many operational paths require Docker, databases, credentials, and substantial model token use.
- Documentation claims alone do not satisfy the direct-dependency/API hard gate.

## Design and implementation value

- The staged reverse-engineering, persistence, conversion, and validation architecture is useful domain context.
- It cannot be attributed to current MAF without a verifiable package/import path.

## Verification

- Immutable metadata, MIT license, README, project manifests, test/CI inventory, and cloud/cost warnings were inspected statically.
- Docker, Neo4j, model conversion, Azure, GitHub Copilot, and credential paths were `not-run`; no code was copied.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 4 | 20 | Strong modernization pipeline decomposition. |
| C-02 | Testing and verification | 25 | 3 | 15 | 29 tests; model/cloud core not reproduced. |
| C-03 | Production depth | 20 | 3 | 12 | Persistence and operational scripts, large external surface. |
| C-04 | Real MAF dependency | 10 | 0 | 0 | No verified current manifest dependency. |
| C-05 | Source/author credibility | 10 | 5 | 10 | Azure-Samples MIT repository. |
| C-06 | Version traceability | 5 | 4 | 4 | Immutable commit, conflicting dependency claim. |
| C-07 | Maintenance activity | 5 | 4 | 4 | Active in August 2026. |
|  | **Total** | **100** |  | **65** |  |

### Hard gates

- Triggered gate: no verifiable direct MAF dependency or actual MAF API coordinate in the inspected project manifests.
- Result: reject regardless of score.

## Decision

- State: `rejected`
- Approved use: none in the curated MAF evidence layer.
- Prohibited or unsafe use: attributing MEAI/Azure/OpenAI composition to MAF or running costly modernization examples.
- Topic-registry promotion proposal: none.
- Collection action: `none`
- Re-review trigger: project manifests add pinned MAF packages and isolated tests exercise those APIs.
- Residual risk: README and implementation may be temporarily inconsistent during an active migration.
