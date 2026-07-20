# Source review: `community-maf-getting-started`

## Snapshot

- Source: MAF getting started
- Canonical URL: https://github.com/NikiforovAll/maf-getting-started
- Source class: community-repository
- Owner/author: NikiforovAll
- Reviewed commit: `f38e4378d404e8be2d1a28aad8e9e9d254721c4e` (2026-04-20)
- Package/API coordinates: C# file-based apps; Microsoft.Agents.AI 1.1.0; AzureAI rc5; hosting/protocol previews 260410
- License: not declared
- Reviewer and date: Codex, 2026-07-17
- Policy version: `v1.1`
- Review track: `code-project`

## Direct Microsoft Agent Framework evidence

- Languages/topics: agents, tools, sessions, memory, workflows, MCP, A2A, AG-UI, Foundry
- Relevant files: src/01-hello-agent.cs through src/14-foundry-evaluations.cs
- Direct evidence: C# file-based apps; Microsoft.Agents.AI 1.1.0; AzureAI rc5; hosting/protocol previews 260410
- Target compatibility: Public .NET concepts remain useful, but 1.1/rc5 and April preview protocol packages predate target 1.13 and require symbol-by-symbol confirmation.

## Design and implementation value

- Reusable decisions: Excellent progressive teaching sequence and single-file reproducibility.
- Verification: No automated tests; CI only publishes presentation material.
- Production and operational depth: Teaching samples expose composition but do not cover security, retry, persistence durability or rollback.
- Safety boundary: treat prompts, tool output and external data as untrusted; sample shortcuts are not production defaults.

## Verification

- Evidence reproduced: immutable GitHub metadata, manifest/import inspection, repository tree and test/CI inventory.
- Checks not run: model, cloud, hosted service, external database, deployment and credential-dependent paths (`not-run` by policy).
- Target comparison: static comparison to upstream revision `5ab8877ba55b4778d778cf51450eafe483194708`; no claim of runtime compatibility beyond the coordinates above.
- Unverified claims: live inference quality, load behavior, cloud identity/authorization, cost, and production recovery.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 4 | 20 | Excellent progressive teaching sequence and single-file reproducibility. |
| C-02 | Testing and verification | 25 | 1 | 5 | No automated tests; CI only publishes presentation material. |
| C-03 | Production depth | 20 | 2 | 8 | Teaching samples expose composition but do not cover security, retry, persistence durability or rollback. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | C# file-based apps; Microsoft.Agents.AI 1.1.0; AzureAI rc5; hosting/protocol previews 260410 |
| C-05 | Source/author credibility | 10 | 4 | 8 | Public GitHub owner NikiforovAll; license not declared. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit f38e4378d404e8be2d1a28aad8e9e9d254721c4e. |
| C-07 | Maintenance activity | 5 | 4 | 4 | Last reviewed commit 2026-04-20; activity judged from repository metadata. |
|  | **Total** | **100** |  | **60** |  |

### Hard gates

- Triggered gates: No rejection gate; score below 65 and redistribution license absent.
- Result: quarantined
- Reviewer decision: quarantined

## Decision

- State: `quarantined`
- Approved use: No formal coding-agent route until re-review.
- Prohibited or unsafe use: Do not copy/vendor source; do not infer current API compatibility; do not run credentialed or costly paths without authorization.
- Topic-registry promotion proposal: agents, tools, sessions, memory, workflows, MCP, A2A, AG-UI, Foundry
- Collection action: `none`
- Re-review trigger: upstream MAF major/API change, source revision/license change, or new compatibility tests.
- Residual risk: Public .NET concepts remain useful, but 1.1/rc5 and April preview protocol packages predate target 1.13 and require symbol-by-symbol confirmation.
