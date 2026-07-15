# External knowledge collection

This directory contains only reviewed, adopted external knowledge.

- `project-routes.json` stores links, immutable coordinates, topics, design notes, and usage boundaries.
  It must never contain copied project source code.
- `documents.json` is the manifest for locally retained documents.
- `documents/` contains normalized Markdown only when redistribution terms permit it.
- `KNOWLEDGE_INDEX.md` is generated from both manifests and is the entry point used by coding agents.

Candidate discovery and reviews remain under `../external-sources`. An item must be `adopted` there before
it can be added here. When a document cannot legally be retained, keep the source link and an original
annotation in the source review; do not create a local document entry.

## Commands

```powershell
# Validate manifests, adopted-source links, hashes, and the generated index.
python tools/coding-agent-kit/knowledge/collect.py check

# Add a project route without downloading project code.
python tools/coding-agent-kit/knowledge/collect.py add-project `
  --source-id <adopted-source-id> --version <commit-or-tag> `
  --route "When to use this project" --design "Reusable design reference" `
  --limitations "Important boundary"

# Retain an adopted document as Markdown. --input accepts a reviewed local HTML/Markdown snapshot;
# omit it to fetch the source URL over HTTPS.
python tools/coding-agent-kit/knowledge/collect.py add-document `
  --source-id <adopted-source-id> --license <redistribution-license> `
  --license-url <license-url> --redistribution-allowed `
  --route "When to read this document" --input <reviewed-file>
```

Every mutating command rebuilds `KNOWLEDGE_INDEX.md`. Use `--root` to operate on another compatible
checkout. Network retrieval is bounded by HTTPS, timeout, content type, and response-size checks.
