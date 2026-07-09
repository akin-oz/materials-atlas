# Books

This index contains books that are useful as long-term foundations or references for Computational Materials Science.

Books are included only when they help build durable understanding. A book is not included because it is popular, recent, or convenient. Most topics should have fewer books, not more.

## Conceptual Navigation

Books are grouped by purpose, but each book also supports one or more conceptual domains:

- Modern materials foundations lead to Computational Materials, CALPHAD, Phase-Field, and Density Functional Theory.
- Scientific Computing leads to Scientific Python, Research Infrastructure, simulation engines, workflows, and machine learning.
- Statistical Mechanics leads to Molecular Dynamics, Monte Carlo, free-energy methods, and LAMMPS.
- Density Functional Theory leads to Hohenberg-Kohn, Kohn-Sham, PBE, VASP, Quantum ESPRESSO, Materials Project, and high-throughput DFT.
- Materials Informatics leads to descriptors, matminer, Materials Project, graph neural networks, and AI for Materials.
- Machine Learning leads to CGCNN, MEGNet, M3GNet, CHGNet, MatterGen, and GNoME.

## Foundations

### Materials Science and Engineering: An Introduction

Authors: William D. Callister Jr. and David G. Rethwisch

Why it matters: This is a broad entry point into structure, processing, properties, and performance. It gives software-oriented learners a common materials vocabulary before they approach computation.

When to read: Early, especially if undergraduate materials knowledge needs review.

Role: Foundational.

Related domains: Modern Materials Science, Computational Materials.

### Physical Metallurgy Principles

Authors: Robert E. Reed-Hill and Reza Abbaschian

Why it matters: Computational materials often depends on metallurgical reasoning about defects, phase transformations, diffusion, and microstructure. This book is useful for rebuilding that physical intuition.

When to read: Early to middle stages, alongside thermodynamics and phase transformations.

Role: Foundational.

Related domains: Modern Materials Science, CALPHAD, Phase-Field.

### Phase Transformations in Metals and Alloys

Authors: David A. Porter, Kenneth E. Easterling, and Mohamed Y. Sherif

Why it matters: Phase transformations connect thermodynamics, kinetics, microstructure, and processing. Many computational methods become more meaningful when the learner understands what transformations they are trying to model.

When to read: Before or during work on CALPHAD, phase-field modeling, solidification, precipitation, or alloy design.

Role: Foundational and reference.

Related domains: Modern Materials Science, CALPHAD, Phase-Field.

## Scientific Computing

### Scientific Computing: An Introductory Survey

Author: Michael T. Heath

Why it matters: The book explains numerical methods in a way that is directly relevant to scientific software: errors, interpolation, linear systems, nonlinear equations, optimization, integration, and differential equations.

When to read: Before relying heavily on simulation codes or implementing numerical methods.

Role: Foundational.

Related domains: Scientific Computing, Research Infrastructure.

### Numerical Linear Algebra

Authors: Lloyd N. Trefethen and David Bau III

Why it matters: Linear algebra is the computational core of electronic structure, optimization, regression, dimensionality reduction, and many machine learning methods.

When to read: During scientific computing, and again when linear algebra becomes a bottleneck in research.

Role: Foundational and reference.

Related domains: Scientific Computing, Density Functional Theory, Materials Informatics, AI for Materials.

### Statistical Mechanics: Theory and Molecular Simulation

Author: Mark Tuckerman

Why it matters: This book provides the missing bridge from thermodynamics to statistical mechanics, molecular dynamics, Monte Carlo, and free-energy methods. It explains why atomistic simulation produces thermodynamic meaning rather than only trajectories.

When to read: After basic thermodynamics and before serious work with molecular dynamics, Monte Carlo, enhanced sampling, or free-energy calculations.

Conceptual gap without it: The learner can run atomistic simulations but cannot explain how microscopic sampling connects to ensembles, thermodynamic averages, and free energy.

Role: Foundational and reference.

Related domains: Statistical Mechanics, Molecular Dynamics.

## Computational Materials

### Introduction to Computational Materials Science

Author: Richard LeSar

Why it matters: This is one of the clearest broad introductions to computational approaches across materials length scales. It helps learners see the field as a set of modeling choices rather than isolated software packages.

When to read: After the foundations of materials science and scientific computing are in place.

Role: Foundational.

Related domains: Computational Materials.

### Understanding Molecular Simulation

Authors: Daan Frenkel and Berend Smit

Why it matters: Molecular simulation is a central language for atomistic modeling. This book explains both the statistical mechanics and the computational practice behind simulation.

When to read: Before serious work with molecular dynamics, Monte Carlo, force fields, or learned interatomic potentials.

Role: Foundational and reference.

Related domains: Statistical Mechanics, Molecular Dynamics.

### Computer Simulation of Liquids

Authors: M. P. Allen and D. J. Tildesley

Why it matters: This is a classic reference for molecular simulation. It remains useful for understanding algorithms, ensembles, correlation functions, and simulation practice.

When to read: As a reference while learning or using atomistic simulation methods.

Role: Reference.

Related domains: Statistical Mechanics, Molecular Dynamics.

### CALPHAD: Calculation of Phase Diagrams

Authors: N. Saunders and A. P. Miodownik

Why it matters: CALPHAD is the canonical computational thermodynamics framework for phase diagrams and phase stability. Without it, the roadmap would name computational thermodynamics without giving learners a durable entry point.

When to read: After thermodynamics and phase transformations, especially before alloy design, phase stability work, or thermodynamic database use.

Conceptual gap without it: The learner misses how thermodynamic models and assessed databases become practical tools for phase stability and alloy design.

Role: Foundational and reference.

Related domains: CALPHAD, Computational Materials.

### Phase-Field Methods in Materials Science and Engineering

Authors: Nikolas Provatas and Ken Elder

Why it matters: Phase-field modeling is a core mesoscale method for microstructure evolution. This book gives the conceptual and mathematical foundation needed to understand how diffuse-interface models connect thermodynamics, kinetics, and morphology.

When to read: After phase transformations, thermodynamics, and numerical methods, especially before work on solidification, precipitation, grain growth, or microstructure evolution.

Conceptual gap without it: The learner lacks a principled route from thermodynamics and kinetics to computational models of evolving microstructure.

Role: Foundational and reference.

Related domains: Phase-Field, Computational Materials.

## Density Functional Theory

### Electronic Structure: Basic Theory and Practical Methods

Author: Richard M. Martin

Why it matters: This is a central bridge between the theory of electronic structure and practical computational methods. It is one of the most important books for understanding what density functional theory codes are doing.

When to read: When moving from using DFT software to understanding DFT methodology.

Role: Foundational and reference.

Related domains: Density Functional Theory, Computational Materials.

### Density Functional Theory: A Practical Introduction

Authors: David S. Sholl and Janice A. Steckel

Why it matters: This book is valuable for learners who need practical orientation before deeper theory. It explains how DFT is used, what choices matter, and how to interpret common outputs.

When to read: At the start of practical DFT work.

Role: Foundational.

Related domains: Density Functional Theory.

### Density-Functional Theory of Atoms and Molecules

Authors: Robert G. Parr and Weitao Yang

Why it matters: This is a deeper theoretical reference for the foundations of density functional theory. It is less about workflow and more about the conceptual structure of the theory.

When to read: After practical exposure to DFT, when theoretical assumptions and limits become important.

Role: Reference.

Related domains: Density Functional Theory.

## Materials Informatics

### Information Science for Materials Discovery and Design

Editors: Turab Lookman, Francis J. Alexander, and Krishna Rajan

Why it matters: This book captures the shift from isolated computation to data-centered materials discovery. It is useful for understanding the intellectual origins of materials informatics.

When to read: When moving from computational materials into data-driven materials research.

Role: Foundational and historical.

Related domains: Materials Informatics, AI for Materials.

## Machine Learning

### The Elements of Statistical Learning

Authors: Trevor Hastie, Robert Tibshirani, and Jerome Friedman

Why it matters: This is a durable reference for supervised learning, model complexity, regularization, validation, and statistical thinking. Those ideas matter more than any specific machine learning trend.

When to read: During materials informatics and before evaluating machine learning claims in papers.

Role: Foundational and reference.

Related domains: Materials Informatics, AI for Materials.

### Pattern Recognition and Machine Learning

Author: Christopher M. Bishop

Why it matters: This book gives a principled treatment of probabilistic modeling and machine learning. It is especially useful for understanding uncertainty, inference, and model assumptions.

When to read: After basic statistics and before deeper work in probabilistic models or uncertainty-aware materials prediction.

Role: Foundational and reference.

Related domains: Materials Informatics, AI for Materials.

### Deep Learning

Authors: Ian Goodfellow, Yoshua Bengio, and Aaron Courville

Why it matters: This is a durable reference for neural network fundamentals. It is useful for understanding the vocabulary and basic mechanisms behind many AI-for-materials papers.

When to read: Before working seriously with graph neural networks, learned potentials, generative models, or modern AI systems.

Role: Reference.

Related domains: AI for Materials.

## Reference Books

### Solid State Physics

Authors: Neil W. Ashcroft and N. David Mermin

Why it matters: Solid-state physics underlies electronic structure, crystal behavior, phonons, bands, and many properties computed in materials research.

When to read: As a reference while studying DFT, electronic materials, phonons, defects, or transport.

Role: Reference.

Related domains: Density Functional Theory, Computational Materials.

### Introduction to Solid State Physics

Author: Charles Kittel

Why it matters: This is a compact classical reference for the vocabulary and basic models of solid-state physics.

When to read: As a companion reference when solid-state concepts appear in computational materials work.

Role: Reference.

Related domains: Density Functional Theory, Computational Materials.

### Thermodynamics in Materials Science

Author: Robert T. DeHoff

Why it matters: Thermodynamics is the language behind phase stability, phase diagrams, defects, interfaces, and many computed materials properties.

When to read: Before or during work on phase stability, CALPHAD, defects, alloy design, or high-throughput thermodynamic screening.

Role: Foundational and reference.

Related domains: CALPHAD, Phase-Field, Computational Materials.
