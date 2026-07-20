# Source review: `official-community-python-series`

## Snapshot

- Source: Learn how to build agents and workflows in Python
- Canonical URL: https://techcommunity.microsoft.com/blog/azuredevcommunityblog/learn-how-to-build-agents-and-workflows-in-python/4502144
- Source class: `official-engineering`; author: Pamela Fox, Microsoft.
- Reviewed page date: 2026-03-18.
- Package/API coordinates: Python MAF 1.x learning series; six sessions, linked `python-agentframework-demos` code, slides and recordings.
- License: no article-specific redistribution license verified; linked repository license/revision must be audited independently.
- Reviewer and date: Codex, 2026-07-17; policy `v1.1`; track `technical-article`.

## Direct Microsoft Agent Framework evidence

- Languages: Python.
- Series routes to runnable open-source demos covering tools, MCP, agents-as-tools, context/memory, OpenTelemetry/evaluation, conditional/structured workflows, orchestration, approvals and checkpoints.
- The page provides dated session descriptions and code repository links, but does not pin one immutable demo commit or package lock.
- Target boundary: topics and core Python 1.x packages align with target `5ab8877ba55b4778d778cf51450eafe483194708`; each linked demo still needs its own revision/dependency check before copying a symbol.

## Design and implementation value

- Reusable: coherent learning route from one agent through state, observability/evaluation and HITL workflows; demos connect explanation to code.
- Limits: livestream/course material is not a production contract; memory providers, model clients and evaluation SDK add provider/version boundaries.
- Failure, cancellation, retry, concurrency, identity, retention, deployment and rollback are uneven across separate sessions.

## Verification

- Search-indexed page content, author/date, six-part scope and code/slides/recording links were inspected.
- No linked cloud demo was run; immutable commit and exact dependency lock for the separate demo repository remain unverified in this article review.
- No article body may be retained without redistribution evidence.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| A-01 | Real demo | 30 | 5 | 30 | Each session links open-source runnable examples. |
| A-02 | Design value | 25 | 4 | 20 | Strong staged coverage; production contracts uneven. |
| A-03 | Technical recency | 15 | 4 | Current 1.x themes; demo commit not pinned here. |
| A-04 | Publication date | 15 | 5 | Recent 2026 series. |
| A-05 | Source/author credibility | 15 | 5 | Named Microsoft Python educator/engineer channel. |
|  | **Total** | **100** |  | **95** |  |

### Hard gates

- Triggered gates: none; page date is a valid article version coordinate.
- Result: passes.
- Reviewer decision: `adopted` as a learning route, not code authority.

## Decision

- State: `adopted`
- Approved use: topic-oriented learning route and discovery of separately pinned demos.
- Prohibited or unsafe use: treating recordings/slides as API proof or using unpinned demo code in production.
- Topic-registry promotion proposal: `getting-started`, `agents`, `workflows`, `approvals-hitl`, `evaluation`.
- Collection action: `link and annotation only`
- Re-review trigger: 12 months, link/package drift, or linked repository review finds incompatible APIs.
- Residual risk: a moving linked repository may no longer reproduce the recorded sessions.
