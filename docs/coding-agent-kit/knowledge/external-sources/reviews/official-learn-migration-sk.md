# Source review: `official-learn-migration-sk`

## Snapshot

- Source: Semantic Kernel to Microsoft Agent Framework migration guide
- Canonical URL: https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-semantic-kernel/
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

- Languages: C# and Python.
- MAF topics: migration.
- Target evidence: `python/samples/semantic-kernel-migration`; `dotnet/src/LegacySupport`; `python/packages/core/agent_framework/__init__.pyi`; `dotnet/src/Microsoft.Agents.AI.Abstractions/AIAgent.cs`.
- Version/maturity: Current guidance but provider/options and legacy-support seams are version-specific.
- Evidence method: live Microsoft Learn page inspected on 2026-07-17; target tree/selected public surfaces checked through the official GitHub API at the immutable revision.
- Important correspondence or drift: The live Python example references typed options and may track post-package changes; exact option names must be checked against the target stub. C# compatibility support is not equivalent to permanent API support.

## Design and implementation value

- Reusable decisions: Canonical mapping of chat clients, agents, tools, sessions, streaming, plugins, and options from Semantic Kernel to MAF.
- Required engineering boundary: examples explain composition, not a complete production contract. Apply typed validation, least privilege, cancellation/timeouts, retry classification, telemetry redaction, evaluation, and rollback where relevant.
- Prohibited shortcut: Do not migrate by symbol substitution alone or retain obsolete persisted state/provider configuration without tests and rollback.

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
- Approved use: primary official explanation and routing source for **migration**, always paired with target revision/package coordinates and matching source/tests.
- Prohibited or unsafe use: Do not migrate by symbol substitution alone or retain obsolete persisted state/provider configuration without tests and rollback.
- Topic-registry promotion proposal: route under `migration`; preserve all additional topic tags from `sources.json`.
- Collection action: `link and annotation only`
- Re-review trigger: page date/content changes, target revision/package upgrade, maturity label change, broken link, or a material source/API contradiction.
- Residual risk: Microsoft Learn is a moving publication surface; this review does not freeze its body, examples, provider matrix, or API-reference latest view.
