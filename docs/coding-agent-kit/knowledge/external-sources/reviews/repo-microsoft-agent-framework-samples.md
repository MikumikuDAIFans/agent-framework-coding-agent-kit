# Source review: `repo-microsoft-agent-framework-samples`

## Snapshot

- Source: `microsoft/Agent-Framework-Samples`
- Canonical URL: https://github.com/microsoft/Agent-Framework-Samples
- Source class: `official-repository`
- Owner/author: Microsoft organization; individual samples have multiple contributors.
- Reviewed commit: `5b854b7e1c3838f17f41bcf2412ef79d7662db37`
- Commit date: `2026-06-06T11:29:15+08:00`
- Local comparison revision: `microsoft/agent-framework@c47f20d9a28d18b0a3f284c8a8365ff72f2e35b1`
  (`2026-07-09`)
- Package/API coordinates: mixed. The repository uses source references, GitHub `main`, unpinned notebook
  installs, `agent-framework>=1.1.0`, and preview dependencies; it does not define one reproducible MAF
  version for the whole corpus.
- License: MIT, Microsoft copyright.
- Reviewer/date: Codex, 2026-07-15.

## Direct Microsoft Agent Framework evidence

- Languages: Python, C#/.NET, Jupyter Notebook, and small frontend/infrastructure portions.
- Inventory at the reviewed commit: 323 tracked files visible to `rg`, including 86 `.py`, 23 `.ipynb`,
  36 `.cs`, and 28 `.csproj` files.
- Direct evidence:
  - Python imports include `Agent`, `WorkflowBuilder`, `WorkflowViz`, provider clients, orchestration
    builders, DevUI, observability, and AG-UI packages.
  - C# examples use `Microsoft.Agents.AI`, workflows, Foundry, DevUI, AG-UI hosting, and OpenTelemetry.
  - Scenario directories cover beginner agents, tools, providers, file-search RAG, workflows, DevUI,
    tracing, AG-UI, hosted agents, and larger cases.
- Topics demonstrated: getting started, providers, tools, RAG, workflows, orchestration, DevUI,
  observability, AG-UI, hosting, and Foundry-specific capabilities.
- Current-symbol comparison: representative symbols such as Python `AgentResponse`, `WorkflowBuilder`,
  `WorkflowViz`, `OpenAIChatCompletionClient`, `OpenAIChatClient`, `ConcurrentBuilder`, and observability
  setup functions exist in the local comparison revision. This confirms relevance, not end-to-end
  compatibility for every sample.
- Maturity boundary: the repository mixes released, preview, source-main, and placeholder configurations.
  Its root statement about a framework 1.0 release does not pin individual examples to that release.

## Design and implementation value

- Reusable value:
  - broad scenario discovery outside the core upstream repository;
  - side-by-side Python and .NET learning routes for several topics;
  - useful examples of workflow topology, DevUI, OpenTelemetry, AG-UI, Foundry tools, and hosted-agent
    composition;
  - case-study ideas that can seed a more rigorous search in local source, tests, and Learn docs.
- Sample shortcuts and hazards:
  - all 28 `.csproj` files contain a placeholder or developer-machine project reference; several contain
    absolute developer-home paths into a local Agent Framework checkout;
  - only one project directly references a `Microsoft.Agents.AI*` NuGet package, so most .NET examples are
    not portable package-consumer examples;
  - Python requirements commonly install from the moving GitHub `main` branch or use unbounded/minimum-only
    versions; notebook cells frequently run `pip install ... -U`;
  - the root README contains a path typo (`requirement.txt` versus `requirements.txt`) and presents the
    corpus as more directly runnable than its project references support;
  - some files contain encoding/mojibake issues;
  - `test_env.py` prints the last ten characters of `GITHUB_TOKEN`; even partial credential disclosure is
    an unsafe diagnostic pattern and must not be copied.
- State/data flow: workflow samples demonstrate routing topology, but most do not define durable ownership,
  checkpoint/replay semantics, tenant isolation, or data retention.
- Tool/side-effect boundaries: Foundry tools, file search, code interpreter, web search, and MCP are shown,
  but production authorization, idempotency, retry classification, cancellation, quotas, and audit controls
  are generally not complete.
- Failure/concurrency behavior: sequential, concurrent, and conditional graphs are illustrated. Systematic
  failure propagation, bounded retry, duplicate delivery, compensation, and cancellation tests are absent.
- Security/identity/data: Azure/GitHub environment setup is described, but least privilege and secret
  handling are not consistently enforced. The token-suffix diagnostic is a concrete negative example.
- Observability/evaluation: DevUI and OpenTelemetry examples are valuable discovery points. The repository
  does not provide a reusable evaluation dataset, baseline, threshold, or release gate.
- Hosting/deployment/rollback: hosted-agent and AG-UI cases show integration shape, but there is no common
  deployment manifest, clean-install gate, health/rollback contract, or repository-wide CI.

## Verification

- Repository-wide static inventory and dependency/reference scan: completed.
- License and immutable commit: verified.
- Python syntax:
  - AST parsing passed for all 86 Python files.
  - `compileall` was not a valid verifier on this Windows checkout because deeply nested paths prevented
    creation of some `__pycache__` files; it also reported one invalid-escape `SyntaxWarning`.
- .NET build:
  - attempted `dotnet build --no-restore` on the basic workflow project;
  - blocked before dependency/reference validation because the machine has .NET SDK 8.0.422 while the
    sample targets .NET 10.0;
  - even with .NET 10, the checked project contains placeholder source-project references and requires
    local path repair before it can build.
- Tests/CI:
  - no GitHub Actions workflow exists; `.github` contains only Dependabot configuration;
  - five Python files have test-like names, but they are manual integration/diagnostic scripts rather than
    a repository-wide assertion-based test suite;
  - cloud/model integration tests were not run because they require credentials and external resources.
- API comparison: representative imported symbols were located in implementation/tests at the local
  upstream revision. A full per-sample compatibility matrix was not run because the source does not provide
  stable package coordinates.

## Provisional factual assessment

- Policy version: `draft-0`
- Policy approval status: `awaiting-owner-definition`
- Final score: not assigned
- Final decision: pending maintainer-approved policy
- Registry state: `in-review`

The evidence below records technical findings only. It is not an adoption, downgrade, rejection, or
promotion decision. The previous eight-dimension score and `context-only` decision are withdrawn because
they were produced before the maintainer defined and approved the review policy.

## Candidate use boundaries for maintainer review

- Potential use:
  - discover scenario ideas and additional Microsoft-owned examples;
  - locate candidate patterns for workflows, DevUI, telemetry, AG-UI, tools, and hosted agents;
  - use an individual sample only after pinning its own commit/dependencies and rechecking the exact API
    against local source, tests, and Microsoft Learn.
- Known unsafe or unsupported use:
  - do not treat the repository root as a reproducible package-consumer reference;
  - do not copy `.csproj` project references, `git@main` requirements, `pip install -U` cells, credential
    diagnostics, or production/security defaults;
  - do not claim a sample is current merely because the repository is Microsoft-owned.
- Topic-registry promotion: prohibited while the policy is unapproved and the source remains `in-review`.
  After policy approval, a later review may propose an individual sample path if it has stable coordinates
  and clear added value over the local upstream corpus.
- Re-review trigger: repository publishes pinned releases or CI, replaces machine/placeholder references,
  or a specific sample becomes the canonical official implementation for a topic.
- Residual risk: individual samples may be newer than, older than, or incompatible with the target MAF
  package even when their symbols still exist.
