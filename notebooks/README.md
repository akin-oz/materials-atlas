# Materials Atlas notebooks

The notebooks are interactive scientific learning documents. Each one joins a focused scientific question to its explanation, executable calculation, visual evidence, and interpretation.

## Philosophy

Materials Atlas uses notebooks as reproducible laboratory records—not as loose coding scratchpads. A reader should be able to understand why a calculation exists, run it from a clean Kernel, inspect the result, and connect it to the wider materials-science curriculum.

Each major concept follows a consistent learning rhythm:

1. Theory and motivation
2. Plain-language explanation
3. Small executable example
4. A learner experiment
5. Reflection
6. A Materials Atlas connection

## Execution order

Run each notebook from top to bottom. Before sharing work or trusting a result, restart the Kernel and use **Run All**. This verifies that the notebook declares its imports, defines every variable before use, and does not rely on hidden execution state.

Code cells must execute successfully in a clean environment. When demonstrating an error, catch it or place it in an explicitly learner-run experiment so that a full top-to-bottom execution remains successful.

Install the notebook dependencies with `uv sync`, then launch the interactive environment with `uv run jupyter lab`. The notebooks use the project environment so their declared NumPy and Matplotlib dependencies remain reproducible.

## Relationship to Markdown documentation

Markdown roadmaps and references remain the canonical Atlas documentation: they own stable definitions, curriculum sequence, and curated context. Notebooks complement that material by making a focused concept executable and observable. A notebook should link learners back to the relevant Atlas context rather than duplicate a broad reference page.

## Naming convention

Notebooks live in a curriculum area and begin with a zero-padded sequence number:

```text
notebooks/<area>/00-topic-name.ipynb
```

For example, `foundations/00-python-environment.ipynb` comes before `foundations/01-linear-algebra.ipynb`. The number communicates the intended learning order; the kebab-case topic name communicates the subject at a glance.

## Current progression

1. `foundations/00-python-environment.ipynb` — the Jupyter workflow and reproducible scientific computing habits.
2. `foundations/01-linear-algebra.ipynb` — vectors, transformations, linear systems, and the mathematical language used throughout the Atlas.
3. `foundations/02-atomic-bonding.ipynb` — energy landscapes, interatomic interactions, and the physical origin of material structure and properties.
4. `foundations/03-crystal-structures.ipynb` — lattices, bases, packing, orientation, and the structural input used by atomistic workflows.
5. `foundations/04-thermodynamics.ipynb` — the next planned notebook, introducing stability, energy, entropy, and equilibrium.

## Expected quality

Every notebook should read as a polished interactive textbook chapter. Keep cells focused, explain before coding, use Markdown for scientific narrative, label figures and units, and use Mermaid diagrams only when they reduce cognitive load. Explain not only *how* something works but also *why it matters* and *where it returns* in computational materials science.

## Place in the Atlas curriculum

Notebooks turn the roadmaps and reference material into practiced computational understanding. They begin with the Jupyter workflow, then build the mathematical, physical, and software foundations needed for atomistic simulation, thermodynamics, electronic structure, and materials informatics.
