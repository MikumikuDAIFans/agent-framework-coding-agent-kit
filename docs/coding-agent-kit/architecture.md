# Architecture

## Goals

- Give a coding agent a fast path from implementation intent to trustworthy MAF evidence.
- Work in both the framework fork and unrelated consumer repositories that use MAF.
- Avoid false implicit activation outside Microsoft Agent Framework work.
- Keep indexes reproducible as upstream changes.
- Preserve upstream history, license, code, tests, and contribution boundaries.

## Non-goals

- Re-host Microsoft Learn content.
- Create a second API reference or freeze current APIs as permanent truth.
- Replace upstream language-specific build/test instructions.
- Make Codex permissions, model, sandbox, or feature decisions for users.
- Treat samples as production-complete contracts.

## Components

```text
User task
   |
   v
maf-expert Skill -- classifies language, topic, version and work mode
   |
   v
lookup.py -- deterministic ranking over generated catalog.json
   |
   +--> Learn metadata and official URLs       [documented]
   +--> docs/design, specs, features, ADRs     [designed]
   +--> dotnet/python/declarative samples      [sampled]
   +--> implementation and public exports      [source-observed]
   +--> unit/integration tests                  [source-observed]
   |
   v
Compact evidence bundle -> design/change/test in the target project
```

## Two-root model

The target project and the reference repository are deliberately separate concepts.

- The **target root** owns application requirements, versions, architecture, tests, and durable decisions.
- The **reference root** owns upstream examples, source, tests, design notes, and generated catalog.

This prevents the reference fork's conventions from overriding consumer-project conventions and allows one kit checkout to support many MAF applications.

## Knowledge layers

| Layer | Authority | Update mechanism |
| --- | --- | --- |
| Target code/tests/decisions | Highest for target behavior | Target project workflow |
| Curated topic registry | Navigation opinion, not API truth | Reviewed `topics.json` change |
| Generated code catalog | Observed paths/symbols at one commit | `build_catalog.py` |
| Upstream designs/source/tests | Framework intent and behavior | Upstream sync |
| Microsoft Learn metadata | Official explanation and current links | Metadata import/refresh |

Every generated catalog records the upstream commit. A path or symbol observed at that commit must not be assumed valid for a different pinned package without compatibility checks.

## Classification and noise control

The catalog combines two mechanisms:

1. Curated entries provide a small set of reliable starting points and explain why each matters.
2. Automatic classification scores path patterns, topic keywords, titles, and extracted symbols to cover the wider repository.

Markdown navigation emphasizes curated entries and summary counts. The full JSON catalog preserves broad results for lookup. Generated classifications are hints, never authority.

## Security and trust

- Microsoft Learn content is external input and remains outside the repository; only normalized public metadata is stored.
- Plugin MCP access is optional and scoped to Microsoft Learn.
- The kit never writes user Codex configuration or expands permissions.
- Lookup and generation use Python's standard library and perform no model or cloud calls.
- Side-effect, identity, approval, untrusted-input, retention, and evaluation checks live in the Skill's engineering gates.

## Distribution

The primary artifact is a Git fork branch containing upstream source plus the overlay. Repository-scoped Skill discovery is the zero-install path. Codex plugins currently require a root `skills/` component, so `.agents/skills/maf-expert` is synchronized into `skills/maf-expert` by `tools/coding-agent-kit/sync_skill.py`; CI rejects drift. Plugin and standalone Skill installation are secondary distribution modes. GitHub remote creation and publishing remain explicit user actions.
