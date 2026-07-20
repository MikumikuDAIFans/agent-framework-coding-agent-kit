# Source review: `community-agent-base`

## Snapshot

- Source: agent-base
- Canonical URL: https://github.com/danielscholl/agent-base
- Source class: community-repository
- Owner/author: danielscholl
- Reviewed commit: `13733a71c1736ab87c02802118320583db866ef4` (2025-11-24)
- Package/API coordinates: Python; agent-framework>=1.0.0b251106; OpenAI and custom provider clients
- License: MIT
- Reviewer and date: Codex, 2026-07-17
- Policy version: `v1.1`
- Review track: `code-project`

## Direct Microsoft Agent Framework evidence

- Languages/topics: observability, hosting, security, context providers, providers
- Relevant files: docs/decisions; docs/design; src/agent/memory/context_provider.py; src/agent/middleware.py; tests
- Direct evidence: Python; agent-framework>=1.0.0b251106; OpenAI and custom provider clients
- Target compatibility: Uses public Context/ContextProvider and client surfaces from an early beta; target revision changed multiple Python names, so route is architectural and tests are not proof of current API.

## Design and implementation value

- Reusable decisions: Detailed ADR/spec corpus and clear seams for provider, skills, memory and middleware.
- Verification: 95 test-named files and four CI workflows, including telemetry and provider tests.
- Production and operational depth: Strong configuration, security, telemetry and container/deployment intent; some integrations remain prototype-grade.
- Safety boundary: treat prompts, tool output and external data as untrusted; sample shortcuts are not production defaults.

## Verification

- Evidence reproduced: immutable GitHub metadata, manifest/import inspection, repository tree and test/CI inventory.
- Checks not run: model, cloud, hosted service, external database, deployment and credential-dependent paths (`not-run` by policy).
- Target comparison: static comparison to upstream revision `5ab8877ba55b4778d778cf51450eafe483194708`; no claim of runtime compatibility beyond the coordinates above.
- Unverified claims: live inference quality, load behavior, cloud identity/authorization, cost, and production recovery.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 5 | 25 | Detailed ADR/spec corpus and clear seams for provider, skills, memory and middleware. |
| C-02 | Testing and verification | 25 | 5 | 25 | 95 test-named files and four CI workflows, including telemetry and provider tests. |
| C-03 | Production depth | 20 | 4 | 16 | Strong configuration, security, telemetry and container/deployment intent; some integrations remain prototype-grade. |
| C-04 | Real MAF dependency | 10 | 4 | 8 | Python; agent-framework>=1.0.0b251106; OpenAI and custom provider clients |
| C-05 | Source/author credibility | 10 | 3 | 6 | Public GitHub owner danielscholl; license MIT. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit 13733a71c1736ab87c02802118320583db866ef4. |
| C-07 | Maintenance activity | 5 | 2 | 2 | Last reviewed commit 2025-11-24; activity judged from repository metadata. |
|  | **Total** | **100** |  | **87** |  |

### Hard gates

- Triggered gates: None; API use is direct but compatibility is bounded to reviewed commit.
- Result: adopted
- Reviewer decision: adopted

## Decision

- State: `adopted`
- Approved use: Version-bounded design and code-navigation reference.
- Prohibited or unsafe use: Do not copy/vendor source; do not infer current API compatibility; do not run credentialed or costly paths without authorization.
- Topic-registry promotion proposal: observability, hosting, security, context providers, providers
- Collection action: `project route`
- Re-review trigger: upstream MAF major/API change, source revision/license change, or new compatibility tests.
- Residual risk: Uses public Context/ContextProvider and client surfaces from an early beta; target revision changed multiple Python names, so route is architectural and tests are not proof of current API.
