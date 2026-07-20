# Source review: `community-taskagent`

## Snapshot

- Source: TaskAgent-AgenticAI
- Canonical URL: https://github.com/cristofima/TaskAgent-AgenticAI
- Source class: community-repository
- Owner/author: cristofima
- Reviewed commit: `4a998448f6b173b366f36a9512ea77c9c355e341` (2026-02-16)
- Package/API coordinates: C#; Microsoft.Agents.AI.OpenAI and Hosting.AGUI.AspNetCore 1.0.0-preview.251125.1
- License: MIT
- Reviewer and date: Codex, 2026-07-17
- Policy version: `v1.1`
- Review track: `code-project`

## Direct Microsoft Agent Framework evidence

- Languages/topics: hosting, sessions, AG-UI, observability, security
- Relevant files: docs/architecture; AgentStreamingService; PostgresChatMessageStore; AgentEventMapper; unit/integration tests
- Direct evidence: C#; Microsoft.Agents.AI.OpenAI and Hosting.AGUI.AspNetCore 1.0.0-preview.251125.1
- Target compatibility: Architecture is reusable; the Nov-2025 preview AG-UI and agent APIs are stale against target 1.13 and must not be copied literally.

## Design and implementation value

- Reusable decisions: Strong clean-architecture separation, persistent chat store and explicit streaming/event mapping.
- Verification: 27 test-named files, three CI workflows and documented unit/integration strategy; live model path not run.
- Production and operational depth: Aspire, PostgreSQL, auth/security notes, telemetry and deployment material make this a substantial application reference.
- Safety boundary: treat prompts, tool output and external data as untrusted; sample shortcuts are not production defaults.

## Verification

- Evidence reproduced: immutable GitHub metadata, manifest/import inspection, repository tree and test/CI inventory.
- Checks not run: model, cloud, hosted service, external database, deployment and credential-dependent paths (`not-run` by policy).
- Target comparison: static comparison to upstream revision `5ab8877ba55b4778d778cf51450eafe483194708`; no claim of runtime compatibility beyond the coordinates above.
- Unverified claims: live inference quality, load behavior, cloud identity/authorization, cost, and production recovery.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 5 | 25 | Strong clean-architecture separation, persistent chat store and explicit streaming/event mapping. |
| C-02 | Testing and verification | 25 | 4 | 20 | 27 test-named files, three CI workflows and documented unit/integration strategy; live model path not run. |
| C-03 | Production depth | 20 | 5 | 20 | Aspire, PostgreSQL, auth/security notes, telemetry and deployment material make this a substantial application reference. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | C#; Microsoft.Agents.AI.OpenAI and Hosting.AGUI.AspNetCore 1.0.0-preview.251125.1 |
| C-05 | Source/author credibility | 10 | 4 | 8 | Public GitHub owner cristofima; license MIT. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit 4a998448f6b173b366f36a9512ea77c9c355e341. |
| C-07 | Maintenance activity | 5 | 3 | 3 | Last reviewed commit 2026-02-16; activity judged from repository metadata. |
|  | **Total** | **100** |  | **91** |  |

### Hard gates

- Triggered gates: None; version drift is an explicit route limitation.
- Result: adopted
- Reviewer decision: adopted

## Decision

- State: `adopted`
- Approved use: Version-bounded design and code-navigation reference.
- Prohibited or unsafe use: Do not copy/vendor source; do not infer current API compatibility; do not run credentialed or costly paths without authorization.
- Topic-registry promotion proposal: hosting, sessions, AG-UI, observability, security
- Collection action: `project route`
- Re-review trigger: upstream MAF major/API change, source revision/license change, or new compatibility tests.
- Residual risk: Architecture is reusable; the Nov-2025 preview AG-UI and agent APIs are stale against target 1.13 and must not be copied literally.
