# Source review: `repo-azure-multi-agent-workshop`

## Snapshot

- Source: `Azure-Samples/multi-agent-orchestration-workshop`
- Canonical URL: https://github.com/Azure-Samples/multi-agent-orchestration-workshop
- Source class: `official-repository`; owner: Azure-Samples/Microsoft.
- Reviewed commit: `4095e86d52e644e691ee19d0076741104dd8111c` (2026-05-27T07:59:03Z).
- Package/API coordinates: centrally versioned .NET MAF core, DevUI, Foundry, Hosting, AG-UI, OpenAI and Workflows packages.
- License: MIT.
- Reviewer and date: Codex, 2026-07-17; policy `v1.1`; track `code-project`.

## Direct Microsoft Agent Framework evidence

- Languages: C# plus localized documentation.
- Four start/complete labs implement sequential, concurrent, handoff and group-chat patterns with Agent, Aspire host, WebUI and service defaults.
- Sixteen project files directly reference MAF packages across pattern variants.
- Tree inspection found no GitHub Actions workflow and no test path at the reviewed commit.

## Design and implementation value

- Reusable: pattern-by-pattern start/complete teaching structure and consistent host/UI decomposition; localization broadens accessibility.
- Production depth is illustrative: Aspire/service defaults and hosting exist, but no automated assertions, eval gates, failure/replay tests, authz/tenant policy, load/SLO or rollback evidence was found.
- Start directories intentionally contain incomplete code and must never be routed as finished implementations.

## Verification

- GitHub API verified commit/date/license, 716 blobs, direct dependency files and absence of detected tests/workflows.
- No build/model/cloud run was performed; target compatibility is a static package/symbol boundary against `5ab8877...`.
- Exact central package versions and complete-lab clean build remain unverified.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 4 | 20 | Clear four-pattern teaching structure. |
| C-02 | Testing and verification | 25 | 0 | 0 | No tests or CI found. |
| C-03 | Production depth | 20 | 3 | 12 | Aspire/hosting shape, no production gates. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | Broad direct MAF references. |
| C-05 | Source/author credibility | 10 | 5 | 10 | Azure-Samples, Microsoft, MIT. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable review commit. |
| C-07 | Maintenance activity | 5 | 4 | 4 | Recent 2026 workshop. |
|  | **Total** | **100** |  | **61** |  |

### Hard gates

- Triggered gates: none.
- Result: score requires quarantine.
- Reviewer decision: `quarantined` pending reproducible verification.

## Decision

- State: `quarantined`
- Approved use: none in coding-agent collection; review notes may guide future recheck.
- Prohibited or unsafe use: start trees, untested APIs, or production reliability claims.
- Topic-registry promotion proposal: none while quarantined.
- Collection action: `none`
- Re-review trigger: complete labs receive CI, tests and pinned/resolved package evidence.
- Residual risk: polished workshop structure can mask runtime/API drift.

