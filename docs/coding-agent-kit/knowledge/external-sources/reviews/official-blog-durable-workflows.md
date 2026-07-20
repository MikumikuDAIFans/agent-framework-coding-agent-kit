# Source review: `official-blog-durable-workflows`

## Snapshot

- Source: Durable Workflows in the Microsoft Agent Framework
- Canonical URL: https://devblogs.microsoft.com/dotnet/durable-workflows-in-microsoft-agent-framework/
- Source class: `official-engineering`; author: Shyju Krishnankutty, Microsoft.
- Reviewed page date: 2026-05-06.
- Package/API coordinates: .NET `Microsoft.Agents.AI`, `.Workflows`, `.DurableTask` (the latter shown as prerelease), Durable Task Scheduler/Azure Functions.
- License: no article-specific redistribution license verified.
- Reviewer and date: Codex, 2026-07-17; policy `v1.1`; track `technical-article`.

## Direct Microsoft Agent Framework evidence

- Languages: C#.
- Complete progression covers typed executors, `WorkflowBuilder`, in-process streaming, durable registration, fan-out/fan-in agents, checkpoints and Azure Functions hosting.
- Target-boundary check: repository code search at `5ab8877ba55b4778d778cf51450eafe483194708` finds `ConfigureDurableOptions` in DurableTask source and matching hosted samples.
- DurableTask/package maturity remains version-sensitive and the article explicitly uses a prerelease package.

## Design and implementation value

- Reusable: preserve the workflow definition while swapping execution runtime; stable executor IDs and typed edges form persistence/compatibility coordinates; checkpoint completed parallel branches.
- Strong state-flow explanation distinguishes in-memory loss from durable scheduler ownership.
- Shortcuts: simulated order/email actions are not idempotent production tools; examples do not fully specify compensation, duplicate delivery, retention, authz or rollout compatibility.
- Hosting and identity are demonstrated, but live deployment and rollback were not validated here.

## Verification

- Page code, commands, environment coordinates and stated checkpoint behavior were inspected.
- Key API mapped to official source/current samples at the target revision.
- No Azure/model/Durable Task resources were provisioned; runtime claims remain `not-run` with static source evidence.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| A-01 | Real demo | 30 | 5 | 30 | End-to-end incremental code and commands. |
| A-02 | Design value | 25 | 5 | 25 | Explicit runtime/state/checkpoint boundaries. |
| A-03 | Technical recency | 15 | 5 | Key APIs map to target revision. |
| A-04 | Publication date | 15 | 5 | Recent 2026 article. |
| A-05 | Source/author credibility | 15 | 5 | Official Microsoft engineer and source links. |
|  | **Total** | **100** |  | **100** |  |

### Hard gates

- Triggered gates: none.
- Result: passes; prerelease maturity is a mandatory usage annotation.
- Reviewer decision: `adopted`.

## Decision

- State: `adopted`
- Approved use: durable workflow design route paired with target source/tests.
- Prohibited or unsafe use: treating simulated side effects as replay-safe or assuming GA/package versions.
- Topic-registry promotion proposal: `durability`, `workflows`, `hosting`.
- Collection action: `link and annotation only`
- Re-review trigger: DurableTask API/maturity or persisted-state compatibility changes.
- Residual risk: distributed replay and failure semantics require exact-version tests.
