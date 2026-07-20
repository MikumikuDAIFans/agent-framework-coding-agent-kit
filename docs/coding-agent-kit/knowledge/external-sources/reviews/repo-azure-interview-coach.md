# Source review: `repo-azure-interview-coach`

## Snapshot

- Source: `Azure-Samples/interview-coach-agent-framework`
- Canonical URL: https://github.com/Azure-Samples/interview-coach-agent-framework
- Source class: `official-repository`; owner: Azure-Samples/Microsoft.
- Reviewed commit: `d9557897274996c2d0f869bfafe0aba7e53393c0` (2026-07-10T12:19:25Z).
- Package/API coordinates: .NET, centrally versioned `Microsoft.Agents.AI`, Foundry, DevUI, Hosting, AG-UI, OpenAI and Workflows packages.
- License: MIT.
- Reviewer and date: Codex, 2026-07-17; policy `v1.1`; track `code-project`.

## Direct Microsoft Agent Framework evidence

- Languages: C# and web assets.
- Direct package references span agent core/provider, workflows, hosting, DevUI and AG-UI; 123-blob end-to-end application includes Agent, Aspire AppHost, MCP interview-data server, WebUI and service defaults.
- A dedicated `HandoffToolResultFixTests.cs` and test project demonstrate at least one regression boundary.
- Exact package resolution is centralized; use the immutable commit and restore lock/output when reproducing.

## Design and implementation value

- Reusable: clear host/agent/MCP/UI/service-default decomposition and a concrete handoff-driven application.
- Production value: Aspire composition, hosted protocol surfaces and provider guidance; static deployment workflow exists.
- Limits: only a small detected test surface; no evidence of exhaustive failure/replay, authorization, tenant isolation, evaluation dataset/threshold, load/SLO or rollback testing.
- External model/Foundry/MCP side effects require credentials and policy controls.

## Verification

- GitHub API verified commit/date/license, direct packages, project topology, workflow and test paths.
- Static inspection only; restore/build and cloud scenarios were not run in this evidence task.
- Target compatibility is bounded to concepts/packages present at `5ab8877...`; exact centralized versions remain a reproduction check.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 5 | 25 | Coherent end-to-end service decomposition. |
| C-02 | Testing and verification | 25 | 3 | 15 | Test project/regression plus workflow, limited breadth. |
| C-03 | Production depth | 20 | 4 | 16 | Aspire, hosting, protocols and service defaults. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | Broad direct MAF packages and API use. |
| C-05 | Source/author credibility | 10 | 5 | 10 | Azure-Samples, Microsoft, MIT. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit and central package manifest. |
| C-07 | Maintenance activity | 5 | 5 | 5 | Updated seven days before review. |
|  | **Total** | **100** |  | **86** |  |

### Hard gates

- Triggered gates: none.
- Result: passes.
- Reviewer decision: `adopted` as a project route.

## Decision

- State: `adopted`
- Approved use: service boundaries, handoff application, MCP/AG-UI/hosting composition.
- Prohibited or unsafe use: assuming sample auth, evaluation, resilience or rollout is complete.
- Topic-registry promotion proposal: `agents`, `tools`, `hosting`, `protocols`.
- Collection action: `project route`
- Re-review trigger: package manifest/API drift, failed clean build, or repository inactivity.
- Residual risk: exact cloud behavior and dependency resolution were not locally run.
