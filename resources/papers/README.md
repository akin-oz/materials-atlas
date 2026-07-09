# Papers

This index is not a long bibliography.

Papers enter Materials Atlas when they help explain the structure of a domain, the origin of a method, the credibility of a tool, the construction of a dataset, or a change in research practice.

The goal is not to collect many papers. The goal is to identify which papers a researcher must understand and why.

## Conceptual Routes

Historical continuity matters because current methods are layered on older ideas:

- Statistical Mechanics leads to Metropolis, Monte Carlo, free-energy methods, and atomistic sampling.
- Molecular Dynamics leads to Verlet, LAMMPS, ASE, learned interatomic potentials, M3GNet, and CHGNet.
- Density Functional Theory leads to Hohenberg-Kohn, Kohn-Sham, PBE, VASP, Quantum ESPRESSO, and high-throughput DFT.
- High-throughput DFT leads to Materials Project, pymatgen, atomate2, OQMD, AFLOW, NOMAD, and Materials Informatics.
- Descriptors lead to matminer, CGCNN, MEGNet, M3GNet, CHGNet, and foundation-model-style AI for Materials.

## Editorial Roles

### Landmark Papers

Landmark papers changed the direction of a field. They may introduce a theory, method, dataset, infrastructure project, or research program that later work depends on.

Landmark status should be earned by lasting influence, not citation count alone.

### Review Papers

Review papers organize a field, clarify terminology, identify open problems, and provide a reliable map of prior work.

A review paper should not be included merely because it is recent. It belongs when it helps a reader understand a domain more clearly than following individual citations alone.

### Software Papers

Software papers document tools that are widely used or methodologically important.

A software paper should explain not only that a package exists, but what scientific workflows it enables and what assumptions it encodes.

### Benchmark Papers

Benchmark papers define evaluation tasks, datasets, baselines, or comparisons that shape how a community measures progress.

Benchmark papers are useful only when their assumptions, limitations, and scope are made clear.

### Perspective Papers

Perspective papers belong when they define a research agenda, synthesize a transition in the field, or make explicit a set of problems that later work responds to.

They should be included sparingly. A perspective paper is useful when it improves judgment, not when it advertises a trend.

## Historical Evolution Anchors

This list is intentionally small. It shows a conceptual progression, not a complete reading program.

### Equation of State Calculations by Fast Computing Machines

Authors: N. Metropolis and collaborators

Why it is canonical: This paper introduced the Monte Carlo method in a form that became foundational for computational statistical mechanics.

When to learn it: After basic statistical mechanics, before serious work with Monte Carlo, sampling, or free-energy methods.

Conceptual gap without it: The learner misses the origin of stochastic sampling as a computational route from microscopic states to thermodynamic behavior.

Category: Landmark and methodology paper.

Related domains: Statistical Mechanics, Molecular Dynamics.

Leads to: Monte Carlo, free-energy methods, atomistic sampling.

### Computer Experiments on Classical Fluids. I. Thermodynamical Properties of Lennard-Jones Molecules

Author: Loup Verlet

Why it is canonical: Verlet's work is a foundational reference for molecular dynamics as numerical experiment, including integration practice and the interpretation of atomistic trajectories.

When to learn it: When moving from statistical mechanics into molecular dynamics.

Conceptual gap without it: Molecular dynamics appears as a software feature rather than a historical method for connecting classical mechanics, simulation, and thermodynamic observables.

Category: Landmark and methodology paper.

Related domains: Molecular Dynamics, Statistical Mechanics.

Implemented by: LAMMPS and other molecular dynamics engines.

### Generalized Gradient Approximation Made Simple

Authors: John P. Perdew, Kieron Burke, and Matthias Ernzerhof

Why it is canonical: PBE is one of the central exchange-correlation approximations in practical DFT materials calculations.

When to learn it: After the Hohenberg-Kohn and Kohn-Sham foundations, before interpreting routine DFT results.

Conceptual gap without it: The learner understands the formal existence of DFT but not the practical approximation that anchors much of modern materials computation.

Category: Methodology paper.

Related domains: Density Functional Theory, Computational Materials.

Implemented by: VASP, Quantum ESPRESSO, and high-throughput DFT workflows.

### Commentary: The Materials Project: A Materials Genome Approach to Accelerating Materials Innovation

Authors: Anubhav Jain and collaborators

Why it is canonical: This paper marks the transition from individual calculations to high-throughput computed materials data as shared research infrastructure.

When to learn it: After basic DFT and before materials informatics or database-driven discovery.

Conceptual gap without it: The learner misses how first-principles calculations became a reusable data platform rather than isolated paper-specific results.

Category: Landmark, software, and infrastructure paper.

Related domains: Materials Informatics, Density Functional Theory, Research Infrastructure.

Related: pymatgen, atomate2, FireWorks, Materials Project, high-throughput DFT.

### Crystal Graph Convolutional Neural Networks for an Accurate and Interpretable Prediction of Material Properties

Authors: Tian Xie and Jeffrey C. Grossman

Why it is canonical: CGCNN is a clear early anchor for graph neural networks on crystal structures, replacing hand-built descriptors with learned structure representations.

When to learn it: After materials informatics basics and before modern graph-based AI for materials.

Conceptual gap without it: The learner misses the shift from feature-engineered materials models to representation learning on crystal graphs.

Category: Landmark and methodology paper.

Related domains: Materials Informatics, AI for Materials.

Leads to: MEGNet and later graph-based materials models.

### Graph Networks as a Universal Machine Learning Framework for Molecules and Crystals

Authors: Chi Chen, Weike Ye, Yunxing Zuo, Chen Zheng, and Shyue Ping Ong

Why it is canonical: MEGNet generalized graph network thinking across molecules and crystals and became an important reference point for materials graph learning.

When to learn it: After CGCNN, when comparing graph architectures and transferable representations.

Conceptual gap without it: The learner misses an important step from crystal-specific graph learning toward broader graph network frameworks in materials and chemistry.

Category: Methodology paper.

Related domains: AI for Materials, Materials Informatics.

Leads to: M3GNet, MatGL, graph neural networks for materials.

### A Universal Graph Deep Learning Interatomic Potential for the Periodic Table

Authors: Chi Chen and Shyue Ping Ong

Why it is canonical: M3GNet connected graph deep learning to interatomic potentials and structural relaxation across broad chemical space.

When to learn it: After graph neural network property prediction and before learned interatomic potentials or AI-accelerated relaxation workflows.

Conceptual gap without it: The learner misses the transition from predicting properties of fixed structures to using learned models as computational engines.

Category: Landmark and methodology paper.

Related domains: AI for Materials, Molecular Dynamics, Materials Informatics.

Leads to: MatGL, CHGNet, learned interatomic potentials.

### CHGNet as a Pretrained Universal Neural Network Potential for Charge-Informed Atomistic Modelling

Authors: Bowen Deng and collaborators

Why it is canonical: CHGNet represents the move toward pretrained neural network potentials that incorporate charge-informed atomistic modeling for broad materials use.

When to learn it: After M3GNet and before evaluating modern universal interatomic potentials.

Conceptual gap without it: The learner misses how learned potentials began to absorb richer physical information and pretrained model practice.

Category: Methodology and benchmark paper.

Related domains: AI for Materials, Molecular Dynamics.

Leads to: pretrained universal potentials and AI-assisted atomistic modeling.

### MatterGen and GNoME

Authors: Microsoft Research and Google DeepMind teams

Why they are canonical: These works represent the current large-scale AI-for-materials turn: generative materials design, massive candidate discovery, and model-driven exploration of inorganic materials space.

When to learn them: After DFT, high-throughput data, materials informatics, and graph neural network foundations.

Conceptual gap without them: The learner misses the shift from prediction and screening toward generative and large-scale AI discovery systems.

Category: Landmark and perspective papers.

Related domains: AI for Materials, Materials Informatics.

Read after: DFT, high-throughput materials data, graph neural networks, and model validation.

## DFT Foundations

These papers remain necessary background for the PBE and high-throughput DFT part of the historical progression.

### Inhomogeneous Electron Gas

Authors: P. Hohenberg and W. Kohn

Why it is canonical: This is one of the foundational papers of density functional theory. It establishes the conceptual basis for treating the ground-state electron density as central.

When to learn it: Before practical DFT, once the learner has enough quantum mechanics to understand the question DFT answers.

Conceptual gap without it: DFT becomes a computational recipe rather than a theory with specific existence claims and limits.

Category: Landmark paper.

Related domains: Density Functional Theory.

Leads to: Kohn-Sham DFT and practical electronic-structure calculation.

### Self-Consistent Equations Including Exchange and Correlation Effects

Authors: W. Kohn and L. J. Sham

Why it is canonical: This paper introduced the Kohn-Sham formulation that made density functional theory computationally practical for many materials problems.

When to learn it: Immediately after Hohenberg-Kohn and before practical plane-wave DFT.

Conceptual gap without it: The learner cannot explain why DFT codes solve effective single-particle equations or where exchange-correlation approximations enter.

Category: Landmark and methodology paper.

Related domains: Density Functional Theory.

Leads to: PBE, VASP, Quantum ESPRESSO, and practical DFT workflows.

## Software Anchors

These papers explain software that became part of the field's working infrastructure.

### Python Materials Genomics: A Robust, Open-Source Python Library for Materials Analysis

Authors: Shyue Ping Ong and collaborators

Why it is canonical: This paper introduced pymatgen as a practical foundation for programmatic materials analysis and many later workflows.

When to learn it: When moving from manual calculation inspection to scripted materials analysis.

Conceptual gap without it: The learner misses how materials structures, entries, phase diagrams, and computed data became programmable objects in Python.

Category: Software paper.

Related domains: Materials Informatics, Scientific Computing, Research Infrastructure.

Leads to: Materials Project workflows, atomate2, matminer, phase diagram analysis.

### Matminer: An Open Source Toolkit for Materials Data Mining

Authors: Logan Ward and collaborators

Why it is canonical: This paper documents one of the central tools for feature generation and machine learning workflows in materials informatics.

When to learn it: When moving from computed datasets to feature-based machine learning.

Conceptual gap without it: The learner misses the practical bridge between materials descriptors, tabular datasets, and machine learning workflows.

Category: Software and methodology paper.

Related domains: Materials Informatics, AI for Materials.

Leads to: descriptor-based materials machine learning and comparison with graph representations.

## Inclusion Criteria

A paper may be added when:

- it is necessary for understanding a domain
- it introduced or clarified an important method
- it shaped a software or data ecosystem
- it provides a durable review of a field
- it defines a benchmark or evaluation practice
- it improves the historical continuity of the atlas
- its importance can be explained in a few precise sentences

If the reason for inclusion is unclear, leave it out.
