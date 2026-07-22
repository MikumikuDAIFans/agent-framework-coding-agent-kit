# Maintenance lifecycle

## Cadence

- Weekly: fetch/compare upstream, discover official changes, probe active sources, and emit drift reports.
- Monthly: re-review changed high-value community sources, package/API maturity, licensing, and topic coverage.
- On a MAF major/minor release or security event: run an immediate full cycle.
- Quarterly: re-evaluate `context-only` and `quarantined` items, stale articles, inactive repositories, replacements, and archive integrity.

## State transitions

Keep the approved review states. Automation only proposes transitions; a maintenance Agent applies them after evidence review.

- New candidates stay outside the formal registry until a review batch starts.
- `adopted` remains active only while its version boundary, legal route, and useful design/API evidence remain valid.
- Use `quarantined` for repairable uncertainty, incompatibility, or temporarily unsafe evidence.
- Use `rejected` when a hard gate fails or the source no longer provides current MAF value.
- Preserve the previous review and collection coordinates in the archive ledger whenever an adopted item leaves active collection.

## Retirement decision

Retire only after confirming at least one material condition:

- the link or repository is permanently unavailable or archived without a maintained successor;
- the source targets removed APIs and no reliable mapping to the current baseline exists;
- a newer official or higher-quality source fully supersedes it;
- licensing, security, provenance, or integrity no longer meets policy;
- the source has lost its unique design or implementation value.

Age alone is a re-review signal. It is not sufficient to retire design history that remains accurate and useful. Record `replacement_source_id` when a successor exists.

## Batch boundaries

Use separate commits for:

1. upstream sync and generated catalog refresh;
2. source reviews, state changes, collection, and archival;
3. maintenance tooling or Skill changes.

Do not combine unrelated upstream framework edits with kit maintenance. Stop publication on dirty-worktree overlap, unresolved merge conflicts, missing legal evidence, structural validation failure, or an upstream history mismatch.

