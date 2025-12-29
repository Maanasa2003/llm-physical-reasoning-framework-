# Project Architecture

This document describes the structure, organization, and design principles of the repository.  
The goal is to maintain clarity, modularity, and reproducibility while supporting multiple physical‑reasoning datasets and evaluation tasks.

## 1. Repository Structure
The project follows a modular, pipeline‑oriented layout:
src/
    pipeline/
        run_pipeline.py
    evaluation/
        piqa_eval.py
        clevrer_eval.py
        phyre_eval.py
        intphys_eval.py
        traysim_eval.py
    data/
        preprocess.py
    utils/
        dataset_loader.py
        logging_utils.py
        config.py
data/
    raw/
    processed/
    DATASETS.md
docs/
    failure_modes/
    methodology/
        pipeline.md
        architecture.md
        evaluation.md
    results/
Each directory has a clear purpose and isolates responsibilities to keep the codebase clean and scalable.

## 2. Directory Responsibilities
### **src/pipeline/**
Contains the main orchestration script (`run_pipeline.py`) that coordinates:
- dataset loading  
- preprocessing  
- evaluation  
- result aggregation  
This is the entry point for running the full evaluation pipeline.

### **src/evaluation/**
Contains evaluation logic for each dataset.  
Each file corresponds to one dataset and defines:
- task format  
- prompt generation  
- model querying  
- metric computation  
This modular design allows you to add new datasets without modifying the core pipeline.

### **src/data/**
Contains preprocessing utilities.  
`preprocess.py` standardizes dataset formats into a unified structure so that evaluation scripts can operate consistently across datasets.

### **src/utils/**
Contains reusable utilities shared across the project:
- `dataset_loader.py` — loads datasets via streaming or URLs  
- `logging_utils.py` — centralized logging configuration  
- `config.py` — constants, paths, and global settings  

This keeps the rest of the code clean and avoids duplication.

### **data/**
Stores dataset‑related documentation and optional cached data.
- `raw/` — unprocessed or streamed data (optional)  
- `processed/` — normalized or preprocessed data (optional)  
- `DATASETS.md` — documentation for all datasets used in the project  
Large datasets are **not** stored in the repo; they are loaded online.

### **docs/**
Contains all project documentation.
- `methodology/` — pipeline, architecture, evaluation  
- `failure_modes/` — analysis of model weaknesses  
- `results/` — evaluation outputs and summaries  
This mirrors the structure of a research paper: methodology → results → analysis.

## 3. Design Principles
### **Modularity**
Each component is isolated:
- dataset loading  
- preprocessing  
- evaluation  
- pipeline orchestration  
This makes the system easy to extend and debug.

### **Clean Code**
The project follows:
- short, single‑purpose functions  
- type hints  
- docstrings  
- consistent naming conventions  
- no hardcoded paths  
This ensures readability and maintainability.

### **Reproducibility**
- datasets loaded online  
- deterministic evaluation scripts  
- documented pipeline and architecture  
- no large files committed to the repo  
Anyone can reproduce results by running the pipeline.

### **Scalability**
New datasets, evaluation tasks, or models can be added by:
- creating a new loader  
- adding a new evaluation script  
- updating the pipeline  
No existing components need to be rewritten.

### **Transparency**
All design decisions and pipeline steps are documented in:
`docs/methodology/`
This makes the project easy to understand for reviewers, collaborators, and future contributors.

## 4. Summary
This architecture provides a clean, modular foundation for evaluating physical reasoning in large language models.  
It balances simplicity with scalability and mirrors the structure of high‑quality research repositories.
