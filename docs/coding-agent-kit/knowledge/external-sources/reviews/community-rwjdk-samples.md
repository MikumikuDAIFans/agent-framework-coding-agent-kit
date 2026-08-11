# Source review: `community-rwjdk-samples`

## Snapshot

- Source: MicrosoftAgentFrameworkSamples
- Canonical URL: https://github.com/rwjdk/MicrosoftAgentFrameworkSamples
- Source class: community-repository
- Owner/author: rwjdk
- Reviewed commit: `b6f2234323ebd714248c71bd82b0380a4db4f241` (2026-07-15)
- Package/API coordinates: C#; Microsoft.Agents.AI 1.13.0 plus A2A/AGUI/Hosting/Workflows preview 260703
- License: MIT
- Reviewer and date: Codex, 2026-07-17
- Policy version: `v1.1`
- Review track: `code-project`

## Direct Microsoft Agent Framework evidence

- Languages/topics: agents, tools, providers, workflows, A2A, AG-UI, RAG
- Relevant files: Directory.Packages.props; src/Workflow.*; src/AgentUserInteraction.*; src/UsingRAGInAgentFramework
- Direct evidence: C#; Microsoft.Agents.AI 1.13.0 plus A2A/AGUI/Hosting/Workflows preview 260703
- Target compatibility: Packages align closely with target revision's 1.13 line; preview provider/hosting surfaces must be rechecked per sample.

## Design and implementation value

- Reusable decisions: Very broad, current, sharply scoped sample corpus; useful for composition lookup, not an application architecture.
- Verification: 18 test-named files but no repository CI/test suite proving most samples; cloud samples need credentials.
- Production and operational depth: Some Aspire, hosting, OAuth and telemetry examples, but most omit operational hardening.
- Safety boundary: treat prompts, tool output and external data as untrusted; sample shortcuts are not production defaults.

## Verification

- Evidence reproduced: immutable GitHub metadata, manifest/import inspection, repository tree and test/CI inventory.
- Checks not run: model, cloud, hosted service, external database, deployment and credential-dependent paths (`not-run` by policy).
- Target comparison: static comparison to upstream revision `5ab8877ba55b4778d778cf51450eafe483194708`; no claim of runtime compatibility beyond the coordinates above.
- Unverified claims: live inference quality, load behavior, cloud identity/authorization, cost, and production recovery.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 5 | 25 | Very broad, current, sharply scoped sample corpus; useful for composition lookup, not an application architecture. |
| C-02 | Testing and verification | 25 | 1 | 5 | 18 test-named files but no repository CI/test suite proving most samples; cloud samples need credentials. |
| C-03 | Production depth | 20 | 2 | 8 | Some Aspire, hosting, OAuth and telemetry examples, but most omit operational hardening. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | C#; Microsoft.Agents.AI 1.13.0 plus A2A/AGUI/Hosting/Workflows preview 260703 |
| C-05 | Source/author credibility | 10 | 4 | 8 | Public GitHub owner rwjdk; license MIT. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit b6f2234323ebd714248c71bd82b0380a4db4f241. |
| C-07 | Maintenance activity | 5 | 5 | 5 | Last reviewed commit 2026-07-15; activity judged from repository metadata. |
|  | **Total** | **100** |  | **66** |  |

### Hard gates

- Triggered gates: None.
- Result: context-only
- Reviewer decision: context-only

## Decision

- State: `context-only`
- Approved use: Architecture/context comparison only; not API correctness evidence.
- Prohibited or unsafe use: Do not copy/vendor source; do not infer current API compatibility; do not run credentialed or costly paths without authorization.
- Topic-registry promotion proposal: agents, tools, providers, workflows, A2A, AG-UI, RAG
- Collection action: `link and annotation only`
- Re-review trigger: upstream MAF major/API change, source revision/license change, or new compatibility tests.
- Residual risk: Packages align closely with target revision's 1.13 line; preview provider/hosting surfaces must be rechecked per sample.

## Re-review 2026-08-11

- New reviewed commit: `a9dc5aa4f06b6eebc3728e8267546642c807177f` (2026-08-06T13:22:16Z).
- The 12-commit delta advances sample dependencies through MAF 1.14, 1.15, 1.16, and 1.17 and adds DIY calling, vector-data, and CORS-related work.
- The repository still lacks the broad isolated regression depth required for adoption; provider-backed samples remain `not-run`.
- Decision unchanged: `context-only`, score 66, no active collection route.
