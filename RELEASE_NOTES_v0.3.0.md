# Materials Atlas v0.3.0 — Repository Engineering

## Overview

v0.3.0 establishes the repository engineering foundation for Materials Atlas.

This release does not expand the scientific curriculum. It makes the repository easier to maintain, validate, contribute to, and evolve as a long-lived open scientific knowledge project.

## Highlights

- Python is the canonical language for repository tooling.
- Ruby hook scripts were replaced with tested Python validators.
- Ruff, Pyright, pytest, coverage reporting, Lefthook, and GitHub Actions now provide a shared quality pipeline.
- The repository generates and verifies a deterministic status report from repository metadata.
- Governance, scientific scope, architecture, contribution flow, and tooling responsibilities are documented separately.
- The commit taxonomy distinguishes governance, tooling, automation, and reader-facing documentation; `meta` is no longer valid.

## Why This Matters

Materials Atlas teaches scientific computing and research software engineering. Its own tooling now follows the same production-quality practices: explicit standards, deterministic generated artifacts, tested behavior, local feedback, and continuous validation.

This reduces maintenance ambiguity for contributors and keeps the repository itself as the single source of truth.

## Breaking Changes

There are no breaking changes to scientific content, repository URLs, or public navigation.

For maintainers, the contributor toolchain now uses Python and `uv`; Ruby is no longer required for repository maintenance.

## What's Next

The next milestone returns focus to educational content under the theme **Scientific Foundations**.

Planned work includes Thermodynamics, Statistical Mechanics, Crystallography, and Electronic Structure. Repository engineering should now evolve incrementally alongside that content.
