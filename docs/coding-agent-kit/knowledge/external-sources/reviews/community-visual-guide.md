# Source review: `community-visual-guide`

## Snapshot

- Source: Agent Framework Visual Guide
- Canonical URL: https://github.com/verdenmax/agent-framework-visual-guide
- Source class: community-repository
- Owner/author: verdenmax
- Reviewed commit: `aef1d4009ee3d3e4bc6cc00562568d6bc1e66447` (2026-06-23)
- Package/API coordinates: Static bilingual Python guide; source notes cite Agent/AgentSession/tool/workflow APIs
- License: MIT
- Reviewer and date: Codex, 2026-07-17
- Policy version: `v1.1`
- Review track: `code-project`

## Direct Microsoft Agent Framework evidence

- Languages/topics: getting started, agents, workflows
- Relevant files: lessons/*.html; build/check scripts; design/spec notes; Pages CI
- Direct evidence: Static bilingual Python guide; source notes cite Agent/AgentSession/tool/workflow APIs
- Target compatibility: Notes target a newer Agent/AgentSession surface, but lessons are generated static content and are not pinned to package version.

## Design and implementation value

- Reusable decisions: Strong visual pedagogy, bilingual navigation and explicit upstream source-reference intent.
- Verification: Link/build checks and two CI workflows, but no runnable MAF dependency or API tests.
- Production and operational depth: Documentation publishing is mature; it is not an agent application.
- Safety boundary: treat prompts, tool output and external data as untrusted; sample shortcuts are not production defaults.

## Verification

- Evidence reproduced: immutable GitHub metadata, manifest/import inspection, repository tree and test/CI inventory.
- Checks not run: model, cloud, hosted service, external database, deployment and credential-dependent paths (`not-run` by policy).
- Target comparison: static comparison to upstream revision `5ab8877ba55b4778d778cf51450eafe483194708`; no claim of runtime compatibility beyond the coordinates above.
- Unverified claims: live inference quality, load behavior, cloud identity/authorization, cost, and production recovery.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 4 | 20 | Strong visual pedagogy, bilingual navigation and explicit upstream source-reference intent. |
| C-02 | Testing and verification | 25 | 2 | 10 | Link/build checks and two CI workflows, but no runnable MAF dependency or API tests. |
| C-03 | Production depth | 20 | 1 | 4 | Documentation publishing is mature; it is not an agent application. |
| C-04 | Real MAF dependency | 10 | 1 | 2 | Static bilingual Python guide; source notes cite Agent/AgentSession/tool/workflow APIs |
| C-05 | Source/author credibility | 10 | 3 | 6 | Public GitHub owner verdenmax; license MIT. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit aef1d4009ee3d3e4bc6cc00562568d6bc1e66447. |
| C-07 | Maintenance activity | 5 | 5 | 5 | Last reviewed commit 2026-06-23; activity judged from repository metadata. |
|  | **Total** | **100** |  | **52** |  |

### Hard gates

- Triggered gates: Real-MAF-dependency hard gate: no runnable dependency or executable MAF API use.
- Result: rejected
- Reviewer decision: rejected

## Decision

- State: `rejected`
- Approved use: No formal coding-agent route until re-review.
- Prohibited or unsafe use: Do not copy/vendor source; do not infer current API compatibility; do not run credentialed or costly paths without authorization.
- Topic-registry promotion proposal: getting started, agents, workflows
- Collection action: `none`
- Re-review trigger: upstream MAF major/API change, source revision/license change, or new compatibility tests.
- Residual risk: Notes target a newer Agent/AgentSession surface, but lessons are generated static content and are not pinned to package version.
