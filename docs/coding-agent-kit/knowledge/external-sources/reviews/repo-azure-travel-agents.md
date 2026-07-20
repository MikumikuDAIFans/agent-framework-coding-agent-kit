# Source review: `repo-azure-travel-agents`

## Snapshot

- Source: `Azure-Samples/azure-ai-travel-agents`
- Canonical URL: https://github.com/Azure-Samples/azure-ai-travel-agents
- Source class: `official-repository`; owner: Azure-Samples/Microsoft.
- Reviewed commit: `a66e229c4bd4aeb4eb9b9460e2ec6d1701f142c1` (2026-04-29T16:11:15Z).
- Package/API coordinates: MAF Python subproject declares `agent-framework>=1.0.0b251001`; multi-framework monorepo also contains LangChain/LlamaIndex and MCP services.
- License: MIT.
- Reviewer and date: Codex, 2026-07-17; policy `v1.1`; track `code-project`.

## Direct Microsoft Agent Framework evidence

- Languages: Python MAF API, TypeScript/JavaScript, C# and other comparison implementations.
- Isolated route: `packages/api-maf-python` with direct MAF dependency, agent/provider/workflow/MCP implementation and tests.
- Tests include agents, configuration, providers, workflow, MCP client and graceful degradation.
- Repository has build/deploy/infra validation, multi-language CodeQL and Azure Developer workflows.
- Dependency lower bound is broad and not a reproducible lock; route must pin commit plus resolved package version.
- Target boundary: the reviewed subproject must be checked against `microsoft/agent-framework@5ab8877ba55b4778d778cf51450eafe483194708`; its open lower bound cannot prove that resolution by itself.

## Design and implementation value

- Reusable: enterprise-style separation of UI, API implementation, MCP servers, containers and infrastructure; useful comparison without conflating framework-specific packages.
- Strong failure evidence includes MCP graceful-degradation tests; CI/security/deployment files raise production value.
- Limits: comparison monorepo complexity, cloud/container dependencies and a permissive MAF version range; not all repository architecture is MAF-derived.
- Application-specific authz, tenant/data retention, eval thresholds, load/SLO and rollback proof need separate validation.

## Verification

- GitHub API verified commit/date/license, 729 blobs, 11 workflow files, dependency and eight test paths.
- Static inspection only; unit/build/deploy commands were not run because the audit does not vendor the external repository and cloud deployment is credentialed/costly.
- Route is explicitly restricted to `packages/api-maf-python` at the reviewed commit.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 5 | 25 | Strong service/MCP/framework isolation. |
| C-02 | Testing and verification | 25 | 4 | 20 | Focused MAF tests and substantial CI. |
| C-03 | Production depth | 20 | 5 | 20 | Containers, infra, deployment, CodeQL, degradation. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | Direct dependency and isolated implementation. |
| C-05 | Source/author credibility | 10 | 5 | 10 | Azure-Samples, Microsoft, MIT. |
| C-06 | Version traceability | 5 | 4 | 4 | Commit pinned; dependency lower bound is broad. |
| C-07 | Maintenance activity | 5 | 5 | 5 | Active workflows/repository near review. |
|  | **Total** | **100** |  | **94** |  |

### Hard gates

- Triggered gates: none.
- Result: passes.
- Reviewer decision: `adopted`, MAF subproject only.

## Decision

- State: `adopted`
- Approved use: MAF Python service/MCP/workflow/degradation-test architecture at pinned commit.
- Prohibited or unsafe use: treating other-framework packages as MAF patterns or using the open dependency range unpinned.
- Topic-registry promotion proposal: `orchestration`, `protocols`, `hosting`, `testing`.
- Collection action: `project route`
- Re-review trigger: MAF subproject removal, dependency/API drift or CI failure.
- Residual risk: exact clean build and cloud deployment were not reproduced.
