# Evaluation Framework
This document describes how physical reasoning is evaluated across the datasets used in this project. Each dataset targets a different dimension of physical understanding.

## 1. PIQA
**Task:** Physical commonsense multiple-choice  
**Format:** Two candidate solutions  
**Metric:** Accuracy  
**Evaluation Script:** `src/evaluation/piqa_eval.py`

## 2. CLEVRER
**Task:** Causal reasoning, temporal reasoning, counterfactuals  
**Format:** Descriptive, explanatory, predictive, and counterfactual questions  
**Metrics:** 
- Causal accuracy  
- Descriptive accuracy  
- Counterfactual correctness  
**Evaluation Script:** `src/evaluation/clevrer_eval.py`

## 3. PHYRE
**Task:** Physical puzzle solving  
**Format:** Agent must choose an action that solves a physics-based puzzle  
**Metric:** Success rate  
**Evaluation Script:** `src/evaluation/phyre_eval.py`

## 4. IntPhys
**Task:** Intuitive physics (object permanence, collisions, occlusions)  
**Format:** Plausible vs implausible video sequences  
**Metric:** Violation detection accuracy  
**Evaluation Script:** `src/evaluation/intphys_eval.py`

## 5. TraySim (LLMPhy)
**Task:** Multi-body physical interactions  
**Format:** Predicting stability, motion, or outcomes  
**Metric:** Stability prediction accuracy  
**Evaluation Script:** `src/evaluation/traysim_eval.py`

## Evaluation Flow
1. Load dataset  
2. Preprocess into unified format  
3. Generate prompts  
4. Query LLM  
5. Compute metrics  
6. Save results to `docs/results/`  
7. Analyze failure modes in `docs/failure_modes/`
