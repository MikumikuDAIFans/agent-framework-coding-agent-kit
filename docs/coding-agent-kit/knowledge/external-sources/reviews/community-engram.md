# Source review: `community-engram`

## Snapshot

- Source: Engram Agent Framework
- Canonical URL: https://github.com/lumetra-io/engram-agent-framework
- Source class: community-repository
- Owner/author: lumetra-io
- Reviewed commit: `0504f9f5a895eaec798e481758f9dc0fbea0c8b8` (2026-05-22)
- Package/API coordinates: Python; agent-framework>=1.5; tool decorator and AgentMiddleware
- License: MIT
- Reviewer and date: Codex, 2026-07-17
- Policy version: `v1.1`
- Review track: `code-project`

## Direct Microsoft Agent Framework evidence

- Languages/topics: memory, tools, middleware
- Relevant files: agent_framework_engram/{client,middleware,skill}.py; examples; tests/test_client.py; PRIVACY.md
- Direct evidence: Python; agent-framework>=1.5; tool decorator and AgentMiddleware
- Target compatibility: Public names may map to target 1.13, but broad >=1.5 constraint and import fallbacks do not prove compatibility.

## Design and implementation value

- Reusable decisions: Useful comparison of model-invoked tools versus automatic middleware memory.
- Verification: Only client tests observed; MAF middleware/tool integration is excluded or not exercised.
- Production and operational depth: Timeout/error wrapper and privacy notes exist, but external-service lifecycle, telemetry and full integration verification are thin.
- Safety boundary: treat prompts, tool output and external data as untrusted; sample shortcuts are not production defaults.

## Verification

- Evidence reproduced: immutable GitHub metadata, manifest/import inspection, repository tree and test/CI inventory.
- Checks not run: model, cloud, hosted service, external database, deployment and credential-dependent paths (`not-run` by policy).
- Target comparison: static comparison to upstream revision `5ab8877ba55b4778d778cf51450eafe483194708`; no claim of runtime compatibility beyond the coordinates above.
- Unverified claims: live inference quality, load behavior, cloud identity/authorization, cost, and production recovery.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 3 | 15 | Useful comparison of model-invoked tools versus automatic middleware memory. |
| C-02 | Testing and verification | 25 | 2 | 10 | Only client tests observed; MAF middleware/tool integration is excluded or not exercised. |
| C-03 | Production depth | 20 | 3 | 12 | Timeout/error wrapper and privacy notes exist, but external-service lifecycle, telemetry and full integration verification are thin. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | Python; agent-framework>=1.5; tool decorator and AgentMiddleware |
| C-05 | Source/author credibility | 10 | 2 | 4 | Public GitHub owner lumetra-io; license MIT. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit 0504f9f5a895eaec798e481758f9dc0fbea0c8b8. |
| C-07 | Maintenance activity | 5 | 4 | 4 | Last reviewed commit 2026-05-22; activity judged from repository metadata. |
|  | **Total** | **100** |  | **60** |  |

### Hard gates

- Triggered gates: No rejection gate; insufficient integration-test evidence.
- Result: quarantined
- Reviewer decision: quarantined

## Decision

- State: `quarantined`
- Approved use: No formal coding-agent route until re-review.
- Prohibited or unsafe use: Do not copy/vendor source; do not infer current API compatibility; do not run credentialed or costly paths without authorization.
- Topic-registry promotion proposal: memory, tools, middleware
- Collection action: `none`
- Re-review trigger: upstream MAF major/API change, source revision/license change, or new compatibility tests.
- Residual risk: Public names may map to target 1.13, but broad >=1.5 constraint and import fallbacks do not prove compatibility.
