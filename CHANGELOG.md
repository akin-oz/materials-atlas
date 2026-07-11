# Changelog

All notable changes to Materials Atlas are documented in this file.

The project follows a curated-documentation model: releases record meaningful improvements to structure, navigation, editorial standards, and canonical content rather than every wording change.

## [0.4.0] — Interactive Foundations

### Added

- Established `notebooks/` as the official interactive learning layer, with reproducible execution and quality standards.
- Added the first four foundation notebooks: Python Environment and Jupyter Workflow, Linear Algebra, Atomic Bonding, and Crystal Structures.
- Added declared JupyterLab, NumPy, and Matplotlib dependencies for the notebook environment.
- Added notebook progression, naming, execution, and Markdown-integration guidance.

### Changed

- Extended the repository architecture so notebooks complement the canonical Markdown roadmaps and references.
- Added notebook-aware repository status reporting and ignored local Jupyter checkpoint files.

## [0.3.0] — Repository Engineering

### Added

- Established Python as the canonical language for repository tooling.
- Added deterministic documentation validation, curriculum sequence checks, and generated repository status reporting.
- Added Ruff, Pyright, pytest, coverage reporting, Lefthook, and GitHub Actions quality gates.
- Defined repository governance, scientific scope, architecture ownership, contribution flow, and tooling standards.

### Changed

- Replaced Ruby hook scripts with tested Python tooling.
- Refined the commit taxonomy to distinguish governance, tooling, automation, and reader-facing documentation.
- Made generated repository health views reproducible and validated them in local hooks and CI.

## [0.2.0] — Knowledge Architecture

### Changed

- Formalized the domain layer as the highest synthesis layer of the Atlas.
- Defined the domain lifecycle from candidate topic through editorial maintenance.
- Added readiness criteria for creating domain pages without placeholders.
- Documented knowledge flow from learning modules, references, resources, and ecosystem indexes into mature domains.
- Clarified cross-reference ownership and refined related repository navigation.

## [0.1.0] — 2026-07-10

First public release.

### Added

- A 16-module curriculum for software engineers transitioning into Computational Materials Science.
- Canonical thermodynamics references for quantities, phase diagrams, and recurring terminology.
- A structured Mermaid diagram library with stable identifiers and editorial ownership.
- Curated resource and ecosystem indexes for books, papers, software, videos, researchers, and institutions.
- Repository-wide editorial, citation, copyright, and licensing foundations.

### Changed

- Standardized curriculum navigation, module names, and internal reference links.
- Added a newcomer-oriented repository entry path and a dedicated reference index.

### Notes

- Domain pages remain intentionally absent until they earn their place through enough curated material.
- A Zenodo DOI is planned after the first stable public release is archived.
