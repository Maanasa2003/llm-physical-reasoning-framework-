# Unifying Physics and Language: A Generalist LLM–Symbolic Reasoning Engine for Comprehensive Physics Understanding

# Physics Reasoning Engine  
A hybrid LLM + symbolic solver for intuitive, causal, and multimodal physics reasoning.

## What This Project Is  
This project is a **physics reasoning engine** that takes natural‑language physics problems and converts them into **structured, solvable mathematical representations**.  
It uses:

- **LLMs** to interpret the scenario, extract variables, and propose equations  
- **Symbolic mathematics (SymPy)** to solve those equations exactly  
- **A reasoning pipeline** that ensures consistency, interpretability, and correctness  

The goal is to build a system that can **reason about real‑world physics**, not just compute formulas — covering intuitive physics, causal dynamics, counterfactuals, and multimodal scenarios.

##  Core Idea  
The core idea behind this project is simple but powerful:

> **Use an LLM to understand the physics problem, then use a symbolic solver to guarantee mathematical correctness.**

LLMs are excellent at interpreting natural language but unreliable at exact computation.  
Symbolic solvers are mathematically perfect but cannot understand language.  
This engine **combines the strengths of both** to produce reliable, interpretable physics reasoning.

##  Features

- Natural‑language physics problem parsing  
- Variable extraction and normalization  
- Equation generation using LLM reasoning  
- Symbolic solving using SymPy  
- Unified pipeline for reasoning + scoring  
- Benchmark suite across four physics categories  
- Clean, modular architecture  
- Fully documented methodology and analysis notebooks  

## Repository Structure
benchmarks/
  - causal_dynamic/
       - free_fall_20m.json
  - counterfactual/
       - block_on_ramp_no_friction.json
       - free_fall_lower_gravity.json
       - spring_mass_double.json
  - intuitive_physics
       - falling_block.json
       - heavier_falls_faster.json
       ramp_vs_freefall.json
       support_failure.json
  - multimodal
       - block_on_ramp.json
       - projectiile_image.json
       - lower_stability.json
data/
  - raw/
       - readme.md
  - processed/
       - readme.md
docs/
  - methodology
       - architecture.md
       - pipeline.md
       - evaluation.md
       - problem_framing.md
  - failure_modes/
       - readme.md
  - result/
       - results.md
notebooks/
  - analysis/
       - analysis.md
  - exploratory/
       - exploratory.md
src/
  - core
       - parsing.py
       - prompt_template.py
       - reasoning_engine.py
       - scoring.py
       - symbolic_solver.py
  - models
       - llm_interface.py
       - world_model.py
  - utils
       - config.py
       - test_env.py
       - test_llm.py
       - test_reasoning.py
cli.py  
requirements.txt  
README.md  
LICENSE

## Installation

Requires:

- Python 3.10+
- A Hugging Face API key (or any supported LLM provider)
Install dependencies:
```bash
pip install -r requirements.txt
Set your API key:
export HF_API_KEY="your_key_here"
Running the Project

## Run a single physics scenario
python cli.py --scenario " your scenario here"

### example:
python cli.py --scenario "a man walked 2km in 5 mins. how much distance will he cover in 45 minutes?"
example output:
=== Answer ===
18

## Run the full benchmark suite
python cli.py --benchmark

This evaluates the system across all benchmark categories and prints accuracy, predictions, and error types.

## Documentation
All instructions for running, understanding, and extending the project are located in the docs/ and notebooks/ directories.
Key files:
• docs/methodology/pipeline.md — how the pipeline works
• docs/methodology/evaluation.md — evaluation + scoring
• docs/methodology/architecture.md — system architecture
• docs/results/results.md — benchmark results
• docs/failure_modes/ — error analysis
• notebooks/analysis/analysis.md — structured analysis
• notebooks/exploratory/exploratory.md — free‑form experiments

### Example Output
The engine produces structured outputs including:
• Extracted variables
• Generated equations
• Symbolic solutions
• Final numeric answers
• Explanations
This makes the system transparent and easy to debug.

Roadmap
• Add unit‑aware equation validation
• Expand benchmark set
• Add visualization tools
• Explore multi‑step reasoning strategies

## Future Scope

This project opens several promising research directions:

- **Generalist Physics Reasoning**  
  Extend the engine to handle a broader range of physics domains including electromagnetism, thermodynamics, quantum systems, and continuum mechanics.

- **Unit‑Aware and Dimensionally Consistent Reasoning**  
  Integrate automatic dimensional analysis to validate equations and catch physically impossible outputs.

- **Multimodal Integration**  
  Expand the multimodal pipeline to incorporate diagrams, free‑body sketches, and video frames for richer physical understanding.

- **Model‑Agnostic Reasoning Layer**  
  Allow seamless swapping of LLM backends (open‑source or proprietary) without changing the reasoning pipeline.

- **Interactive Physics Sandbox**  
  Build a simulation interface where users can modify parameters and observe symbolic + numerical predictions.

- **Benchmark Expansion**  
  Grow the benchmark suite into a standardized evaluation set for general physics reasoning across intuitive, causal, counterfactual, and multimodal tasks.

## Limitations

Despite its capabilities, the system has several current limitations:

- **LLM Dependency**  
  The quality of variable extraction and equation generation depends on the underlying LLM’s reasoning ability.

- **Ambiguity in Natural Language**  
  Highly ambiguous or underspecified problems may lead to incorrect or incomplete symbolic formulations.

- **No Numerical Simulation Engine**  
  The system focuses on symbolic reasoning and does not yet integrate numerical solvers or physics engines.

- **Limited Multimodal Depth**  
  Image‑based reasoning is currently shallow and relies on textual descriptions rather than full visual understanding.

- **No Uncertainty Quantification**  
  The pipeline does not yet estimate confidence or detect when the model is likely to be wrong.

These limitations define clear directions for future research and engineering improvements.

## License

**All Rights Reserved.**
This project and all associated files are the intellectual property of the author.  
No part of this repository may be copied, modified, distributed, or used in any form  
without explicit written permission from the author.

© 2026 Manasa. All Rights Reserved.

Author:
Maanasa Panchakarla
Master’s in Artificial Intelligence, Dublin City University (DCU)  
Focused on hybrid neural–symbolic reasoning, llm-physics understanding, quantum AI, and space‑oriented scientific intelligence
