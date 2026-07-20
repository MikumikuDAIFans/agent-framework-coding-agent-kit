# Source review: `community-loop-engineering`

## Snapshot

- Source: Loop engineering with MAF
- Canonical URL: https://github.com/akshaykokane/loop-engineering-with-microsoft-agent-framework
- Source class: community-repository
- Owner/author: akshaykokane
- Reviewed commit: `ee451db4c8b8786ed297946a679d6904e7a816b5` (2026-07-02)
- Package/API coordinates: C#; Microsoft.Agents.AI/OpenAI 1.12.0; Harness preview 260629
- License: not declared
- Reviewer and date: Codex, 2026-07-17
- Policy version: `v1.1`
- Review track: `code-project`

## Direct Microsoft Agent Framework evidence

- Languages/topics: workflows, evaluation, tools, harness
- Relevant files: BlogLoop.cs; HarnessAgentFactory.cs; LoopUtils.cs; LoopAgentWithMAF.csproj
- Direct evidence: C#; Microsoft.Agents.AI/OpenAI 1.12.0; Harness preview 260629
- Target compatibility: 1.12 is near target 1.13, but Harness is preview and must be checked for the 1.13 breaking changes.

## Design and implementation value

- Reusable decisions: Small, legible example of bounded iterative generation with harness integration.
- Verification: No tests or CI; live loop requires model credentials and was not run.
- Production and operational depth: No persistence, telemetry, policy, retry or deployment layer.
- Safety boundary: treat prompts, tool output and external data as untrusted; sample shortcuts are not production defaults.

## Verification

- Evidence reproduced: immutable GitHub metadata, manifest/import inspection, repository tree and test/CI inventory.
- Checks not run: model, cloud, hosted service, external database, deployment and credential-dependent paths (`not-run` by policy).
- Target comparison: static comparison to upstream revision `5ab8877ba55b4778d778cf51450eafe483194708`; no claim of runtime compatibility beyond the coordinates above.
- Unverified claims: live inference quality, load behavior, cloud identity/authorization, cost, and production recovery.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 3 | 15 | Small, legible example of bounded iterative generation with harness integration. |
| C-02 | Testing and verification | 25 | 0 | 0 | No tests or CI; live loop requires model credentials and was not run. |
| C-03 | Production depth | 20 | 1 | 4 | No persistence, telemetry, policy, retry or deployment layer. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | C#; Microsoft.Agents.AI/OpenAI 1.12.0; Harness preview 260629 |
| C-05 | Source/author credibility | 10 | 2 | 4 | Public GitHub owner akshaykokane; license not declared. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit ee451db4c8b8786ed297946a679d6904e7a816b5. |
| C-07 | Maintenance activity | 5 | 4 | 4 | Last reviewed commit 2026-07-02; activity judged from repository metadata. |
|  | **Total** | **100** |  | **42** |  |

### Hard gates

- Triggered gates: score below 50; no automated verification or production evidence.
- Result: rejected
- Reviewer decision: rejected

## Decision

- State: `rejected`
- Approved use: No formal coding-agent route until re-review.
- Prohibited or unsafe use: Do not copy/vendor source; do not infer current API compatibility; do not run credentialed or costly paths without authorization.
- Topic-registry promotion proposal: workflows, evaluation, tools, harness
- Collection action: `none`
- Re-review trigger: upstream MAF major/API change, source revision/license change, or new compatibility tests.
- Residual risk: 1.12 is near target 1.13, but Harness is preview and must be checked for the 1.13 breaking changes.
