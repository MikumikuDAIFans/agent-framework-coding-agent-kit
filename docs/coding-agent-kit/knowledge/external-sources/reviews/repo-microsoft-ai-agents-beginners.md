# Source review: `repo-microsoft-ai-agents-beginners`

## Snapshot

- Source: `microsoft/ai-agents-for-beginners`
- Canonical URL: https://github.com/microsoft/ai-agents-for-beginners
- Source class: `official-repository`; owner: Microsoft.
- Reviewed commit: `ad068048e785ecc3f05d663e7c4ba18a55e72972` (2026-07-14T21:24:23Z).
- Package/API coordinates: `agent-framework~=1.10.0`, `agent-framework-foundry~=1.10.0`, `agent-framework-openai~=1.10.0` in root requirements.
- License: MIT.
- Reviewer and date: Codex, 2026-07-17; policy `v1.1`; track `code-project`.

## Direct Microsoft Agent Framework evidence

- Languages: Python, C# curriculum text and notebooks; dedicated lesson `14-microsoft-agent-framework` and workflow sample under lesson 08.
- Direct pinned-compatible Python MAF dependency exists; lessons cover agents, tools, orchestration, protocols, memory, production and security in a wider multi-framework course.
- Target boundary: 1.10-era lesson material is close to target `5ab8877ba55b4778d778cf51450eafe483194708`, but each notebook/symbol still needs lookup because the repository is not exclusively MAF.

## Design and implementation value

- Reusable as a beginner curriculum and framework-comparison context, especially the dedicated MAF lesson.
- Repository breadth and translations dilute exact MAF engineering depth; demos emphasize learning over durable state, failure semantics, authorization, deployment and rollback.
- One smoke-test workflow and test area provide basic verification, not a comprehensive MAF test/evaluation gate.

## Verification

- GitHub API verified commit/date/license, 9,700 blobs, three workflow files and direct root requirements.
- Static dependency/tree review only; model-backed notebooks were not run due credentials/cost.
- Exact translated-page parity and full notebook execution are unverified.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 3 | 15 | Good pedagogy, limited reusable architecture. |
| C-02 | Testing and verification | 25 | 3 | 15 | Smoke CI/tests, not comprehensive MAF verification. |
| C-03 | Production depth | 20 | 2 | 8 | Production/security lessons, mostly educational. |
| C-04 | Real MAF dependency | 10 | 4 | 8 | Direct 1.10 requirements and dedicated examples. |
| C-05 | Source/author credibility | 10 | 5 | 10 | Microsoft education repository, MIT. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit and compatible dependency range. |
| C-07 | Maintenance activity | 5 | 5 | 5 | Updated within three days. |
|  | **Total** | **100** |  | **66** |  |

### Hard gates

- Triggered gates: none.
- Result: passes gates, context-only score band.
- Reviewer decision: `context-only`.

## Decision

- State: `context-only`
- Approved use: beginner explanations and discovery of lesson-scoped examples.
- Prohibited or unsafe use: API authority, production architecture or cross-framework API substitution.
- Topic-registry promotion proposal: none; use only as secondary context.
- Collection action: `none`
- Re-review trigger: dedicated MAF lesson gains tested, exact-version engineering artifacts.
- Residual risk: large translation/curriculum surface can lag package changes unevenly.
