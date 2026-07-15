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
- Current states: 63 `queued`, 1 `in-review`, 1 `discovered`, 0 adopted, 0 context-only,
  0 quarantined, 0 rejected

Search breadth is not an endorsement. Until an individual review is committed, every item remains
quarantined from the generated topic catalog and must not be cited as API truth.

## Active review

- Policy `v1.1` is approved and effective. Coding agents may complete reviews, decisions, and collection.
- `repo-microsoft-agent-framework-samples` remains the only active source. Its factual investigation is
  preserved and must now be evaluated with the project/code rubric and hard gates.
- `official-learn-overview` is next and will use the official-document direct-adoption check.

Reviews may be batched by source class or topic when evidence remains independently traceable. Each source
still receives its own review file and state decision.

## Ordered batches

### Batch A — canonical truth and maturity

1. `repo-microsoft-agent-framework-samples` — `in-review`, factual investigation recorded 2026-07-15;
   final evaluation pending application of policy v1.1
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

1. `official-community-python-series`
2. `community-awesome-article-content-strategy`
3. `official-learn-functional-workflow`
4. `official-learn-declarative-workflows`
5. `official-learn-a2a`
6. `official-learn-rag`
7. `community-sideseat`
8. `community-opik`
9. `community-zep`
10. `community-maf-getting-started`
11. `community-maf-boilerplate`
12. `community-visual-guide`
13. `community-maf-workshop`
14. `community-copilot-learning`
15. `community-loop-engineering`

`community-awesome-maf` remains `discovered` as a discovery-only meta index. Its linked primary sources
may enter the queue independently, but the list itself is not reviewed or promoted.

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
- every evidence requirement and evaluation field defined by the approved policy is complete;
- the decision, authority, and approved-use boundary satisfy the approved policy;
- `sources.json` and this queue agree on the resulting state;
- the adopted source has a collection action: project route, retained Markdown, or link/annotation only;
- project routes contain no copied code, and retained documents have verified redistribution metadata;
- collection manifests and the generated knowledge index pass `collect.py check`.
