# Source review: `community-a2a-travel`

## Snapshot

- Source: Multi-agent travel planner A2A interop
- Canonical URL: https://github.com/zhuohanl/multi-agent-travel-planner-a2a-interop
- Source class: community-repository
- Owner/author: zhuohanl
- Reviewed commit: `61bbe36cc8ef4433b4715ccf8147c74a3f8d04bb` (2026-02-26)
- Package/API coordinates: Python; agent-framework>=1.0.0b260107; agent-framework-azure-ai; Azure agent server
- License: not declared
- Reviewer and date: Codex, 2026-07-17
- Policy version: `v1.1`
- Review track: `code-project`

## Direct Microsoft Agent Framework evidence

- Languages/topics: A2A, orchestration, hosted agents
- Relevant files: src/shared/agents/base_agent.py; interoperability/foundry; A2A services and tests
- Direct evidence: Python; agent-framework>=1.0.0b260107; agent-framework-azure-ai; Azure agent server
- Target compatibility: Imports private agent_framework._types and _threads and old ChatAgent/AzureAIAgentClient surfaces; not compatible as-is with target.

## Design and implementation value

- Reusable decisions: Ambitious interoperability topology and deployment wrapper model.
- Verification: Large test corpus and CI, but cloud/A2A end-to-end path was not run.
- Production and operational depth: Deployment automation and wrappers exist; credentials, hosted resources and many moving services increase risk.
- Safety boundary: treat prompts, tool output and external data as untrusted; sample shortcuts are not production defaults.

## Verification

- Evidence reproduced: immutable GitHub metadata, manifest/import inspection, repository tree and test/CI inventory.
- Checks not run: model, cloud, hosted service, external database, deployment and credential-dependent paths (`not-run` by policy).
- Target comparison: static comparison to upstream revision `5ab8877ba55b4778d778cf51450eafe483194708`; no claim of runtime compatibility beyond the coordinates above.
- Unverified claims: live inference quality, load behavior, cloud identity/authorization, cost, and production recovery.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 5 | 25 | Ambitious interoperability topology and deployment wrapper model. |
| C-02 | Testing and verification | 25 | 4 | 20 | Large test corpus and CI, but cloud/A2A end-to-end path was not run. |
| C-03 | Production depth | 20 | 4 | 16 | Deployment automation and wrappers exist; credentials, hosted resources and many moving services increase risk. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | Python; agent-framework>=1.0.0b260107; agent-framework-azure-ai; Azure agent server |
| C-05 | Source/author credibility | 10 | 3 | 6 | Public GitHub owner zhuohanl; license not declared. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit 61bbe36cc8ef4433b4715ccf8147c74a3f8d04bb. |
| C-07 | Maintenance activity | 5 | 3 | 3 | Last reviewed commit 2026-02-26; activity judged from repository metadata. |
|  | **Total** | **100** |  | **85** |  |

### Hard gates

- Triggered gates: Current-API hard gate: reviewed code depends on private/removed early-beta surfaces; license also undeclared.
- Result: rejected
- Reviewer decision: rejected

## Decision

- State: `rejected`
- Approved use: No formal coding-agent route until re-review.
- Prohibited or unsafe use: Do not copy/vendor source; do not infer current API compatibility; do not run credentialed or costly paths without authorization.
- Topic-registry promotion proposal: A2A, orchestration, hosted agents
- Collection action: `none`
- Re-review trigger: upstream MAF major/API change, source revision/license change, or new compatibility tests.
- Residual risk: Imports private agent_framework._types and _threads and old ChatAgent/AzureAIAgentClient surfaces; not compatible as-is with target.
