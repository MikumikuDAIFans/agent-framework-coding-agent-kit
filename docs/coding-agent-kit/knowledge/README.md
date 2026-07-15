# Knowledge lifecycle

The kit indexes upstream knowledge; it does not become the application project's memory. Durable findings belong at the narrowest authoritative location.

## Target project knowledge

A consumer project should maintain its own:

- architecture and system/data-flow descriptions;
- accepted ADRs and compatibility decisions;
- verified reusable patterns;
- troubleshooting records with reproduction and regression evidence;
- evaluation datasets, baselines, thresholds, and release decisions;
- deployment/runtime constraints and rollback procedures.

Use the templates in `../templates` as starting points. Completed artifacts stay in the target project's approved documentation area.

## Kit knowledge

The kit should retain only knowledge that improves coding-agent retrieval across MAF projects:

- topic vocabulary and stable high-value entry points in `tools/coding-agent-kit/indexer/topics.json`;
- indexer behavior and tests;
- retrieval/evidence guidance;
- kit architecture, maintenance, and distribution decisions.

Broad internet and community research first enters the
[external source review layer](external-sources/README.md). Its
[candidate registry](external-sources/sources.json) and
[review queue](external-sources/REVIEW_QUEUE.md) are deliberately separate from the generated catalog.
Only sources with a completed `adopted` review may be proposed for the curated topic registry.

Do not promote a one-off application choice into the topic registry.

## Upstream knowledge

Framework API defects, missing tests, or broadly applicable design changes should be proposed upstream using the upstream repository's contribution process. Keep kit navigation changes separate from framework behavior changes so each can be reviewed on its own merits.

## Promotion gate

Before making a discovery durable, record:

1. what was observed and at which package/commit;
2. evidence and reproduction;
3. applicability boundary;
4. whether it is fact, decision, workaround, or hypothesis;
5. validation and residual risk;
6. the narrowest owner: target project, kit, Microsoft Learn, or upstream framework.
