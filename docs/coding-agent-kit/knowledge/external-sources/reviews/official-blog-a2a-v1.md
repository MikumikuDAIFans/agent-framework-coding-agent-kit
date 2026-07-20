# Source review: `official-blog-a2a-v1`

## Snapshot

- Source: A2A v1 Is Here: Cross-Platform Agent Communication in Microsoft Agent Framework for .NET
- Canonical URL: https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/
- Source class: `official-engineering`; author: Sergey Menshykh, Principal Software Engineer, Microsoft.
- Reviewed page date: 2026-04-28.
- Package/API coordinates: A2A protocol v1.0; Agent Framework .NET A2A client/hosting packages still preview.
- License: no article-specific redistribution license verified.
- Reviewer and date: Codex, 2026-07-17; policy `v1.1`; track `technical-article`.

## Direct Microsoft Agent Framework evidence

- Languages: C#.
- Complete client/hosting examples cover `A2ACardResolver`, `GetAIAgentAsync`, binding preference, streaming, `AddA2AServer`, `MapA2AHttpJson` and well-known Agent Cards.
- Target-boundary check: these identifiers occur in A2A implementation, samples and tests at target revision `5ab8877ba55b4778d778cf51450eafe483194708`.
- The stable protocol must not be confused with preview SDK/package maturity.

## Design and implementation value

- Reusable: wrap a remote endpoint behind `AIAgent`; keep discovery, server registration, transport mapping and Agent Card publication explicit; select bindings deliberately.
- Security notes such as signed cards/multitenancy are protocol capabilities, not an application authorization implementation.
- Sample endpoints omit production authentication policy, SSRF/egress controls for discovery, tenant isolation, retry/backpressure, card trust validation and audit/redaction.

## Verification

- Date, author, examples, migration note and preview statement inspected.
- All material MAF symbols mapped to target source/samples through official repository code search.
- No remote agent or cloud model was contacted.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| A-01 | Real demo | 30 | 5 | 30 | Client, streaming, hosting and multi-agent snippets. |
| A-02 | Design value | 25 | 5 | 25 | Clear interop and protocol boundary decomposition. |
| A-03 | Technical recency | 15 | 5 | v1 APIs map to target code. |
| A-04 | Publication date | 15 | 5 | Recent 2026 article. |
| A-05 | Source/author credibility | 15 | 5 | Official framework engineer. |
|  | **Total** | **100** |  | **100** |  |

### Hard gates

- Triggered gates: none.
- Result: passes with mandatory preview-package boundary.
- Reviewer decision: `adopted`.

## Decision

- State: `adopted`
- Approved use: A2A v1 client/host design route paired with local source/tests.
- Prohibited or unsafe use: assuming protocol stability implies SDK GA or trusting arbitrary cards/endpoints.
- Topic-registry promotion proposal: `protocols`, `hosting`.
- Collection action: `link and annotation only`
- Re-review trigger: A2A package GA/breaking change, protocol revision, or security guidance change.
- Residual risk: external endpoint trust and transport policy are application concerns.

