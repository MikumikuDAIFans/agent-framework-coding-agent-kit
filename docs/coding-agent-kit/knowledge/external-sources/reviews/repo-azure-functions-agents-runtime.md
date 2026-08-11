# Source review: `repo-azure-functions-agents-runtime`

## Snapshot

- Source: `Azure/azure-functions-agents-runtime`
- Canonical URL: https://github.com/Azure/azure-functions-agents-runtime
- Source class: `official-repository`; owner: Azure.
- Reviewed commit: `cc5e14ccda96bfd8ebc3197d33a5730b6cc89762` (observed 2026-08-11).
- Package coordinates: public-preview Python runtime pinned to `agent-framework-core/openai/foundry==1.3.*`.
- License: MIT.
- Reviewer and date: Codex, 2026-08-11; policy `v1.1`; track `code-project`.

## Direct Microsoft Agent Framework evidence

- The runtime directly embeds MAF in a markdown-first Azure Functions programming model with tools, skills, MCP, subagents, streaming, storage triggers, and experimental durable workflows.
- The reviewed tree has 429 files and 177 tests, including many local configuration and endpoint tests plus end-to-end harnesses.
- Its strict MAF 1.3 pins materially trail local target `d0a4165f170193ba1d026a259af40d35bb7eaefe` and current 1.17-generation APIs.

## Design and implementation value

- Strong hosting/configuration and serverless-event design evidence, especially capability filtering and managed-identity boundaries.
- Public-preview and old package pins prevent adoption into current API lookup until migration evidence exists.

## Verification

- Immutable metadata, MIT license, README maturity statement, manifests, tests, samples, and identity/provider boundaries were inspected statically.
- Azure Functions, Azurite, Foundry/OpenAI, credentials, connectors, storage, and deployment were `not-run`; no code was copied.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 4 | 20 | Clear serverless agent/trigger model. |
| C-02 | Testing and verification | 25 | 5 | 25 | 177 tests with local and E2E layers. |
| C-03 | Production depth | 20 | 3 | 12 | Identity, triggers, storage, observability; preview. |
| C-04 | Real MAF dependency | 10 | 4 | 8 | Direct but old 1.3 pins. |
| C-05 | Source/author credibility | 10 | 5 | 10 | Azure-owned MIT repository. |
| C-06 | Version traceability | 5 | 4 | 4 | Immutable commit and strict pins. |
| C-07 | Maintenance activity | 5 | 5 | 5 | Active on 2026-08-11. |
|  | **Total** | **100** |  | **84** |  |

### Hard gates

- Repairable compatibility gap: the primary MAF packages are pinned to 1.3 preview and were not mapped to the target 1.17 generation.
- Result: quarantine despite the structural score; do not infer current compatibility.

## Decision

- State: `quarantined`
- Approved use: none in active lookup; retain review for future hosting comparison.
- Prohibited or unsafe use: presenting 1.3 preview APIs as current or running Azure resources without authorization.
- Topic-registry promotion proposal: reconsider `hosting`, `durability`, and `agent-harness` after migration.
- Collection action: `none`
- Re-review trigger: MAF pins advance and local compatibility tests or an official migration boundary are published.
- Residual risk: the repository is active enough that its package pins may change rapidly after this review.
