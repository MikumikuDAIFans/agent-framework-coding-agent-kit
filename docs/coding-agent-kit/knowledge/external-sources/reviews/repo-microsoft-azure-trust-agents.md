# Source review: `repo-microsoft-azure-trust-agents`

## Snapshot

- Source: `microsoft/azure-trust-agents`
- Canonical URL: https://github.com/microsoft/azure-trust-agents
- Source class: `official-repository`
- Owner/author: Microsoft organization; workshop contributors.
- Reviewed commit, tag, or page date: commit `55b1641b640195b1a45640214f30294cc0d973c9` (2026-01-28); no release tag.
- Package/API coordinates: Python; `agent-framework-core`, `agent-framework-azure-ai`, and `agent-framework-devui` at `1.0.0b251016`; `mcp==1.23.0`; Azure AI and telemetry preview dependencies.
- License: MIT.
- Reviewer and date: Codex, 2026-07-17.
- Policy version: `v1.1`
- Review track: `code-project`

## Direct Microsoft Agent Framework evidence

- Languages: Python and notebooks.
- Package references/imports: pinned MAF packages in `requirements.txt`; direct imports of `WorkflowBuilder`, `WorkflowContext`, `WorkflowOutputEvent`, `executor`, `ChatAgent`, `HostedMCPTool`, `AzureAIAgentClient`, and `AzureOpenAIResponsesClient`.
- Relevant files: `challenge-1/workflow/sequential_workflow.py`, `challenge-1/devui/fraud_detection_workflow/workflow.py`, `challenge-2/agents/sequential_workflow_chal2.py`, and `challenge-3/workflow_observability.py`.
- MAF topics demonstrated: typed workflow executors, sequential/parallel routing, Azure AI agents, DevUI, hosted MCP tools, and OpenTelemetry-style workflow observability.
- Preview, experimental, deprecated, or provider-specific surfaces: the complete MAF coordinate is the October 2025 beta and Azure provider-specific. Against target revision `5ab8877ba55b4778d778cf51450eafe483194708`, the concepts remain useful but every named symbol and event contract must be rechecked; this review does not claim drop-in source compatibility.

## Design and implementation value

- Reusable decisions: staged fraud/compliance processing, typed executor payloads, fan-out after risk analysis, and business telemetry mapped to workflow stages.
- Sample shortcuts that must not be copied into production: database clients are created at import time; mutable model defaults are used; broad exceptions are converted to payload strings; SQL-like Cosmos queries are interpolated; and environment configuration has little startup validation.
- State and data flow: customer and transaction data flow through risk analysis into compliance and alert branches, but durable ownership, replay, retention, and tenant isolation are not specified.
- Tool and side-effect boundaries: Cosmos reads and hosted MCP actions are real side effects; authorization, idempotency, approval, quotas, and audit guarantees are incomplete.
- Failure, cancellation, retry, and concurrency behavior: errors are often swallowed into result objects. Parallel topology is illustrated, but cancellation, retry classification, bounded execution, duplicate delivery, and compensation are not tested.
- Security, identity, and data handling: Azure CLI identity is used for agent access, while Cosmos key configuration and query interpolation are unsafe production references. Financial data minimization and retention are not defined.
- Observability and evaluation: extensive span/metric/business-event instrumentation is the strongest reusable aspect. No repeatable eval corpus, baseline, threshold, or release gate exists.
- Hosting, deployment, and rollback: devcontainer/workshop setup exists; there is no production deployment, health, migration, rollback, or disaster-recovery contract.

## Verification

- Commands documented by the source: challenge setup and Python launch commands; Azure CLI login and provisioned-resource prerequisites.
- Checks reproduced locally: GitHub repository metadata, immutable commit, MIT license, tree inventory, dependency file, representative implementation, and telemetry files were inspected through GitHub API/raw immutable URLs.
- Test/eval coverage: no repository CI workflow and no assertion-based MAF test suite were found at the reviewed commit.
- Conflicts with local upstream source, tests, or Microsoft Learn: package coordinates predate target revision `5ab8877...`; current target APIs must supersede workshop syntax.
- Unverified claims: cloud workflows, Cosmos data, hosted MCP actions, model output, DevUI, and telemetry export are `not-run` because they require credentials/resources. Static source and dependency inspection is the substitute evidence.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 4 | 20 | Useful typed compliance workflow, fan-out, and observability decomposition. |
| C-02 | Testing and verification | 25 | 1 | 5 | Demonstration scripts but no CI or deterministic assertions. |
| C-03 | Production depth | 20 | 2 | 8 | Real Azure/Cosmos/telemetry seams, with major security and reliability gaps. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | Pinned packages and extensive direct API calls. |
| C-05 | Source/author credibility | 10 | 5 | 10 | Microsoft-owned MIT workshop repository. |
| C-06 | Version traceability | 5 | 4 | 4 | Immutable commit and pinned MAF beta, but no release. |
| C-07 | Maintenance activity | 5 | 3 | 3 | 2026 activity, but reviewed code lags the target revision. |
|  | **Total** | **100** |  | **60** |  |

### Hard gates

- Triggered gates: the source's central `ChatAgent` and `AzureAIAgentClient` surfaces are absent from the
  target `5ab8877...` Python packages (`Agent` and current Foundry/provider clients are the applicable
  boundaries); a mechanical current-version mapping is therefore not established.
- Result: reject under the removed/unmappable-major-API gate, independently of the score.
- Reviewer decision: `rejected`; a migrated revision can be reviewed again.

## Decision

- State: `rejected`
- Approved use: none in the curated coding-agent evidence layer; the review may remain as a rejection rationale.
- Prohibited or unsafe use: do not route to coding agents as current API proof; do not copy query construction, secret handling, exception swallowing, or side-effect defaults.
- Topic-registry promotion proposal: none while quarantined.
- Collection action: `none`
- Re-review trigger: migration to `Agent` and current Foundry/provider surfaces compatible with target `5ab8877...`, plus deterministic workflow tests and CI.
- Residual risk: a realistic domain narrative can make workshop shortcuts look production-ready.
