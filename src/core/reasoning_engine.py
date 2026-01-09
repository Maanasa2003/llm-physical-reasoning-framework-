from typing import Optional, Dict, Any

from src.core.prompt_template import build_reasoning_prompt
from src.core.parsing import parse_answer
from src.core.scoring import score_answer
from src.models.llm_interface import LLMInterface


class ReasoningEngine:
    """
    High-level orchestrator for:
      1. Building a reasoning prompt
      2. Querying the LLM
      3. Parsing the LLM output
      4. Scoring the parsed answer
    """

    def __init__(
        self,
        model_name: str = "meta-llama/Llama-3.2-1B-Instruct",
        expected_answer: Optional[str] = None,
    ):
        """
        :param model_name: HF model routed via the Hugging Face Router.
        :param expected_answer: Optional ground-truth answer for scoring.
        """
        self.llm = LLMInterface(model_name=model_name)
        self.expected_answer = expected_answer

    def run(self, scenario: str) -> Dict[str, Any]:
        """
        Run the full reasoning pipeline on a given physical scenario.

        :param scenario: Natural-language description of the problem.
        :return: Dictionary containing:
            - prompt
            - raw_output
            - reasoning
            - final_answer
            - score
            - correct
            - feedback
        """
        # 1. Build the prompt
        prompt = build_reasoning_prompt(scenario)

        # 2. Query the LLM
        raw_output = self.llm.generate(prompt)

        # 3. Parse the output into structure
        parsed = parse_answer(raw_output)

        # 4. Score against expected answer (if provided)
        scored = score_answer(parsed, expected_answer=self.expected_answer)

        # 5. Return enriched result
        result = {
            "prompt": prompt,
            "raw_output": raw_output,
            "reasoning": scored.get("reasoning"),
            "final_answer": scored.get("final_answer"),
            "score": scored.get("score"),
            "correct": scored.get("correct"),
            "feedback": scored.get("feedback"),
        }
        return result