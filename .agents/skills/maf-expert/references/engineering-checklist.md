# Engineering checklist

Apply only relevant sections, but never omit a material risk silently.

## Compatibility

- Confirm language, exact package/source version, provider, runtime, hosting, and maturity.
- Verify public symbols in exports plus implementation/tests; do not infer from a sample alone.
- Keep C#, Python, declarative, provider, and version evidence separate.

## Agent and context

- Narrow responsibility and explicit input/output/termination contracts.
- Deterministic business rules stay outside prompts.
- Bound context size and define session/history/memory ownership, retention, compaction, and tenant isolation.

## Tools

- Typed schemas and validation at trust boundaries.
- Authentication, authorization, least privilege, and tenant isolation.
- Idempotency/deduplication, retries, timeout, cancellation, rate limits, and error contracts.
- Approval for destructive, costly, externally visible, or irreversible actions.
- Redaction and independent handler tests.

## Workflows

- State owner, transition invariants, ordering, concurrency, and resource limits.
- Checkpoint/resume/replay and duplicate-delivery semantics.
- Bounded loops/fan-out/retries, compensation, cancellation, and failure propagation.
- Routing, recovery, human approval, and persistence tests.

## Security and operations

- Treat retrieved/tool/agent content as untrusted data, not instructions.
- Secret storage, data minimization, audit, retention, deletion, and incident diagnostics.
- Startup validation, health checks, telemetry, backpressure, quotas/cost, rollback, and provider failure.

## Verification

- Formatting/static analysis and focused deterministic tests.
- Contract/integration tests with controlled doubles for external boundaries.
- Validation, timeout, cancellation, retry, provider failure, authorization, and recovery paths.
- Behavioral eval set, baseline, evaluator, threshold, repeat policy, and preserved failures.
- Exact commands/results plus explicit `not-run` and residual risks.
