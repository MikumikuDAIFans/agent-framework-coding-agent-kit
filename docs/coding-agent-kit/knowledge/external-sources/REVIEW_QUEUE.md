# External source review queue

Snapshot: 2026-07-15. The machine-readable source of truth is [sources.json](sources.json).

## Inventory

- Total candidates: 65
- Official documentation: 23
- Official engineering articles: 7
- Official repositories: 14
- Community repositories: 19
- Community articles: 1
- Discovery-only meta indexes: 1
- Current states: 64 `queued`, 0 adopted, 1 context-only, 0 quarantined, 0 rejected

Search breadth is not an endorsement. Until an individual review is committed, every item remains
quarantined from the generated topic catalog and must not be cited as API truth.

## Active review

- Next source: `official-learn-overview`
- Reason: it defines the canonical framework scope, agents-versus-workflows boundary, maturity, and
  third-party integration risk that later reviews must use as their conceptual baseline.
- Review artifact: `reviews/official-learn-overview.md`
- State: `queued`

Only one source is `in-review` at a time unless maintainers explicitly split reviews by non-overlapping
language or topic.

## Ordered batches

### Batch A — canonical truth and maturity

1. `repo-microsoft-agent-framework-samples` — `context-only`, reviewed 2026-07-15
2. `official-learn-overview`
3. `official-learn-agents`
4. `official-learn-tools`
5. `official-learn-conversations`
6. `official-learn-workflows`
7. `official-learn-observability`
8. `official-learn-evaluation`
9. `official-learn-security`
10. `official-blog-orchestration-1`
11. `official-dotnet-api`
12. `official-python-api`

### Batch B — official end-to-end and production cases

1. `repo-azure-interview-coach`
2. `repo-azure-multi-agent-workshop`
3. `official-blog-durable-workflows`
4. `official-blog-hosted-agents`
5. `official-learn-durable-extension`
6. `repo-microsoft-spec-to-agents`
7. `repo-microsoft-azure-trust-agents`
8. `repo-microsoft-claims-processing`
9. `repo-azure-travel-agents`
10. `repo-microsoft-agent-governance-toolkit`
11. `official-blog-a2a-v1`
12. `official-learn-agui`

### Batch C — strongest community implementation candidates

1. `community-rwjdk-samples`
2. `community-taskagent`
3. `community-agent-base`
4. `community-engram`
5. `community-a2a-travel`
6. `community-graphrag-neo4j`
7. `community-agui-template`
8. `community-conference-assistant`
9. `community-agenteval`
10. `community-opendeepwiki`

### Batch D — focused integrations and teaching material

1. `community-awesome-maf`
2. `official-community-python-series`
3. `community-awesome-article-content-strategy`
4. `official-learn-functional-workflow`
5. `official-learn-declarative-workflows`
6. `official-learn-a2a`
7. `official-learn-rag`
8. `community-sideseat`
9. `community-opik`
10. `community-zep`
11. `community-maf-getting-started`
12. `community-maf-boilerplate`
13. `community-visual-guide`
14. `community-maf-workshop`
15. `community-copilot-learning`
16. `community-loop-engineering`

### Batch E — remaining breadth and narrow-scope sources

Review all remaining `queued` entries in `sources.json`, preserving registry order. These include the
documentation hubs, migration guides, beginner curricula, localized workshop, M365/MAUI/eShop examples,
and introduction-era articles. They remain useful for coverage, but the earlier batches are more likely
to produce high-value code/design evidence.

## Per-source completion gate

A queue item is complete only when:

- the review names an immutable commit/tag or page date;
- direct MAF imports/package references and relevant files are recorded;
- the demonstrated API is checked against the local upstream revision and current official docs;
- license and attribution are explicit;
- sample shortcuts and production gaps are identified;
- all eight score dimensions contain evidence;
- the decision and approved-use boundary are explicit;
- `sources.json` and this queue agree on the resulting state;
- any proposed promotion to `topics.json` is a separate, reviewable change.
