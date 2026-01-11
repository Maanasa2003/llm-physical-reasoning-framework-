# Benchmark Overview

The benchmarks directory contains structured evaluation datasets for testing the physics‑reasoning capabilities of the LLM‑SymPy hybrid engine. Each benchmark is designed to probe a different aspect of physical understanding — from equation‑based reasoning to intuitive judgments about stability, motion, and counterfactual changes.
The benchmarks are organized into subfolders by reasoning type:
benchmarks/
    causal_dynamics
    counterfactuals
    intuitive_physics
    multimodal

Each benchmark file is stored in JSON format and includes:
• A natural‑language scenario
• The physics domain
• The expected equation or qualitative answer
• Known values (if applicable)
• The expected numeric or qualitative result
• A tolerance for numeric comparisons
• Tags for categorization
These datasets allow automated evaluation of the reasoning engine across diverse physics tasks.

1. Causal Dynamics Benchmarks
Folder: benchmarks/causal_dynamics/
These benchmarks test the model’s ability to:
• Identify the correct physics domain
• Select appropriate governing equations
• Extract variables and constants
• Solve using symbolic reasoning
• Produce correct numeric answers
Typical scenarios include:
• Free fall
• Constant acceleration
• Springs and oscillations
• Newtonian forces
• Energy conservation
These tasks require explicit equation‑based reasoning.

2. Counterfactual Benchmarks
Folder: benchmarks/counterfactuals/
These benchmarks evaluate whether the model can reason about changes to physical conditions, such as:
• “What if gravity were lower?”
• “What if the mass doubled?”
• “What if friction were removed?”
Each benchmark includes:
• The original scenario
• A counterfactual variation
• Known values for both cases
• Expected answers for both
• A tolerance for numeric comparison
This tests causal understanding, not just equation solving.

3. Intuitive Physics Benchmarks
Folder: benchmarks/intuitive_physics/
These benchmarks focus on qualitative physical reasoning, including:
• Stability and support
• Center of mass
• Object permanence
• “Will it fall?”
• “Which object hits first?”
• Common misconceptions
These tasks do not require equations.  
They test whether the model grasps the structure of the physical world.

4. Multimodal Physics Benchmarks (optional)
Folder: benchmarks/multimodal/
These benchmarks (if included) evaluate reasoning over visual scenes, using:
• Image descriptions
• Diagrams
• Sketches
• Physical setups
They test whether the model can combine visual cues with physics knowledge.

Benchmark File Structure
Each benchmark JSON file follows this general schema:
{
  "id": "unique_identifier",
  "scenario": "Natural language description of the problem.",
  "counterfactual": "Optional counterfactual variation.",
  "domain": "physics domain or reasoning type",
  "equation": "Symbolic equation (if applicable)",
  "solve_for": "Variable to solve for",
  "known_values": { "key": value },
  "expected_answer": 0.0,
  "tolerance": 0.05,
  "tags": ["category", "keywords"]
}

Purpose of the Benchmark Suite
This benchmark suite enables:
• Automated evaluation of the reasoning engine
• Regression testing as the system evolves
• Cross‑domain coverage of physics concepts
• Comparison of LLM‑only vs hybrid LLM+SymPy performance
• Identification of failure modes in reasoning
It forms the foundation for a robust, research‑grade physics reasoning framework.