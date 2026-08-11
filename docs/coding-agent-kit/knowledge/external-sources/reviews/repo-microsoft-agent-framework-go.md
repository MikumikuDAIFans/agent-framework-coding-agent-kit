# Source review: `repo-microsoft-agent-framework-go`

## Snapshot

- Source: `microsoft/agent-framework-go`
- Canonical URL: https://github.com/microsoft/agent-framework-go
- Source class: `official-repository`; owner: Microsoft.
- Reviewed commit: `206863eab447fe89787a9be123c19967b3066a09` (observed 2026-08-11).
- Package/API coordinates: Go module `github.com/microsoft/agent-framework-go`; public preview.
- License: MIT.
- Reviewer and date: Codex, 2026-08-11; policy `v1.1`; track `code-project`.

## Direct Microsoft Agent Framework evidence

- This is Microsoft's separate Go implementation of Agent Framework, not a port stored in the .NET/Python monorepo.
- The reviewed tree has 459 files, 119 tests, and 13 CI workflows across agents, tools, middleware, harness, workflows, checkpointing, MCP, A2A, AG-UI, providers, and observability.
- Explicit preview gaps include declarative agents, RAG, CodeAct, functional workflows, and handoff orchestration.

## Design and implementation value

- Strong cross-language evidence for interface boundaries and workflow semantics, with dedicated Go tests and API-consistency automation.
- Go symbols and maturity must never be substituted for .NET or Python contracts.

## Verification

- GitHub metadata, MIT license, immutable commit, recursive tree, `go.mod`, README maturity statement, tests, and CI inventory were inspected.
- No provider, cloud, model, credential, or production deployment path was run; those checks are `not-run`.
- No external code was copied or retained.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 5 | 25 | Full Go agent/workflow/protocol architecture. |
| C-02 | Testing and verification | 25 | 5 | 25 | 119 tests and 13 CI workflows. |
| C-03 | Production depth | 20 | 5 | 20 | Hosting, telemetry, checkpoints, protocols, and safety boundaries. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | Official implementation itself. |
| C-05 | Source/author credibility | 10 | 5 | 10 | Microsoft-owned MIT repository. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit and Go module coordinate. |
| C-07 | Maintenance activity | 5 | 5 | 5 | Active through 2026-08-10. |
|  | **Total** | **100** |  | **100** |  |

### Hard gates

- Triggered gates: none.
- Result: passes; public-preview maturity is an explicit route limitation.

## Decision

- State: `adopted`
- Approved use: immutable Go design, implementation, tests, and samples when the requested language is Go.
- Prohibited or unsafe use: mixing Go symbols into .NET/Python answers or treating preview gaps as implemented.
- Topic-registry promotion proposal: external routes for agents, workflows, harness, protocols, durability, observability, and providers.
- Collection action: `project route`
- Re-review trigger: module release, major API movement, license change, or preview-to-stable transition.
- Residual risk: the Go repository evolves independently from target `d0a4165f170193ba1d026a259af40d35bb7eaefe`.
