# External source research and review

This directory is the quarantine and review layer for knowledge that does not live in the
`microsoft/agent-framework` checkout. It keeps broad discovery useful without allowing an
unreviewed blog post or repository to become API evidence.

## Evidence classes

1. `official-doc`: Microsoft Learn API or conceptual documentation.
2. `official-engineering`: Microsoft-owned engineering blogs, announcements, and design explanations.
3. `official-repository`: repositories owned by Microsoft, Azure-Samples, OfficeDev, or another clearly
   identified Microsoft documentation organization.
4. `community-repository`: runnable third-party code that directly imports or references Microsoft Agent
   Framework packages.
5. `community-article`: third-party explanations or experience reports with inspectable technical detail.
6. `meta-index`: a curated list used only to discover additional sources.

Official ownership establishes provenance, not compatibility. Every source still needs a version and
maturity check before an agent uses its API details.

## Review states

- `discovered`: search found the source, but direct MAF evidence has not been checked.
- `queued`: the source passed a lightweight relevance and ownership check and awaits a full review.
- `in-review`: one reviewer is inspecting it against the review template.
- `adopted`: strong enough to become a recommended external starting point.
- `context-only`: useful background, but not suitable as implementation evidence.
- `quarantined`: potentially useful but currently stale, unclear, incomplete, or license-constrained.
- `rejected`: unrelated, copied without attribution, unsafe, misleading, or too weak to retain.

Only `adopted` sources may be promoted into the topic registry. `context-only` sources may be linked from
an explanation when their boundary is explicit. All other states are discovery data only.

## Review policy

The review mechanism is owned and approved by the project maintainer. Its only normative location is
[REVIEW_POLICY.md](REVIEW_POLICY.md). That document is currently an owner-editable draft and is not yet
effective. No score, threshold, or adoption decision may be inferred until the maintainer approves it.

## Review procedure

1. Claim exactly one source from [REVIEW_QUEUE.md](REVIEW_QUEUE.md).
2. Resolve its default branch, current commit, license, release/package coordinates, and direct MAF files.
3. Apply the currently approved [review policy](REVIEW_POLICY.md). If no policy is approved, collect facts
   but do not issue a quality score or final adoption decision.
4. Compare every material API pattern with the matching local source/export/tests and current Microsoft
   Learn page.
5. Identify reusable design decisions separately from sample shortcuts.
6. Record security, reliability, state, observability, evaluation, and deployment gaps.
7. Save the review under `reviews/<source-id>.md` using [review-template.md](review-template.md).
8. Update `sources.json` and the queue. Promotion to `topics.json` is a separate reviewed change.

Do not copy external page bodies or substantial source code into this repository. Store URLs, metadata,
small factual annotations, and original review conclusions.
