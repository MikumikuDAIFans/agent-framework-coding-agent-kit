# Source review: `community-agenteval`

## Snapshot

- Source: AgentEval
- Canonical URL: https://github.com/AgentEvalHQ/AgentEval
- Source class: community-repository
- Owner/author: AgentEvalHQ
- Reviewed commit: `404ee133c7ba7e1c6b7f3460f52efc40c7ebde83` (2026-07-17)
- Package/API coordinates: C#; Microsoft.Agents.AI/OpenAI/Workflows 1.13.0; Foundry/Harness preview 260703
- License: MIT
- Reviewer and date: Codex, 2026-07-17
- Policy version: `v1.1`
- Review track: `code-project`

## Direct Microsoft Agent Framework evidence

- Languages/topics: evaluation, observability, harness, Foundry
- Relevant files: Directory.Packages.props; src/AgentEval.MAF; samples/AgentEval.MafEvalLightPath; test and benchmark corpus
- Direct evidence: C#; Microsoft.Agents.AI/OpenAI/Workflows 1.13.0; Foundry/Harness preview 260703
- Target compatibility: Pins the same 1.13 generation as target revision and documents breaking-change checks; preview Foundry/Harness remain sample-only.

## Design and implementation value

- Reusable decisions: Deep reusable evaluation abstractions, adapters, reports, datasets and benchmark composition.
- Verification: Extensive unit/integration/acceptance corpus, CI and NuGet-consumer validation; cloud judges not run.
- Production and operational depth: Version/security pins, provider isolation, CLI/reporting and explicit ADRs demonstrate high production depth.
- Safety boundary: treat prompts, tool output and external data as untrusted; sample shortcuts are not production defaults.

## Verification

- Evidence reproduced: immutable GitHub metadata, manifest/import inspection, repository tree and test/CI inventory.
- Checks not run: model, cloud, hosted service, external database, deployment and credential-dependent paths (`not-run` by policy).
- Target comparison: static comparison to upstream revision `5ab8877ba55b4778d778cf51450eafe483194708`; no claim of runtime compatibility beyond the coordinates above.
- Unverified claims: live inference quality, load behavior, cloud identity/authorization, cost, and production recovery.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 5 | 25 | Deep reusable evaluation abstractions, adapters, reports, datasets and benchmark composition. |
| C-02 | Testing and verification | 25 | 5 | 25 | Extensive unit/integration/acceptance corpus, CI and NuGet-consumer validation; cloud judges not run. |
| C-03 | Production depth | 20 | 5 | 20 | Version/security pins, provider isolation, CLI/reporting and explicit ADRs demonstrate high production depth. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | C#; Microsoft.Agents.AI/OpenAI/Workflows 1.13.0; Foundry/Harness preview 260703 |
| C-05 | Source/author credibility | 10 | 5 | 10 | Public GitHub owner AgentEvalHQ; license MIT. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit 404ee133c7ba7e1c6b7f3460f52efc40c7ebde83. |
| C-07 | Maintenance activity | 5 | 5 | 5 | Last reviewed commit 2026-07-17; activity judged from repository metadata. |
|  | **Total** | **100** |  | **100** |  |

### Hard gates

- Triggered gates: None.
- Result: adopted
- Reviewer decision: adopted

## Decision

- State: `adopted`
- Approved use: Version-bounded design and code-navigation reference.
- Prohibited or unsafe use: Do not copy/vendor source; do not infer current API compatibility; do not run credentialed or costly paths without authorization.
- Topic-registry promotion proposal: evaluation, observability, harness, Foundry
- Collection action: `project route`
- Re-review trigger: upstream MAF major/API change, source revision/license change, or new compatibility tests.
- Residual risk: Pins the same 1.13 generation as target revision and documents breaking-change checks; preview Foundry/Harness remain sample-only.

## Re-review 2026-08-11

- New reviewed commit: `3d1643f39c69bbfefb58a555e2e048261ae8bc99` (2026-08-07T17:04:18Z).
- The 49-commit delta substantially expands Gatekeeper, Agent Skills drift enforcement, calibrated judges, fleet correlation, replay fixtures, security reviews, and fail-open/fabrication remediation; 258 returned files carry test/security/evaluation signals.
- No changed file directly rewrites the MAF adapter surface, so this remains design and evaluation evidence rather than current API proof.
- Decision unchanged: `adopted`, score 100, at the new immutable coordinate.
