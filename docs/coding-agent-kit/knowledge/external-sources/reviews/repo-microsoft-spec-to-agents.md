# Source review: `repo-microsoft-spec-to-agents`

## Snapshot

- Source: `microsoft/spec-to-agents`
- Canonical URL: https://github.com/microsoft/spec-to-agents
- Source class: `official-repository`
- Owner/author: Microsoft organization.
- Reviewed commit, tag, or page date: commit `f40268fa5573ce42a6403eb0edb48997eb24532a` (2026-04-22); no release tag.
- Package/API coordinates: Python 3.10+; `agent-framework-core`, `agent-framework-azure-ai`, `agent-framework-a2a`, and `agent-framework-devui` pinned to `1.0.0b251111`; application version `0.0.1`.
- License: MIT.
- Reviewer and date: Codex, 2026-07-17.
- Policy version: `v1.1`
- Review track: `code-project`

## Direct Microsoft Agent Framework evidence

- Languages: Python plus Bicep/container assets.
- Package references/imports: pinned MAF packages; direct `Workflow`, `WorkflowBuilder`, workflow contexts/events, response handlers, Azure AI client, tools, A2A, and DevUI usage.
- Relevant files: `src/spec_to_agents/workflow/core.py`, `workflow/executors.py`, tool/agent modules, `tests/test_workflow*.py`, `tests/test_tools_*.py`, `.github/workflows/ci.yml`, `azure.yaml`, and `infra/`.
- MAF topics demonstrated: typed multi-agent workflow, explicit coordinator topology, human-in-the-loop request/response, tool boundaries, MCP, A2A/DevUI exposure, and deployment.
- Preview, experimental, deprecated, or provider-specific surfaces: pinned November 2025 beta APIs and Azure AI provider. Target revision `5ab8877ba55b4778d778cf51450eafe483194708` is newer; treat topology and tests as reusable, but re-map exact constructors, events, response-handler and provider lifecycle APIs before implementation.

## Design and implementation value

- Reusable decisions: specs describe the intended workflow; implementation uses typed executors and bidirectional coordinator edges; HITL is an explicit protocol; external capabilities are separated into tools; tests cover both workflow behavior and tool contracts.
- Sample shortcuts that must not be copied into production: demo providers/resources and event-planning assumptions remain scenario-specific; some tests rely on mocks that cannot prove cloud behavior.
- State and data flow: the coordinator owns event-planning progression and can pause for user information. Durable checkpoint/replay and multi-tenant retention remain outside the sample's strongest evidence.
- Tool and side-effect boundaries: calendar, weather, search, and MCP adapters are separate and testable. Production authorization, approval granularity, idempotency, quota, and data classification still need target decisions.
- Failure, cancellation, retry, and concurrency behavior: unit/integration tests cover workflow and handoff paths; full provider failure, cancellation, duplicate delivery, and compensation coverage is incomplete.
- Security, identity, and data handling: managed Azure identity/RBAC infrastructure is preferable to secrets. Tenant isolation, prompt-injection defenses, retention, and detailed audit requirements are not complete.
- Observability and evaluation: Azure Monitor infrastructure and tests are present; no behavioral eval corpus with threshold/repeat policy was verified.
- Hosting, deployment, and rollback: Docker, `azure.yaml`, Container Apps, Foundry, monitoring, registry, and RBAC Bicep provide a credible deployment reference. Rollback and data migration remain implicit.

## Verification

- Commands documented by the source: local `uv`/Python execution, tests/lint, container execution, and `azd` provisioning/deployment.
- Checks reproduced locally: immutable commit, MIT license, tree, pinned dependencies, workflow implementation, CI configuration, tests, and infrastructure inspected through GitHub API/raw immutable URLs.
- Test/eval coverage: CI plus unit/integration files for agents, tools, console, executors, workflow, HITL, and summarization behavior. Cloud-dependent coverage was not reproduced.
- Conflicts with local upstream source, tests, or Microsoft Learn: target `5ab8877...` postdates the pinned beta, so exact API compatibility is not assumed.
- Unverified claims: Azure deployment, hosted agents, models, search, calendar, and MCP are `not-run` because they need credentials/resources. Static CI/test and source evidence substitutes for live execution.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 4 | 20 | Clear spec-to-typed-workflow, HITL, and tool decomposition. |
| C-02 | Testing and verification | 25 | 4 | 20 | CI and broad unit/integration suite, with cloud gaps. |
| C-03 | Production depth | 20 | 4 | 16 | Identity/RBAC, container, monitoring, and deployment assets. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | Pinned packages and extensive direct framework APIs. |
| C-05 | Source/author credibility | 10 | 5 | 10 | Microsoft-owned MIT repository. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit and exact MAF package pins. |
| C-07 | Maintenance activity | 5 | 4 | 4 | Active in 2026, no tagged release. |
|  | **Total** | **100** |  | **85** |  |

### Hard gates

- Triggered gates: none.
- Result: pass.
- Reviewer decision: `adopted` as a version-bounded project route.

## Decision

- State: `adopted`
- Approved use: route workflow/HITL/tool/CI/deployment questions to the immutable commit, then map APIs against target `5ab8877...` and local tests.
- Prohibited or unsafe use: do not copy external code; do not silently upgrade beta syntax; do not treat mocked tests as live-provider proof.
- Topic-registry promotion proposal: `workflows`, `approvals-hitl`, `tools`, `protocols`, and `hosting` as an external project route.
- Collection action: `project route`
- Re-review trigger: source package update/release, target MAF major/API change, broken deployment assets, or license change.
- Residual risk: deployment completeness may obscure missing tenant, eval, retry, and rollback decisions.
