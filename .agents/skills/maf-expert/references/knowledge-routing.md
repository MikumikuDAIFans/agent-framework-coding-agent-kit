# Knowledge routing

Store a durable discovery at the narrowest source of truth.

| Discovery | Destination |
| --- | --- |
| Target application's architecture or decision | That project's architecture docs or ADRs |
| Reusable MAF topic route or important reference entry | `tools/coding-agent-kit/indexer/topics.json` |
| Index generation behavior | `tools/coding-agent-kit/indexer` tests and documentation |
| Upstream API defect or missing framework test | Upstream code/test change in the applicable subtree |
| Upstream framework design intent | Existing `docs/design`, `docs/specs`, `docs/features`, or ADR process |
| Microsoft Learn statement | Official URL metadata; do not copy page body |
| One-off troubleshooting evidence | Target project unless it generalizes across MAF consumers |

Before promoting a one-off observation into the curated topic registry, require a stable path, clear topic relevance, and an explanation of why it is a strong starting point. Generated catalog files must never be edited by hand.
