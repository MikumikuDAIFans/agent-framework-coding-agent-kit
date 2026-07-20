# Source review: `community-copilot-learning`

## Snapshot

- Source: Learn MAF with GitHub Copilot Agent
- Canonical URL: https://github.com/kinfey/Learn-MAF-With-GitHubCopilotAgent
- Source class: community-repository
- Owner/author: kinfey
- Reviewed commit: `ce82bc9125ad1bdf2ee5f67550347dbe873be00f` (2026-05-24)
- Package/API coordinates: Python and C# labs; GitHub Copilot provider; .NET uses wildcard prerelease versions
- License: not declared
- Reviewer and date: Codex, 2026-07-17
- Policy version: `v1.1`
- Review track: `code-project`

## Direct Microsoft Agent Framework evidence

- Languages/topics: getting started, workflows, MCP, AG-UI, Copilot provider
- Relevant files: lab-01..05; .github/skills agent-framework-* references; one HelloZava csproj
- Direct evidence: Python and C# labs; GitHub Copilot provider; .NET uses wildcard prerelease versions
- Target compatibility: Concepts are recent, but wildcard package versions and unmaterialized labs prevent reproducible target-revision proof.

## Design and implementation value

- Reusable decisions: Valuable bilingual learning path and coding-agent skill decomposition.
- Verification: No automated tests or CI; most later labs are prompts/instructions rather than checked-in runnable implementations.
- Production and operational depth: Educational only; no operational hardening.
- Safety boundary: treat prompts, tool output and external data as untrusted; sample shortcuts are not production defaults.

## Verification

- Evidence reproduced: immutable GitHub metadata, manifest/import inspection, repository tree and test/CI inventory.
- Checks not run: model, cloud, hosted service, external database, deployment and credential-dependent paths (`not-run` by policy).
- Target comparison: static comparison to upstream revision `5ab8877ba55b4778d778cf51450eafe483194708`; no claim of runtime compatibility beyond the coordinates above.
- Unverified claims: live inference quality, load behavior, cloud identity/authorization, cost, and production recovery.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 4 | 20 | Valuable bilingual learning path and coding-agent skill decomposition. |
| C-02 | Testing and verification | 25 | 1 | 5 | No automated tests or CI; most later labs are prompts/instructions rather than checked-in runnable implementations. |
| C-03 | Production depth | 20 | 1 | 4 | Educational only; no operational hardening. |
| C-04 | Real MAF dependency | 10 | 3 | 6 | Python and C# labs; GitHub Copilot provider; .NET uses wildcard prerelease versions |
| C-05 | Source/author credibility | 10 | 4 | 8 | Public GitHub owner kinfey; license not declared. |
| C-06 | Version traceability | 5 | 1 | 1 | Immutable commit ce82bc9125ad1bdf2ee5f67550347dbe873be00f. |
| C-07 | Maintenance activity | 5 | 4 | 4 | Last reviewed commit 2026-05-24; activity judged from repository metadata. |
|  | **Total** | **100** |  | **48** |  |

### Hard gates

- Triggered gates: score below 50; immutable package and runnable verification evidence are insufficient.
- Result: rejected
- Reviewer decision: rejected

## Decision

- State: `rejected`
- Approved use: No formal coding-agent route until re-review.
- Prohibited or unsafe use: Do not copy/vendor source; do not infer current API compatibility; do not run credentialed or costly paths without authorization.
- Topic-registry promotion proposal: getting started, workflows, MCP, AG-UI, Copilot provider
- Collection action: `none`
- Re-review trigger: upstream MAF major/API change, source revision/license change, or new compatibility tests.
- Residual risk: Concepts are recent, but wildcard package versions and unmaterialized labs prevent reproducible target-revision proof.
