# Problem Framing

This document explains how the Physics Reasoning Engine interprets and structures a natural‑language physics scenario before attempting to solve it. Problem framing is the foundation of the entire pipeline: if the scenario is framed incorrectly, every downstream step will fail.

## 1. Motivation

Most physics problems encountered in education, research, and engineering begin as natural‑language descriptions.  
However, large language models often:

- Misinterpret the scenario  
- Miss key variables  
- Produce incorrect or incomplete equations  
- Fail to maintain physical consistency  

These issues make LLM‑only reasoning unreliable for scientific tasks.

The motivation behind this module is to create a **robust, structured, and interpretable bridge** between human‑written scenarios and symbolic mathematics.  
By framing the problem correctly, the system dramatically improves accuracy, reduces hallucination, and ensures reproducibility.

## 2. Core Problem

Natural‑language physics problems are inherently ambiguous.  
The system must answer:

**“How do we convert an informal, human‑written scenario into a precise mathematical representation that a symbolic solver can understand?”**

This involves several challenges:

- Identifying all relevant variables  
- Extracting numerical values and units  
- Determining what the problem is asking for  
- Inferring implicit assumptions  
- Ensuring consistency in variable naming  
- Avoiding hallucinated or irrelevant information  

The core problem is not solving the physics — it is **structuring the problem correctly** so that solving becomes possible.

## 3. Research Gap

Existing LLM‑based physics solvers typically fall into two categories:

1. **Pure LLM reasoning**  
   - Prone to hallucination  
   - Inconsistent variable usage  
   - Unreliable algebra  
   - No symbolic grounding  

2. **Symbolic solvers without natural‑language understanding**  
   - Require fully structured inputs  
   - Cannot interpret human‑written scenarios  

There is a clear gap:

> **No existing system reliably converts natural‑language physics problems into structured, symbolic‑ready representations using a hybrid LLM + symbolic approach.**

This project fills that gap by introducing a modular, interpretable problem‑framing pipeline.

## 4. Inputs and Outputs

### Input
A raw natural‑language scenario, for example:

> “A car accelerates from rest at 2 m/s² for 5 seconds. What is its final velocity?”

### Output
A structured JSON‑like representation:

```json
{
  "variables": {
    "a": "acceleration",
    "t": "time",
    "v": "final velocity",
    "u": "initial velocity"
  },
  "knowns": {
    "a": 2,
    "t": 5,
    "u": 0
  },
  "unknowns": ["v"],
  "assumptions": [
    "motion is linear",
    "acceleration is constant"
  ]
}

## 5. Steps in Problem Framing
5.1 Variable Identification
The LLM identifies all physical quantities mentioned or implied in the scenario:
• Velocity
• Time
• Distance
• Mass
• Acceleration
• Force
It assigns consistent variable names (e.g., v, t, a, m).
5.2 Extraction of Knowns
The model extracts numerical values and units:
• t = 5 s
• a = 2 m/s²
• u = 0
5.3 Identification of Unknowns
The system determines what the problem is asking for:
• Final velocity
• Distance travelled
• Force applied
5.4 Assumption Detection
Many physics problems rely on implicit assumptions:
• Constant acceleration
• No air resistance
• Linear motion
• Ideal conditions
These assumptions are made explicit to avoid ambiguity.
5.5 Scenario Normalization
The system rewrites the scenario into a clean, structured form:
• Removes irrelevant text
• Standardizes variable names
• Ensures units are consistent

## 6. Why Problem Framing Matters
Accurate problem framing is essential because:
• The symbolic solver cannot interpret raw natural language
• Incorrect variable extraction leads to unsolvable equations
• Missing assumptions cause ambiguous or contradictory setups
• Clean structure reduces hallucination in later stages
This step is the backbone of the entire reasoning engine.

## 7. Common Failure Modes in Problem Framing
• Missing variables
• Incorrect variable names
• Misinterpreted units
• Ambiguous or incomplete knowns
• Incorrect identification of the target unknown
• Over‑ or under‑assumption of physical conditions
These issues are documented in detail in docs/failure_modes/.

## 8. Future Improvements
Planned enhancements to the problem‑framing module include:
• Unit‑aware parsing
• More robust variable‑name normalization
• Detection of multi‑part problems
• Support for diagrams or structured inputs
• Automatic clarification prompts for ambiguous scenarios
These improvements will make the system more reliable and more generalizabl