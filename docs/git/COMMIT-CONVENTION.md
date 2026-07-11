# Commit Convention

> A concise record of why the Atlas changed.

## Purpose

Commit history is part of the repository's editorial record.

Each commit should describe one durable change: a new layer of knowledge, a meaningful refinement, a release boundary, or a maintainer policy. Do not use commits as a running work log.

## Subject Format

Use:

```text
<category>: <imperative summary>
```

Keep the subject concise, begin the summary with a lowercase verb, and omit trailing punctuation.

Good:

```text
reference: add thermodynamic quantities reference
```

Bad:

```text
updated stuff
```

Use an optional body when the subject alone cannot explain a non-obvious editorial decision, source choice, migration, or compatibility concern.

## Categories

| Category | Use for | Example | Do not use for |
|----------|---------|---------|----------------|
| `architecture` | Repository structure, navigation, or ownership boundaries | `architecture: define domain knowledge flow` | A single scientific explanation |
| `editorial` | Editorial standards, templates, or curation rules | `editorial: clarify resource inclusion criteria` | Routine wording fixes |
| `curriculum` | Learning modules, study paths, and capability progression | `curriculum: add molecular dynamics module` | A standalone reference page |
| `reference` | Canonical internal concepts, notation, and durable explanations | `reference: add phase diagram guide` | A reusable diagram-only change |
| `diagram` | Canonical Mermaid diagrams and diagram-library structure | `diagram: add CALPHAD workflow model` | Decorative diagrams inside one page |
| `resources` | Curated books, papers, software, datasets, and videos | `resources: curate primary CALPHAD texts` | Ecosystem profiles |
| `domain` | A mature domain page or a domain-specific synthesis | `domain: map materials informatics` | A candidate-topic note |
| `ecosystem` | Researchers, institutions, infrastructure, and field context | `ecosystem: add Materials Project context` | Software documentation already owned by resources |
| `research` | Research practice, reproducibility, evidence, and workflow guidance | `research: document provenance expectations` | General Git policy |
| `governance` | Maintainer policy, contribution rules, licensing, and repository stewardship | `governance: establish contribution standards` | Tool implementation or release metadata |
| `tooling` | Developer tooling, scripts, local validation, and maintenance configuration | `tooling: establish Python validation foundation` | CI workflow behavior or generated reports |
| `automation` | CI workflows, hooks, and deterministic generated repository artifacts | `automation: add deterministic status reporting` | A manually run tool without automated enforcement |
| `release` | Version, changelog, tag, and release-preparation changes | `release: prepare v0.4.0 interactive foundations` | Ordinary documentation work |
| `docs` | Reader-facing repository navigation and explanatory documentation without another owner | `docs: clarify repository navigation` | Governance, tooling, or a content layer |

Choose the narrowest category that explains the change.

## Taxonomy Decision

`meta` is not a valid category. It describes repository maintenance without saying what changed, which makes history difficult to search and release notes difficult to generate.

Choose `governance` for maintainer policy, `tooling` for developer tooling, and `automation` for enforced or generated behavior. Use `docs` only for reader-facing repository documentation that belongs to none of those responsibilities.

## Grouping Rules

- One logical change per commit.
- Keep structural moves separate from content expansion when either can be reviewed independently.
- Squash temporary corrections before sharing a branch.
- Do not mix release metadata with unrelated content.
- Preserve a release boundary as its own commit so annotated tags point to a meaningful state.

## Anti-Patterns

- Do not use generic categories such as `chore`, `feat`, or `fix`; choose the Atlas layer that owns the change.
- Do not use a release commit to hide unrelated editorial work.
- Do not commit generated report changes without the source change that caused them.
- Do not create formatting-only commits unless they are necessary and clearly documented for blame history.
- Do not rewrite published history after contributors or citations depend on it.

## References

Include a body when a commit needs to record a decision, source constraint, or migration detail. Reference an issue, paper, or external source only when it helps a future maintainer understand the change.

Do not add references merely to make a commit look formal.

## Enforcement

The `commit-msg` hook validates the category, separator, lowercase imperative opening, length, and absence of trailing punctuation. It cannot determine whether a sentence is truly imperative; maintainers remain responsible for that judgment.

Install Lefthook once in each clone:

```text
lefthook install
```

The `pre-commit` hook checks Python formatting, linting, types, tooling tests, staged Markdown files, and the generated status report. Hooks are intentionally fast and do not require network access after `uv sync --group dev`.

The repository does not currently contain a `.git-blame-ignore-revs` file because it has no formatting-only commit to ignore. Add one only alongside a documented formatting-only change.
