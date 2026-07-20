# Source review: `community-sideseat`

## Snapshot

- Source: SideSeat Agent Framework sample
- Canonical URL: https://github.com/sideseat/sideseat/tree/main/misc/samples/python/agent-framework
- Source class: community-repository
- Owner/author: sideseat
- Reviewed commit: `c40efef761da8af0e63dc5103afd1e0f01d0cc18` (2026-05-30)
- Package/API coordinates: Python; agent-framework>=1.0.0b0 and anthropic>=1.0.0b0; built-in observability
- License: Apache-2.0
- Reviewer and date: Codex, 2026-07-17
- Policy version: `v1.1`
- Review track: `code-project`

## Direct Microsoft Agent Framework evidence

- Languages/topics: observability, evaluation, agents, tools, RAG
- Relevant files: misc/samples/python/agent-framework/{runner,telemetry_setup,samples,pyproject.toml}
- Direct evidence: Python; agent-framework>=1.0.0b0 and anthropic>=1.0.0b0; built-in observability
- Target compatibility: Comment identifies rc4 observability API while dependency floor floats from beta; exact target 1.13 behavior must be verified.

## Design and implementation value

- Reusable decisions: Compact cross-framework instrumentation sample set useful for trace-shape comparison.
- Verification: Parent repo has tests/CI, but no dedicated MAF sample tests were found.
- Production and operational depth: SideSeat SDK/workbench is production-oriented; sample itself enables sensitive telemetry and is not a hardened app.
- Safety boundary: treat prompts, tool output and external data as untrusted; sample shortcuts are not production defaults.

## Verification

- Evidence reproduced: immutable GitHub metadata, manifest/import inspection, repository tree and test/CI inventory.
- Checks not run: model, cloud, hosted service, external database, deployment and credential-dependent paths (`not-run` by policy).
- Target comparison: static comparison to upstream revision `5ab8877ba55b4778d778cf51450eafe483194708`; no claim of runtime compatibility beyond the coordinates above.
- Unverified claims: live inference quality, load behavior, cloud identity/authorization, cost, and production recovery.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 4 | 20 | Compact cross-framework instrumentation sample set useful for trace-shape comparison. |
| C-02 | Testing and verification | 25 | 2 | 10 | Parent repo has tests/CI, but no dedicated MAF sample tests were found. |
| C-03 | Production depth | 20 | 3 | 12 | SideSeat SDK/workbench is production-oriented; sample itself enables sensitive telemetry and is not a hardened app. |
| C-04 | Real MAF dependency | 10 | 4 | 8 | Python; agent-framework>=1.0.0b0 and anthropic>=1.0.0b0; built-in observability |
| C-05 | Source/author credibility | 10 | 4 | 8 | Public GitHub owner sideseat; license Apache-2.0. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit c40efef761da8af0e63dc5103afd1e0f01d0cc18. |
| C-07 | Maintenance activity | 5 | 4 | 4 | Last reviewed commit 2026-05-30; activity judged from repository metadata. |
|  | **Total** | **100** |  | **67** |  |

### Hard gates

- Triggered gates: None; direct imports are present, but compatibility confidence is limited.
- Result: context-only
- Reviewer decision: context-only

## Decision

- State: `context-only`
- Approved use: Architecture/context comparison only; not API correctness evidence.
- Prohibited or unsafe use: Do not copy/vendor source; do not infer current API compatibility; do not run credentialed or costly paths without authorization.
- Topic-registry promotion proposal: observability, evaluation, agents, tools, RAG
- Collection action: `link and annotation only`
- Re-review trigger: upstream MAF major/API change, source revision/license change, or new compatibility tests.
- Residual risk: Comment identifies rc4 observability API while dependency floor floats from beta; exact target 1.13 behavior must be verified.
