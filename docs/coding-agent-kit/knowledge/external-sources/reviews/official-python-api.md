# Source review: `official-python-api`

## Snapshot

- Source: agent_framework Python API reference
- Canonical URL: https://learn.microsoft.com/en-us/python/api/agent-framework-core/agent_framework
- Source class: `official-doc`
- Owner/author: Microsoft Learn / Microsoft
- Reviewed page date: No page-level update date is displayed; retrieved 2026-07-17
- Target source revision: `microsoft/agent-framework@5ab8877ba55b4778d778cf51450eafe483194708` (2026-07-16)
- Package/API coordinates: target source revision above; `agent-framework-core==1.11.0` at the target revision
- License/reuse boundary: Microsoft Learn Terms of Use are linked by the page, but no page-specific redistribution grant was verified in this review. Retain only the URL and original annotation.
- Reviewer and date: Codex, 2026-07-17
- Policy version: `v1.1`
- Review track: `official-doc`

## Direct Microsoft Agent Framework evidence

- Languages: Python.
- MAF topics: agents.
- Target evidence: `python/packages/core/pyproject.toml`; `python/packages/core/agent_framework/__init__.pyi`; `python/packages/core/agent_framework/_agents.py`; core tests.
- Version/maturity: The canonical URL redirects to `view=agent-framework-python-latest`; target Python core declares version `1.11.0`, while individual features may be experimental.
- Evidence method: live Microsoft Learn page inspected on 2026-07-17; target tree/selected public surfaces checked through the official GitHub API at the immutable revision.
- Important correspondence or drift: The moving latest view can drift from target `agent-framework-core==1.11.0` at commit `5ab8877b…`; the target stub and tests are the compatibility authority.

## Design and implementation value

- Reusable decisions: Authoritative published module/class/function lookup when paired with an explicit package version.
- Required engineering boundary: examples explain composition, not a complete production contract. Apply typed validation, least privilege, cancellation/timeouts, retry classification, telemetry redaction, evaluation, and rollback where relevant.
- Prohibited shortcut: Do not import private underscored modules based on generated docs or assume experimental exports have stable signatures.

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
- Approved use: primary official explanation and routing source for **agents**, always paired with target revision/package coordinates and matching source/tests.
- Prohibited or unsafe use: Do not import private underscored modules based on generated docs or assume experimental exports have stable signatures.
- Topic-registry promotion proposal: route under `agents`; preserve all additional topic tags from `sources.json`.
- Collection action: `link and annotation only`
- Re-review trigger: page date/content changes, target revision/package upgrade, maturity label change, broken link, or a material source/API contradiction.
- Residual risk: Microsoft Learn is a moving publication surface; this review does not freeze its body, examples, provider matrix, or API-reference latest view.
