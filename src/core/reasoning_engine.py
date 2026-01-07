#The main class that runs reasoning steps using the LLM
# core/reasoning_engine.py

from typing import Dict, Any
from src.models.llm_interface import LLMInterface
from core.prompt_templates import build_reasoning_prompt
from core.parsing import parse_answer
from core.scoring import score_answer

class ReasoningEngine:
    """
    Runs structured physical reasoning using an LLM.
    """

    def __init__(self, llm: LLMInterface):
        self.llm = llm

    def run(self, scenario: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executes the full reasoning pipeline:
        1. Build prompt
        2. Query LLM
        3. Parse output
        4. Score reasoning
        """
        prompt = build_reasoning_prompt(scenario)
        raw_output = self.llm.generate(prompt)
        parsed = parse_answer(raw_output)
        score = score_answer(parsed, scenario)

        return {
            "prompt": prompt,
            "raw_output": raw_output,
            "parsed": parsed,
            "score": score
        }