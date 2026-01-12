# Results

This document summarizes the performance of the Physics Reasoning Engine on the current benchmark set. The results reflect the system’s ability to parse natural‑language scenarios, generate equations, solve them symbolically, and produce correct final answers.

## 1. Benchmark Summary

The benchmark consists of 11 physics word problems covering:

- Kinematics  
- Newtonian mechanics  
- Energy and work  
- Basic algebraic manipulation  
- Unit‑based reasoning  

The system was evaluated end‑to‑end using the full pipeline.

**Final Score:**  
**7 / 11 correct**

This accuracy is primarily limited by the reasoning capacity of the small LLM used in the current implementation.

## 2. Performance Breakdown

### Correct Predictions (7)
The system performed well on problems where:

- Variables were clearly stated  
- Equations followed standard kinematic forms  
- Units were consistent  
- Only one unknown needed solving  
- Symbolic solving was straightforward  

These cases demonstrate the strength of the hybrid LLM + SymPy architecture.

### Incorrect Predictions (4)
The incorrect cases were caused by:

- Missing or malformed equations  
- Empty or incomplete LLM outputs  
- Incorrect variable extraction  
- Unit inconsistencies  
- Symbolic parsing failures  

These issues are documented in detail in `docs/failure_modes/`.

## 3. Error Categories

The errors fall into four main categories:

### 3.1 Model Capacity Limitations
Small models struggle with:

- Multi‑step reasoning  
- Maintaining variable consistency  
- Algebraic manipulation  
- Structured output formatting  

This is the dominant source of error.

### 3.2 Equation Generation Errors
Some failures occurred because the LLM produced:

- Incorrect equations  
- Ambiguous expressions  
- Variables that did not match the parsed scenario  

### 3.3 Symbolic Solver Failures
SymPy rejected equations when:

- Variables were undefined  
- Expressions were malformed  
- Units were embedded inside symbolic expressions  

### 3.4 Formatting Mismatches
Even when the reasoning was correct, answers were marked incorrect due to:

- Extra text  
- Missing units  
- Slight formatting differences  

## 4. Interpretation of Results

The benchmark score should be interpreted as:

- **Architecture‑sound**  
- **Model‑limited**  
- **Scalable with better LLMs**

The hybrid design is functioning correctly.  
The bottleneck is the small LLM’s reasoning ability, not the pipeline.

With a more capable model, accuracy is expected to increase significantly.

## 5. Strengths Demonstrated

- Reliable symbolic solving  
- Consistent variable extraction in simpler cases  
- Clear final explanations  
- Deterministic outputs from the symbolic engine  
- Modular pipeline that handles errors gracefully  

These strengths validate the design choices behind the system.

## 6. Future Improvements

To improve benchmark performance, the following enhancements are planned:

- Use of larger or more capable LLMs  
- More robust equation‑generation prompts  
- Unit‑aware symbolic algebra  
- Better normalization of predicted answers  
- Partial‑credit scoring for multi‑step reasoning  
- Expanded benchmark coverage  

These improvements will make the evaluation more comprehensive and the system more reliable.