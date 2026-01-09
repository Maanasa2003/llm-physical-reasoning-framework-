# Extracts structured answers from LLM output
def parse_answer(model_output: str) -> dict:
    """
    Extracts the reasoning steps and final answer from the LLM output.
    This is a simple baseline parser that you can improve later.
    """
    lines = model_output.strip().split("\n")
    reasoning_steps = []
    final_answer = None
    for line in lines:
        lower = line.lower()
        # Detect final answer
        if lower.startswith("final answer:"):
            final_answer = line.split(":", 1)[1].strip()
        else:
            reasoning_steps.append(line.strip())
    return {
        "reasoning": reasoning_steps,
        "final_answer": final_answer
    }