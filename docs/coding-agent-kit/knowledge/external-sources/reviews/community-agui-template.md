# Source review: `community-agui-template`

## Snapshot

- Source: MAF AG-UI Azure Template
- Canonical URL: https://github.com/xxyckiki/MAF-AGUI-Azure-Template
- Source class: community-repository
- Owner/author: xxyckiki
- Reviewed commit: `8da9c9e8e219eb510f633297efc63a7f127aac29` (2025-12-09)
- Package/API coordinates: Python; agent-framework/ag-ui/azure-ai >=1.0.0b251120
- License: Apache-2.0
- Reviewer and date: Codex, 2026-07-17
- Policy version: `v1.1`
- Review track: `code-project`

## Direct Microsoft Agent Framework evidence

- Languages/topics: AG-UI, workflows, hosting, approvals
- Relevant files: main.py; src/services/{agent,workflow,tools}.py; middleware; Cosmos store; Terraform; tests
- Direct evidence: Python; agent-framework/ag-ui/azure-ai >=1.0.0b251120
- Target compatibility: Uses ChatAgent, ai_function, AgentRunContext and old AG-UI adapter names from Nov-2025 beta; target 1.13 has incompatible surfaces.

## Design and implementation value

- Reusable decisions: Good full-stack template boundaries, Cosmos history, middleware and Terraform.
- Verification: Eight test-named files and two workflows; cloud deployment not run.
- Production and operational depth: IaC, observability and persistent store are valuable, but preview protocol/security defaults need review.
- Safety boundary: treat prompts, tool output and external data as untrusted; sample shortcuts are not production defaults.

## Verification

- Evidence reproduced: immutable GitHub metadata, manifest/import inspection, repository tree and test/CI inventory.
- Checks not run: model, cloud, hosted service, external database, deployment and credential-dependent paths (`not-run` by policy).
- Target comparison: static comparison to upstream revision `5ab8877ba55b4778d778cf51450eafe483194708`; no claim of runtime compatibility beyond the coordinates above.
- Unverified claims: live inference quality, load behavior, cloud identity/authorization, cost, and production recovery.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 5 | 25 | Good full-stack template boundaries, Cosmos history, middleware and Terraform. |
| C-02 | Testing and verification | 25 | 3 | 15 | Eight test-named files and two workflows; cloud deployment not run. |
| C-03 | Production depth | 20 | 4 | 16 | IaC, observability and persistent store are valuable, but preview protocol/security defaults need review. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | Python; agent-framework/ag-ui/azure-ai >=1.0.0b251120 |
| C-05 | Source/author credibility | 10 | 3 | 6 | Public GitHub owner xxyckiki; license Apache-2.0. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit 8da9c9e8e219eb510f633297efc63a7f127aac29. |
| C-07 | Maintenance activity | 5 | 2 | 2 | Last reviewed commit 2025-12-09; activity judged from repository metadata. |
|  | **Total** | **100** |  | **79** |  |

### Hard gates

- Triggered gates: Current-API hard gate triggered despite architectural value.
- Result: rejected
- Reviewer decision: rejected

## Decision

- State: `rejected`
- Approved use: No formal coding-agent route until re-review.
- Prohibited or unsafe use: Do not copy/vendor source; do not infer current API compatibility; do not run credentialed or costly paths without authorization.
- Topic-registry promotion proposal: AG-UI, workflows, hosting, approvals
- Collection action: `none`
- Re-review trigger: upstream MAF major/API change, source revision/license change, or new compatibility tests.
- Residual risk: Uses ChatAgent, ai_function, AgentRunContext and old AG-UI adapter names from Nov-2025 beta; target 1.13 has incompatible surfaces.
