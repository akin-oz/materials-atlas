# Module 00 — Mathematical & Physical Recovery

> Rebuild the scientific intuition required for modern Computational Materials Science.

---

# Purpose

This module rebuilds the mathematical, physical, and materials science intuition required for the rest of the curriculum.

It is intentionally selective.

The objective is not to repeat an undergraduate degree.

The objective is to remove future learning bottlenecks.

Every concept introduced here should immediately become useful in later modules.

---

# Why This Module Exists

Most Computational Materials Science resources assume knowledge that experienced software engineers often no longer retain.

Examples include:

- crystal structures
- thermodynamic equilibrium
- Gibbs free energy
- diffusion
- vectors and matrices
- derivatives and gradients
- probability distributions

Without rebuilding these concepts first, later topics such as Density Functional Theory, Molecular Dynamics, CALPHAD, and Materials Informatics become collections of equations instead of understandable models.

This module restores the scientific intuition needed to understand—not memorize—the rest of the curriculum.

---

# Learning Philosophy

This module follows four principles.

- Recover intuition before mathematical rigor.
- Learn only what unlocks future modules.
- Build while learning.
- Produce one durable artifact every study session.

See:

- `STUDY-METHOD.md`

---

# Prerequisites

None.

The curriculum assumes:

- professional software engineering experience
- basic Python familiarity
- willingness to write code while learning

---

# Capability Map

| Capability | Primary Resource | Artifact | Mastery Gate |
|------------|------------------|-----------|--------------|
| Scientific Thinking | Callister Ch.1 | Markdown note | Explain scientific models |
| Linear Algebra Intuition | 3Blue1Brown | NumPy notebook | Implement vector operations |
| Calculus Intuition | 3Blue1Brown | Visualization notebook | Explain gradients conceptually |
| Atomic Bonding | Callister Ch.2 | Notebook | Explain bonding mechanisms |
| Crystal Structures | Callister Ch.3 | Python visualization | Generate FCC/BCC/HCP structures |

---

# Learning Outcomes

After completing this module you should be able to:

- explain why different materials exhibit different properties
- describe metallic, ionic, covalent, and secondary bonding
- reason about crystal structures
- interpret Gibbs free energy conceptually
- understand equilibrium without relying on equations
- manipulate vectors and matrices comfortably
- understand derivatives and gradients conceptually
- read introductory computational materials literature without feeling lost

---

# Scope

Included:

- scientific thinking
- basic materials science
- linear algebra intuition
- calculus intuition
- atomic bonding
- crystal structures
- equilibrium intuition

Explicitly excluded:

- quantum mechanics
- advanced statistical mechanics
- continuum mechanics
- tensor calculus
- Density Functional Theory
- Molecular Dynamics

These topics appear later when they become necessary.

---

# Canonical Resources

## Primary Book

William D. Callister Jr.

*Materials Science and Engineering: An Introduction*

### Read

- Chapter 1
- Chapter 2
- Chapter 3

### Skip For Now

- Mechanical Properties
- Failure
- Ceramics
- Polymers
- Composites
- Corrosion

These topics return in later modules.

---

## Mathematics

### 3Blue1Brown — Essence of Linear Algebra

Required:

- Chapters 1–4
- Chapter 6
- Chapter 7
- Chapter 9
- Chapters 14–15

Optional:

- Remaining chapters

---

### 3Blue1Brown — Essence of Calculus

Watch the complete series.

Focus on intuition rather than symbolic manipulation.

---

## Physics

MIT OpenCourseWare

### 3.091 — Introduction to Solid State Chemistry

Watch only the lectures directly supporting:

- atomic structure
- bonding
- crystal structures

Ignore mathematical derivations.

---

# Four-Week Study Plan

## Week 1

### Read

- Callister Chapter 1

### Watch

- 3Blue1Brown Linear Algebra (Chapters 1–4)

### Build

Notebook:

`01-linear-algebra.ipynb`

Topics:

- vectors
- matrices
- transformations

---

## Week 2

### Read

- Callister Chapter 2

### Watch

- Remaining required Linear Algebra videos
- Beginning of Essence of Calculus

### MIT

Selected bonding lectures

### Build

Notebook:

`02-atomic-bonding.ipynb`

---

## Week 3

### Read

- Callister Chapter 3

### Watch

Complete Essence of Calculus

### Build

Notebook:

`03-crystal-structures.ipynb`

Implement:

- FCC
- BCC
- HCP

using Python.

---

## Week 4

Review.

Refactor notebooks.

Finish summaries.

Complete the mini project.

Perform an oral review with ChatGPT.

---

# Practical Work

## Notebook 01

Linear Algebra Intuition

Implement:

- vectors
- dot product
- matrix multiplication
- coordinate transformations

---

## Notebook 02

Atomic Bonding

Visualize:

- ionic
- covalent
- metallic

bonding.

---

## Notebook 03

Crystal Structures

Generate:

- FCC
- BCC
- HCP

using NumPy.

---

## Notebook 04

Thermodynamic Intuition

Visualize:

- entropy
- Gibbs free energy
- equilibrium

using simple plots.

---

# Reading Workflow

For every chapter:

Do **not** summarize everything.

Answer only:

## Big Idea

What is the central idea?

---

## Why It Matters

Why does this concept exist?

---

## Computational View

How would software represent it?

---

## Related Modules

Where will this appear again?

---

## Artifact

Which notebook or visualization supports it?

---

## Open Questions

What remains unclear?

---

# Mini Project

Create:

**Scientific Recovery Notebook**

A single Jupyter notebook explaining:

- atomic bonding
- crystal structures
- vectors
- Gibbs free energy

using figures, code, and plain language.

Assume the audience is another experienced software engineer entering Computational Materials Science.

---

# Mastery Gates

## Scientific Thinking

Can you explain:

- model
- approximation
- measurement

without referring to equations?

---

## Linear Algebra

Can you:

- explain vectors geometrically?
- explain basis?
- explain matrix transformations?
- implement them using NumPy?

---

## Atomic Bonding

Can you explain:

- metallic bonding?
- ionic bonding?
- covalent bonding?

Can you relate bonding to material properties?

---

## Crystal Structures

Can you:

- distinguish FCC, BCC, and HCP?
- explain unit cell vs. lattice?
- generate simple structures in Python?

---

## Thermodynamics

Can you explain:

- Gibbs free energy?
- equilibrium?
- entropy?

without using memorized formulas?

---

# Exit Criteria

Proceed to Module 01 only if you can:

- explain the relationship between atomic structure and material properties
- explain Gibbs free energy conceptually
- distinguish FCC, BCC, and HCP
- perform basic NumPy linear algebra comfortably
- explain why statistical mechanics is needed before Molecular Dynamics
- read introductory computational materials literature without feeling overwhelmed

---

# Common Mistakes

Do not:

- memorize equations
- solve hundreds of textbook exercises
- read entire textbooks sequentially
- optimize for speed
- chase mathematical rigor before intuition

Optimize for understanding.

---

# Relationships

## Supports Roadmap

- Module 01 — Foundations of Materials Science
- Module 03 — Thermodynamics
- Module 05 — Crystallography
- Module 06 — Electronic Structure

## Related Domains

- Foundations of Materials Science
- Crystallography
- Scientific Computing

## Primary Resources

- Callister
- 3Blue1Brown
- MIT 3.091

---

# Estimated Duration

Approximately **4 weeks**

assuming **10–15 focused hours per week**.

Advance based on mastery, not time.

---

# Continue With

**Module 01 — Foundations of Materials Science**