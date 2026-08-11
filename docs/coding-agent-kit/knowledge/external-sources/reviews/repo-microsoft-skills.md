# Source review: `repo-microsoft-skills`

## Snapshot

- Source: `microsoft/skills`
- Canonical URL: https://github.com/microsoft/skills
- Source class: `official-repository`; owner: Microsoft.
- Reviewed commit: `849ffefb22c133c1e8c6a282a3ded018cb9c4ad7` (observed 2026-08-11).
- Relevant coordinate: MAF Azure AI Python skill version 1.0.0 within a multi-SDK coding-agent skill repository.
- License: MIT.
- Reviewer and date: Codex, 2026-08-11; policy `v1.1`; track `code-project`.

## Direct Microsoft Agent Framework evidence

- The repository contains a dedicated `agent-framework-azure-ai-py` skill with current MAF imports, hosted tools, MCP, thread, streaming, and credential-lifecycle guidance.
- The broader tree has 2,154 files, 456 tests, and six CI workflows, but most coverage targets other SDK skills rather than MAF runtime behavior.
- It is coding-agent guidance, not the canonical MAF implementation or package test suite.

## Design and implementation value

- Useful for Azure provider discovery, secure credential patterns, and skill/evaluation design.
- Snippets and instructions must be checked against local exports and tests before use.

## Verification

- Immutable metadata, MIT license, MAF skill body, related evaluation scenarios, tree, and CI were inspected statically.
- Skill evals, Azure credentials, hosted tools, and model paths were `not-run`; no content was copied.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 4 | 20 | Useful provider and coding-agent guidance. |
| C-02 | Testing and verification | 25 | 4 | 20 | Strong repository eval harness, indirect MAF runtime coverage. |
| C-03 | Production depth | 20 | 3 | 12 | Credential/resource guidance, not a production host. |
| C-04 | Real MAF dependency | 10 | 3 | 6 | Real API snippets but no pinned runtime project. |
| C-05 | Source/author credibility | 10 | 5 | 10 | Microsoft-owned MIT repository. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit and skill version. |
| C-07 | Maintenance activity | 5 | 5 | 5 | Active through 2026-08-10. |
|  | **Total** | **100** |  | **78** |  |

### Hard gates

- Triggered gates: none; actual MAF calls are present, but executable package compatibility is incomplete.
- Result: passes gates in the context-only score band.

## Decision

- State: `context-only`
- Approved use: provider/skill design context and discovery of APIs to verify locally.
- Prohibited or unsafe use: treating skill prose or eval output as canonical MAF API proof.
- Topic-registry promotion proposal: none.
- Collection action: `none`
- Re-review trigger: a pinned runnable MAF project and isolated compatibility tests are added.
- Residual risk: rapid skill updates can drift from released MAF packages.
