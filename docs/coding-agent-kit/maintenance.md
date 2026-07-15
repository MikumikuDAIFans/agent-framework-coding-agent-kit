# Maintenance and upstream synchronization

## Sync upstream

Keep the original Microsoft remote available as `upstream` or retain `origin` until the fork remote is configured. Review upstream changes before rebasing or merging.

Typical fork setup after creating the GitHub repository:

```bash
git remote rename origin upstream
git remote add origin <your-fork-url>
git fetch upstream
git rebase upstream/main
```

Use merge instead of rebase when the project's published-history policy requires it. Never rewrite a shared branch without explicit maintainer agreement.

After each upstream sync:

1. read upstream release/migration notes and changed nested `AGENTS.md` files;
2. update `tools/coding-agent-kit/indexer/upstream-base.json` to the synchronized upstream commit;
3. regenerate the catalog;
4. inspect removed curated paths as blocking failures;
5. review topic count changes and newly unclassified high-value sample directories;
6. run kit validation;
7. update the plugin version and release notes only for a deliberate kit release.

## Refresh Microsoft Learn metadata

Import a public manifest produced by the local Learn mirror workflow:

```bash
python tools/coding-agent-kit/indexer/build_catalog.py \
  --learn-manifest /path/to/agent-framework-md/manifest.json
```

The importer retains page title, section path, official URL, Markdown URL, source timestamp, and logical document path. It does not copy page content. Review unexpected domain changes before committing.

After an official page is adopted, its body may be collected separately when redistribution terms are
verified. Use `tools/coding-agent-kit/knowledge/collect.py`; do not add document files by hand.

## Maintain external knowledge

- External projects stay in `knowledge/collection/project-routes.json` as links, immutable versions, routes,
  design notes, and limitations. Never clone or copy them into the collection directory.
- Retained documents must be `adopted`, license-verified, and created by `collect.py add-document`.
- Run `python tools/coding-agent-kit/knowledge/collect.py check` after every manifest or document change.
- Re-review an entry after MAF/version/license changes, stale dates, security findings, or broken links.
- Rebuilds update `knowledge/collection/KNOWLEDGE_INDEX.md`; do not edit that file by hand.

## Change the topic registry

Update `tools/coding-agent-kit/indexer/topics.json` when:

- a new stable framework surface appears;
- an existing curated path moves or stops being the best entry point;
- lookup repeatedly misses a common MAF concept;
- a topic is too broad to produce a compact evidence bundle.

Do not add every matching file as curated. A curated entry should be stable, representative, and explain a design, usage pattern, implementation seam, or test contract.

## Generated files

Run:

```bash
python tools/coding-agent-kit/indexer/build_catalog.py
python tools/coding-agent-kit/indexer/build_catalog.py --check
```

Commit registry/indexer changes and regenerated outputs together. Never hand-edit `docs/coding-agent-kit/catalog`.

The repository Skill under `.agents/skills/maf-expert` is canonical. After editing it, run:

```bash
python tools/coding-agent-kit/sync_skill.py
python tools/coding-agent-kit/sync_skill.py --check
```

Do not hand-edit the generated plugin copy under `skills/maf-expert`.
