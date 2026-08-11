# Source review: `community-rwjdk-agent-framework-toolkit`

## Snapshot

- Source: `rwjdk/AgentFrameworkToolkit`
- Canonical URL: https://github.com/rwjdk/AgentFrameworkToolkit
- Source class: `community-repository`; owner: rwjdk.
- Reviewed commit: `9cc6f1bfd3e78b93e2ab8d98006ec0184fbd26dd` (observed 2026-08-11).
- Package coordinates: .NET toolkit over `Microsoft.Agents.AI` 1.17.0; preview Anthropic/Foundry providers.
- License: MIT.
- Reviewer and date: Codex, 2026-08-11; policy `v1.1`; track `code-project`.

## Direct Microsoft Agent Framework evidence

- Nineteen project manifests provide provider adapters, tool factories, skills, approvals, workflow helpers, and MAF samples.
- The reviewed tree has 241 files, 23 tests, and one build workflow; tests cover tools, Agent Skills, provider representation, and confinement boundaries.
- Paid/provider-backed tests require credentials and are not local compatibility proof.

## Design and implementation value

- The toolkit offers focused .NET composition conveniences and a broad sample matrix at the same 1.17 generation as the local target.
- Opinionated wrappers can obscure native lifecycle and provider differences, so routes must lead back to MAF source/tests for API claims.

## Verification

- Immutable metadata, MIT license, package versions, source/sample/test inventory, and CI were inspected statically.
- Provider and paid-model tests were `not-run`; no external code was copied.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 5 | 25 | Broad, focused .NET composition and sample patterns. |
| C-02 | Testing and verification | 25 | 4 | 20 | 23 tests and build CI; live provider paths excluded. |
| C-03 | Production depth | 20 | 4 | 16 | Confinement, approvals, provider and workflow seams. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | Direct MAF 1.17 packages. |
| C-05 | Source/author credibility | 10 | 4 | 8 | Active public MIT project with release metadata. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit and central package pins. |
| C-07 | Maintenance activity | 5 | 5 | 5 | Updated 2026-08-05. |
|  | **Total** | **100** |  | **89** |  |

### Hard gates

- Triggered gates: none.
- Result: passes.

## Decision

- State: `adopted`
- Approved use: version-bounded .NET toolkit design and sample navigation.
- Prohibited or unsafe use: copying code, substituting wrapper APIs for native MAF contracts, or treating paid-model tests as reproduced.
- Topic-registry promotion proposal: agents, providers, tools, skills, workflows, approvals, and security.
- Collection action: `project route`
- Re-review trigger: MAF package movement, toolkit release, provider-preview change, or license/security drift.
- Residual risk: wrapper convenience can hide ownership and lifecycle decisions that applications must make explicitly.
