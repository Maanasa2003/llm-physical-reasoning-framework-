# Analysis Notebook

This document describes the purpose and structure of the analysis notebook included in the project.  
The notebook is used to explore model behavior, inspect intermediate outputs, and understand how the Physics Reasoning Engine performs on individual benchmark problems.

## 1. Purpose of the Analysis Notebook

The analysis notebook serves as an interactive environment for:

- Inspecting LLM outputs step‑by‑step  
- Visualizing how variables, equations, and solutions are generated  
- Debugging incorrect benchmark predictions  
- Comparing symbolic vs. LLM reasoning  
- Understanding failure modes in detail  
- Testing prompt variations and model configurations  

It is not part of the main pipeline; instead, it is a research and debugging tool.

## 2. What the Notebook Contains

The notebook typically includes:

### 2.1 Scenario Exploration
Cells that allow you to input a physics scenario and observe:

- Parsed variables  
- Extracted knowns and unknowns  
- Generated equations  
- Symbolic solutions  
- Final explanations  

This helps verify whether the pipeline behaves as expected.

### 2.2 Benchmark Inspection
Tools to load benchmark problems and examine:

- The model’s raw outputs  
- Normalized answers  
- Scoring decisions  
- Error categories  

This is useful for understanding why the system achieved **7/11** accuracy.

### 2.3 Failure Mode Demonstrations
Examples of:

- Malformed equations  
- Missing variables  
- Unit inconsistencies  
- Empty LLM outputs  
- Symbolic parsing failures  

These examples help refine prompts and improve robustness.

### 2.4 Prompt Experiments
Cells for testing:

- Alternative prompt templates  
- Stricter formatting constraints  
- Different variable‑naming strategies  
- Multi‑step reasoning prompts  

This is where most prompt engineering experiments happen.

## 3. How the Notebook Is Used

The notebook is primarily used during development to:

- Debug pipeline behavior  
- Validate new features  
- Test improvements before integrating them into the CLI  
- Explore model limitations  
- Document reproducible examples  

It is not required for running the system, but it is extremely valuable for research and iteration.

## 4. Typical Workflow

A common workflow inside the notebook looks like:

1. Load a scenario or benchmark item  
2. Run it through the LLM parsing step  
3. Inspect the extracted variables  
4. Generate equations  
5. Check symbolic solving  
6. Compare predicted vs. expected answers  
7. Categorize errors  
8. Adjust prompts or logic  
9. Re‑run and observe improvements  

This iterative loop helps refine the system.

## 5. Why the Notebook Matters

The notebook provides:

- Transparency into the reasoning pipeline  
- A controlled environment for experimentation  
- A way to reproduce and analyze failures  
- A sandbox for testing improvements before committing them  

It is especially useful for documenting insights that feed into:

- `docs/failure_modes/`  
- `docs/evaluation.md`  
- `docs/pipeline.md`  
- `docs/results.md`  

## 6. Future Extensions

Planned enhancements for the analysis notebook include:

- Visualizations of symbolic expressions  
- Side‑by‑side comparisons of multiple models  
- Automated error categorization  
- Interactive sliders for modifying scenario parameters  
- Unit‑aware equation inspection  
- Graphical free‑body diagrams (future feature)  

These additions will make the notebook even more powerful for research and debugging.