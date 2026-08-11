# Source review: `community-sokolaidev-maf-extensions`

## Snapshot

- Source: `sokolaidev/maf-extensions`
- Canonical URL: https://github.com/sokolaidev/maf-extensions
- Source class: `community-repository`; owner: sokolaidev.
- Reviewed commit: `696b39d34d8041072d77321004a86673a90c43dd` (observed 2026-08-11).
- Package coordinates: Python `maf-sandbox` 0.6.0 and backend packages; `agent-framework-core>=1.13.0,<2`.
- License: MIT.
- Reviewer and date: Codex, 2026-08-11; policy `v1.1`; track `code-project`.

## Direct Microsoft Agent Framework evidence

- The repository implements a sandbox protocol/router and MAF glue plus ACAS, WSL, Docker, Bicep, and CodeAct workloads.
- The reviewed tree has 140 files, 28 tests, and five CI workflows with packaging, boundary, proxy-parity, and provenance tests.
- It was created only four days before review and some backends require external runtimes or privileged environments.

## Design and implementation value

- Useful minimum-isolation and workload-capability contracts for CodeAct/tool execution.
- Operational and security maturity across every backend is not yet established.

## Verification

- Immutable metadata, MIT license, package versions, tests, CI, and sample inventory were inspected statically.
- Docker, WSL, ACAS, cloud sandboxes, live samples, and privileged operations were `not-run`; no code was copied.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 4 | 20 | Explicit isolation/capability seam. |
| C-02 | Testing and verification | 25 | 4 | 20 | 28 boundary and packaging tests plus CI. |
| C-03 | Production depth | 20 | 3 | 12 | Multiple backends, limited operational history. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | Direct core dependency and glue tests. |
| C-05 | Source/author credibility | 10 | 2 | 4 | Very new single-owner public repository. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit and package versions. |
| C-07 | Maintenance activity | 5 | 5 | 5 | Active on 2026-08-11. |
|  | **Total** | **100** |  | **76** |  |

### Hard gates

- Triggered gates: none; repairable maturity and environment-verification gaps remain.
- Result: quarantine until independent operational evidence exists.

## Decision

- State: `quarantined`
- Approved use: none in active lookup; retain the review for future sandbox-boundary comparison.
- Prohibited or unsafe use: treating backend names as guaranteed isolation or running privileged/destructive paths.
- Topic-registry promotion proposal: reconsider `security`, `tools`, and `codeact` after re-review.
- Collection action: `none`
- Re-review trigger: stable release history, threat model, backend compatibility matrix, and reproducible safe local tests.
- Residual risk: early rapid development can invalidate security and API assumptions quickly.

## Same-cycle drift follow-up 2026-08-11

- Updated reviewed coordinate: `e328dafe513047e6d68de9542754562dff9e3601` after two commits landed during the maintenance run.
- The delta adds ACAS artifact-output handling that refuses unsupported symlinks, substantially expands backend tests, and removes an over-broad regularity guarantee from documentation.
- These are positive hardening signals but also confirm rapid API/security movement; `quarantined` remains the correct state.
