# Pipeline Overview

This document describes the end-to-end pipeline used to evaluate physical reasoning in large language models. The pipeline is modular, reproducible, and designed to support multiple datasets with minimal duplication.

## 1. Data Loading
All datasets are loaded through streaming or URL-based loaders defined in:
`src/utils/dataset_loader.py`

Supported datasets:
- PIQA
- CLEVRER
- PHYRE
- IntPhys
- TraySim (LLMPhy)
Each loader returns a unified Python object that downstream components can process consistently.

## 2. Preprocessing
Preprocessing utilities are located in:
`src/data/preprocess.py`

Responsibilities:
- Normalize dataset formats
- Convert raw dataset entries into a unified structure
- Extract relevant fields (question, context, choices, labels)
- Apply optional filtering or cleaning

This ensures that all datasets follow a consistent interface before evaluation.

## 3. Evaluation
Each dataset has a dedicated evaluation script in:
`src/evaluation/`
Examples:
- `piqa_eval.py`
- `clevrer_eval.py`
- `phyre_eval.py`
- `intphys_eval.py`
- `traysim_eval.py`

Evaluation scripts:
- define the task format
- generate prompts for the LLM
- query
