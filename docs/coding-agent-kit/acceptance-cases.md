# Coding-agent behavior acceptance cases

Run these in a new Codex task after repository, Skill, or plugin installation. Evaluate behavior and evidence, not exact wording.

## Positive trigger and retrieval

Prompt:

> In Microsoft Agent Framework Python, implement a workflow that checkpoints before human approval and resumes after restart.

Pass conditions:

- `maf-expert` activates;
- Python/version/provider/hosting coordinates are established;
- lookup routes to `workflows`, `durability`, and `approvals-hitl`;
- the answer cites an official page, curated checkpoint/HITL samples, implementation, and tests where available;
- state owner, checkpoint/resume/replay, duplicate delivery, approval identity, and recovery tests are covered.

## Cross-language isolation

Prompt:

> Compare current C# and Python Microsoft Agent Framework session APIs and persistence behavior.

Pass conditions:

- C# and Python symbols and paths remain separate;
- source revision/package versions and maturity are explicit;
- designs, exports/abstractions, samples, and tests are distinguished;
- uncertainty is labeled instead of filling gaps with invented parity.

## Side-effecting tool

Prompt:

> Design a Microsoft Agent Framework tool that cancels customer orders.

Pass conditions: typed contract, identity/authorization, tenant boundary, idempotency/deduplication, timeout/cancellation, retry classification, approval, audit/redaction, compensation, and failure-path tests are present.

## Debugging

Prompt:

> A Python MAF tool sometimes executes twice after workflow resume. Diagnose before proposing a fix.

Pass conditions: reproducible symptom and expected behavior first; evidence routes through tool, workflow, checkpoint/persistence, duplicate delivery, and telemetry; root cause/fix/workaround are separated; regression evidence is required.

## Evaluation

Prompt:

> We changed MAF agent routing instructions. Define a release evaluation.

Pass conditions: versioned dataset, baseline, deterministic assertions/graders, normal/boundary/adversarial/failure cases, quality/safety/latency/cost metrics, thresholds, repeat policy, preserved failures, and release gate are present.

## Negative triggers

The Skill must not activate implicitly for:

> Write a generic CSV cleanup script.

> Build an agent using LangGraph.

> Explain Azure Storage lifecycle policies.

> Create an OpenAI Responses API example that does not use Microsoft Agent Framework.

If the user explicitly invokes `$maf-expert` for these tasks, the Skill should state the scope mismatch and hand the task back to the appropriate generic or framework-specific workflow.
