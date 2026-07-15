---
name: maf-expert
description: "Use only for Microsoft Agent Framework (microsoft/agent-framework) development: C#/.NET or Python APIs, agents, tools, sessions, context, memory, middleware, providers, workflows, orchestration, checkpointing, approvals, evaluation, DevUI, MCP, A2A, AG-UI, declarative agents, hosting, migration, debugging, review, or deployment. Do not trigger for generic AI, other agent frameworks, unrelated Microsoft SDKs, or ordinary non-MAF coding."
---

# Microsoft Agent Framework Expert

Build version-aware MAF systems from evidence. Route each implementation detail to matching documentation, design, examples, source, and tests; do not rely on remembered API names.

## Establish the two roots

Resolve two independent roots:

1. **Target root**: the application or library the user wants to change.
2. **Reference root**: a checkout of this coding-agent-kit fork or `microsoft/agent-framework` plus the kit catalog.

Find the reference root in this order:

- the target root itself when it contains `docs/coding-agent-kit/catalog/catalog.json`;
- the path in `MAF_REFERENCE_REPO`;
- the absolute path recorded in `references/local-reference-root.txt` by the standalone installer;
- an ancestor of this `SKILL.md` containing `dotnet`, `python`, and `docs/coding-agent-kit`;
- a sibling directory named `agent-framework-coding-agent-kit` or `agent-framework`;
- otherwise operate from official Microsoft Learn and clearly state that local source/test evidence is unavailable.

Do not require a project `.codex/config.toml`. Tool availability comes from the Codex host, explicit user configuration, or this plugin's declared Microsoft Learn MCP dependency.

Read applicable `AGENTS.md` files in both roots before edits. Target-project rules govern the target; upstream nested rules govern any upstream files.

## Classify before searching

Capture:

- work mode: explain/design, implement/refactor, debug, review/test, migrate/upgrade, or deploy/operate;
- language: C#, Python, declarative/schema, cross-language comparison, or language-neutral;
- topic: choose the closest topic ID from [topic-routing.md](references/topic-routing.md);
- compatibility coordinates: package/version or source revision, provider/model, runtime, hosting target, persisted-state/protocol version, and feature maturity.

Discover material coordinates from manifests and code. If one remains unknown, state a bounded assumption rather than silently choosing the latest API.

## Retrieve a compact evidence bundle

When a reference root is available:

1. Run:

   ```powershell
   python <reference-root>/tools/coding-agent-kit/indexer/lookup.py "<task concepts>" --language <python|csharp|any>
   ```

2. Read the topic's curated entries in `docs/coding-agent-kit/catalog/CATALOG.md`.
3. Inspect the smallest relevant set: one official explanation or design note, one sample, the matching implementation/export, and one or more tests.
4. Search exact symbols with `rg` only after the catalog narrows the route.

Use Microsoft Learn MCP for missing, conflicting, or plausibly stale behavior. Online evidence supplements the target version; it does not silently upgrade pinned packages.

Label each conclusion:

- `documented`: official Microsoft documentation;
- `designed`: upstream design/spec/ADR intent;
- `sampled`: a demonstrated composition pattern, not a complete production contract;
- `source-observed`: implementation or test behavior at a named commit/version;
- `project decision`: behavior chosen by the target project;
- `inference`: unresolved interpretation requiring validation.

## Execute by mode

### Explain or design

Lead with a concrete recommendation. Cover responsibility boundaries, API shape, state/data flow, failure semantics, security, observability, evaluation, deployment implications, and alternatives. Cite repository-relative paths and flag preview/version sensitivity.

### Implement or refactor

Inspect target seams and tests first. Follow target conventions. Keep deterministic rules outside prompts; wrap external capabilities in typed, independently testable services and narrow tools. Implement the smallest coherent change and update durable knowledge only for a lasting decision or reusable discovery.

### Debug

Establish a reproducible symptom and expected behavior. Trace configuration/identity -> provider client -> agent/session/context -> middleware -> tools -> workflow/persistence -> hosting -> telemetry as applicable. Separate root cause, fix, workaround, and residual risk; add regression evidence.

### Review or test

Report findings before summary, ordered by impact. Check version/API correctness, cross-language/provider leakage, state/concurrency, side effects, security/privacy, reliability, observability, evaluation quality, and missing tests. Map material behavior and risks to verifiers.

### Migrate or upgrade

Inventory packages, public imports/exports, provider configuration, persisted state, behavior, and tests. Establish a characterization baseline, follow the matching guide, change one compatibility boundary at a time, and verify rollback.

### Deploy or operate

Verify identity, secrets, least privilege, startup validation, health, telemetry/redaction, retention, network access, scaling/backpressure, quotas/cost, timeouts/retries/idempotency, approvals, compatibility, and rollback. Do not mutate live resources without explicit authorization.

## Quality gates and output

Read [engineering-checklist.md](references/engineering-checklist.md). For substantive work report:

1. recommendation or outcome;
2. compatibility coordinates;
3. evidence bundle with labels and repository-relative paths;
4. implementation/design and tradeoffs;
5. verification commands and results;
6. unverified items, assumptions, and residual risks.

Use [knowledge-routing.md](references/knowledge-routing.md) for deciding whether a durable discovery belongs in the target project, this kit's curated registry, or upstream documentation. External projects remain links and annotations; retain adopted document bodies only when redistribution terms have been verified.

When the target project needs a durable design or evidence artifact, start from the matching template under `<reference-root>/docs/coding-agent-kit/templates` and save the completed artifact in the target project's approved documentation area.
