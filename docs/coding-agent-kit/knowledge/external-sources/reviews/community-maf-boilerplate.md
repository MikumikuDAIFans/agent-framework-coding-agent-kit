# Source review: `community-maf-boilerplate`

## Snapshot

- Source: maf-boilerplate
- Canonical URL: https://github.com/HakjunMIN/maf-boilerplate
- Source class: community-repository
- Owner/author: HakjunMIN
- Reviewed commit: `5b21471e7765bf9207c737dc5ea955a262766f9e` (2026-05-14)
- Package/API coordinates: Python; agent-framework>=1.2.0; private agent_framework._agents and legacy agent_framework_openai
- License: not declared
- Reviewer and date: Codex, 2026-07-17
- Policy version: `v1.1`
- Review track: `code-project`

## Direct Microsoft Agent Framework evidence

- Languages/topics: getting started, RAG, hosting, observability
- Relevant files: src/homestyle_agent/infrastructure/maf.py; observability.py; tests; CI
- Direct evidence: Python; agent-framework>=1.2.0; private agent_framework._agents and legacy agent_framework_openai
- Target compatibility: Private _agents import and legacy provider package make it unsafe against target 1.13.

## Design and implementation value

- Reusable decisions: Well-structured application boilerplate with infrastructure seams.
- Verification: 29 test-named files and four workflows.
- Production and operational depth: Observability/configuration scaffolding is substantial, but framework adapter bypasses public API.
- Safety boundary: treat prompts, tool output and external data as untrusted; sample shortcuts are not production defaults.

## Verification

- Evidence reproduced: immutable GitHub metadata, manifest/import inspection, repository tree and test/CI inventory.
- Checks not run: model, cloud, hosted service, external database, deployment and credential-dependent paths (`not-run` by policy).
- Target comparison: static comparison to upstream revision `5ab8877ba55b4778d778cf51450eafe483194708`; no claim of runtime compatibility beyond the coordinates above.
- Unverified claims: live inference quality, load behavior, cloud identity/authorization, cost, and production recovery.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 4 | 20 | Well-structured application boilerplate with infrastructure seams. |
| C-02 | Testing and verification | 25 | 4 | 20 | 29 test-named files and four workflows. |
| C-03 | Production depth | 20 | 4 | 16 | Observability/configuration scaffolding is substantial, but framework adapter bypasses public API. |
| C-04 | Real MAF dependency | 10 | 4 | 8 | Python; agent-framework>=1.2.0; private agent_framework._agents and legacy agent_framework_openai |
| C-05 | Source/author credibility | 10 | 2 | 4 | Public GitHub owner HakjunMIN; license not declared. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit 5b21471e7765bf9207c737dc5ea955a262766f9e. |
| C-07 | Maintenance activity | 5 | 4 | 4 | Last reviewed commit 2026-05-14; activity judged from repository metadata. |
|  | **Total** | **100** |  | **77** |  |

### Hard gates

- Triggered gates: Current-API hard gate triggered; redistribution license also absent.
- Result: rejected
- Reviewer decision: rejected

## Decision

- State: `rejected`
- Approved use: No formal coding-agent route until re-review.
- Prohibited or unsafe use: Do not copy/vendor source; do not infer current API compatibility; do not run credentialed or costly paths without authorization.
- Topic-registry promotion proposal: getting started, RAG, hosting, observability
- Collection action: `none`
- Re-review trigger: upstream MAF major/API change, source revision/license change, or new compatibility tests.
- Residual risk: Private _agents import and legacy provider package make it unsafe against target 1.13.
