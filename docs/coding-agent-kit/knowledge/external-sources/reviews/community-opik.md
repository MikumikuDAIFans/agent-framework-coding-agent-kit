# Source review: `community-opik`

## Snapshot

- Source: Opik
- Canonical URL: https://github.com/comet-ml/opik
- Source class: community-repository
- Owner/author: comet-ml
- Reviewed commit: `9e207b4693948fd276e659098195155f490a3785` (2026-07-17)
- Package/API coordinates: Generic OpenTelemetry integration; MAF Python and .NET examples in Opik documentation
- License: Apache-2.0
- Reviewer and date: Codex, 2026-07-17
- Policy version: `v1.1`
- Review track: `code-project`

## Direct Microsoft Agent Framework evidence

- Languages/topics: observability, evaluation
- Relevant files: MAF integration documentation; backend/SDK/evaluation platform; deployment manifests
- Direct evidence: Generic OpenTelemetry integration; MAF Python and .NET examples in Opik documentation
- Target compatibility: MAF route relies on standard OpenTelemetry rather than a pinned MAF adapter; docs currently show Agent/OpenAIChatClient and .NET ChatClientAgent, which must be checked at target revision.

## Design and implementation value

- Reusable decisions: Production observability platform and a low-coupling OTLP export pattern.
- Verification: Large mature test/CI corpus, but no evidence that MAF examples themselves are regression-tested.
- Production and operational depth: Self-host/cloud deployment, auth, SDKs, dashboards and operations are comprehensive.
- Safety boundary: treat prompts, tool output and external data as untrusted; sample shortcuts are not production defaults.

## Verification

- Evidence reproduced: immutable GitHub metadata, manifest/import inspection, repository tree and test/CI inventory.
- Checks not run: model, cloud, hosted service, external database, deployment and credential-dependent paths (`not-run` by policy).
- Target comparison: static comparison to upstream revision `5ab8877ba55b4778d778cf51450eafe483194708`; no claim of runtime compatibility beyond the coordinates above.
- Unverified claims: live inference quality, load behavior, cloud identity/authorization, cost, and production recovery.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 4 | 20 | Production observability platform and a low-coupling OTLP export pattern. |
| C-02 | Testing and verification | 25 | 4 | 20 | Large mature test/CI corpus, but no evidence that MAF examples themselves are regression-tested. |
| C-03 | Production depth | 20 | 5 | 20 | Self-host/cloud deployment, auth, SDKs, dashboards and operations are comprehensive. |
| C-04 | Real MAF dependency | 10 | 3 | 6 | Generic OpenTelemetry integration; MAF Python and .NET examples in Opik documentation |
| C-05 | Source/author credibility | 10 | 5 | 10 | Public GitHub owner comet-ml; license Apache-2.0. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit 9e207b4693948fd276e659098195155f490a3785. |
| C-07 | Maintenance activity | 5 | 5 | 5 | Last reviewed commit 2026-07-17; activity judged from repository metadata. |
|  | **Total** | **100** |  | **86** |  |

### Hard gates

- Triggered gates: None: documentation contains actual MAF API calls and the integration is intentionally protocol-based.
- Result: adopted
- Reviewer decision: adopted

## Decision

- State: `adopted`
- Approved use: Version-bounded design and code-navigation reference.
- Prohibited or unsafe use: Do not copy/vendor source; do not infer current API compatibility; do not run credentialed or costly paths without authorization.
- Topic-registry promotion proposal: observability, evaluation
- Collection action: `project route`
- Re-review trigger: upstream MAF major/API change, source revision/license change, or new compatibility tests.
- Residual risk: MAF route relies on standard OpenTelemetry rather than a pinned MAF adapter; docs currently show Agent/OpenAIChatClient and .NET ChatClientAgent, which must be checked at target revision.
