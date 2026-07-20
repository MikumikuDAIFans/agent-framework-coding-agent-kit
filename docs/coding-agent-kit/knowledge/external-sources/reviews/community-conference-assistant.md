# Source review: `community-conference-assistant`

## Snapshot

- Source: .NET AI Conference Assistant
- Canonical URL: https://github.com/luisquintanilla/dotnet-ai-conference-assistant
- Source class: community-repository
- Owner/author: luisquintanilla
- Reviewed commit: `f1042022a7e3b680768e8292053e286600cf5a86` (2026-03-31)
- Package/API coordinates: C#; Microsoft.Agents.AI/OpenAI/Workflows 1.0.0-rc4; Hosting preview 260311
- License: MIT
- Reviewer and date: Codex, 2026-07-17
- Policy version: `v1.1`
- Review track: `code-project`

## Direct Microsoft Agent Framework evidence

- Languages/topics: agents, RAG, workflows, MCP, Aspire hosting
- Relevant files: docs/architecture.md; ConferenceAssistant.Agents; Ingestion; MCP; three test projects
- Direct evidence: C#; Microsoft.Agents.AI/OpenAI/Workflows 1.0.0-rc4; Hosting preview 260311
- Target compatibility: rc4 public .NET surface predates target 1.13; retain architecture, verify all constructor/hosting symbols.

## Design and implementation value

- Reusable decisions: Coherent end-to-end application with ingestion, retrieval, specialized agents, workflow and MCP boundaries.
- Verification: Dedicated agent, ingestion and MCP test projects; no CI workflow observed and cloud inference not run.
- Production and operational depth: Aspire composition and service separation are useful; auth, load, recovery and rollback evidence is limited.
- Safety boundary: treat prompts, tool output and external data as untrusted; sample shortcuts are not production defaults.

## Verification

- Evidence reproduced: immutable GitHub metadata, manifest/import inspection, repository tree and test/CI inventory.
- Checks not run: model, cloud, hosted service, external database, deployment and credential-dependent paths (`not-run` by policy).
- Target comparison: static comparison to upstream revision `5ab8877ba55b4778d778cf51450eafe483194708`; no claim of runtime compatibility beyond the coordinates above.
- Unverified claims: live inference quality, load behavior, cloud identity/authorization, cost, and production recovery.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 5 | 25 | Coherent end-to-end application with ingestion, retrieval, specialized agents, workflow and MCP boundaries. |
| C-02 | Testing and verification | 25 | 4 | 20 | Dedicated agent, ingestion and MCP test projects; no CI workflow observed and cloud inference not run. |
| C-03 | Production depth | 20 | 4 | 16 | Aspire composition and service separation are useful; auth, load, recovery and rollback evidence is limited. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | C#; Microsoft.Agents.AI/OpenAI/Workflows 1.0.0-rc4; Hosting preview 260311 |
| C-05 | Source/author credibility | 10 | 4 | 8 | Public GitHub owner luisquintanilla; license MIT. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit f1042022a7e3b680768e8292053e286600cf5a86. |
| C-07 | Maintenance activity | 5 | 4 | 4 | Last reviewed commit 2026-03-31; activity judged from repository metadata. |
|  | **Total** | **100** |  | **88** |  |

### Hard gates

- Triggered gates: None.
- Result: adopted
- Reviewer decision: adopted

## Decision

- State: `adopted`
- Approved use: Version-bounded design and code-navigation reference.
- Prohibited or unsafe use: Do not copy/vendor source; do not infer current API compatibility; do not run credentialed or costly paths without authorization.
- Topic-registry promotion proposal: agents, RAG, workflows, MCP, Aspire hosting
- Collection action: `project route`
- Re-review trigger: upstream MAF major/API change, source revision/license change, or new compatibility tests.
- Residual risk: rc4 public .NET surface predates target 1.13; retain architecture, verify all constructor/hosting symbols.
