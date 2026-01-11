# Computes correctness, confidence, and reasoning quality
def score_answer(parsed_output: dict, expected_answer: str = None) -> dict:

    reasoning = parsed_output.get("reasoning", [])

    sympy_answer = parsed_output.get("sympy_solution")
    llm_answer = parsed_output.get("final_answer")

    # Prefer SymPy
    final_answer = sympy_answer if sympy_answer is not None else llm_answer

    if expected_answer is None:
        return {
            "score": None,
            "correct": None,
            "feedback": "No expected answer provided.",
            "reasoning": reasoning,
            "final_answer": final_answer
        }

    if final_answer is None:
        return {
            "score": 0,
            "correct": False,
            "feedback": "No final answer produced.",
            "reasoning": reasoning,
            "final_answer": None
        }

    # Numeric comparison
    try:
        fa = float(final_answer)
        ea = float(expected_answer)
        correct = abs(fa - ea) < 0.05
    except:
        # Qualitative comparison
        correct = final_answer.strip().lower() == expected_answer.strip().lower()

    feedback = "Correct answer." if correct else "Incorrect answer."

    return {
        "score": 1 if correct else 0,
        "correct": correct,
        "feedback": feedback,
        "reasoning": reasoning,
        "final_answer": final_answer
    }