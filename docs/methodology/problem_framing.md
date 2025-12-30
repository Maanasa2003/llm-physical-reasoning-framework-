# Problem Framing

## 1. Motivation
Large Language Models (LLMs) have demonstrated impressive capabilities in language understanding, reasoning, and generalisation. However, their ability to perform physical reasoning—understanding how objects behave, interact, and evolve in the real world—remains poorly understood. Physical reasoning is foundational for robotics, embodied AI, simulation‑based planning, safety‑critical decision‑making, and scientific discovery.
Despite its importance, current evaluations are fragmented, dataset‑specific, and inconsistent. There is no unified framework that tests LLMs across multiple dimensions of physical reasoning. This project addresses that gap.

## 2. Core Problem
LLMs are trained on text, not physics.  
They learn correlations, not causal dynamics.  
They can describe the world, but can they predict it?
The central question becomes:
Can LLMs demonstrate consistent, generalisable physical reasoning across diverse tasks that require understanding of causality, dynamics, and intuitive physics?
To answer this, we need a systematic, multi‑dataset evaluation pipeline that tests:
- physical commonsense
- causal reasoning
- counterfactual reasoning
- intuitive physics
- multi‑body interactions
- stability and motion prediction
No single dataset captures all of these dimensions.  
But together, they form a comprehensive benchmark.

## 3. Research Gap
Existing evaluations suffer from three limitations:
#### A. Fragmentation
Each dataset has its own format, metrics, and evaluation logic, making cross‑dataset comparison nearly impossible.
#### B. Narrow Scope
Most benchmarks test only one aspect of physical reasoning (e.g., PIQA tests commonsense, CLEVRER tests causality). Real‑world reasoning requires all of them.
#### C. Lack of Unified Pipeline
There is no open, reproducible framework that:
- loads datasets consistently
- preprocesses them into a unified format
- evaluates models with standardized prompts
- aggregates results
- analyzes failure modes
This project will try to fill this gap.

## 4. Problem Statement
LLMs lack a unified, systematic evaluation framework for physical reasoning across diverse tasks.
This project aims to build a modular, reproducible pipeline that evaluates LLMs on:
- physical commonsense (PIQA)
- causal reasoning (CLEVRER)
- physical puzzle solving (PHYRE)
- intuitive physics (IntPhys)
- multi‑body interactions (TraySim / LLMPhy)
The goal is to determine whether LLMs possess generalizable physical reasoning abilities or whether their performance is dataset‑specific and brittle.

## 5. Objectives
Primary Objective
Build a unified evaluation pipeline that measures physical reasoning capabilities of LLMs across multiple datasets and reasoning types.
Secondary Objectives
- Create a consistent data interface across all datasets
- Standardize prompt templates and evaluation logic
- Produce interpretable metrics and visualizations
- Document failure modes and reasoning errors
- Enable reproducible experiments for future research

## 6. Why This Matters
A unified physical reasoning benchmark is essential for:
- understanding the limits of current LLMs
- guiding the development of physics‑aware models
- informing robotics and embodied AI research
- identifying failure modes that impact safety
- bridging the gap between language and physical world understanding
This project lays the groundwork for evaluating—and eventually improving—LLMs’ ability to reason about the real world.
