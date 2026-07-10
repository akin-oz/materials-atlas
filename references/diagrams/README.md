# Diagram Library

> Canonical diagrams for Materials Atlas.

This directory is the authoritative home for reusable diagrams.

The Mermaid style guide explains how diagrams should be written. This library defines which canonical diagrams exist, where they belong, and how they should be reused.

## Purpose

The Diagram Library prevents diagrams from becoming scattered across modules.

A canonical diagram should be reused whenever the same idea appears in multiple places. If a concept needs a new visual model, add it here only after confirming that no existing diagram already communicates the idea.

## Navigation

Current canonical files:

- [foundations.md](foundations.md): foundational materials-science diagrams and cross-field mental models.
- [research-workflows.md](research-workflows.md): scientific, learning, research, and computational workflow diagrams.
- [thermodynamics.md](thermodynamics.md): thermodynamic quantities, phase stability, phase diagrams, and computational thermodynamics.
- [statistical-mechanics.md](statistical-mechanics.md): diagrams connecting microscopic states to macroscopic thermodynamics.
- [materials-informatics.md](materials-informatics.md): materials discovery and data-to-model pipelines.
- [software-infrastructure.md](software-infrastructure.md): computational software stack and infrastructure diagrams.

Future canonical files should be created only when at least one diagram exists for that area. Do not create empty category files.

## Diagram Categories

The library is organized by conceptual ownership, not by the module where a diagram first appears.

Each diagram belongs to exactly one canonical file. Other pages may reference or embed it, but they should not duplicate it.

Current ownership:

- Foundations: structure-property-performance, structural hierarchy, defects, diffusion, and field-level method maps.
- Research workflows: scientific reasoning, learning loops, research lifecycle, and computational study workflow.
- Thermodynamics: energy, free energy, phase stability, phase diagrams, and computational thermodynamics.
- Statistical mechanics: microstates, probability, partition functions, and thermodynamic emergence.
- Materials informatics: discovery pipelines and data-to-prediction flows.
- Software infrastructure: reusable diagrams for scientific software stacks.

## Numbering Policy

Diagram identifiers are permanent. Do not renumber existing diagrams.

Use reserved ranges for long-term growth:

- D-001-D-099: Foundations, research workflows, and cross-field orientation.
- D-100-D-199: Thermodynamics and phase stability.
- D-200-D-299: Statistical mechanics, Monte Carlo, molecular dynamics foundations, and free-energy methods.
- D-300-D-399: Crystallography, defects, microstructure, and diffusion.
- D-400-D-499: Electronic structure and density functional theory.
- D-500-D-599: Molecular dynamics, interatomic potentials, and atomistic simulation workflows.
- D-600-D-699: CALPHAD, phase-field, mesoscale modeling, and computational thermodynamics workflows.
- D-700-D-799: Materials informatics, databases, descriptors, and high-throughput screening.
- D-800-D-899: AI for materials, graph models, foundation models, and autonomous discovery.
- D-900-D-999: Research infrastructure, scientific software, reproducibility, and publication workflows.

Existing diagrams keep their original IDs even if a future range would have placed them elsewhere.

When adding a diagram, use the next available ID in the relevant range. If a range fills, continue with a documented extension range rather than renumbering.

## Editorial Rules

Every canonical diagram must have:

- one stable identifier
- one authoritative file
- one primary purpose
- one conceptual owner
- at least one expected reuse context

Every diagram should answer one question. If the question cannot be stated in one sentence, split the diagram.

Prefer improving an existing canonical diagram over adding a new one.

Do not duplicate diagrams across files.

Do not add diagrams for decoration.

If a diagram is never reused, reconsider whether it should remain canonical.

## Contribution Workflow

Before adding a new diagram:

1. Search this directory for an existing diagram that answers the same question.
2. Check [../../STYLE-GUIDES/MERMAID.md](../../STYLE-GUIDES/MERMAID.md) for visual grammar.
3. Decide the conceptual owner and reserved ID range.
4. Add the diagram to exactly one canonical file.
5. Include purpose, scope, modules using it, related domains, and related reference documents.
6. Update this README only if a new category file or numbering range is justified.

## Future Placement Guidance

Future diagrams should live where their conceptual owner belongs:

- Fracture mechanics: use a future mechanics or continuum-mechanics file in the D-300 or D-600 range, depending on whether the diagram is microstructure-centered or model-centered.
- Finite element methods: use a future continuum-mechanics or research-infrastructure file, likely D-900 for workflow/infrastructure or D-600 for modeling concepts.
- Continuum mechanics: use a future continuum-mechanics file if enough diagrams exist.
- Batteries: use a future energy-materials or application-domain file only after reusable diagrams exist across battery modules.
- Polymers: use a future polymers file only after polymer-specific canonical diagrams exist.
- Machine learning: use materials-informatics.md for descriptor/data diagrams and a future ai-for-materials.md file for model-family or discovery-system diagrams.
- Research workflows: use research-workflows.md unless the diagram is specifically about software infrastructure or publication provenance.

## Architecture Review

This architecture is intended to scale to hundreds of diagrams without forcing hundreds of files.

The library should grow by conceptual ownership:

- add diagrams inside existing category files when the concept fits
- create new category files only when repeated diagrams need a stable owner
- keep numbering independent from file names so future reorganizations do not break IDs
- keep interpretations close to diagrams so modules can reuse the visual without copying explanatory text

The main maintenance risk is over-fragmentation. Avoid creating one file per topic until the topic has enough canonical diagrams to justify ownership.
