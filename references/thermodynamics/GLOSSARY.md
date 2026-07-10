# Thermodynamics & Statistical Mechanics Glossary

> Plain-language definitions for recurring thermodynamics and statistical mechanics concepts.

---

# Purpose

This glossary defines recurring terms used across thermodynamics, statistical mechanics, Molecular Dynamics, CALPHAD, and Phase-Field modules.

Definitions should be short, stable, and useful.

This is not a textbook.

---

# Terms

## Internal Energy

The total energy stored inside a system.

Used as the starting point for many thermodynamic potentials.

## Enthalpy

Internal energy plus pressure-volume work.

Useful for systems at approximately constant pressure.

## Entropy

A measure of the number of microscopic states compatible with a macroscopic state.

Do not reduce entropy to "disorder."

## Helmholtz Free Energy

Thermodynamic potential minimized at constant temperature and volume.

Often relevant to atomistic simulations.

## Gibbs Free Energy

Thermodynamic potential minimized at constant temperature and pressure.

Central to phase stability and phase diagrams.

## Chemical Potential

The change in free energy associated with adding particles.

Important for diffusion, phase equilibrium, defects, and electrochemistry.

## Microstate

A complete microscopic configuration of a system.

Includes atomic positions, momenta, or other microscopic degrees of freedom depending on context.

## Macrostate

A macroscopic description of a system.

Examples include temperature, pressure, volume, and composition.

Many microstates can correspond to the same macrostate.

## Ensemble

A collection of possible microstates consistent with specified macroscopic constraints.

Examples:

- NVE
- NVT
- NPT

## Partition Function

A mathematical object that sums over weighted microstates.

It connects microscopic physics to macroscopic thermodynamics.

## Boltzmann Distribution

Probability distribution that describes how likely states are at a given temperature.

Lower-energy states are more likely, but higher-energy states can still occur.

## Free Energy

Energy adjusted for entropy and thermodynamic constraints.

Different free energies apply under different conditions.

## Equilibrium

A state where the relevant thermodynamic potential is minimized under the imposed constraints.

## Phase Stability

Whether a phase is thermodynamically favored under given conditions.

Usually determined by comparing free energies.

## Metastability

A state that is not globally stable but remains trapped due to kinetic barriers.

## Driving Force

A free-energy difference that motivates transformation.

Driving force does not determine transformation rate by itself.

## Kinetics

The study of rates and pathways.

Thermodynamics says what is favored.

Kinetics says how fast it happens.

## Phase Diagram

A map of stable phases as a function of variables such as temperature, composition, and pressure.

## Common Tangent

A graphical construction used to determine phase coexistence from free-energy curves.

## Ensemble Average

The average value of a property over sampled microscopic states.

Used to connect simulations to macroscopic observables.

## Sampling

The process of exploring microscopic states.

Molecular Dynamics and Monte Carlo are two common sampling methods.

---

# Editorial Rule

Add a term only if it appears in multiple modules or reference pages.

Do not add one-off definitions.

