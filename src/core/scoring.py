# Computes correctness, confidence, and reasoning quality
def score_answer(parsed_output: dict, expected_answer: str = None) -> dict:
    """
    Very simple baseline scoring function.
    Compares the model's final answer to an expected answer (if provided)
    and returns a score + feedback structure.
    """
    final_answer = parsed_output.get("final_answer")
    reasoning = parsed_output.get("reasoning", [])
    # Default score
    score = 0
    feedback = ""
    if expected_answer is None:
        # No ground truth provided — just return the reasoning
        feedback = "No expected answer provided. Returning reasoning only."
        return {
            "score": None,
            "correct": None,
            "feedback": feedback,
            "reasoning": reasoning,
            "final_answer": final_answer
        }
    # Compare final answer to expected answer (case-insensitive)
    if final_answer is None:
        feedback = "Model did not provide a final answer."
        correct = False
    else:
        correct = final_answer.strip().lower() == expected_answer.strip().lower()
        feedback = "Correct answer." if correct else "Incorrect answer."
    score = 1 if correct else 0
    return {
        "score": score,
        "correct": correct,
        "feedback": feedback,
        "reasoning": reasoning,
        "final_answer": final_answer
    }