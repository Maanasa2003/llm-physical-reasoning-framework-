# Pipeline

This document describes the end‑to‑end pipeline used by the Physics Reasoning Engine.  
The pipeline combines natural‑language reasoning from an LLM with symbolic mathematics from SymPy to produce reliable, interpretable physics solutions.

## 1. Overview

The pipeline processes a physics scenario through four major stages:
1. **Scenario Parsing (LLM)**
2. **Equation Generation (LLM)**
3. **Symbolic Solving (SymPy)**
4. **Final Answer Generation (LLM)**
Each stage is modular and can be improved or replaced independently.

## 2. Stage 1 — Scenario Parsing

The LLM receives the raw natural‑language scenario and extracts:

- Variables  
- Known values  
- Unknowns  
- Physical relationships implied by the text  

The output is a structured representation that the next stage can use.

Example output structure:

```json
{
  "variables": {
    "v": "initial velocity",
    "t": "time",
    "a": "acceleration"
  },
  "knowns": {
    "t": 5,
    "a": 2
  },
  "unknowns": ["v"]
}

## 3. Stage 2 — Equation Generation
Using the parsed scenario, the LLM proposes one or more equations that relate the variables.
Examples:
• v = u + at
• s = ut + 0.5at^2
The system expects:
• Clean algebraic expressions
• Consistent variable names
• No units inside symbolic expressions
If the equations are malformed, the symbolic solver will reject them.

## 4. Stage 3 — Symbolic Solving (SymPy)
The symbolic engine performs:
• Parsing of LLM‑generated equations
• Solving for unknown variables
• Validation of the solution
• Detection of inconsistencies or unsolvable systems
This stage grounds the reasoning in deterministic mathematics and reduces hallucination.
Example symbolic solution:
{
  "solution": {
    "v": 15
  }
}
If the solver fails (e.g., malformed equations), the pipeline returns an error message.

## 5. Stage 4 — Final Answer Generation
The LLM receives:
• The symbolic solution
• The original scenario
• The extracted variables
It produces a final explanation that is:
• Clear
• Physically correct
• Consistent with the symbolic result
Example:
“Using the equation ￼, and substituting ￼ m/s² and ￼ s, the final velocity is 15 m/s.”

## 6. Benchmark Pipeline
When running in benchmark mode:
1. Load all benchmark problems
2. Run each through the full pipeline
3. Normalize predicted answers
4. Compare with expected answers
5. Compute accuracy
Current performance: 7 / 11 correct, limited by the small LLM’s reasoning capacity.

## 7. Error Handling
The pipeline detects and reports:
• Empty LLM outputs
• Malformed equations
• Symbolic parsing failures
• Missing variables
• Unit inconsistencies
These issues are documented in docs/failure_modes/.

## 8. Extensibility
The pipeline is designed to support:
• Larger LLMs
• More advanced symbolic reasoning
• Additional physics domains
• Unit‑aware algebra
• Web or API interfaces
The modular design ensures that improvements in one stage do not require rewriting the entire system.

## 9. Pipeline Diagram

```mermaid
flowchart TD

    A[User Scenario Input] --> B[CLI Layer]
    B --> C[LLM: Scenario Parsing]
    C --> D[LLM: Equation Generation]
    D --> E[SymPy: Symbolic Solver]
    E --> F[LLM: Final Answer Generation]
    F --> G[CLI Output]

    %% Benchmark Path
    H[Benchmark JSON] --> I[Benchmark Runner]
    I --> C
    G --> J[Scorer & Report Generator]