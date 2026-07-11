# Versioning and Release Policy

> Version releases when the repository reaches a coherent editorial milestone.

## Version Format

Materials Atlas uses annotated semantic versions:

```text
vMAJOR.MINOR.PATCH
```

The project is currently in its pre-1.0 phase. During this period:

- `v0.MINOR.0` marks a coherent public milestone that may revise editorial architecture, learning paths, or reference structure.
- `v0.MINOR.PATCH` corrects or refines an existing milestone without changing its intended scope.
- `v1.0.0` should be reserved for a stable public contract: readers and contributors can rely on the repository's core structure, naming, and release expectations.

The current release is `v0.4.0`.

| Version | Milestone |
|---------|-----------|
| `v0.1.0` | Foundation |
| `v0.2.0` | Knowledge Architecture |
| `v0.3.0` | Repository Engineering |
| `v0.4.0` | Interactive Foundations |

## Release Naming

Each milestone receives a short descriptive title:

```text
v0.4.0 — Interactive Foundations
```

The title should describe the durable theme of the release, not market it.

## Release Policy

Create a release only when a change is coherent enough to be understood as a single editorial milestone.

Before tagging a release:

1. Update `CHANGELOG.md`.
2. Update the current version in `CITATION.cff` and `CITING.md`.
3. Verify internal Markdown links and Mermaid source.
4. Prepare a concise GitHub Release description.
5. Create an annotated tag on the release commit.
6. Push the branch and tag, then publish the GitHub Release.

Do not create releases on a fixed calendar. Release when the repository has reached a stable, reviewable milestone.

## Release Boundaries

Release commits should contain release metadata and small consistency fixes only. Major content or architectural work belongs in earlier commits so the tag records a clear final state.

After external contributors or citations depend on a release, do not move or replace its tag. Correct mistakes in a new release.

## Branch Strategy

Use a small branch model:

- `main` is the canonical, releasable history.
- `feature/<topic>` is for a bounded contribution that benefits from isolated review.
- `release/<version>` is optional and short-lived, used only when release preparation must proceed alongside other active work.

Do not maintain a permanent `develop` branch. Do not use GitFlow unless concurrent release maintenance creates a real need for it.

Rebase or squash a contribution branch before it reaches `main` when doing so improves the historical record without losing meaningful review context.

## History Policy

Before broad external adoption, maintainers may rewrite unpublished history to correct accidental commits, noisy sequences, or inaccurate release boundaries.

Once contributors, forks, citations, or releases rely on a commit range, prefer additive corrective commits. History rewriting should then be exceptional and explicitly communicated.
