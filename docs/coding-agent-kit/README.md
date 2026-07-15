# Agent Framework Coding Agent Kit

This kit turns the upstream `microsoft/agent-framework` repository into a navigable engineering reference for coding agents. It does not replace Microsoft Learn or framework source; it connects a development intent to the smallest useful evidence bundle.

## What a coding agent gets

For a topic such as tool approval, session persistence, workflow checkpointing, middleware, A2A, or hosting, the kit provides:

1. official Microsoft Learn page metadata and links;
2. upstream design/spec/ADR context when available;
3. curated C# and Python sample entry points;
4. matching implementation and public export paths;
5. matching unit/integration test paths;
6. deterministic lookup commands for deeper discovery.

Start with the generated [catalog](catalog/CATALOG.md), or query it:

```bash
python tools/coding-agent-kit/indexer/lookup.py "checkpoint resume workflow" --language python
python tools/coding-agent-kit/indexer/lookup.py "function tool approval" --language csharp
python tools/coding-agent-kit/indexer/lookup.py "A2A hosting" --topic protocols
```

## Usage modes

### Work inside this fork

Open this repository as the workspace. Codex discovers `.agents/skills/maf-expert`, and `AGENTS.md` routes MAF-specific tasks to it. No project `.codex/config.toml` is required.

### Use as a reference for another MAF project

Install the Skill into the target repository or user Skill directory. The installer records this checkout as the reference root without changing Codex configuration or permissions:

```bash
# User scope
python tools/coding-agent-kit/install.py --scope user --dry-run
python tools/coding-agent-kit/install.py --scope user

# One consumer repository
python tools/coding-agent-kit/install.py --scope repo --target /path/to/project
```

You can override the recorded path later with `MAF_REFERENCE_REPO`. The Skill keeps the target root and reference root separate, so target project rules remain authoritative.

### Install as a Codex plugin

The repository root contains `.codex-plugin/plugin.json` and `.mcp.json`. Plugin installation exposes the Skill and an optional Microsoft Learn MCP fallback. The plugin does not change the user's model, permission, sandbox, web-search, or feature settings.

## Catalog model

- `tools/coding-agent-kit/indexer/topics.json` is the curated source of truth for topic intent, search vocabulary, and high-value entry points.
- `tools/coding-agent-kit/indexer/data/learn-pages.json` contains normalized Microsoft Learn metadata only—no page bodies.
- `build_catalog.py` scans the current checkout and generates machine-readable and Markdown catalogs.
- `lookup.py` ranks focused references for a coding task.
- Generated files under `docs/coding-agent-kit/catalog` are not hand-edited.

See [architecture.md](architecture.md) for component boundaries, [maintenance.md](maintenance.md) for upstream synchronization, and [CONTRIBUTING.md](CONTRIBUTING.md) for contribution rules.
Use [GITHUB_PUBLISHING.md](GITHUB_PUBLISHING.md) when the branch is ready for a remote fork.
Run the positive and negative prompts in [acceptance-cases.md](acceptance-cases.md) after installation.

## Quick verification

```bash
python tools/coding-agent-kit/indexer/build_catalog.py --check
python -m unittest discover tools/coding-agent-kit/indexer/tests
python tools/coding-agent-kit/validate.py
```

## Attribution and scope

This is a derivative branch of [`microsoft/agent-framework`](https://github.com/microsoft/agent-framework), retaining its MIT license and history. It is intended to help coding agents build systems with Microsoft Agent Framework; it is not an official Microsoft distribution and does not alter upstream support or security policies.
