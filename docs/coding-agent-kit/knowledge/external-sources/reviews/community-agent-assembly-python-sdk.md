# Source review: `community-agent-assembly-python-sdk`

## Snapshot

- Source: `ai-agent-assembly/python-sdk`
- Canonical URL: https://github.com/ai-agent-assembly/python-sdk
- Source class: `community-repository`; owner: ai-agent-assembly.
- Reviewed commit: `72a9d7d30b1724438968ff5c1399e90124d0701a` (observed 2026-08-11).
- Package coordinates: Python prerelease 0.0.1rc6 with a dedicated Microsoft Agent Framework adapter.
- License: MIT.
- Reviewer and date: Codex, 2026-08-11; policy `v1.1`; track `code-project`.

## Direct Microsoft Agent Framework evidence

- Dedicated adapter, patch layer, documentation, quickstart, and isolated unit tests target Microsoft Agent Framework tool governance.
- The reviewed tree has 352 files, 113 tests, and 19 CI workflows across policy, topology, redaction, fail-open conformance, integration, performance, and packaging.
- The repository and release are very new, with minimal independent adoption evidence.

## Design and implementation value

- Strong governance interception and test structure, especially fail-open and credential-redaction checks.
- Monkey-patch/interception behavior and prerelease native components need deeper compatibility and threat-model review.

## Verification

- Immutable metadata, MIT license, adapter/test paths, prerelease coordinate, benchmarks, and CI were inspected statically.
- Network gateway, policy service, model, credentials, native-core, and live integration paths were `not-run`; no code was copied.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 4 | 20 | Focused governance/interception architecture. |
| C-02 | Testing and verification | 25 | 5 | 25 | 113 tests and 19 CI workflows. |
| C-03 | Production depth | 20 | 3 | 12 | Redaction, policy, topology; prerelease operational history. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | Dedicated MAF adapter and tests. |
| C-05 | Source/author credibility | 10 | 2 | 4 | New organization with little independent usage. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit and rc version. |
| C-07 | Maintenance activity | 5 | 5 | 5 | Active on 2026-08-11. |
|  | **Total** | **100** |  | **81** |  |

### Hard gates

- Triggered gates: none; repairable prerelease, interception-safety, and operational-evidence gaps remain.
- Result: quarantine despite the structural score.

## Decision

- State: `quarantined`
- Approved use: none in active lookup; retain for future governance comparison.
- Prohibited or unsafe use: installing interception patches or calling policy gateways from production without dedicated review.
- Topic-registry promotion proposal: reconsider `security`, `tools`, `observability`, and `evaluation` after maturity evidence.
- Collection action: `none`
- Re-review trigger: stable release, independent users, pinned MAF compatibility, and reproduced safe local adapter tests.
- Residual risk: broad monkey-patching can change application behavior outside the intended tool boundary.
