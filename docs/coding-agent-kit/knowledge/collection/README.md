# External knowledge collection

This directory contains only reviewed, adopted external knowledge.

- `project-routes.json` stores links, immutable coordinates, topics, design notes, and usage boundaries.
  It must never contain copied project source code.
- `link-references.json` stores adopted document/article URLs plus original routing annotations when
  redistribution permission has not been verified. It never stores the source body.
- `documents.json` is the manifest for locally retained documents.
- `documents/` contains normalized Markdown only when redistribution terms permit it.
- `KNOWLEDGE_INDEX.md` is generated from all three manifests and is the entry point used by coding agents.

Candidate discovery and reviews remain under `../external-sources`. An item must be `adopted` there before
it can be added here. When a document cannot legally be retained, add its source link and an original
annotation to `link-references.json`; do not create a retained document body or `documents.json` entry.

## Commands

```powershell
# Validate manifests, adopted-source links, hashes, and the generated index.
python tools/coding-agent-kit/knowledge/collect.py check

# Regenerate the Markdown index from all collection manifests.
python tools/coding-agent-kit/knowledge/collect.py rebuild

# Add a project route without downloading project code.
python tools/coding-agent-kit/knowledge/collect.py add-project `
  --source-id <adopted-source-id> --version <commit-or-tag> `
  --route "When to use this project" --design "Reusable design reference" `
  --limitations "Important boundary"

# Adopt a document/article without retaining its body.
python tools/coding-agent-kit/knowledge/collect.py add-link `
  --source-id <adopted-source-id> --route "When to follow this link" `
  --annotation "Original summary of its design value" `
  --limitations "Version, maturity, and redistribution boundaries"

# Retain an adopted document as Markdown. --input accepts a reviewed local HTML/Markdown snapshot;
# omit it to fetch the source URL over HTTPS.
python tools/coding-agent-kit/knowledge/collect.py add-document `
  --source-id <adopted-source-id> --license <redistribution-license> `
  --license-url <license-url> --redistribution-allowed `
  --route "When to read this document" --input <reviewed-file>
```

Every mutating command rebuilds `KNOWLEDGE_INDEX.md`. Use `--root` to operate on another compatible
checkout. Network retrieval is bounded by HTTPS, timeout, content type, and response-size checks.
