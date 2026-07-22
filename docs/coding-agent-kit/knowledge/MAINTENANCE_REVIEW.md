# Maintenance system review

## Review snapshot

- Date: `2026-07-22 Asia/Shanghai`
- Kit commit reviewed: `b378caf6e40e1375308491191e91c98a44a4d433`
- Indexed upstream baseline: `5ab8877ba55b4778d778cf51450eafe483194708` (`2026-07-16`)
- Microsoft `main` observed through the GitHub API: `848443ac68b9470de5c43c3a355829625d7f0a3a` (`2026-07-21`)
- Existing knowledge registry: 65 sources; 42 adopted, 5 context-only, 5 quarantined, 12 rejected, and one discovery-only meta-index.

## Findings

### Strong foundations

- The catalog already indexes official design, samples, implementation, tests, schemas, and 133 Microsoft Learn routes.
- External projects are URL- and immutable-version-only; external document bodies are not retained without redistribution permission.
- `maintenance.py` correctly distinguishes `pass`, `drift`, `needs-review`, `failed`, and `not-run` and never mutates review state automatically.
- Collection and lookup are generated and validated together, and upstream has a disabled push URL.

### Gaps addressed in this maintenance revision

1. Agent Skills, Agent Harness, and CodeAct were present in the indexed corpus but lacked dedicated topic routes. Generic routing made focused queries miss their strongest design/source/test bundles.
2. The existing maintenance command detected drift but did not define a complete discovery-to-retirement operating cycle.
3. There was no explicit archive ledger for adopted sources removed from active lookup.
4. Plugin synchronization assumed exactly one Skill, preventing the kit from shipping a dedicated maintainer Skill.
5. The CI workflow validated changes but did not perform a scheduled external drift scan.

## Current technology delta

The official MAF surface now prominently includes Agent Skills, Agent Harness, CodeAct, Foundry Hosted Agents, stable orchestration patterns, and a separate Go implementation. These must be tracked as versioned evidence rather than inferred from older preview-era articles.

High-priority discovery candidates for the next review batch include:

| Candidate | Why it matters | Initial route |
| --- | --- | --- |
| `microsoft/agent-framework-go` | Official, active MIT implementation with agents, harness, skills, protocols, workflows, checkpointing, providers, and extensive tests. | External project route pinned to a commit; never mix Go symbols into .NET/Python answers. |
| `rwjdk/AgentFrameworkToolkit` | Active MIT .NET toolkit with multiple provider adapters, Agent Skills helpers, tool confinement tests, and broad integration tests. | Community design reference pending full scoring and current-package compatibility review. |
| MAF Agent Skills release posts | Record the July 2026 maturity change from experimental to stable for Python and .NET. | Official engineering article, paired with exact exports and tests. |
| MAF Agent Harness series | Runnable, cross-language explanation of planning, memory, approvals, files, skills, and scaling patterns. | Official engineering route; examples remain sample evidence, not production defaults. |
| GitHub Copilot SDK integration documentation | A current provider integration with runnable workflows and tools. | Official third-party documentation; verify package versions against upstream. |

Older public-preview tutorials and repositories are not automatically removed. They enter re-review when their API surface, date, or value boundary conflicts with the current baseline; age alone does not erase still-useful design history.

## Maintenance model

The safe model is two-stage:

1. Scheduled automation performs discovery, upstream comparison, reachability/version/license checks, catalog checks, and produces reports.
2. `$maf-kit-maintainer` evaluates evidence, updates or archives sources, rebuilds indexes, runs the complete gate, and publishes only a coherent verified batch.

This keeps routine observation automatic while preserving the approved review policy and preventing transient network failures from deleting knowledge.

