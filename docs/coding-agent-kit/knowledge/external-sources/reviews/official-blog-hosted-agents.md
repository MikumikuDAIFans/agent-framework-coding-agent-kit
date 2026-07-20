# Source review: `official-blog-hosted-agents`

## Snapshot

- Source: From Local to Production: Deploy Your Microsoft Agent Framework Agent with Foundry Hosted Agents
- Canonical URL: https://devblogs.microsoft.com/agent-framework/from-local-to-production-deploy-your-microsoft-agent-framework-agent-with-foundry-hosted-agents/
- Source class: `official-engineering`; authors: Tao Chen and Shawn Henry, Microsoft.
- Reviewed page date: 2026-05-06.
- Package/API coordinates: .NET Foundry hosting and Python Foundry hosting; Responses/Invocations protocols; hosted integration stated not yet GA.
- License: no article-specific redistribution license verified.
- Reviewer and date: Codex, 2026-07-17; policy `v1.1`; track `technical-article`.

## Direct Microsoft Agent Framework evidence

- Languages: C# and Python.
- Article gives minimal host code (`AddFoundryResponses`/`MapFoundryResponses`, `ResponsesHostServer`) and links detailed official samples for both languages.
- Target-boundary check: both identifiers occur in official implementation and hosted samples at `5ab8877ba55b4778d778cf51450eafe483194708`.
- Preview boundary: article explicitly says Foundry Hosted Agent/MAF integration is progressing toward GA.

## Design and implementation value

- Reusable: container/runtime separation, Entra workload identity, per-session isolation, versioned immutable deployments, weighted rollout/rollback, scale-to-zero, persistent session filesystem and injected telemetry.
- Protocol selection between conversational Responses and generic Invocations is a useful contract boundary.
- Limits: platform claims, retention windows, network controls and economics are service facts that can drift; application authorization, idempotency, data classification and evaluation gates remain the developer's responsibility.

## Verification

- Page, authors, date, code, linked samples and explicit preview statement inspected.
- Both host API names mapped to target repository source/samples.
- Deployment was not run: it requires Azure credentials, billable resources and externally visible changes.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| A-01 | Real demo | 30 | 5 | 30 | Both-language host code and detailed sample routes. |
| A-02 | Design value | 25 | 5 | 25 | Identity, state, protocol and rollout boundaries. |
| A-03 | Technical recency | 15 | 5 | APIs map to target; preview stated. |
| A-04 | Publication date | 15 | 5 | Recent 2026 article. |
| A-05 | Source/author credibility | 15 | 5 | Official engineering/product authors. |
|  | **Total** | **100** |  | **100** |  |

### Hard gates

- Triggered gates: none.
- Result: passes with preview/service-drift annotation.
- Reviewer decision: `adopted`.

## Decision

- State: `adopted`
- Approved use: hosting architecture and route to exact-version samples/docs.
- Prohibited or unsafe use: treating preview integration or service limits as permanent; deploying without identity/network/cost review.
- Topic-registry promotion proposal: `hosting`, `providers`, `observability`.
- Collection action: `link and annotation only`
- Re-review trigger: hosting GA, protocol/service contract change, or 12 months.
- Residual risk: service behavior can change independently of the SDK commit.

