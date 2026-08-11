# Source review: `community-temporal-dotnet-agents`

## Snapshot

- Source: `temporal-community/temporal-dotnet-agents`
- Canonical URL: https://github.com/temporal-community/temporal-dotnet-agents
- Source class: `community-repository`; owner: temporal-community.
- Reviewed commit: `4a98f2b14eccccaf3cc2c96a64ea178050d536b9` (observed 2026-08-11).
- Package coordinates: Temporalio 1.17.0 and `Microsoft.Agents.AI` / OpenAI 1.17.0.
- License: MIT.
- Reviewer and date: Codex, 2026-08-11; policy `v1.1`; track `code-project`.

## Direct Microsoft Agent Framework evidence

- Dedicated MAF libraries, architecture docs, samples, and tests cover durable turns, sessions, middleware, approvals, tools, context providers, skills, routing, observability, replay, and compatibility snapshots.
- The reviewed tree has 588 files, 215 tests, three CI workflows, and exact central package pins matching the local 1.17 generation.
- Temporal service integration remains separately versioned and is not equivalent to the official Durable Task extension.

## Design and implementation value

- Particularly strong evidence for determinism, replay compatibility, durable session ownership, bounded histories, and integration tests.
- Runtime/service deployment and operational policy remain application-specific.

## Verification

- Immutable metadata, MIT license, architecture/how-to corpus, package versions, test inventory, compatibility histories, and CI were inspected statically.
- Temporal service, model/provider, cloud, credential, and production paths were `not-run`; no code was copied.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 5 | 25 | Deep durability/determinism architecture. |
| C-02 | Testing and verification | 25 | 5 | 25 | 215 tests, compatibility histories, CI. |
| C-03 | Production depth | 20 | 5 | 20 | Replay, approvals, telemetry, lifecycle and failure seams. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | Direct MAF 1.17 libraries and samples. |
| C-05 | Source/author credibility | 10 | 4 | 8 | Temporal community organization, public MIT project. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit and central pins. |
| C-07 | Maintenance activity | 5 | 5 | 5 | Active on 2026-08-11. |
|  | **Total** | **100** |  | **98** |  |

### Hard gates

- Triggered gates: none.
- Result: passes.

## Decision

- State: `adopted`
- Approved use: version-bounded durability, replay, compatibility, and Temporal integration design evidence.
- Prohibited or unsafe use: treating Temporal semantics as official Durable Task behavior or running service/model paths without authorization.
- Topic-registry promotion proposal: durability, workflows, sessions-context, approvals-hitl, observability, and testing.
- Collection action: `project route`
- Re-review trigger: MAF/Temporal package movement, replay format change, license change, or security issue.
- Residual risk: local static review does not reproduce a live Temporal service or provider-backed integration.
