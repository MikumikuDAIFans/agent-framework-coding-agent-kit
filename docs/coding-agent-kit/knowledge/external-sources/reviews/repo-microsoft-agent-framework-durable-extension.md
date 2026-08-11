# Source review: `repo-microsoft-agent-framework-durable-extension`

## Snapshot

- Source: `microsoft/agent-framework-durable-extension`
- Canonical URL: https://github.com/microsoft/agent-framework-durable-extension
- Source class: `official-repository`; owner: Microsoft.
- Reviewed commit: `ad941eff53617840c0a046498be36d0b3871329b` (observed 2026-08-11).
- Package coordinates: Python `agent-framework-durabletask` and `agent-framework-azurefunctions` 1.0.0 beta; .NET DurableTask/Azure Functions extensions against MAF 1.13 packages.
- License: MIT.
- Reviewer and date: Codex, 2026-08-11; policy `v1.1`; track `code-project`.

## Direct Microsoft Agent Framework evidence

- This is the official extraction target named by upstream ADR 0032 and now owns the removed Durable Task/Azure Functions implementation, samples, and tests.
- The reviewed tree has 629 files, 106 tests, 5 CI workflows, 64 manifests, extensive durable agent/workflow samples, state serialization, replay, HITL, streaming, and Azure Functions hosting.
- Python packages require `agent-framework-core>=1.11.0,<2`; .NET central versions use MAF 1.13.0 with some provider previews.

## Design and implementation value

- Restores the canonical evidence route for durability content deliberately removed from the main monorepo.
- Independent release cadence and beta/provider boundaries require exact extension and core coordinates.

## Verification

- GitHub metadata, MIT license, immutable tree, manifests, CI, tests, sample inventory, and extraction ADR were inspected statically.
- Azure Functions, Durable Task emulator, storage, model, credential, and integration paths were `not-run`.
- No external code was copied or retained.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 5 | 25 | Canonical durable agent/workflow extraction. |
| C-02 | Testing and verification | 25 | 5 | 25 | 106 tests and dedicated CI. |
| C-03 | Production depth | 20 | 5 | 20 | Persistence, replay, HITL, streaming, hosting. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | Direct MAF packages and extracted source. |
| C-05 | Source/author credibility | 10 | 5 | 10 | Microsoft-owned MIT repository named by upstream ADR. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit and exact package manifests. |
| C-07 | Maintenance activity | 5 | 5 | 5 | Active through 2026-08-10. |
|  | **Total** | **100** |  | **100** |  |

### Hard gates

- Triggered gates: none.
- Result: passes; beta and provider-preview surfaces remain explicit.

## Decision

- State: `adopted`
- Approved use: exact-revision durability, checkpoint/replay, Azure Functions hosting, state, and sample evidence.
- Prohibited or unsafe use: assuming core and extension versions are interchangeable or running cloud/emulator examples without authorization.
- Topic-registry promotion proposal: external `durability`, `hosting`, `workflows`, and `approvals-hitl` route.
- Collection action: `project route`
- Re-review trigger: extension release, core floor change, serialization/state change, or license/security drift.
- Residual risk: the extension's beta cadence can diverge from the local MAF 1.17-generation source.
