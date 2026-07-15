# Contributing to the coding-agent kit

Follow the upstream repository's `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, and the closest nested `AGENTS.md`. Kit-only changes should stay within:

- `.agents/skills/maf-expert`
- `skills/maf-expert` only through `tools/coding-agent-kit/sync_skill.py`
- `.codex-plugin/plugin.json` and `.mcp.json`
- `docs/coding-agent-kit`
- `tools/coding-agent-kit`
- the root `AGENTS.md` and the kit introduction in `README.md`

Do not modify framework code or samples merely to improve indexing. If upstream behavior is wrong, make a separately reviewable upstream-compatible change with the required language-specific tests.

## Pull request expectations

- Explain the coding-agent failure or retrieval gap the change addresses.
- Identify affected topic IDs and languages.
- For curated entries, explain why the path is a strong starting point.
- Regenerate catalogs and include the validation result.
- Keep Microsoft Learn content to metadata and official URLs.
- Do not commit credentials, local absolute paths, generated caches, or private project knowledge.

## Validation

```bash
python tools/coding-agent-kit/indexer/build_catalog.py --check
python -m unittest discover tools/coding-agent-kit/indexer/tests
python tools/coding-agent-kit/validate.py
```

Framework-code changes require all additional checks mandated by the nearest upstream `AGENTS.md`.
