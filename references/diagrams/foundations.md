# Foundational Diagrams

## Purpose

These diagrams define the basic visual language for materials-science structure, scale, defects, diffusion, and field-level orientation.

## Scope

Use this file for diagrams that introduce durable mental models across multiple domains.

## Modules Using These Diagrams

- Module 01 — Foundations of Materials Science
- Roadmaps
- Future domain pages

## Related Domains

- Modern Materials Science
- Computational Materials
- Crystallography
- Diffusion
- Microstructure
- Multiscale Modeling

## Related Reference Documents

- [../../STYLE-GUIDES/MERMAID.md](../../STYLE-GUIDES/MERMAID.md)
- [../thermodynamics/THERMODYNAMIC-QUANTITIES.md](../thermodynamics/THERMODYNAMIC-QUANTITIES.md)

---

# D-001 — Processing → Structure → Properties → Performance

## Purpose

The central mental model of Materials Science.

Used in:

- Module 01
- Foundations of Materials Science
- Microstructure
- Processing
- Mechanical Properties

```mermaid
flowchart LR
    P[Processing] --> S[Structure]
    S --> PR[Properties]
    PR --> PF[Performance]
```

---

# D-002 — Structural Hierarchy

## Purpose

Shows the hierarchy of structural scales.

Used in:

- Module 01
- Crystallography
- Electronic Structure
- Multiscale Modeling

```mermaid
flowchart TD
    ES[Electronic Structure] --> AS[Atomic Structure]
    AS --> CS[Crystal Structure]
    CS --> MS[Microstructure]
    MS --> CO[Component]
    CO --> SYS[Engineering System]
```

---

# D-003 — Crystal Defects

## Purpose

Illustrates the primary defect families.

Used in:

- Crystal Defects
- Diffusion
- Mechanical Behavior

```mermaid
graph TD
    Crystal --> Vacancy
    Crystal --> Interstitial
    Crystal --> Substitutional
    Crystal --> Dislocation
    Crystal --> GrainBoundary[Grain Boundary]

    Vacancy --> Diffusion
    Dislocation --> Plasticity
    GrainBoundary --> Strength
```

---

# D-004 — Diffusion

## Purpose

Conceptual view of diffusion.

Used in:

- Diffusion
- Kinetics
- Molecular Dynamics

```mermaid
flowchart LR
    Atoms --> RandomWalk[Random Walk]
    RandomWalk --> Gradient[Concentration Gradient]
    Gradient --> Diffusion
    Diffusion --> Microstructure
```

---

# D-005 — Computational Materials Landscape

## Purpose

Maps computational methods to the field.

Used in:

- README
- Roadmaps
- Domain pages

```mermaid
flowchart LR
    QM[Quantum Mechanics] --> DFT[Density Functional Theory]
    DFT --> MD[Molecular Dynamics]
    MD --> PF[Phase-Field]
    CAL[CALPHAD] --> PF
    MI[Materials Informatics] --> AI[AI for Materials]
```
