# Source review: `official-blog-hub`

## Snapshot

- Source: Microsoft Agent Framework engineering blog index
- Canonical URL: https://devblogs.microsoft.com/agent-framework/
- Source class: `official-engineering`
- Owner/author: Microsoft Agent Framework team; individual posts have named authors.
- Reviewed page date: live index observed 2026-07-17; newest listed post dated 2026-07-15.
- Package/API coordinates: moving multi-version index, not one versioned technical artifact.
- License: no article-specific redistribution license verified.
- Reviewer and date: Codex, 2026-07-17; policy `v1.1`; track `technical-article`.

## Direct Microsoft Agent Framework evidence

- Languages: .NET and Python across linked posts.
- The page is an official discovery stream for releases, protocols, hosting, orchestration, skills and harness features.
- It contains summaries and links, but no self-contained dependencies, setup, runnable code or result for one demo.
- Version boundary: the index mixes preview-era and 1.x material. Every linked post must be reviewed independently against `microsoft/agent-framework@5ab8877ba55b4778d778cf51450eafe483194708`.

## Design and implementation value

- Reusable decision: use as a discovery feed and maintenance trigger only.
- It must not prove API correctness, maturity, production readiness, or cross-language parity.
- No test, failure, security, observability, deployment, or rollback contract exists at index level.

## Verification

- Live page title, ownership, dates, post summaries and archive were inspected.
- No runnable demo exists on the reviewed page; linked materials were not collapsed into this source's evidence.
- No cloud or model operation was run.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| A-01 | Real demo | 30 | 1 | 6 | Discovery summaries only. |
| A-02 | Design value | 25 | 2 | 10 | Broad routing value, no single design argument. |
| A-03 | Technical recency | 15 | 5 | Current release stream. |
| A-04 | Publication date | 15 | 5 | Live and recently updated. |
| A-05 | Source/author credibility | 15 | 5 | Official Microsoft team channel. |
|  | **Total** | **100** |  | **61** |  |

### Hard gates

- Triggered gates: real Demo level is below 3.
- Result: mandatory rejection despite official ownership.
- Reviewer decision: `rejected` as an evidence source; retain only as a discovery seed outside collection.

## Decision

- State: `rejected`
- Approved use: manual discovery of candidate primary sources and re-review triggers.
- Prohibited or unsafe use: API/design proof or collection routing.
- Topic-registry promotion proposal: none.
- Collection action: `none`
- Re-review trigger: index becomes a versioned, runnable engineering artifact (unlikely).
- Residual risk: moving content can silently change the visible summaries.

