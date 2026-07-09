# Software

This index maps foundational software and infrastructure in Computational Materials Science and Materials Informatics.

Software is included when it enables important research workflows, anchors a community, or teaches how the field is practiced. This is not a package directory.

The ecosystem is organized by layer. A learner should understand the difference between a simulation engine, a scientific library, a workflow system, and a data platform. Confusing these layers makes the field harder to navigate.

## How Layers Interact

Software should be read as workflows, not as a flat list:

- High-throughput DFT: VASP or Quantum ESPRESSO leads to custodian, atomate2 or AiiDA, then Materials Project, OQMD, AFLOW, NOMAD, or Materials Cloud.
- Programmatic materials analysis: Scientific Python leads to pymatgen, then phase diagrams, structure analysis, Materials Project data, and workflow construction.
- Atomistic simulation: Statistical Mechanics leads to LAMMPS and ASE, then learned interatomic potentials, MatGL, M3GNet, CHGNet, and AI for Materials.
- Computational thermodynamics: Thermodynamics leads to CALPHAD, then Thermo-Calc or pycalphad, then alloy design and phase stability workflows.
- Reproducible computation: Git, provenance, FAIR principles, HPC awareness, and scientific workflows lead to AiiDA, Materials Cloud, NOMAD, and publishable computational evidence.

## Scientific Python Foundation

Before domain-specific materials software, a learner should understand the Scientific Python ecosystem.

NumPy and SciPy are not materials packages, but they are part of the computational substrate. NumPy provides array programming and numerical data structures. SciPy provides numerical algorithms for optimization, linear algebra, interpolation, integration, signal processing, and statistics.

Why it matters: Most Python-based materials tools assume fluency with arrays, numerical routines, data structures, and reproducible scripting. Without this layer, domain-specific libraries become black boxes.

When to learn: During Scientific Computing, before depending heavily on pymatgen, ASE, matminer, workflow systems, or machine learning libraries.

Related domains: Scientific Computing, Research Infrastructure.

## Research Infrastructure Practices

Git, reproducibility, provenance, FAIR principles, scientific workflows, and HPC awareness are foundational practices in modern computational materials research.

They are not DevOps topics in this atlas. They matter because computational materials results are produced through code, inputs, dependencies, workflows, databases, schedulers, and analysis scripts. A calculation that cannot be traced, rerun, inspected, or shared is weak scientific evidence.

When to learn: Alongside Scientific Computing and before large calculation campaigns, high-throughput screening, or collaborative software work.

Conceptual gap without them: The learner can produce results but cannot evaluate whether those results are reproducible, reusable, auditable, or suitable for long-term scientific use.

Related domains: Research Infrastructure, Scientific Computing.

## Layer 1: Simulation Engines

Simulation engines perform the scientific calculations. They encode physical models, numerical methods, approximations, and performance tradeoffs.

### VASP

Purpose: A production electronic-structure code widely used for density functional theory calculations in materials research.

Why it matters: VASP is one of the dominant DFT engines in academic and industrial computational materials work. Many high-throughput datasets, papers, and workflows assume familiarity with its calculation model and outputs.

When to learn: After DFT foundations and before interpreting production first-principles workflows.

Conceptual gap without it: The learner misses one of the main production environments behind modern DFT-based materials research.

Typical users: Computational materials researchers running first-principles calculations for structure, stability, defects, surfaces, electronic properties, and screening workflows.

Prerequisites: DFT fundamentals, solid-state physics, HPC awareness, and practical understanding of convergence, pseudopotentials, k-points, and exchange-correlation choices.

Related domains: Density Functional Theory, Computational Materials.

Leads to: custodian, atomate2, Materials Project, OQMD, AFLOW.

### Quantum ESPRESSO

Purpose: An open-source suite for plane-wave electronic-structure calculations.

Why it matters: Quantum ESPRESSO is a canonical open-source DFT ecosystem. It gives learners a transparent route into plane-wave DFT practice and a widely used platform for method development and reproducible research.

When to learn: After DFT foundations, especially when open-source electronic-structure workflows or method development matter.

Conceptual gap without it: The learner sees DFT mainly through closed production software and misses a central open-source ecosystem.

Typical users: Researchers, students, and developers working with electronic structure, phonons, materials properties, and DFT-based workflows.

Prerequisites: DFT fundamentals, solid-state physics, command-line workflows, and HPC basics.

Related domains: Density Functional Theory, Computational Materials, Research Infrastructure.

Leads to: ASE, AiiDA, Materials Cloud, NOMAD.

### LAMMPS

Purpose: A molecular dynamics engine for classical atomistic and coarse-grained simulations.

Why it matters: LAMMPS is foundational for large-scale molecular dynamics in materials, soft matter, mechanics, and learned-potential workflows. It represents the atomistic simulation layer that complements electronic-structure engines.

When to learn: After statistical mechanics and molecular dynamics foundations.

Conceptual gap without it: The learner lacks a practical anchor for classical atomistic simulation at scales beyond first-principles methods.

Typical users: Researchers modeling deformation, diffusion, phase behavior, interfaces, polymers, fluids, and atomistic mechanisms at scales beyond first-principles methods.

Prerequisites: Statistical mechanics, molecular dynamics, interatomic potentials, and basic HPC awareness.

Related domains: Molecular Dynamics, Statistical Mechanics, Computational Materials.

Leads to: ASE, MatGL, learned interatomic potentials, AI for Materials.

### Thermo-Calc

Purpose: A commercial platform for CALPHAD-based thermodynamic and kinetic calculations.

Why it matters: Thermo-Calc represents industrial-strength computational thermodynamics. It is important for understanding how phase diagrams, phase stability, and thermodynamic databases are used in alloy and process design.

When to learn: After thermodynamics, phase diagrams, and CALPHAD foundations.

Conceptual gap without it: The learner misses how computational thermodynamics is used in industrial and applied alloy design.

Typical users: Alloy designers, computational thermodynamics researchers, process engineers, and industrial materials teams.

Prerequisites: Thermodynamics, phase diagrams, phase transformations, and CALPHAD concepts.

Related domains: CALPHAD, Computational Materials.

Leads to: alloy design, phase stability, industrial computational thermodynamics.

### pycalphad

Purpose: An open-source Python library for CALPHAD calculations.

Why it matters: pycalphad makes computational thermodynamics programmable and inspectable. It complements Thermo-Calc by exposing CALPHAD concepts within the Scientific Python ecosystem.

When to learn: After CALPHAD foundations and basic Scientific Python.

Conceptual gap without it: The learner lacks an open, scriptable route into computational thermodynamics.

Typical users: Researchers, students, and software developers who need open, scriptable thermodynamic calculations.

Prerequisites: Thermodynamics, phase equilibria, Python, and CALPHAD concepts.

Related domains: CALPHAD, Scientific Computing.

Leads to: scriptable thermodynamic calculations and reproducible phase stability analysis.

## Layer 2: Scientific Libraries

Scientific libraries provide reusable analysis, representation, modeling, and machine learning capabilities. They do not replace simulation engines; they help researchers prepare inputs, analyze outputs, build models, and connect workflows.

### pymatgen

Purpose: A Python library for materials analysis, structure manipulation, input/output handling, and workflows around computed materials data.

Why it matters: pymatgen is one of the central programming foundations of the modern materials informatics ecosystem.

Typical users: Researchers writing analysis scripts, workflow developers, database users, and scientific software engineers.

Prerequisites: Python, basic crystallography, and familiarity with materials structures and computed properties.

Related domains: Materials Informatics, Computational Materials, Scientific Computing.

Leads to: Materials Project, atomate2, matminer, phase diagram analysis.

### ASE

Purpose: The Atomic Simulation Environment provides Python tools for setting up, running, and analyzing atomistic simulations across multiple calculators.

Why it matters: ASE is a flexible interface layer for atomistic modeling and is widely used across simulation, workflow, and machine learning contexts.

Typical users: Atomistic simulation researchers, computational chemists, materials scientists, and developers connecting calculators to workflows.

Prerequisites: Python, atomistic simulation concepts, and basic knowledge of the calculator or simulation engine being used.

Related domains: Molecular Dynamics, Computational Materials, Scientific Computing.

Leads to: LAMMPS workflows, calculator interfaces, machine-learning potentials.

### matminer

Purpose: A toolkit for materials data mining, feature generation, dataset access, and machine learning workflows.

Why it matters: matminer helped standardize practical materials informatics workflows and made feature-based machine learning more accessible.

Typical users: Materials informatics researchers, students, and data scientists working with materials datasets.

Prerequisites: Python, pandas-style data analysis, basic machine learning, and materials descriptors.

Related domains: Materials Informatics, AI for Materials.

Leads to: descriptor-based learning, CGCNN-era representation learning, model evaluation.

### MatGL

Purpose: A library for graph deep learning models for materials, including machine-learning interatomic potentials and property prediction models.

Why it matters: MatGL represents the connection between materials graph representations, deep learning, and practical materials modeling workflows.

Typical users: AI-for-materials researchers, materials informatics practitioners, and developers using graph neural networks for materials tasks.

Prerequisites: Machine learning fundamentals, Python, materials structures, and enough atomistic modeling knowledge to interpret predictions.

Related domains: AI for Materials, Materials Informatics, Molecular Dynamics.

Leads to: graph neural networks, learned interatomic potentials, M3GNet and CHGNet.

## Layer 3: Workflow Systems

Workflow systems organize calculations into reproducible, inspectable, and recoverable computational campaigns. They are research infrastructure, not scientific models by themselves.

### atomate2

Purpose: A workflow library for running complex materials simulations, especially around modern Materials Project-style workflows.

Why it matters: atomate2 represents the move from one-off calculations to structured, reproducible, automated computational materials workflows.

Typical users: Researchers running high-throughput calculations, workflow maintainers, and computational materials groups.

Prerequisites: pymatgen, workflow concepts, jobflow, and practical experience with electronic structure or atomistic calculations.

Related domains: Research Infrastructure, Density Functional Theory, Materials Informatics.

Leads to: Materials Project-style high-throughput workflows.

### jobflow

Purpose: A Python framework for defining and executing computational workflows as jobs and flows.

Why it matters: jobflow provides workflow abstractions used by modern materials automation tools, including atomate2.

Typical users: Workflow developers, computational researchers, and scientific software engineers building reusable calculation pipelines.

Prerequisites: Python, serialization concepts, and experience with computational workflows.

Related domains: Research Infrastructure, Scientific Computing.

Leads to: atomate2 and reusable workflow design.

### custodian

Purpose: A tool for error handling, monitoring, and recovery in high-throughput computational workflows.

Why it matters: High-throughput materials computation requires automatic handling of common failures. custodian encodes practical operational knowledge that makes large calculation campaigns more reliable.

Typical users: Researchers running many electronic structure calculations and developers maintaining automated workflows.

Prerequisites: Familiarity with the target simulation code, typical failure modes, and workflow execution.

Related domains: Research Infrastructure, Density Functional Theory.

Leads to: resilient high-throughput DFT workflows.

### AiiDA

Purpose: A workflow and provenance platform for automated, reproducible computational science.

Why it matters: AiiDA emphasizes provenance, data lineage, and reproducibility, which are central problems in computational materials research.

Typical users: Computational materials groups, workflow developers, and researchers who need rigorous provenance tracking.

Prerequisites: Scientific computing, workflow concepts, databases at a practical level, and the simulation codes being automated.

Related domains: Research Infrastructure, Computational Materials.

Leads to: provenance-aware workflows and reproducible computational campaigns.

### FireWorks

Purpose: A workflow management system for defining, executing, and tracking large numbers of computational jobs.

Why it matters: FireWorks has been important in high-throughput computational materials workflows and the broader Materials Project ecosystem.

Typical users: Researchers and groups running automated calculation campaigns on local clusters or high-performance computing systems.

Prerequisites: Python, batch computing, workflow concepts, and practical experience with the calculations being automated.

Related domains: Research Infrastructure, Materials Informatics.

Leads to: high-throughput materials campaigns and Materials Project-style automation.

## Layer 4: Data Platforms

Data platforms organize computed or curated materials data for search, comparison, reuse, and reproducibility. They complement each other through different workflows, coverage, provenance models, and community histories.

### Materials Project

Purpose: A large-scale computed materials database and platform for materials discovery.

Why it matters: Materials Project made high-throughput computed materials data broadly usable and helped define modern database-driven computational materials research.

Typical users: Materials researchers, computational scientists, data scientists, students, and software engineers building tools on computed materials data.

Prerequisites: Basic materials science, crystallography concepts, and familiarity with computed properties such as formation energy, stability, band gap, and structure.

Related domains: Materials Informatics, Density Functional Theory, Research Infrastructure.

Implemented by: high-throughput DFT workflows, pymatgen, atomate lineage, workflow infrastructure.

### Materials Cloud

Purpose: A platform for sharing, discovering, and reproducing computational materials data and workflows.

Why it matters: Materials Cloud emphasizes reproducibility, provenance, and published computational results, making it important for research practice and data stewardship.

Typical users: Computational materials researchers, workflow developers, and readers trying to inspect or reproduce published computational work.

Prerequisites: Computational materials basics, workflow concepts, and enough domain knowledge to interpret archived data.

Related domains: Research Infrastructure, Computational Materials.

Leads to: reproducible data publication and provenance-aware research.

### JARVIS

Purpose: A materials data and tools ecosystem focused on computed properties, datasets, and materials design workflows.

Why it matters: JARVIS is an important complement to other computed materials data platforms, especially for learners comparing databases, workflows, and property coverage.

Typical users: Computational materials researchers, data-driven materials scientists, and AI-for-materials practitioners.

Prerequisites: Materials science foundations, computed materials data concepts, and Python for programmatic use.

Related domains: Materials Informatics, AI for Materials.

Leads to: comparison of computed data ecosystems and AI-ready datasets.

### OQMD

Purpose: A high-throughput database of computed materials thermodynamics and crystal structures.

Why it matters: OQMD provides an independent pillar of computed formation energies and phase stability data. It complements Materials Project by giving learners another major view of high-throughput DFT thermodynamics.

When to learn: After Materials Project and phase stability concepts, when comparing high-throughput thermodynamic data sources.

Conceptual gap without it: The learner may mistake one database's choices and coverage for the whole computed thermodynamics landscape.

Typical users: Researchers studying phase stability, compound discovery, alloy spaces, and high-throughput thermodynamic screening.

Prerequisites: DFT-derived formation energies, phase stability, convex hulls, and basic crystallography.

Related domains: Materials Informatics, Density Functional Theory, CALPHAD.

Leads to: phase stability comparison across computed data platforms.

### AFLOW

Purpose: A high-throughput computational materials framework and database.

Why it matters: AFLOW is one of the major early high-throughput materials data ecosystems. It complements Materials Project by representing a distinct infrastructure lineage, data model, and automation approach.

When to learn: After understanding high-throughput DFT databases and before comparing materials data ecosystems.

Conceptual gap without it: The learner misses a major independent lineage in automated materials computation.

Typical users: Computational materials researchers, data-driven materials scientists, and users comparing high-throughput property datasets.

Prerequisites: Computed materials data concepts, DFT properties, and awareness of high-throughput screening workflows.

Related domains: Materials Informatics, Density Functional Theory.

Leads to: comparison of independent high-throughput DFT infrastructures.

### NOMAD

Purpose: A platform for collecting, normalizing, and sharing computational materials science data across codes and workflows.

Why it matters: NOMAD addresses a different problem from a single curated database: broad data aggregation, metadata, normalization, and reuse across computational materials outputs. It is central to provenance and FAIR data practice.

When to learn: During research practice, especially when studying reproducibility, metadata, and cross-code data reuse.

Conceptual gap without it: The learner misses the infrastructure problem of making heterogeneous computational materials data reusable beyond one database or code.

Typical users: Researchers publishing or reusing computational data, infrastructure developers, and groups concerned with metadata, reproducibility, and data stewardship.

Prerequisites: Computational materials basics, metadata concepts, provenance, and familiarity with simulation outputs.

Related domains: Research Infrastructure, Materials Informatics.

Leads to: FAIR computational data, cross-code normalization, and reusable simulation archives.
