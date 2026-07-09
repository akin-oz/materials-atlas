# Learning Roadmap

This roadmap defines the high-level learning progression for Materials Atlas.

It is not a bibliography. It does not list papers, books, courses, software, datasets, or videos. Those belong in curated domain pages and secondary resource indexes.

The purpose of this file is to explain the sequence of understanding a learner should build when entering Computational Materials Science, Materials Informatics, Scientific Software Engineering, and AI for Materials.

## 1. Modern Materials Science

Objective: Build the scientific foundation needed to reason about materials across composition, structure, processing, properties, performance, and failure.

Why it exists: Computational methods do not replace materials science judgment. A simulation result, model prediction, or dataset entry only becomes meaningful when connected to thermodynamics, kinetics, crystallography, defects, microstructure, phase transformations, and structure-property relationships.

Prerequisites: General chemistry, introductory physics, calculus, and introductory materials science.

Expected outcome: The learner can explain how atomic structure, microstructure, defects, interfaces, thermodynamics, kinetics, and processing history influence material behavior.

Exit criteria: The learner can read a materials science paper and identify the material system, governing phenomena, measured or predicted properties, processing route, relevant length scales, and likely sources of uncertainty.

Relationship to later stages: This stage supplies the physical interpretation needed for every later stage. Without it, computational materials becomes numerical output, materials informatics becomes pattern matching, and AI for materials becomes ungrounded prediction.

Canon connections: Read foundational materials science and thermodynamics before treating simulations or datasets as evidence. This stage leads to Statistical Mechanics, CALPHAD, Phase-Field, Molecular Dynamics, and Density Functional Theory.

## 2. Scientific Computing

Objective: Build the computational foundation required to implement, run, inspect, and trust numerical work.

Why it exists: Computational materials research depends on numerical methods, software environments, data pipelines, reproducibility, and performance constraints. A researcher must understand not only what a method claims to calculate, but how computation can fail.

Prerequisites: Programming fundamentals, linear algebra, calculus, and basic probability.

Expected outcome: The learner understands numerical error, discretization, optimization, linear algebra, data handling, version control, testing, reproducibility, the Scientific Python ecosystem, and the practical limits of computation.

Exit criteria: The learner can write and review scientific code, use NumPy and SciPy as basic research tools, reproduce a computational result, inspect numerical assumptions, manage computational data, and distinguish implementation errors from model limitations.

Relationship to later stages: This stage is the engineering substrate for simulation, workflow automation, data curation, machine learning, and open source scientific software. Domain-specific materials tools should be learned after this layer, not before it.

Canon connections: Read after Modern Materials Science. Use Scientific Python, Git, reproducibility, provenance, FAIR principles, scientific workflows, and HPC awareness as the base layer before domain-specific software. This stage leads to simulation engines, workflow systems, and reproducible data platforms.

## 3. Computational Materials

Objective: Understand how computation is used to model materials across electronic, atomistic, mesoscale, and continuum scales.

Why it exists: Computational Materials Science is not one method. It is a set of approximations and models tied to different length scales, time scales, and physical assumptions. A useful practitioner must know which method answers which kind of question.

Prerequisites: Modern materials science, scientific computing, thermodynamics, kinetics, and basic quantum and statistical mechanics.

Expected outcome: The learner can distinguish major computational approaches, understand what each method predicts, and recognize when a method is appropriate or inappropriate.

Exit criteria: The learner can place electronic structure, molecular dynamics, Monte Carlo, CALPHAD, phase-field modeling, and continuum simulation within a multiscale materials context and explain the assumptions behind each.

Relationship to later stages: This stage provides the source of many datasets, descriptors, labels, workflows, and scientific constraints used in materials informatics and AI for materials.

Canon connections: Read after Scientific Computing and the relevant physics. Connect statistical mechanics to Metropolis, Verlet, Molecular Dynamics, and LAMMPS. Connect electronic structure to Hohenberg-Kohn, Kohn-Sham, PBE, VASP, and Quantum ESPRESSO. Connect thermodynamics and kinetics to CALPHAD, Thermo-Calc, pycalphad, and Phase-Field.

## 4. Materials Informatics

Objective: Understand how data, descriptors, databases, statistics, and machine learning are used to organize and accelerate materials research.

Why it exists: Modern materials research increasingly depends on structured data and computational screening. Materials informatics connects physical knowledge, computed or experimental data, and statistical modeling into a research workflow.

Prerequisites: Computational materials, statistics, data modeling, and practical programming experience.

Expected outcome: The learner can reason about materials datasets, feature representations, labels, model evaluation, data quality, bias, uncertainty, and the relationship between physical insight and statistical prediction.

Exit criteria: The learner can evaluate a materials informatics study by inspecting its data source, representation, validation strategy, baseline comparisons, uncertainty treatment, and scientific claim.

Relationship to later stages: This stage is the bridge from classical computational materials to AI for materials. It teaches the data discipline required before larger models or autonomous workflows can be trusted.

Canon connections: Read after Computational Materials. Connect Materials Project, pymatgen, matminer, JARVIS, OQMD, AFLOW, NOMAD, and Materials Cloud to the question of how computed results become reusable data. This stage leads from descriptors and tabular learning toward graph representations.

## 5. AI for Materials

Objective: Understand how modern AI methods are applied to materials discovery, property prediction, inverse design, synthesis planning, autonomous laboratories, and scientific software.

Why it exists: AI methods are changing how materials hypotheses are generated, screened, and connected to experiments. They also introduce new failure modes: data leakage, weak benchmarks, poor uncertainty estimates, and predictions detached from synthesis or deployment constraints.

Prerequisites: Materials informatics, machine learning fundamentals, scientific computing, and domain-specific materials knowledge.

Expected outcome: The learner can distinguish useful AI applications from weak automation, evaluate claims about model performance, and understand how AI systems interact with physical models and experimental constraints.

Exit criteria: The learner can assess an AI-for-materials paper by examining the task definition, dataset provenance, model architecture, validation regime, uncertainty treatment, baseline quality, and evidence of scientific usefulness.

Relationship to later stages: This stage prepares the learner to evaluate emerging research, build responsible tools, and specialize in discovery workflows, learned potentials, inverse design, or autonomous materials research.

Canon connections: Read after Materials Informatics and machine learning foundations. Follow the historical route from descriptors to CGCNN, MEGNet, M3GNet, CHGNet, and then MatterGen or GNoME. Connect MatGL to graph models and learned interatomic potentials.

## 6. Research Practice

Objective: Learn how computational materials research is evaluated, reproduced, communicated, and connected to the broader scientific literature.

Why it exists: The field is too large to navigate by search results alone. Researchers need to identify canonical work, understand citation lineages, evaluate novelty, reproduce claims, and recognize the difference between durable contributions and short-term trends. They also need research infrastructure habits: Git, provenance, FAIR data principles, scientific workflows, and awareness of high-performance computing constraints.

Prerequisites: Experience reading papers, running code, and understanding at least one computational materials domain.

Expected outcome: The learner can follow citation trails, identify central papers and groups, evaluate methods, reproduce results where possible, track provenance, reason about workflow design, and separate scientific contribution from presentation quality.

Exit criteria: The learner can produce a research map for a narrow topic, identify leading groups and tools, explain unresolved questions, describe what evidence would change the field's understanding, and inspect whether a computational result is reproducible in principle.

Relationship to later stages: This stage turns technical literacy into research judgment. It supports specialization, contribution to open source, and responsible use of AI-driven claims.

Canon connections: Read after using at least one simulation or data workflow. Connect Git, provenance, FAIR principles, scientific workflows, AiiDA, Materials Cloud, NOMAD, and HPC awareness to reproducible computational evidence.

## 7. Open Source

Objective: Learn how scientific software is built, maintained, reviewed, cited, and used by research and industry communities.

Why it exists: Much of Computational Materials Science runs on open source infrastructure. Understanding the software ecosystem is necessary for reproducibility, collaboration, method development, and long-term research credibility.

Prerequisites: Scientific computing, version control, software engineering fundamentals, and familiarity with at least one materials software ecosystem.

Expected outcome: The learner understands contribution workflows, testing, documentation, licensing, citation, reproducibility, governance, and the social structure of scientific software projects.

Exit criteria: The learner can make a meaningful contribution to an open source scientific software project or evaluate whether a project is healthy enough to depend on for research.

Relationship to later stages: This stage converts learning into participation. It also provides a practical route into the field for software engineers who can improve tools, workflows, documentation, testing, and reproducibility.

Canon connections: Read after Scientific Computing and Research Practice. Connect pymatgen, ASE, matminer, MatGL, atomate2, jobflow, custodian, AiiDA, and FireWorks to contribution pathways in scientific software.

## 8. Specialization

Objective: Move from broad literacy to depth in a specific domain, method, material class, or research problem.

Why it exists: The field is too broad for undirected mastery. A researcher eventually needs a defensible position in a narrower area, including its history, methods, tools, datasets, institutions, and open problems.

Prerequisites: The earlier stages of the roadmap and enough research practice to navigate primary literature independently.

Expected outcome: The learner develops a coherent understanding of one area and can explain its technical foundations, standard tools, leading groups, industrial relevance, and unresolved questions.

Exit criteria: The learner can define a credible research or engineering direction, choose appropriate methods, identify important resources, and explain how the area connects to the wider materials ecosystem.

Relationship to later stages: Specialization is not the end of the roadmap. It is the point where the learner begins contributing back to the map through research, software, datasets, reviews, or careful curation.

Canon connections: Read after the earlier stages. Use domains as the primary navigation: Density Functional Theory, Molecular Dynamics, Statistical Mechanics, CALPHAD, Phase-Field, Computational Materials, Materials Informatics, AI for Materials, Scientific Computing, and Research Infrastructure.
