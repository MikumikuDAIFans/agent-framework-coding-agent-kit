# Source review: `official-learn-declarative-workflows`

## Snapshot

- Source: Declarative Workflows overview
- Canonical URL: https://learn.microsoft.com/en-us/agent-framework/workflows/declarative
- Source class: `official-doc`
- Owner/author: Microsoft Learn / Microsoft
- Reviewed page date: 2026-06-26
- Target source revision: `microsoft/agent-framework@5ab8877ba55b4778d778cf51450eafe483194708` (2026-07-16)
- Package/API coordinates: target source revision above; published package versions must be pinned by the consuming project
- License/reuse boundary: Microsoft Learn Terms of Use are linked by the page, but no page-specific redistribution grant was verified in this review. Retain only the URL and original annotation.
- Reviewer and date: Codex, 2026-07-17
- Policy version: `v1.1`
- Review track: `official-doc`

## Direct Microsoft Agent Framework evidence

- Languages: C#, Python, and declarative YAML; no Go support.
- MAF topics: declarative, workflows.
- Target evidence: `declarative-agents/workflow-samples`; `python/packages/declarative`; `dotnet/src/Microsoft.Agents.AI.Workflows.Declarative`; declarative unit/integration tests.
- Version/maturity: Feature and supported action set are version-sensitive; individual providers/actions can be preview.
- Evidence method: live Microsoft Learn page inspected on 2026-07-17; target tree/selected public surfaces checked through the official GitHub API at the immutable revision.
- Important correspondence or drift: Target contains both implementations and samples, but C# and Python supported actions/providers are not automatically symmetric. YAML must be validated against the target schema/runtime.

## Design and implementation value

- Reusable decisions: Canonical schema-driven workflow route, expression/state model, action taxonomy, portability boundaries, and testing guidance.
- Required engineering boundary: examples explain composition, not a complete production contract. Apply typed validation, least privilege, cancellation/timeouts, retry classification, telemetry redaction, evaluation, and rollback where relevant.
- Prohibited shortcut: Do not execute untrusted declarative definitions or assume embedded expressions/tools are sandboxed, authorized, or portable.

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
- Approved use: primary official explanation and routing source for **declarative, workflows**, always paired with target revision/package coordinates and matching source/tests.
- Prohibited or unsafe use: Do not execute untrusted declarative definitions or assume embedded expressions/tools are sandboxed, authorized, or portable.
- Topic-registry promotion proposal: route under `declarative`; preserve all additional topic tags from `sources.json`.
- Collection action: `link and annotation only`
- Re-review trigger: page date/content changes, target revision/package upgrade, maturity label change, broken link, or a material source/API contradiction.
- Residual risk: Microsoft Learn is a moving publication surface; this review does not freeze its body, examples, provider matrix, or API-reference latest view.
