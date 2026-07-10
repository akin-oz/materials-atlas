# Tooling

> Python is the canonical language for Materials Atlas repository tooling.

## Canonical Language

Repository scripts use Python unless a compelling technical reason requires another language. The burden of proof lies with introducing a new runtime.

This aligns tooling with the Scientific Python curriculum and keeps it approachable for software engineers, computational materials researchers, and PhD students.

## Dependency Philosophy

Use the Python standard library by default. Add a third-party dependency only when it creates substantial long-term value that explicit standard-library code cannot provide.

## Tooling Principles

- Keep scripts readable and explicit; avoid frameworks for straightforward repository checks.
- Produce deterministic output. Generated artifacts must not depend on timestamps, random order, or machine-specific state.
- Give each script one responsibility and a module docstring that states purpose, usage, inputs, and outputs.
- Keep scripts independently runnable. Compose existing checks rather than duplicating their logic in new automation.
- Keep hooks fast and offline. CI may compose the same checks but should not invent separate rules.

## Quality Stack

The repository uses one configuration source, [`pyproject.toml`](../../pyproject.toml), for Python tooling:

- Ruff formats and lints repository scripts.
- Pyright type-checks scripts and tests.
- pytest validates tooling behavior.
- pytest-cov reports tooling coverage in CI.

Use `uv` to provision these development tools from the lockfile:

```text
uv sync --locked --group dev
```

`uv` is a package manager, not a second scripting runtime. Contributors only need Python to read and maintain repository tooling.

Run the complete local quality chain with:

```text
uv run --group dev ruff format --check scripts tests
uv run --group dev ruff check scripts tests
uv run --group dev pyright
uv run --group dev pytest --cov=scripts --cov-report=term-missing
uv run --group dev python scripts/check_docs.py --all
uv run --group dev python scripts/generate_status.py --check
```

## Validation Responsibilities

`scripts/check_docs.py` validates Markdown hygiene, local links, optional frontmatter structure, Mermaid fences, module sequence, and canonical diagram identifiers. `scripts/generate_status.py` reuses those checks when it renders repository health; it does not duplicate them.

Lefthook runs fast local checks before commits. GitHub Actions runs the same commands with coverage reporting. Generated reports are checked for staleness but are never committed automatically.

## Repository Configuration

- [`.editorconfig`](../../.editorconfig) keeps text encoding, line endings, final newlines, and whitespace consistent across editors.
- [`.gitattributes`](../../.gitattributes) normalizes text files and marks generated status output for GitHub.
- [`.gitignore`](../../.gitignore) excludes local environments, caches, and coverage output from version control.
- `.git-blame-ignore-revs` is intentionally absent until a documented formatting-only commit needs it.
- [`lefthook.yml`](../../lefthook.yml) orchestrates fast local validation without reimplementing repository rules.

Keep configuration small. Add a file only when it establishes a durable ownership boundary that `pyproject.toml`, existing tooling, or repository documentation cannot provide.

## Current Scripts

| Script | Responsibility |
|--------|----------------|
| `scripts/check_docs.py` | Validate Markdown filenames, local links, optional frontmatter, Mermaid structure, curriculum sequence, and canonical diagram IDs. |
| `scripts/check_commit_message.py` | Validate commit subjects against the repository convention. |
| `scripts/generate_status.py` | Generate and verify the deterministic repository status report. |

Lefthook and GitHub Actions orchestrate these scripts. They do not contain separate validation implementations.
