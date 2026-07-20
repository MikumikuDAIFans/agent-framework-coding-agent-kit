# Source review: `repo-eshoplite`

## Snapshot

- Source: `Azure-Samples/eShopLite`
- Canonical URL: https://github.com/Azure-Samples/eShopLite
- Source class: `official-repository`
- Owner/author: Microsoft Azure-Samples organization and contributors.
- Reviewed commit, tag, or page date: commit `f6349114992b233daf92c0ff7ccba0e151e1deff` (2026-06-07); no release tag.
- Package/API coordinates: C#/.NET 10; MAF scenarios pin `Microsoft.Agents.AI*` packages to `1.0.0-preview.251125.1`, with one Hosting.OpenAI alpha; provider/Aspire package versions vary by scenario.
- License: MIT.
- Reviewer and date: Codex, 2026-07-17.
- Policy version: `v1.1`
- Review track: `code-project`

## Direct Microsoft Agent Framework evidence

- Languages: C#/.NET plus Aspire/Bicep/configuration.
- Package references/imports: direct MAF packages and `AIAgent`, `CreateAIAgent`, `AgentWorkflowBuilder`, `InProcessExecution`, workflow events, DevUI, Hosting, OpenAI, and AzureAI APIs.
- Relevant files: `scenarios/07-AgentsConcurrent`, `scenarios/14-MAFDevUI`, and their application/service projects. A2A-named scenarios include plain HTTP services and must not automatically be treated as MAF evidence.
- MAF topics demonstrated: concurrent agent analysis, keyed DI agents, sequential/handoff orchestration, deterministic fallback, DevUI, hosting, provider setup, Aspire composition, and application integration.
- Preview, experimental, deprecated, or provider-specific surfaces: old November 2025 preview/alpha package set, .NET 10, OpenAI/Azure provider and Aspire dependencies. Against target revision `5ab8877ba55b4778d778cf51450eafe483194708`, exact workflow builder/events/hosting APIs need migration; stale Learn paths in comments are not authority.

## Design and implementation value

- Reusable decisions: agents are integrated into a real multi-service domain; keyed registrations separate roles; concurrent analysis is explicit; checkout has deterministic fallback; workflow events are transformed into application models; Aspire exposes service/telemetry topology.
- Sample shortcuts that must not be copied into production: model text is parsed heuristically; some demo endpoints use random data; fallback paths can mark a degraded agent execution as success; prompts contain deterministic discount rules that belong in code; and scenario packages are not centrally aligned.
- State and data flow: store/API requests invoke agent services and persist derived insights or checkout steps. Durable workflow checkpoint/replay, message deduplication, schema migration, and tenant isolation are not established.
- Tool and side-effect boundaries: database writes and commerce decisions occur near model output. Authorization, approval, idempotency, audit, validation, and transactional boundaries need strengthening.
- Failure, cancellation, retry, and concurrency behavior: concurrent tasks and exception fallback are demonstrated, but cancellation propagation, timeouts, retry taxonomy, backpressure, partial failure, and duplicate execution are not comprehensively tested.
- Security, identity, and data handling: Azure identity/configuration and service defaults exist. Prompt injection, PII retention, tenant boundaries, secrets, tool authorization, and output provenance remain incomplete.
- Observability and evaluation: Aspire/OpenTelemetry/service health assets provide operational visibility; no MAF behavioral eval corpus or threshold gate was verified.
- Hosting, deployment, and rollback: multi-service Aspire and Azure infrastructure are valuable; scenario drift, preview packages, data migrations, rollout, and rollback are not consistently defined.

## Verification

- Commands documented by the source: scenario-specific .NET/Aspire execution and Azure provisioning, requiring .NET 10 and provider credentials.
- Checks reproduced locally: immutable commit, MIT license, scenario tree, exact package pins, agent registration, workflow/orchestrator logic, test inventory, and infra/CI metadata inspected via GitHub API/raw immutable URLs.
- Test/eval coverage: product/store tests exist in MAF scenario solutions, but include placeholders and do not directly verify core agent/workflow behavior. Repository workflows emphasize CodeQL/docs/project automation rather than a comprehensive scenario build/test gate.
- Conflicts with local upstream source, tests, or Microsoft Learn: target `5ab8877...` is newer than the preview pins; exact MAF APIs and persisted/event semantics must be sourced locally.
- Unverified claims: builds, models, Aspire, databases, DevUI, and Azure deployment are `not-run` due to SDK/provider/resource requirements. Static source/test/infra evidence substitutes.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 4 | 20 | Real application seams, concurrent/workflow patterns, deterministic fallback. |
| C-02 | Testing and verification | 25 | 2 | 10 | Some app tests; agent/workflow and repo-wide gates are weak. |
| C-03 | Production depth | 20 | 4 | 16 | Aspire, health/telemetry, data and Azure assets with material controls missing. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | Exact packages and extensive direct APIs in isolated scenarios. |
| C-05 | Source/author credibility | 10 | 5 | 10 | Microsoft Azure-Samples, MIT. |
| C-06 | Version traceability | 5 | 4 | 4 | Immutable commit and package pins, no release and cross-scenario drift. |
| C-07 | Maintenance activity | 5 | 4 | 4 | Recent 2026 activity, reviewed MAF pins remain old preview. |
|  | **Total** | **100** |  | **74** |  |

### Hard gates

- Triggered gates: none; direct MAF dependencies and calls are verified in scoped scenarios.
- Result: pass, below adoption threshold.
- Reviewer decision: `context-only` until MAF scenarios are current and directly tested.

## Decision

- State: `context-only`
- Approved use: application-architecture background for integrating MAF with DI, Aspire, data services, concurrent analysis, DevUI, and deterministic degradation.
- Prohibited or unsafe use: do not treat the whole repository or A2A-named HTTP services as MAF; do not copy external code; do not copy preview APIs, heuristic parsing, prompt-based business rules, or success-on-degradation semantics.
- Topic-registry promotion proposal: none; retain context annotations for `agents`, `workflows`, `hosting`, `observability`, and `tools`.
- Collection action: `link and annotation only`
- Re-review trigger: MAF package refresh, focused agent/workflow tests, stable release, or scenario CI that builds/runs the reviewed paths.
- Residual risk: the large application and polished Aspire experience can mask weak agent correctness and version drift.
