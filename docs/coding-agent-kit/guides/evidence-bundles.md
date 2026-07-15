# Evidence bundles for coding agents

An evidence bundle is the smallest set of sources needed to make one implementation decision safely. It prevents both memory-only API invention and indiscriminate loading of the whole repository.

## Default bundle

For an API-sensitive implementation detail, collect:

1. **Documented** — one relevant Microsoft Learn page or official explanation.
2. **Designed** — one matching design, spec, feature note, or ADR when available.
3. **Sampled** — one same-language sample at the target provider/version boundary.
4. **Source-observed** — the public export plus implementation seam.
5. **Source-observed test** — a unit/integration test that establishes edge behavior.
6. **Target evidence** — the target project's pinned package, conventions, current tests, and decisions.

Not every task has all six lanes. Missing lanes must be named rather than silently replaced with inference.

## Retrieval sequence

```bash
python tools/coding-agent-kit/indexer/lookup.py "<task concepts>" --language <language>
rg -n "<ExactSymbol>" <narrowed-source-and-test-paths>
```

Read curated entries first. Use ranked catalog results to select the smallest same-language paths, then confirm exact symbols with `rg`. Query Microsoft Learn MCP only for missing, conflicting, or plausibly stale behavior.

## Evidence labels

- `documented` does not prove the target package version contains the API;
- `designed` explains intent but can precede or differ from final implementation;
- `sampled` demonstrates composition but usually omits production security/operations;
- `source-observed` applies to the recorded commit/version;
- `project decision` is authoritative only for the target project;
- `inference` must carry an assumption and verifier.

## When to expand the bundle

Add more evidence for:

- cross-language comparisons;
- provider-specific behavior;
- persisted-state/protocol compatibility;
- security, identity, destructive side effects, or tenant data;
- concurrency, checkpoint/replay, and failure recovery;
- migrations and release/deployment decisions.
