# Source review: `repo-microsoft-claims-processing`

## Snapshot

- Source: `microsoft/claims-processing-hack`
- Canonical URL: https://github.com/microsoft/claims-processing-hack
- Source class: `official-repository`
- Owner/author: Microsoft organization; hack/workshop contributors.
- Reviewed commit, tag, or page date: commit `5327acd85e0b65e013ec470bef1f367ae18a459a` (2026-03-24); no release tag.
- Package/API coordinates: Python; unpinned prerelease `agent-framework-azure-ai` and `agent-framework-azure-ai-search` declarations; implementation primarily uses Azure AI Projects/Persistent Agents APIs directly.
- License: MIT.
- Reviewer and date: Codex, 2026-07-17.
- Policy version: `v1.1`
- Review track: `code-project`

## Direct Microsoft Agent Framework evidence

- Languages: Python, shell, notebooks, and container configuration.
- Package references/imports: root `requirements.txt` declares two MAF packages without versions. Repository-wide GitHub code search at the reviewed snapshot found the MAF term only in that dependency file; representative orchestration uses `AIProjectClient`, `DefaultAzureCredential`, and persistent-agent creation directly rather than MAF APIs.
- Relevant files: `requirements.txt`, `challenge-4/workflow_orchestrator.py`, `challenge-4/test_api_client.py`, `challenge-4/test_e2e.sh`, and `challenge-6/validation_workflow.py`.
- MAF topics demonstrated: none verifiably implemented. The claims scenario demonstrates Azure AI agent/resource orchestration, MCP, APIs, and human review concepts adjacent to MAF.
- Preview, experimental, deprecated, or provider-specific surfaces: Azure AI Projects/Persistent Agents and prerelease dependencies are provider-specific. There is no package pin to compare reliably with target revision `5ab8877ba55b4778d778cf51450eafe483194708`.

## Design and implementation value

- Reusable decisions: staged OCR, structuring, validation, orchestration, API wrapping, and a human review scenario form a useful domain decomposition.
- Sample shortcuts that must not be copied into production: agent provisioning occurs in the execution path, dependencies float, sample file paths/resources are assumed, and test scripts depend on live services.
- State and data flow: claim image to OCR to structured JSON to validation/review is clear, but persistence, replay, retention, and duplicate processing semantics are not complete.
- Tool and side-effect boundaries: agent creation, document access, MCP calls, and claim decisions are externally visible; authorization, approval, idempotency, and audit controls remain workshop-level.
- Failure, cancellation, retry, and concurrency behavior: logging and basic exceptions exist, but no systematic cancellation, retry taxonomy, timeout, compensation, or concurrency tests were verified.
- Security, identity, and data handling: `DefaultAzureCredential` is preferable to embedded secrets, but sensitive claim-data classification, least privilege, tenant isolation, deletion, and redaction are not specified.
- Observability and evaluation: logs and scenario validation exist; no stable eval data, threshold, or MAF regression gate exists.
- Hosting, deployment, and rollback: container material and API stages exist, but production health, migration, rollback, and scaling contracts are incomplete.

## Verification

- Commands documented by the source: challenge-specific Python/API/container commands requiring Azure provisioning and credentials.
- Checks reproduced locally: immutable commit, metadata, MIT license, tree, dependency declaration, orchestration, test scripts, and validation workflow inspected through GitHub API/raw immutable URLs.
- Test/eval coverage: manual API and end-to-end scripts exist; no repository GitHub Actions workflow or isolated MAF unit suite was found.
- Conflicts with local upstream source, tests, or Microsoft Learn: the source does not expose a concrete MAF API surface to map to target `5ab8877...`.
- Unverified claims: live claim processing, hosted agents, MCP, and human review are `not-run` due to cloud credentials/resources; static inspection is the substitute evidence.

## Evaluation under the approved policy

| ID | Dimension | Weight | Level (0–5) | Weighted score | Evidence |
| --- | --- | ---: | ---: | ---: | --- |
| C-01 | Design value | 25 | 3 | 15 | Useful domain staging, but not a reusable MAF composition. |
| C-02 | Testing and verification | 25 | 2 | 10 | Manual API/e2e checks without CI or isolated MAF assertions. |
| C-03 | Production depth | 20 | 2 | 8 | Real API/container seams, incomplete operational controls. |
| C-04 | Real MAF dependency | 10 | 1 | 2 | Dependency declarations only; no verified MAF API use. |
| C-05 | Source/author credibility | 10 | 5 | 10 | Microsoft-owned MIT repository. |
| C-06 | Version traceability | 5 | 3 | 3 | Commit pinned, MAF packages unpinned and prerelease. |
| C-07 | Maintenance activity | 5 | 4 | 4 | Recent 2026 repository activity. |
|  | **Total** | **100** |  | **52** |  |

### Hard gates

- Triggered gates: no verifiable direct MAF import or actual MAF API call.
- Result: reject regardless of score.
- Reviewer decision: `rejected` as a MAF coding reference; it may remain a discovery clue for Azure claims scenarios.

## Decision

- State: `rejected`
- Approved use: none in the curated MAF evidence layer.
- Prohibited or unsafe use: do not present Azure AI Projects/Persistent Agents calls as Microsoft Agent Framework APIs, and do not infer compatibility from unused dependency declarations.
- Topic-registry promotion proposal: none.
- Collection action: `none`
- Re-review trigger: repository adds direct, pinned MAF implementation and tests.
- Residual risk: product naming and adjacent Azure agent SDKs can cause framework misattribution.

## Re-review 2026-08-11

- The repository remains at `5327acd85e0b65e013ec470bef1f367ae18a459a` and now reports `archived: true`; MIT metadata is unchanged.
- No direct MAF import or API call appeared, so the original hard-gate failure still applies. Cloud and credential paths remain `not-run`.
- Decision unchanged: `rejected`. There was no active collection route to archive; the historical review is retained as the retirement record.
