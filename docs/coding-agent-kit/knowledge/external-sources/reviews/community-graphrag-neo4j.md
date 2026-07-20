# Source review: `community-graphrag-neo4j`

## Snapshot

- Source: Agent Framework GraphRAG Neo4j
- Canonical URL: https://github.com/iLoveAgents/agent-framework-graphrag-neo4j
- Source class: community-repository
- Owner/author: iLoveAgents
- Reviewed commit: `c29e6590ff257ba41137c5129b2f91ecc908a7e4` (2025-11-07)
- Package/API coordinates: Python; agent-framework>=0.1.0; agent_framework.azure.AzureOpenAIResponsesClient
- License: MIT
- Reviewer and date: Codex, 2026-07-17
- Policy version: `v1.1`
- Review track: `code-project`

## Direct Microsoft Agent Framework evidence

- Languages/topics: GraphRAG, Neo4j, DevUI
- Relevant files: 01_extract_contracts.py; contract_graphrag/agent_config.py; devui.py
- Direct evidence: Python; agent-framework>=0.1.0; agent_framework.azure.AzureOpenAIResponsesClient
- Target compatibility: Uses 0.1-era agent_framework.azure imports that do not map directly to target 1.13 provider layout.

## Design and implementation value

- Reusable decisions: Clear contract-review GraphRAG pipeline and separation of extraction/retrieval.
- Verification: No tests or CI found; requires Azure and Neo4j credentials.
- Production and operational depth: Demo includes external stores but lacks failure, security, observability and deployment depth.
- Safety boundary: treat prompts, tool output and external data as untrusted; sample shortcuts are not production defaults.

## Verification

- Evidence reproduced: immutable GitHub metadata, manifest/import inspection, repository tree and test/CI inventory.
- Checks not run: model, cloud, hosted service, external database, deployment and credential-dependent paths (`not-run` by policy).
- Target comparison: static comparison to upstream revision `5ab8877ba55b4778d778cf51450eafe483194708`; no claim of runtime compatibility beyond the coordinates above.
- Unverified claims: live inference quality, load behavior, cloud identity/authorization, cost, and production recovery.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 4 | 20 | Clear contract-review GraphRAG pipeline and separation of extraction/retrieval. |
| C-02 | Testing and verification | 25 | 0 | 0 | No tests or CI found; requires Azure and Neo4j credentials. |
| C-03 | Production depth | 20 | 2 | 8 | Demo includes external stores but lacks failure, security, observability and deployment depth. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | Python; agent-framework>=0.1.0; agent_framework.azure.AzureOpenAIResponsesClient |
| C-05 | Source/author credibility | 10 | 2 | 4 | Public GitHub owner iLoveAgents; license MIT. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit c29e6590ff257ba41137c5129b2f91ecc908a7e4. |
| C-07 | Maintenance activity | 5 | 1 | 1 | Last reviewed commit 2025-11-07; activity judged from repository metadata. |
|  | **Total** | **100** |  | **48** |  |

### Hard gates

- Triggered gates: Current-API hard gate triggered.
- Result: rejected
- Reviewer decision: rejected

## Decision

- State: `rejected`
- Approved use: No formal coding-agent route until re-review.
- Prohibited or unsafe use: Do not copy/vendor source; do not infer current API compatibility; do not run credentialed or costly paths without authorization.
- Topic-registry promotion proposal: GraphRAG, Neo4j, DevUI
- Collection action: `none`
- Re-review trigger: upstream MAF major/API change, source revision/license change, or new compatibility tests.
- Residual risk: Uses 0.1-era agent_framework.azure imports that do not map directly to target 1.13 provider layout.
