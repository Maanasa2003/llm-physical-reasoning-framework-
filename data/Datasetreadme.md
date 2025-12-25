# Dataset Documentation

This project uses a curated set of physics-reasoning datasets. All datasets are accessed online at runtime (streaming or URL-based loading), so they are not stored directly in this repository. The `data/raw/` and `data/processed/` directories are reserved for temporary caching or optional local preprocessing.

## 1. PIQA (Physical Interaction QA)
**Purpose:** Physical commonsense reasoning  
**Why it's useful:** Tests basic intuitive physics and everyday physical affordances  
**Access:** https://huggingface.co/datasets/facebook/piqa  
**Loaded via:** Hugging Face streaming

## 2. CLEVRER
**Purpose:** Causal reasoning, object interactions, counterfactuals  
**Why it's useful:** Evaluates temporal and causal physical reasoning  
**Access:** https://github.com/clevrer/clevrer  
**Loaded via:** URL-based loaders or local extraction

## 3. PHYRE
**Purpose:** Puzzle-based physical reasoning  
**Why it's useful:** Tests generalization and physical prediction  
**Access:** https://github.com/facebookresearch/phyre  
**Loaded via:** Python API or dataset download

## 4. IntPhys
**Purpose:** Intuitive physics (object permanence, collisions, occlusions)  
**Why it's useful:** Detects deep physical plausibility failures  
**Access:** https://github.com/deepmind/intphys  
**Loaded via:** URL-based loaders

## 5. TraySim (LLMPhy)
**Purpose:** Multi-body physical interactions  
**Why it's useful:** Modern dataset designed specifically for LLM physical reasoning  
**Access:** Provided in LLMPhy paper  
**Loaded via:** URL or custom loader

## Notes on Data Handling
- `data/raw/` is used for optional local caching during debugging.
- `data/processed/` stores normalized or pre-tokenized versions if needed.
- The main pipeline loads datasets **online** to avoid large downloads.
