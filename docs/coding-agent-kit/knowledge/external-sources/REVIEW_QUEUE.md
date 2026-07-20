# External source review queue

Snapshot: 2026-07-20. The machine-readable source of truth is [sources.json](sources.json).

## Inventory

- Total candidates: 65
- Reviewable sources in terminal states: 64
- Discovery-only meta indexes: 1
- Final states: 42 `adopted`, 5 `context-only`, 5 `quarantined`, 12 `rejected`, 1 `discovered`
- `queued`: 0; `in-review`: 0

All 64 reviewable sources have an independent review, evidence, a terminal decision, and a collection action.
Only `community-awesome-maf` remains `discovered`; it is a discovery-only meta index and is never promoted directly.

## Final review ledger

| Source | Class | State | Score | Immutable/page coordinate | Collection result |
| --- | --- | --- | ---: | --- | --- |
| [official-learn-hub](reviews/official-learn-hub.md) | `official-doc` | `adopted` | direct | 2026-07-17 | link and annotation only |
| [official-learn-overview](reviews/official-learn-overview.md) | `official-doc` | `adopted` | direct | 2026-07-17 | link and annotation only |
| [official-learn-get-started](reviews/official-learn-get-started.md) | `official-doc` | `adopted` | direct | 2026-07-17 | link and annotation only |
| [official-learn-agents](reviews/official-learn-agents.md) | `official-doc` | `adopted` | direct | 2026-07-17 | link and annotation only |
| [official-learn-tools](reviews/official-learn-tools.md) | `official-doc` | `adopted` | direct | 2026-07-17 | link and annotation only |
| [official-learn-conversations](reviews/official-learn-conversations.md) | `official-doc` | `adopted` | direct | 2026-07-17 | link and annotation only |
| [official-learn-middleware](reviews/official-learn-middleware.md) | `official-doc` | `adopted` | direct | 2026-07-17 | link and annotation only |
| [official-learn-rag](reviews/official-learn-rag.md) | `official-doc` | `adopted` | direct | 2026-07-17 | link and annotation only |
| [official-learn-observability](reviews/official-learn-observability.md) | `official-doc` | `adopted` | direct | 2026-07-17 | link and annotation only |
| [official-learn-evaluation](reviews/official-learn-evaluation.md) | `official-doc` | `adopted` | direct | 2026-07-17 | link and annotation only |
| [official-learn-security](reviews/official-learn-security.md) | `official-doc` | `adopted` | direct | 2026-07-17 | link and annotation only |
| [official-learn-workflows](reviews/official-learn-workflows.md) | `official-doc` | `adopted` | direct | 2026-07-17 | link and annotation only |
| [official-learn-workflow-builder](reviews/official-learn-workflow-builder.md) | `official-doc` | `adopted` | direct | 2026-07-17 | link and annotation only |
| [official-learn-functional-workflow](reviews/official-learn-functional-workflow.md) | `official-doc` | `adopted` | direct | 2026-07-17 | link and annotation only |
| [official-learn-declarative-workflows](reviews/official-learn-declarative-workflows.md) | `official-doc` | `adopted` | direct | 2026-07-17 | link and annotation only |
| [official-learn-integrations](reviews/official-learn-integrations.md) | `official-doc` | `adopted` | direct | 2026-07-17 | link and annotation only |
| [official-learn-a2a](reviews/official-learn-a2a.md) | `official-doc` | `adopted` | direct | 2026-07-17 | link and annotation only |
| [official-learn-agui](reviews/official-learn-agui.md) | `official-doc` | `adopted` | direct | 2026-07-17 | link and annotation only |
| [official-learn-durable-extension](reviews/official-learn-durable-extension.md) | `official-doc` | `adopted` | direct | 2026-07-17 | link and annotation only |
| [official-learn-migration-autogen](reviews/official-learn-migration-autogen.md) | `official-doc` | `adopted` | direct | 2026-07-17 | link and annotation only |
| [official-learn-migration-sk](reviews/official-learn-migration-sk.md) | `official-doc` | `adopted` | direct | 2026-07-17 | link and annotation only |
| [official-dotnet-api](reviews/official-dotnet-api.md) | `official-doc` | `adopted` | direct | 2026-07-17 | link and annotation only |
| [official-python-api](reviews/official-python-api.md) | `official-doc` | `adopted` | direct | 2026-07-17 | link and annotation only |
| [official-blog-hub](reviews/official-blog-hub.md) | `official-engineering` | `rejected` | 61 | 2026-07-17 | none |
| [official-blog-introduction](reviews/official-blog-introduction.md) | `official-engineering` | `adopted` | 80 | 2026-07-17 | link and annotation only |
| [official-blog-durable-workflows](reviews/official-blog-durable-workflows.md) | `official-engineering` | `adopted` | 100 | 2026-07-17 | link and annotation only |
| [official-blog-orchestration-1](reviews/official-blog-orchestration-1.md) | `official-engineering` | `adopted` | 100 | 2026-07-17 | link and annotation only |
| [official-blog-hosted-agents](reviews/official-blog-hosted-agents.md) | `official-engineering` | `adopted` | 100 | 2026-07-17 | link and annotation only |
| [official-blog-a2a-v1](reviews/official-blog-a2a-v1.md) | `official-engineering` | `adopted` | 100 | 2026-07-17 | link and annotation only |
| [official-community-python-series](reviews/official-community-python-series.md) | `official-engineering` | `adopted` | 95 | 2026-07-17 | link and annotation only |
| [repo-microsoft-agent-framework](reviews/repo-microsoft-agent-framework.md) | `official-repository` | `adopted` | 100 | `5ab8877ba55b4778d778cf51450eafe483194708` | project route |
| [repo-microsoft-agent-framework-samples](reviews/repo-microsoft-agent-framework-samples.md) | `official-repository` | `quarantined` | 58 | `5b854b7e1c3838f17f41bcf2412ef79d7662db37` | none |
| [repo-microsoft-ai-agents-beginners](reviews/repo-microsoft-ai-agents-beginners.md) | `official-repository` | `context-only` | 66 | `ad068048e785ecc3f05d663e7c4ba18a55e72972` | none |
| [repo-azure-interview-coach](reviews/repo-azure-interview-coach.md) | `official-repository` | `adopted` | 86 | `d9557897274996c2d0f869bfafe0aba7e53393c0` | project route |
| [repo-azure-travel-agents](reviews/repo-azure-travel-agents.md) | `official-repository` | `adopted` | 94 | `a66e229c4bd4aeb4eb9b9460e2ec6d1701f142c1` | project route |
| [repo-azure-multi-agent-workshop](reviews/repo-azure-multi-agent-workshop.md) | `official-repository` | `quarantined` | 61 | `4095e86d52e644e691ee19d0076741104dd8111c` | none |
| [repo-azure-maf-workshop-ko](reviews/repo-azure-maf-workshop-ko.md) | `official-repository` | `quarantined` | 57 | `8c79b3c6552e5271f80e834e28cf40565e93d4f1` | none |
| [repo-microsoft-azure-trust-agents](reviews/repo-microsoft-azure-trust-agents.md) | `official-repository` | `rejected` | 60 | `55b1641b640195b1a45640214f30294cc0d973c9` | none |
| [repo-microsoft-claims-processing](reviews/repo-microsoft-claims-processing.md) | `official-repository` | `rejected` | 52 | `5327acd85e0b65e013ec470bef1f367ae18a459a` | none |
| [repo-microsoft-spec-to-agents](reviews/repo-microsoft-spec-to-agents.md) | `official-repository` | `adopted` | 85 | `f40268fa5573ce42a6403eb0edb48997eb24532a` | project route |
| [repo-microsoft-agent-governance-toolkit](reviews/repo-microsoft-agent-governance-toolkit.md) | `official-repository` | `adopted` | 96 | `d00ccdbf31258db917495ca65fa2ecd9e64461b9` | project route |
| [repo-dotnet-docs-maui](reviews/repo-dotnet-docs-maui.md) | `official-repository` | `rejected` | 47 | `e75fa6a805d14c89b18a8a51199e05a007082b41` | none |
| [repo-office-m365-agent-samples](reviews/repo-office-m365-agent-samples.md) | `official-repository` | `context-only` | 76 | `31201f60982d6acf6fc4afa411eecccc6abae717` | link and annotation only |
| [repo-eshoplite](reviews/repo-eshoplite.md) | `official-repository` | `context-only` | 74 | `f6349114992b233daf92c0ff7ccba0e151e1deff` | link and annotation only |
| `community-awesome-maf` | `meta-index` | `discovered` | n/a | discovery only | discovery only |
| [community-rwjdk-samples](reviews/community-rwjdk-samples.md) | `community-repository` | `context-only` | 66 | `b6f2234323ebd714248c71bd82b0380a4db4f241` | link and annotation only |
| [community-maf-getting-started](reviews/community-maf-getting-started.md) | `community-repository` | `quarantined` | 60 | `f38e4378d404e8be2d1a28aad8e9e9d254721c4e` | none |
| [community-taskagent](reviews/community-taskagent.md) | `community-repository` | `adopted` | 91 | `4a998448f6b173b366f36a9512ea77c9c355e341` | project route |
| [community-agent-base](reviews/community-agent-base.md) | `community-repository` | `adopted` | 87 | `13733a71c1736ab87c02802118320583db866ef4` | project route |
| [community-conference-assistant](reviews/community-conference-assistant.md) | `community-repository` | `adopted` | 88 | `f1042022a7e3b680768e8292053e286600cf5a86` | project route |
| [community-opendeepwiki](reviews/community-opendeepwiki.md) | `community-repository` | `adopted` | 93 | `2940a6eb5e90447d57273883330c48b05ab8dfdd` | project route |
| [community-agenteval](reviews/community-agenteval.md) | `community-repository` | `adopted` | 100 | `404ee133c7ba7e1c6b7f3460f52efc40c7ebde83` | project route |
| [community-opik](reviews/community-opik.md) | `community-repository` | `adopted` | 86 | `9e207b4693948fd276e659098195155f490a3785` | project route |
| [community-zep](reviews/community-zep.md) | `community-repository` | `adopted` | 100 | `175dd66e0254085ef6347b5763addb19e777611f` | project route |
| [community-engram](reviews/community-engram.md) | `community-repository` | `quarantined` | 60 | `0504f9f5a895eaec798e481758f9dc0fbea0c8b8` | none |
| [community-sideseat](reviews/community-sideseat.md) | `community-repository` | `context-only` | 67 | `c40efef761da8af0e63dc5103afd1e0f01d0cc18` | link and annotation only |
| [community-a2a-travel](reviews/community-a2a-travel.md) | `community-repository` | `rejected` | 85 | `61bbe36cc8ef4433b4715ccf8147c74a3f8d04bb` | none |
| [community-graphrag-neo4j](reviews/community-graphrag-neo4j.md) | `community-repository` | `rejected` | 48 | `c29e6590ff257ba41137c5129b2f91ecc908a7e4` | none |
| [community-agui-template](reviews/community-agui-template.md) | `community-repository` | `rejected` | 79 | `8da9c9e8e219eb510f633297efc63a7f127aac29` | none |
| [community-maf-boilerplate](reviews/community-maf-boilerplate.md) | `community-repository` | `rejected` | 77 | `5b21471e7765bf9207c737dc5ea955a262766f9e` | none |
| [community-visual-guide](reviews/community-visual-guide.md) | `community-repository` | `rejected` | 52 | `aef1d4009ee3d3e4bc6cc00562568d6bc1e66447` | none |
| [community-maf-workshop](reviews/community-maf-workshop.md) | `community-repository` | `rejected` | 50 | `4e9467066cac049d82bf88db0e26fb3754b8ba17` | none |
| [community-copilot-learning](reviews/community-copilot-learning.md) | `community-repository` | `rejected` | 48 | `ce82bc9125ad1bdf2ee5f67550347dbe873be00f` | none |
| [community-loop-engineering](reviews/community-loop-engineering.md) | `community-repository` | `rejected` | 42 | `ee451db4c8b8786ed297946a679d6904e7a816b5` | none |
| [community-awesome-article-content-strategy](reviews/community-awesome-article-content-strategy.md) | `community-article` | `adopted` | 92 | 2026-07-17 | link and annotation only |

## Collection summary

- 12 adopted repositories are stored as URL-only project routes at immutable reviewed commits. No external project code is copied.
- 30 adopted documents/articles are stored as URL plus original annotation in `collection/link-references.json` because redistribution permission for their bodies was not verified.
- 0 external document bodies are retained; `collection/documents.json` is intentionally empty.
- 22 non-adopted sources have no collection entry. Four context-only repository reviews retain a link-only *review action* for context, but policy correctly excludes them from collection.
- The meta-index remains discovery-only.

## Completion gate

This queue is closed only while all of the following remain true:

- every reviewable source remains in a terminal state and has a matching independent review;
- registry state, score, reviewed coordinate, and collection action match the review;
- every adopted source has exactly one project route, link reference, or legally retained document;
- project routes contain no copied code, and retained documents require verified redistribution metadata and hashes;
- `collect.py check`, representative lookup queries, maintenance checks, and the kit validator pass.
