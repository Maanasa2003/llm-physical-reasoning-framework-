# Stores reusable prompt templates for physical reasoning
def build_reasoning_prompt(question: str) -> str:
    """
    Build a structured reasoning prompt for the LLM.
    """

    prompt = f"""
You are an advanced reasoning model. Analyze the following scenario step-by-step.

Question:
     question

Instructions:
1. Think through the problem logically.
2. Break your reasoning into clear steps.
3. Provide a final answer at the end.

Begin your reasoning now.
"""

    return prompt.strip()