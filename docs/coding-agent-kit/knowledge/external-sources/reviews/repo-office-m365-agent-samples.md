# Source review: `repo-office-m365-agent-samples`

## Snapshot

- Source: `OfficeDev/microsoft-365-agents-toolkit-samples`
- Canonical URL: https://github.com/OfficeDev/microsoft-365-agents-toolkit-samples
- Source class: `official-repository`
- Owner/author: Microsoft OfficeDev organization and sample contributors.
- Reviewed commit, tag, or page date: commit `31201f60982d6acf6fc4afa411eecccc6abae717` (2026-07-08); no repository release tag.
- Package/API coordinates: reviewed MAF scope is `ProxyAgent-CSharp/AzureAgentToM365ATK`; .NET with `Microsoft.Agents.AI`, AzureAI, and AzureAI.Persistent `1.0.0-preview.260108.1`, plus Microsoft 365 Agents SDK `1.3.176` and Azure persistent agents beta.
- License: repository MIT; the scoped sample also contains an MIT license.
- Reviewer and date: Codex, 2026-07-17.
- Policy version: `v1.1`
- Review track: `code-project`

## Direct Microsoft Agent Framework evidence

- Languages: C# for the reviewed MAF proxy; the wider repository is multi-language and mostly unrelated to MAF.
- Package references/imports: direct package pins and calls to `GetAIAgentAsync`, `AIAgent.RunStreamingAsync`, `AgentThread`, thread serialization, and Azure persistent-agent client APIs.
- Relevant files: `ProxyAgent-CSharp/AzureAgentToM365ATK/AzureAgentToM365ATK.csproj`, `Agents/AzureAgent.cs`, `Program.cs`, `AspNetExtensions.cs`, and paired M365 agent/deployment assets.
- MAF topics demonstrated: wrapping an existing Foundry agent for Microsoft 365, streaming responses, bridging conversation state to an MAF thread, authentication, and ASP.NET/M365 hosting.
- Preview, experimental, deprecated, or provider-specific surfaces: Azure AI Persistent and the reviewed MAF packages are preview/beta and tightly provider/M365-specific. Target revision `5ab8877ba55b4778d778cf51450eafe483194708` is newer; thread/session APIs require explicit migration review.

## Design and implementation value

- Reusable decisions: isolate the proxy adapter, retrieve an existing agent rather than reprovision per turn, stream output, and serialize framework thread state into host conversation state.
- Sample shortcuts that must not be copied into production: a single stored thread blob needs tenant/user size, corruption, migration, concurrency, retention, and privacy controls; credentials and agent IDs need startup validation.
- State and data flow: M365 activity becomes an MAF message, an existing persistent agent/thread is invoked, streaming updates return through the host, and serialized thread state is stored in conversation state.
- Tool and side-effect boundaries: agent tools execute behind a proxy; the sample does not prove end-to-end user authorization for every downstream tool or irreversible action.
- Failure, cancellation, retry, and concurrency behavior: cancellation is forwarded. Thread write races, transient retry/idempotency, partial streaming, duplicate turns, and state migration are not covered by focused tests.
- Security, identity, and data handling: M365 auth, `DefaultAzureCredential`, manifests, RBAC/deployment assets, and host state are substantive. Least privilege, OBO/user authorization, redaction, retention, and tenant isolation require deployment review.
- Observability and evaluation: host logging/CI exists, but no focused MAF eval dataset, quality threshold, or proxy telemetry contract was verified.
- Hosting, deployment, and rollback: local/Azure deployment assets, app registration, Bot OAuth, App Insights, App Service, and manifests are valuable; rollback and persisted-thread schema migration are incomplete.

## Verification

- Commands documented by the source: local/Azure M365 Agents Toolkit deployment and .NET launch requiring tenant, Azure, and Foundry configuration.
- Checks reproduced locally: immutable current snapshot, license, package pins, agent adapter, state serialization, deployment assets, and repository sample-validation CI inspected through GitHub API/raw immutable URLs.
- Test/eval coverage: repository CI validates samples/manifests/dependencies, but no focused unit/integration tests for the scoped MAF proxy/thread behavior were found.
- Conflicts with local upstream source, tests, or Microsoft Learn: preview persistent `AgentThread` usage must be re-mapped to the target revision's session/persistence contract; no drop-in compatibility claim is made.
- Unverified claims: tenant login, Azure deployment, Foundry agent, M365 client, OAuth, and streaming are `not-run` due to credentials/cloud resources. Static implementation/infra/CI evidence substitutes.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 4 | 20 | Valuable M365-to-MAF proxy and persisted conversation bridge. |
| C-02 | Testing and verification | 25 | 2 | 10 | Repository validation CI, no focused proxy/thread tests. |
| C-03 | Production depth | 20 | 4 | 16 | Auth, manifests, App Service/App Insights and deployment assets, with state gaps. |
| C-04 | Real MAF dependency | 10 | 5 | 10 | Exact packages and direct streaming/thread APIs. |
| C-05 | Source/author credibility | 10 | 5 | 10 | Microsoft OfficeDev, MIT. |
| C-06 | Version traceability | 5 | 5 | 5 | Immutable commit and exact preview coordinates. |
| C-07 | Maintenance activity | 5 | 5 | 5 | Active in July 2026. |
|  | **Total** | **100** |  | **76** |  |

### Hard gates

- Triggered gates: none.
- Result: pass, but below adoption threshold.
- Reviewer decision: `context-only` because focused verification and current-API mapping are insufficient.

## Decision

- State: `context-only`
- Approved use: design background for M365 proxy hosting, streaming, identity, and host-to-session state mapping; confirm every API in local target evidence.
- Prohibited or unsafe use: do not route as current API authority; do not copy external code; do not reuse thread persistence or authorization defaults without concurrency/security tests.
- Topic-registry promotion proposal: none; retain review as context for `protocols`, `hosting`, and `sessions-context`.
- Collection action: `link and annotation only`
- Re-review trigger: stable MAF packages, focused proxy/thread tests, or official canonicalization of this integration.
- Residual risk: the large multi-framework repository can cause unrelated samples to be attributed to MAF.
