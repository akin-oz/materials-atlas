# Contributing

> Contribute clarity, not volume.

## Before You Start

Read these documents in order:

1. [CONSTITUTION.md](CONSTITUTION.md) for durable repository principles.
2. [SCIENTIFIC_SCOPE.md](SCIENTIFIC_SCOPE.md) for inclusion boundaries.
3. [EDITORIAL.md](EDITORIAL.md) for content standards.
4. [ARCHITECTURE.md](ARCHITECTURE.md) to determine where information belongs.
5. [docs/repository/TOOLING.md](docs/repository/TOOLING.md) for repository tooling.
6. [docs/git/COMMIT-CONVENTION.md](docs/git/COMMIT-CONVENTION.md) for commit and hook setup.

## Contribution Flow

1. Identify the canonical owner of the information before adding text.
2. Confirm that the addition reduces uncertainty and does not duplicate an existing page.
3. Keep the change focused on one editorial or architectural purpose.
4. Run `uv sync --locked --group dev` and `lefthook install` once per clone, then run `lefthook run pre-commit` before committing.
5. Regenerate the repository report with `uv run --group dev python scripts/generate_status.py` when repository metadata changes.

## Where Changes Belong

- Learning sequence or module outcome: `roadmaps/`
- Stable internal explanation or canonical terminology: `references/`
- External source selection: `resources/`
- Researcher, laboratory, or infrastructure context: `ecosystem/`
- Mature field-level synthesis: `domains/`
- Reproducible project artifact: `projects/` only when a real project exists

## Pull Requests

Explain the reader problem the change solves, the reason for the selected sources or structure, and any limitation that remains. Avoid broad cleanup, speculative directories, or placeholder pages in the same pull request as a focused contribution.

## Generated Files

[reports/STATUS.md](reports/STATUS.md) is generated. Do not edit it manually. Run the generator and commit the resulting file when its inputs change.
