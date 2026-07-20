# Source review: `community-zep`

## Snapshot

- Source: Zep Microsoft Agent Framework integration
- Canonical URL: https://github.com/getzep/zep
- Source class: community-repository
- Owner/author: getzep
- Reviewed commit: `175dd66e0254085ef6347b5763addb19e777611f` (2026-07-15)
- Package/API coordinates: Python; zep-ms-agent-framework; agent-framework-core>=1.8.1; optional OpenAI>=1.8.1
- License: Apache-2.0
- Reviewer and date: Codex, 2026-07-17
- Policy version: `v1.1`
- Review track: `code-project`

## Direct Microsoft Agent Framework evidence

- Languages/topics: context provider, memory, graph search tools, middleware
- Relevant files: integrations/ms-agent-framework/python/{src,tests,examples,README,CHANGELOG}
- Direct evidence: Python; zep-ms-agent-framework; agent-framework-core>=1.8.1; optional OpenAI>=1.8.1
- Target compatibility: Targets >=1.8.1 and explicitly audits framework session/state limitations; verify target 1.13 provider hooks before reuse.

## Design and implementation value

- Reusable decisions: Focused adapter with explicit identity/state ownership, graceful-degradation semantics and parameter exposure controls.
- Verification: Dedicated basic, context-builder, provisioning, search and integration tests plus monorepo CI.
- Production and operational depth: Idempotent provisioning, failure contracts, typed search exposure and changelog provide solid production guidance.
- Safety boundary: treat prompts, tool output and external data as untrusted; sample shortcuts are not production defaults.

## Verification

- Evidence reproduced: immutable GitHub metadata, manifest/import inspection, repository tree and test/CI inventory.
- Checks not run: model, cloud, hosted service, external database, deployment and credential-dependent paths (`not-run` by policy).
- Target comparison: static comparison to upstream revision `5ab8877ba55b4778d778cf51450eafe483194708`; no claim of runtime compatibility beyond the coordinates above.
- Unverified claims: live inference quality, load behavior, cloud identity/authorization, cost, and production recovery.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 5 | 25 | Focused adapter with explicit identity/state ownership, graceful-degradation semantics and parameter exposure controls. |
| C-02 | Testing and verification | 25 | 5 | 25 | Dedicated basic, context-builder, provisioning, search and integration tests plus monorepo CI. |
| C-03 | Production depth | 20 | 5 | 20 | Idempotent provisioning, failure contracts, typed search exposure and changelog provide solid production guidance. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | Python; zep-ms-agent-framework; agent-framework-core>=1.8.1; optional OpenAI>=1.8.1 |
| C-05 | Source/author credibility | 10 | 5 | 10 | Public GitHub owner getzep; license Apache-2.0. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit 175dd66e0254085ef6347b5763addb19e777611f. |
| C-07 | Maintenance activity | 5 | 5 | 5 | Last reviewed commit 2026-07-15; activity judged from repository metadata. |
|  | **Total** | **100** |  | **100** |  |

### Hard gates

- Triggered gates: None.
- Result: adopted
- Reviewer decision: adopted

## Decision

- State: `adopted`
- Approved use: Version-bounded design and code-navigation reference.
- Prohibited or unsafe use: Do not copy/vendor source; do not infer current API compatibility; do not run credentialed or costly paths without authorization.
- Topic-registry promotion proposal: context provider, memory, graph search tools, middleware
- Collection action: `project route`
- Re-review trigger: upstream MAF major/API change, source revision/license change, or new compatibility tests.
- Residual risk: Targets >=1.8.1 and explicitly audits framework session/state limitations; verify target 1.13 provider hooks before reuse.
