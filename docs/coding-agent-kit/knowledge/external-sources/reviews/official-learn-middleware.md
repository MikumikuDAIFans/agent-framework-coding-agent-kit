# Source review: `official-learn-middleware`

## Snapshot

- Source: Agent middleware overview
- Canonical URL: https://learn.microsoft.com/en-us/agent-framework/agents/middleware/
- Source class: `official-doc`
- Owner/author: Microsoft Learn / Microsoft
- Reviewed page date: 2026-07-10
- Target source revision: `microsoft/agent-framework@5ab8877ba55b4778d778cf51450eafe483194708` (2026-07-16)
- Package/API coordinates: target source revision above; published package versions must be pinned by the consuming project
- License/reuse boundary: Microsoft Learn Terms of Use are linked by the page, but no page-specific redistribution grant was verified in this review. Retain only the URL and original annotation.
- Reviewer and date: Codex, 2026-07-17
- Policy version: `v1.1`
- Review track: `official-doc`

## Direct Microsoft Agent Framework evidence

- Languages: C#, Python, and separately maintained Go SDK.
- MAF topics: middleware.
- Target evidence: `docs/decisions/0007-agent-filtering-middleware.md`; `docs/decisions/0016-python-context-middleware.md`; `python/packages/core/agent_framework/_middleware.py`; `dotnet/samples/02-agents/Agents/Agent_Step11_Middleware`.
- Version/maturity: Core middleware exists in C# and Python; scope/context hooks and provider middleware differ by language.
- Evidence method: live Microsoft Learn page inspected on 2026-07-17; target tree/selected public surfaces checked through the official GitHub API at the immutable revision.
- Important correspondence or drift: Target design and Python contracts match the main concepts; exact ordering and hook types are language-specific. Go middleware is external to this target.

## Design and implementation value

- Reusable decisions: Authoritative interception model for agent/run scopes, chat/tool calls, runtime context, result overrides, termination, and exception handling.
- Required engineering boundary: examples explain composition, not a complete production contract. Apply typed validation, least privilege, cancellation/timeouts, retry classification, telemetry redaction, evaluation, and rollback where relevant.
- Prohibited shortcut: Do not swallow failures, mutate shared state unsafely, leak prompts/tool payloads to telemetry, or assume middleware replaces authorization.

## Verification

- Page reachability and canonical title: verified on 2026-07-17.
- Immutable target revision: verified through the official GitHub API.
- Local/cloud execution: not run; this is a documentation-to-source review, and no cloud credentials, paid resources, or production systems were needed.
- Conflicts with target source/tests: recorded above; no unresolved contradiction blocks link adoption.
- Unverified claims: every provider/service capability not implemented and tested in the target repository remains provider-specific and must be rechecked at use time.

## Evaluation under the approved policy

### Official documentation direct-adoption check

- [x] Canonical URL, title, review date, and language recorded.
- [x] Target package/API version and maturity recorded.
- [x] Compared with target upstream source/public API/tests.
- [x] Drift, language differences, and implementation gaps recorded.

### Hard gates

- Triggered gates: none. Official documentation is directly eligible after this check.
- Result: pass for official link adoption.
- Reviewer decision: `adopted`.

## Decision

- State: `adopted`
- Approved use: primary official explanation and routing source for **middleware**, always paired with target revision/package coordinates and matching source/tests.
- Prohibited or unsafe use: Do not swallow failures, mutate shared state unsafely, leak prompts/tool payloads to telemetry, or assume middleware replaces authorization.
- Topic-registry promotion proposal: route under `middleware`; preserve all additional topic tags from `sources.json`.
- Collection action: `link and annotation only`
- Re-review trigger: page date/content changes, target revision/package upgrade, maturity label change, broken link, or a material source/API contradiction.
- Residual risk: Microsoft Learn is a moving publication surface; this review does not freeze its body, examples, provider matrix, or API-reference latest view.
