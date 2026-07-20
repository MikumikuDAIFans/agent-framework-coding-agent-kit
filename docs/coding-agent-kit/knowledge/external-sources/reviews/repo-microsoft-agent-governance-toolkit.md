# Source review: `repo-microsoft-agent-governance-toolkit`

## Snapshot

- Source: `microsoft/agent-governance-toolkit`
- Canonical URL: https://github.com/microsoft/agent-governance-toolkit
- Source class: `official-repository`
- Owner/author: Microsoft organization and open-source contributors.
- Reviewed commit, tag, or page date: commit `d00ccdbf31258db917495ca65fa2ecd9e64461b9` (2026-07-17); latest release observed: `v4.1.0` (2026-06-09).
- Package/API coordinates: .NET companion package `Microsoft.AgentGovernance.Extensions.Microsoft.Agents`, public preview, directly references `Microsoft.Agents.AI` `1.13.0`; wider repository contains multi-language governance SDKs/tools.
- License: MIT at repository root; component license/notice files must remain authoritative for any use.
- Reviewer and date: Codex, 2026-07-17.
- Policy version: `v1.1`
- Review track: `code-project`

## Direct Microsoft Agent Framework evidence

- Languages: C#/.NET is the reviewed MAF integration; the wider toolkit also contains Python, Go, TypeScript/JavaScript, policies, and CLIs.
- Package references/imports: direct `Microsoft.Agents.AI` package; adapter consumes `AIAgent`, `AgentSession`, `AgentRunOptions`, `AgentResponse`, streaming updates, and function-invocation middleware.
- Relevant files: `agent-governance-dotnet/src/AgentGovernance.Extensions.Microsoft.Agents/`, matching `AgentFrameworkGovernance*Tests.cs`, and `policy-engine/sdk/dotnet/...AgentFramework/`.
- MAF topics demonstrated: run middleware, function/tool middleware, policy enforcement, blocking, audit emission, identity derivation, streaming, and dependency-injection extensions.
- Preview, experimental, deprecated, or provider-specific surfaces: the companion package declares itself public preview. Its `Microsoft.Agents.AI 1.13.0` coordinate is independently released and must be resolved against the package/source represented by target revision `5ab8877ba55b4778d778cf51450eafe483194708`; do not infer binary compatibility from matching symbol names alone.

## Design and implementation value

- Reusable decisions: a thin adapter maps MAF run/tool surfaces into a framework-neutral policy kernel; deny decisions fail closed before inner execution; audit events are emitted; extension methods avoid application-specific middleware duplication.
- Sample shortcuts that must not be copied into production: default identity derivation, policy content, blocked-response text, storage, and audit sinks require explicit application decisions. A library cannot by itself establish organization-wide governance.
- State and data flow: messages/session metadata and tool arguments become policy inputs; allowed calls continue to the inner agent/tool; denied calls return bounded responses and audit records.
- Tool and side-effect boundaries: function middleware is the key control point. Policy backend availability, fail-open/closed semantics, argument redaction, authorization context, and audit durability must be configured and tested per deployment.
- Failure, cancellation, retry, and concurrency behavior: cancellation is forwarded; tests cover allow/deny and single-pass enumeration. Backend failure, distributed consistency, duplicate audit delivery, and high-contention behavior still require target validation.
- Security, identity, and data handling: policy, credential-vault, prompt-defense, sandbox, rate-limit, trust, kill-switch, and redaction capabilities are substantive. Correct policy provenance, least privilege, secrets, tenant isolation, retention, and incident handling remain deployment responsibilities.
- Observability and evaluation: audit/metrics/SRE components and extensive tests/CI are present. Governance policy effectiveness still needs target threat cases and measurable acceptance gates.
- Hosting, deployment, and rollback: packages, containers, policies, release automation, SBOM, CodeQL, dependency review, scorecard, and supply-chain workflows provide strong operational evidence. Consumers still need staged rollout and emergency bypass/rollback procedures.

## Verification

- Commands documented by the source: package installation, .NET build/test, policy/CLI and container workflows.
- Checks reproduced locally: metadata, immutable commit/release, MIT license, package coordinate, adapter/extension implementation, focused MAF tests, and repository CI/security workflow inventory inspected via GitHub API/raw immutable URLs.
- Test/eval coverage: focused adapter run/function/extension tests plus a broad toolkit test corpus and extensive CI/security/release automation.
- Conflicts with local upstream source, tests, or Microsoft Learn: no semantic conflict established, but package `1.13.0` was not built against the local target checkout and the integration is public preview.
- Unverified claims: package restore/build and live policy backends are `not-run`; they would fetch dependencies or require external systems. Static implementation/tests/CI are substitute evidence.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 5 | 25 | Thin, explicit run/tool governance adapter with reusable boundaries. |
| C-02 | Testing and verification | 25 | 5 | 25 | Focused MAF tests plus broad CI/security automation. |
| C-03 | Production depth | 20 | 4 | 16 | Packages, policies, audit, security, release and supply-chain controls; preview caveat. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | Direct package and middleware API integration. |
| C-05 | Source/author credibility | 10 | 5 | 10 | Microsoft-owned, released, MIT repository. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit, exact dependency, and tagged releases. |
| C-07 | Maintenance activity | 5 | 5 | 5 | Active on the review date. |
|  | **Total** | **100** |  | **96** |  |

### Hard gates

- Triggered gates: none.
- Result: pass.
- Reviewer decision: `adopted` with public-preview and package-compatibility boundaries.

## Decision

- State: `adopted`
- Approved use: route MAF middleware/governance/security design to the immutable .NET integration and its tests, then verify target package compatibility and deployment policy semantics.
- Prohibited or unsafe use: do not copy external code; do not claim the toolkit alone provides compliance; do not use example identity/policy/audit defaults without threat modeling and tests.
- Topic-registry promotion proposal: `middleware`, `security`, `tools`, and `observability` as an external project route.
- Collection action: `project route`
- Re-review trigger: companion package leaves preview, MAF middleware signatures change, security advisory, policy schema/release change, or license change.
- Residual risk: broad governance claims can be over-applied without verifying enforcement coverage and fail-closed behavior in the target host.
