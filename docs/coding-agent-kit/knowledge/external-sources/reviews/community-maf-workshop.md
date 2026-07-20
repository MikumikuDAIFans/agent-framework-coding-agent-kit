# Source review: `community-maf-workshop`

## Snapshot

- Source: MAF workshop
- Canonical URL: https://github.com/antoniosql/maf-workshop
- Source class: community-repository
- Owner/author: antoniosql
- Reviewed commit: `4e9467066cac049d82bf88db0e26fb3754b8ba17` (2025-11-28)
- Package/API coordinates: Python; agent-framework>=1.0.0b251120; core>=b251001; Azure Functions preview
- License: MIT
- Reviewer and date: Codex, 2026-07-17
- Policy version: `v1.1`
- Review track: `code-project`

## Direct Microsoft Agent Framework evidence

- Languages/topics: agents, MCP, workflows, observability, Azure Functions
- Relevant files: agents/*.py; README; durable agents guide
- Direct evidence: Python; agent-framework>=1.0.0b251120; core>=b251001; Azure Functions preview
- Target compatibility: ChatAgent, handler/executor decorators and agent_framework.azure imports are early-beta APIs incompatible as-is with target.

## Design and implementation value

- Reusable decisions: Useful Spanish workshop progression and runnable-file organization.
- Verification: No automated tests or CI found; model/cloud examples not run.
- Production and operational depth: A hosting guide exists, but examples omit systematic reliability/security validation.
- Safety boundary: treat prompts, tool output and external data as untrusted; sample shortcuts are not production defaults.

## Verification

- Evidence reproduced: immutable GitHub metadata, manifest/import inspection, repository tree and test/CI inventory.
- Checks not run: model, cloud, hosted service, external database, deployment and credential-dependent paths (`not-run` by policy).
- Target comparison: static comparison to upstream revision `5ab8877ba55b4778d778cf51450eafe483194708`; no claim of runtime compatibility beyond the coordinates above.
- Unverified claims: live inference quality, load behavior, cloud identity/authorization, cost, and production recovery.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 4 | 20 | Useful Spanish workshop progression and runnable-file organization. |
| C-02 | Testing and verification | 25 | 0 | 0 | No automated tests or CI found; model/cloud examples not run. |
| C-03 | Production depth | 20 | 2 | 8 | A hosting guide exists, but examples omit systematic reliability/security validation. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | Python; agent-framework>=1.0.0b251120; core>=b251001; Azure Functions preview |
| C-05 | Source/author credibility | 10 | 3 | 6 | Public GitHub owner antoniosql; license MIT. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit 4e9467066cac049d82bf88db0e26fb3754b8ba17. |
| C-07 | Maintenance activity | 5 | 1 | 1 | Last reviewed commit 2025-11-28; activity judged from repository metadata. |
|  | **Total** | **100** |  | **50** |  |

### Hard gates

- Triggered gates: Current-API hard gate triggered.
- Result: rejected
- Reviewer decision: rejected

## Decision

- State: `rejected`
- Approved use: No formal coding-agent route until re-review.
- Prohibited or unsafe use: Do not copy/vendor source; do not infer current API compatibility; do not run credentialed or costly paths without authorization.
- Topic-registry promotion proposal: agents, MCP, workflows, observability, Azure Functions
- Collection action: `none`
- Re-review trigger: upstream MAF major/API change, source revision/license change, or new compatibility tests.
- Residual risk: ChatAgent, handler/executor decorators and agent_framework.azure imports are early-beta APIs incompatible as-is with target.
