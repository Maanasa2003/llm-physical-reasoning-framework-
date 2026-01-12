# Architecture Overview

This document describes the system architecture of the Physics Reasoning Engine, a hybrid framework that combines a language model with symbolic mathematics to solve physics word problems reliably and transparently.

## 1. High‑Level Design

The system follows a hybrid LLM + SymPy pipeline:

1. User provides a natural‑language scenario through the CLI.
2. The LLM parses the scenario, extracts variables, and proposes equations.
3. The symbolic engine (SymPy) validates and solves the equations.
4. The LLM generates a final explanation using the symbolic solution.
5. The CLI displays the structured result.

This architecture ensures interpretability, reproducibility, reduced hallucination, and consistent output formatting.

## 2. System Components

### 2.1 CLI Layer (`cli.py`)
- Accepts user input (`--scenario` or `--benchmark`)
- Routes requests to the appropriate pipeline
- Handles argument parsing and validation
- Ensures consistent user experience

### 2.2 LLM Reasoning Module
Responsible for:
- Extracting variables
- Identifying knowns and unknowns
- Proposing equations
- Generating the final explanation

Small models may produce incomplete reasoning or empty outputs; these limitations are documented in the failure modes.

### 2.3 Symbolic Solver Module
Uses SymPy to:
- Parse equations
- Solve for unknowns
- Validate LLM‑generated expressions
- Catch algebraic inconsistencies

This module acts as a grounding mechanism to reduce hallucination.

### 2.4 Benchmark Engine
- Loads benchmark problems
- Runs them through the pipeline
- Normalizes outputs
- Scores predictions
- Produces accuracy metrics (currently 7/11, limited by model capacity)

### 2.5 Logging and Error Handling
- Captures malformed equations
- Detects empty LLM outputs
- Flags symbolic parsing failures
- Provides actionable error messages

## 3. Data Flow
User Input → CLI → LLM Reasoning → Symbolic Solver → LLM Explanation → Output
For benchmarks:
Benchmark JSON → Pipeline → Normalizer → Scorer → Report

## 4. Design Principles

### 4.1 Modularity
Each component is isolated:
- CLI
- LLM prompts
- Symbolic solver
- Benchmark runner
- Utilities

### 4.2 Transparency
Every step is visible:
- Extracted variables
- Proposed equations
- Symbolic solutions
- Final explanation

### 4.3 Scalability
The architecture supports:
- Larger LLMs
- More complex physics domains
- Additional symbolic tools
- Dataset‑based training (if added later)

### 4.4 Reproducibility
- Deterministic symbolic solving
- Structured output schema
- Clear separation of concerns

## 5. Known Limitations

### 5.1 Model Capacity
The current benchmark score (7/11) is limited by the small LLM’s reasoning ability, not by the architecture.

### 5.2 Equation Parsing
LLM‑generated equations may be incomplete, incorrect, or ambiguous.

### 5.3 Unit Handling
Mixed or missing units can cause symbolic failures.

### 5.4 Scenario Ambiguity
Underspecified problems may lead to multiple valid interpretations.
All limitations are documented in `docs/failure_modes/`.

## 6. Future Extensions

- Support for larger LLMs
- Multi‑step symbolic derivations
- Unit‑aware symbolic algebra
- Visual explanations (free‑body diagrams, graphs)
- Dataset‑based training modules
- Web UI or API endpoints