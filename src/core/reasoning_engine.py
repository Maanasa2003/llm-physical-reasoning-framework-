from typing import Optional, Dict, Any

from src.core.prompt_template import build_reasoning_prompt
from src.core.parsing import parse_answer
from src.core.scoring import score_answer
from src.models.llm_interface import LLMInterface
from src.core.symbolic_solver import solve_equation


class ReasoningEngine:

    def __init__(
        self,
        model_name: str = "meta-llama/Meta-Llama-3-70B-Instruct",
        expected_answer: Optional[str] = None,
        scenario: Optional[str] = None
    ):
        """
        If scenario is provided here, run() can be called without arguments.
        If scenario is NOT provided here, run() must be called with a scenario.
        """
        self.llm = LLMInterface(model_name=model_name)
        self.expected_answer = expected_answer
        self.scenario = scenario

    def run(self, scenario: Optional[str] = None) -> Dict[str, Any]:
        """
        Runs the reasoning engine on a scenario.
        Priority:
        1. scenario passed to run()
        2. scenario stored in self.scenario
        """

        # Determine which scenario to use
        if scenario is None:
            if self.scenario is None:
                raise ValueError(
                    "No scenario provided. Pass a scenario to ReasoningEngine() or to run()."
                )
            scenario = self.scenario

        # Build prompt
        prompt = build_reasoning_prompt(scenario)

        # Query LLM
        raw_output = self.llm.generate(prompt, max_tokens=1024)

        # Parse JSON
        parsed = parse_answer(raw_output)

        # Optional symbolic solving
        equation = parsed.get("equation")
        solve_for = parsed.get("solve_for")
        known_values = parsed.get("known_values")

        if equation and solve_for and known_values:
            try:
                solutions = solve_equation(
                    equation_str=equation,
                    solve_for=solve_for,
                    known_values=known_values
                )
                if solutions:
                    parsed["sympy_solution"] = str(float(solutions[0]))
            except Exception as e:
                parsed["sympy_solution"] = None
                parsed["sympy_error"] = str(e)

        # Score the answer
        scored = score_answer(parsed, expected_answer=self.expected_answer)

        return {
            "prompt": prompt,
            "raw_output": raw_output,
            "reasoning": scored.get("reasoning"),
            "final_answer": scored.get("final_answer"),
            "score": scored.get("score"),
            "correct": scored.get("correct"),
            "feedback": scored.get("feedback"),
        }
    