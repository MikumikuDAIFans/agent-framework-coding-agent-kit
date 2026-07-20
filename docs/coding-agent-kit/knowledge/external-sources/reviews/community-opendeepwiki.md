# Source review: `community-opendeepwiki`

## Snapshot

- Source: OpenDeepWiki
- Canonical URL: https://github.com/AIDotNet/OpenDeepWiki
- Source class: community-repository
- Owner/author: AIDotNet
- Reviewed commit: `2940a6eb5e90447d57273883330c48b05ab8dfdd` (2026-07-15)
- Package/API coordinates: C#; Microsoft.Agents.AI 1.7.0, OpenAI 1.7.0, Anthropic preview 260526, AzureAI rc5
- License: MIT
- Reviewer and date: Codex, 2026-07-17
- Policy version: `v1.1`
- Review track: `code-project`

## Direct Microsoft Agent Framework evidence

- Languages/topics: memory/RAG, tools, multi-provider hosting
- Relevant files: src/OpenDeepWiki; Directory.Packages.props; EFCore providers; tests/OpenDeepWiki.Tests; Docker/CI
- Direct evidence: C#; Microsoft.Agents.AI 1.7.0, OpenAI 1.7.0, Anthropic preview 260526, AzureAI rc5
- Target compatibility: Stable core 1.7 patterns are near-current but target is 1.13; Anthropic/AzureAI previews require separate checks.

## Design and implementation value

- Reusable decisions: Large real application showing repository ingestion, retrieval and multi-provider boundaries.
- Verification: 89 test-named files and two workflows, though framework-specific coverage is only a subset.
- Production and operational depth: Database choices, cache abstractions, web UI, containers and active operations provide strong production context.
- Safety boundary: treat prompts, tool output and external data as untrusted; sample shortcuts are not production defaults.

## Verification

- Evidence reproduced: immutable GitHub metadata, manifest/import inspection, repository tree and test/CI inventory.
- Checks not run: model, cloud, hosted service, external database, deployment and credential-dependent paths (`not-run` by policy).
- Target comparison: static comparison to upstream revision `5ab8877ba55b4778d778cf51450eafe483194708`; no claim of runtime compatibility beyond the coordinates above.
- Unverified claims: live inference quality, load behavior, cloud identity/authorization, cost, and production recovery.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 5 | 25 | Large real application showing repository ingestion, retrieval and multi-provider boundaries. |
| C-02 | Testing and verification | 25 | 4 | 20 | 89 test-named files and two workflows, though framework-specific coverage is only a subset. |
| C-03 | Production depth | 20 | 5 | 20 | Database choices, cache abstractions, web UI, containers and active operations provide strong production context. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | C#; Microsoft.Agents.AI 1.7.0, OpenAI 1.7.0, Anthropic preview 260526, AzureAI rc5 |
| C-05 | Source/author credibility | 10 | 4 | 8 | Public GitHub owner AIDotNet; license MIT. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit 2940a6eb5e90447d57273883330c48b05ab8dfdd. |
| C-07 | Maintenance activity | 5 | 5 | 5 | Last reviewed commit 2026-07-15; activity judged from repository metadata. |
|  | **Total** | **100** |  | **93** |  |

### Hard gates

- Triggered gates: None.
- Result: adopted
- Reviewer decision: adopted

## Decision

- State: `adopted`
- Approved use: Version-bounded design and code-navigation reference.
- Prohibited or unsafe use: Do not copy/vendor source; do not infer current API compatibility; do not run credentialed or costly paths without authorization.
- Topic-registry promotion proposal: memory/RAG, tools, multi-provider hosting
- Collection action: `project route`
- Re-review trigger: upstream MAF major/API change, source revision/license change, or new compatibility tests.
- Residual risk: Stable core 1.7 patterns are near-current but target is 1.13; Anthropic/AzureAI previews require separate checks.
