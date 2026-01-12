# Evaluation

This document explains how the Physics Reasoning Engine is evaluated using a small benchmark of physics word problems. The goal of the evaluation is to measure the system’s ability to extract variables, generate equations, solve them symbolically, and produce correct final answers.

## 1. Evaluation Method

The evaluation uses a set of benchmark problems stored in JSON format. Each benchmark entry contains:
- A natural‑language physics scenario
- The expected final answer
- Optional metadata (units, variable names, etc.)

The CLI provides a `--benchmark` mode that runs all benchmark problems through the full reasoning pipeline:

1. Parse scenario  
2. Generate variables and equations using the LLM  
3. Solve equations using SymPy  
4. Produce a final answer  
5. Compare the predicted answer with the expected answer  

The scorer then reports:
- Total number of problems
- Number of correct predictions
- Final accuracy

## 2. Current Results

The current benchmark accuracy is:

**7 / 11 correct**

This score reflects the limitations of the small LLM used in the project. The architecture itself is capable of higher accuracy when paired with a more capable model.

## 3. Common Sources of Error

The incorrect benchmark cases typically arise from:

### 3.1 Model Capacity Limitations
Small models may:
- Fail to generate complete equations  
- Produce empty or partially structured outputs  
- Mis-handle algebraic steps  
- Misinterpret the scenario  

These issues are expected and documented in the failure modes.

### 3.2 Equation Parsing Issues
Some predictions fail because:
- The LLM outputs malformed expressions  
- Variable names are inconsistent  
- The symbolic solver cannot parse the equations  

### 3.3 Unit Handling
Errors occur when:
- Units are missing  
- Units are mixed (e.g., km/h with m/s)  
- The LLM outputs unit‑annotated variables that SymPy cannot process  

### 3.4 Formatting Mismatches
Even when the reasoning is correct, the answer may be marked incorrect due to:
- Minor formatting differences  
- Extra text around the answer  
- Missing units  

## 4. Interpretation of Results

The benchmark score should be interpreted as a **model‑limited performance**, not a limitation of the system design.

The architecture is intentionally modular so that:
- Larger LLMs can be plugged in  
- More complex benchmarks can be added  
- Symbolic reasoning can be extended  

With a stronger model, accuracy is expected to increase significantly.

## 5. Future Improvements

Planned enhancements to the evaluation pipeline include:

- More robust normalization of predicted answers  
- Unit‑aware comparison  
- Partial‑credit scoring for multi‑step reasoning  
- Expanded benchmark coverage  
- Support for multiple physics domains  
- Automated error categorization  

These improvements will make the evaluation more reliable and more informative for future development.