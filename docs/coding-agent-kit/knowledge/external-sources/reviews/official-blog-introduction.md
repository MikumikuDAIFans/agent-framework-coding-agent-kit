# Source review: `official-blog-introduction`

## Snapshot

- Source: Introducing Microsoft Agent Framework (Preview)
- Canonical URL: https://devblogs.microsoft.com/dotnet/introducing-microsoft-agent-framework-preview/
- Source class: `official-engineering`; author: Luis Quintanilla, Microsoft.
- Reviewed page date: 2025-10-01.
- Package/API coordinates: preview .NET packages; `Microsoft.Agents.AI`, `Microsoft.Extensions.AI`, OpenAI/GitHub Models.
- License: no article-specific redistribution license verified.
- Reviewer and date: Codex, 2026-07-17; policy `v1.1`; track `technical-article`.

## Direct Microsoft Agent Framework evidence

- Languages: C#.
- The article supplies prerequisites, package commands, environment setup and runnable story-agent/workflow code using `AIAgent`, `ChatClientAgent`, `ChatClientAgentOptions`, `RunAsync` and workflow composition.
- Target-boundary check: `ChatClientAgentOptions` and the agent abstractions are present in the current official repository indexed at `5ab8877ba55b4778d778cf51450eafe483194708`; this does not validate every preview command or orchestration snippet.
- Preview boundary: `--prerelease`, .NET 9-era setup and launch-era maturity statements are historical, not current package guidance.

## Design and implementation value

- Reusable: agents separate reasoning/context/tools; workflows provide explicit structure; `IChatClient` is the provider seam; agents and workflows are composable.
- Shortcuts: direct environment-token setup, toy tools and happy-path console execution omit authorization, retries, cancellation, telemetry, evaluation and deployment controls.
- The architecture explanation remains useful, but current Learn/source/tests take precedence for APIs and maturity.

## Verification

- Page date, author, commands, code and linked GitHub sample were inspected.
- Static target-revision symbol mapping was performed; cloud/model execution was not run because it requires credentials.
- Unverified: exact old prerelease package set and every workflow snippet as a clean build at the target revision.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| A-01 | Real demo | 30 | 4 | 24 | Setup, complete agent code and run command. |
| A-02 | Design value | 25 | 4 | 20 | Clear abstraction and composition boundaries. |
| A-03 | Technical recency | 15 | 3 | Core symbols map; preview commands/maturity drifted. |
| A-04 | Publication date | 15 | 4 | Within 24 months. |
| A-05 | Source/author credibility | 15 | 5 | Named Microsoft author on .NET Blog. |
|  | **Total** | **100** |  | **80** |  |

### Hard gates

- Triggered gates: none; historical preview material is explicitly bounded.
- Result: passes.
- Reviewer decision: `adopted` for architecture/history and a version-bounded starter route.

## Decision

- State: `adopted`
- Approved use: conceptual architecture and locating the matching upstream hello-agent sample.
- Prohibited or unsafe use: copying preview package commands, token handling, or production defaults without current verification.
- Topic-registry promotion proposal: `agents`, `workflows`, `getting-started` as secondary explanation.
- Collection action: `link and annotation only`
- Re-review trigger: removal of mapped agent symbols or a major MAF version.
- Residual risk: readers may mistake launch-era preview maturity for current status.
