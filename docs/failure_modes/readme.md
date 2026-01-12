# Failure Modes

This document outlines the known failure modes of the Physics Reasoning Engine.  
The goal is to help users understand where the system may behave unpredictably and how to interpret such cases.

## 1. LLM Hallucination
The language model may occasionally:
- Produce incorrect intermediate reasoning steps  
- Invent physical assumptions not present in the scenario  
- Provide a correct final answer but incorrect derivation  
- Provide a plausible but physically invalid explanation  

This is mitigated by:
- Structured prompts  
- Symbolic verification using SymPy  
- Strict output formatting  

## 2. Symbolic Engine Mismatch
The symbolic solver may:
- Fail to parse malformed expressions from the LLM  
- Misinterpret ambiguous variable names  
- Return empty or trivial solutions  
- Reject equations that are not well‑posed  

Mitigation:
- Normalization of variable names  
- Validation before symbolic solving  
- Fallback to LLM-only reasoning  

## 3. Unit Handling Errors
The system may struggle when:
- Units are missing  
- Units are mixed (e.g., km/h with m/s)  
- The LLM outputs expressions without units  
- The symbolic engine receives unit‑annotated variables  

Mitigation:
- Unit‑stripping before symbolic solving  
- Explicit unit prompts  
- Post‑processing checks  

## 4. Benchmark Scoring Issues
During evaluation:
- Keys may not match expected benchmark formats  
- Empty outputs may cause scoring failures  
- Minor formatting differences may be counted as incorrect  

Mitigation:
- Strict output schema  
- Normalization of answers  
- Clear error messages  

## 5. Scenario Parsing Failures
The CLI may fail when:
- The scenario text is incomplete  
- Quotes are not closed (shell `dquote>` state)  
- Special characters break argument parsing  

Mitigation:
- Use of proper quoting  
- Input validation  
- Helpful CLI error messages  

## 6. Model Capability Ceilings
Small models may:
- Fail to solve multi-step physics problems  
- Produce empty or irrelevant outputs  
- Struggle with algebraic manipulation  

Mitigation:
- Hybrid LLM + SymPy architecture  
- Clearer prompts  
- Option to switch models  

## 7. Ambiguous or Underspecified Scenarios
The system may behave unpredictably when:
- The scenario lacks numerical values  
- The physical setup is unclear  
- Multiple interpretations are possible  

Mitigation:
- Prompting the user for clarification  
- Default assumptions documented in the code  

## 8. Model Capacity Limitations

The benchmark accuracy (7/11) is primarily due to the limited reasoning capability of the small LLM used in this project. Smaller models often struggle with:

- Multi-step physics reasoning  
- Algebraic manipulation  
- Maintaining variable consistency  
- Producing structured outputs that match the expected schema  
- Solving problems requiring symbolic insight  

These limitations are expected and do not reflect issues in the project architecture.  
Using a larger or more capable model typically improves benchmark performance significantly.

## Summary
These failure modes are expected in hybrid reasoning systems.  
Documenting them ensures transparency and helps users interpret results responsibly.