# Topic routing

Use the narrowest matching topic ID. Query the generated catalog for exact entries and current counts.

| Topic ID | Use for |
| --- | --- |
| `getting-started` | basic agent construction, installation, first tool/session/workflow |
| `agents` | agent lifecycle, invocation, responses, structured output, composition |
| `tools` | function tools, MCP tools, dynamic tools, schemas, side effects |
| `sessions-context` | sessions, conversations, context providers, history, compaction |
| `memory-rag` | memory providers, vector/graph retrieval, RAG, embeddings |
| `middleware` | agent/function middleware, interception, exception handling, guardrails |
| `providers` | Foundry, Azure OpenAI, OpenAI, Anthropic, Bedrock, Ollama and other clients |
| `workflows` | executors, edges, graph construction, state and events |
| `orchestration` | sequential, concurrent, handoff, group chat, magentic patterns |
| `durability` | checkpoint, resume, replay, persistence, Durable Task/Agents |
| `approvals-hitl` | tool approval, human-in-the-loop, pause/resume, escalation |
| `observability` | OpenTelemetry, tracing, metrics, logging and diagnostics |
| `evaluation` | agent/workflow evals, datasets, graders, red teaming and benchmarks |
| `hosting` | local hosting, containers, Azure Functions, Foundry-hosted agents |
| `protocols` | MCP, A2A, AG-UI, ChatKit and integration contracts |
| `declarative` | YAML/JSON agents and workflows, schemas and loaders |
| `security` | identity, permissions, data boundaries, prompt injection and code execution |
| `migration` | AutoGen/Semantic Kernel migration, compatibility and upgrades |
| `devui` | DevUI discovery, registration, visualization and local debugging |

If a task spans topics, choose one primary topic and at most two supporting topics. Do not load every topic.
