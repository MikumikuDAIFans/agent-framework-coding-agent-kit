# External source review queue

Snapshot: 2026-08-11. The machine-readable source of truth is [sources.json](sources.json).

## Inventory

- Total candidates: 74
- Reviewable sources in terminal states: 73
- Discovery-only meta indexes: 1
- Final states: 46 `adopted`, 6 `context-only`, 8 `quarantined`, 13 `rejected`, 1 `discovered`
- `queued`: 0; `in-review`: 0

All 73 reviewable sources have an independent review, evidence, a terminal decision, and a collection action.
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
| [official-community-python-series](reviews/official-community-python-series.md) | `official-engineering` | `adopted` | 95 | 2026-08-11 | link and annotation only |
| [repo-microsoft-agent-framework](reviews/repo-microsoft-agent-framework.md) | `official-repository` | `adopted` | 100 | `d0a4165f170193ba1d026a259af40d35bb7eaefe` | project route |
| [repo-microsoft-agent-framework-samples](reviews/repo-microsoft-agent-framework-samples.md) | `official-repository` | `quarantined` | 58 | `5b854b7e1c3838f17f41bcf2412ef79d7662db37` | none |
| [repo-microsoft-ai-agents-beginners](reviews/repo-microsoft-ai-agents-beginners.md) | `official-repository` | `context-only` | 66 | `15ad10ca60577b75199c1ba828887ab7e66bac87` | none |
| [repo-azure-interview-coach](reviews/repo-azure-interview-coach.md) | `official-repository` | `adopted` | 86 | `d9557897274996c2d0f869bfafe0aba7e53393c0` | project route |
| [repo-azure-travel-agents](reviews/repo-azure-travel-agents.md) | `official-repository` | `adopted` | 94 | `a66e229c4bd4aeb4eb9b9460e2ec6d1701f142c1` | project route |
| [repo-azure-multi-agent-workshop](reviews/repo-azure-multi-agent-workshop.md) | `official-repository` | `quarantined` | 61 | `4095e86d52e644e691ee19d0076741104dd8111c` | none |
| [repo-azure-maf-workshop-ko](reviews/repo-azure-maf-workshop-ko.md) | `official-repository` | `quarantined` | 57 | `8c79b3c6552e5271f80e834e28cf40565e93d4f1` | none |
| [repo-microsoft-azure-trust-agents](reviews/repo-microsoft-azure-trust-agents.md) | `official-repository` | `rejected` | 60 | `55b1641b640195b1a45640214f30294cc0d973c9` | none |
| [repo-microsoft-claims-processing](reviews/repo-microsoft-claims-processing.md) | `official-repository` | `rejected` | 52 | `5327acd85e0b65e013ec470bef1f367ae18a459a` | none |
| [repo-microsoft-spec-to-agents](reviews/repo-microsoft-spec-to-agents.md) | `official-repository` | `adopted` | 85 | `f40268fa5573ce42a6403eb0edb48997eb24532a` | project route |
| [repo-microsoft-agent-governance-toolkit](reviews/repo-microsoft-agent-governance-toolkit.md) | `official-repository` | `adopted` | 96 | `81955d48025c6b11deb3fc9dabf89f74f4145775` | project route |
| [repo-dotnet-docs-maui](reviews/repo-dotnet-docs-maui.md) | `official-repository` | `rejected` | 47 | `193868ac9559ce4a06f81fa2f82f03dcee61b4bd` | none |
| [repo-office-m365-agent-samples](reviews/repo-office-m365-agent-samples.md) | `official-repository` | `context-only` | 76 | `7913e8753f423f1f39539ae676f985d66b7b9e41` | link and annotation only |
| [repo-eshoplite](reviews/repo-eshoplite.md) | `official-repository` | `context-only` | 74 | `f6349114992b233daf92c0ff7ccba0e151e1deff` | link and annotation only |
| `community-awesome-maf` | `meta-index` | `discovered` | n/a | discovery only | discovery only |
| [community-rwjdk-samples](reviews/community-rwjdk-samples.md) | `community-repository` | `context-only` | 66 | `a9dc5aa4f06b6eebc3728e8267546642c807177f` | link and annotation only |
| [community-maf-getting-started](reviews/community-maf-getting-started.md) | `community-repository` | `quarantined` | 60 | `f38e4378d404e8be2d1a28aad8e9e9d254721c4e` | none |
| [community-taskagent](reviews/community-taskagent.md) | `community-repository` | `adopted` | 91 | `4a998448f6b173b366f36a9512ea77c9c355e341` | project route |
| [community-agent-base](reviews/community-agent-base.md) | `community-repository` | `adopted` | 87 | `13733a71c1736ab87c02802118320583db866ef4` | project route |
| [community-conference-assistant](reviews/community-conference-assistant.md) | `community-repository` | `adopted` | 88 | `f1042022a7e3b680768e8292053e286600cf5a86` | project route |
| [community-opendeepwiki](reviews/community-opendeepwiki.md) | `community-repository` | `adopted` | 93 | `a71a441a017bb3b8d1a0064afbdf22a3ad9d5383` | project route |
| [community-agenteval](reviews/community-agenteval.md) | `community-repository` | `adopted` | 100 | `3d1643f39c69bbfefb58a555e2e048261ae8bc99` | project route |
| [community-opik](reviews/community-opik.md) | `community-repository` | `adopted` | 86 | `bcbbf44ed5062023ecd3da0068178f4bca5147c1` | project route |
| [community-zep](reviews/community-zep.md) | `community-repository` | `adopted` | 100 | `ba4fc3cc5b00cda7dde63833007467ffd6cba3a8` | project route |
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
| [community-awesome-article-content-strategy](reviews/community-awesome-article-content-strategy.md) | `community-article` | `adopted` | 92 | 2026-08-11 | link and annotation only |
| [repo-microsoft-agent-framework-go](reviews/repo-microsoft-agent-framework-go.md) | `official-repository` | `adopted` | 100 | `206863eab447fe89787a9be123c19967b3066a09` | project route |
| [repo-microsoft-agent-framework-durable-extension](reviews/repo-microsoft-agent-framework-durable-extension.md) | `official-repository` | `adopted` | 100 | `ad941eff53617840c0a046498be36d0b3871329b` | project route |
| [repo-microsoft-skills](reviews/repo-microsoft-skills.md) | `official-repository` | `context-only` | 78 | `849ffefb22c133c1e8c6a282a3ded018cb9c4ad7` | none |
| [repo-azure-functions-agents-runtime](reviews/repo-azure-functions-agents-runtime.md) | `official-repository` | `quarantined` | 84 | `cc5e14ccda96bfd8ebc3197d33a5730b6cc89762` | none |
| [repo-azure-legacy-modernization-agents](reviews/repo-azure-legacy-modernization-agents.md) | `official-repository` | `rejected` | 65 | `3511138b890cb5b385ef417b2092018cb82263aa` | none |
| [community-rwjdk-agent-framework-toolkit](reviews/community-rwjdk-agent-framework-toolkit.md) | `community-repository` | `adopted` | 89 | `9cc6f1bfd3e78b93e2ab8d98006ec0184fbd26dd` | project route |
| [community-temporal-dotnet-agents](reviews/community-temporal-dotnet-agents.md) | `community-repository` | `adopted` | 98 | `4a98f2b14eccccaf3cc2c96a64ea178050d536b9` | project route |
| [community-sokolaidev-maf-extensions](reviews/community-sokolaidev-maf-extensions.md) | `community-repository` | `quarantined` | 76 | `e328dafe513047e6d68de9542754562dff9e3601` | none |
| [community-agent-assembly-python-sdk](reviews/community-agent-assembly-python-sdk.md) | `community-repository` | `quarantined` | 81 | `72a9d7d30b1724438968ff5c1399e90124d0701a` | none |

## Collection summary

- 16 adopted repositories are stored as URL-only project routes at immutable reviewed commits. No external project code is copied.
- 30 adopted documents/articles are stored as URL plus original annotation in `collection/link-references.json` because redistribution permission for their bodies was not verified.
- 0 external document bodies are retained; `collection/documents.json` is intentionally empty.
- 27 non-adopted reviewable sources have no collection entry. Context-only repository reviews may retain a link-only *review action* in their review metadata, but policy correctly excludes them from collection.
- The meta-index remains discovery-only.

## Completion gate

This queue is closed only while all of the following remain true:

- every reviewable source remains in a terminal state and has a matching independent review;
- registry state, score, reviewed coordinate, and collection action match the review;
- every adopted source has exactly one project route, link reference, or legally retained document;
- project routes contain no copied code, and retained documents require verified redistribution metadata and hashes;
- `collect.py check`, representative lookup queries, maintenance checks, and the kit validator pass.
