import json
import re

def parse_answer(raw_output: str):
    """
    Extracts JSON from the model output and returns the final_answer field.
    Falls back to old parsing logic if JSON is missing.
    """

    # Try to extract JSON block
    json_match = re.search(r"\{.*\}", raw_output, re.DOTALL)
    if json_match:
        try:
            data = json.loads(json_match.group(0))
            return {
                "reasoning": [],
                "equation": None,
                "solve_for": None,
                "known_values": {},
                "final_answer": data.get("final_answer")
            }
        except json.JSONDecodeError:
            pass  # fall back to legacy parser

    # Legacy fallback (your old logic)
    lines = raw_output.split("\n")

    reasoning = []
    equation = None
    solve_for = None
    known_values = {}
    final_answer = None

    for line in lines:
        stripped = line.strip()

        if stripped[:2].isdigit() and stripped[1] == '.':
            reasoning.append(stripped)

        if stripped.startswith("Equation:"):
            equation = stripped.split(":", 1)[1].strip()

        elif stripped.startswith("Solve for:"):
            solve_for = stripped.split(":", 1)[1].strip()

        elif stripped.startswith("Known values:"):
            kv_pairs = stripped.split(":", 1)[1].strip()
            for pair in kv_pairs.split(","):
                if "=" in pair:
                    parts = pair.split("=")
                    k = parts[0].strip()
                    v = parts[1].strip()
                    try:
                        known_values[k] = float(v)
                    except:
                        pass

        elif stripped.startswith("Final Answer:"):
            final_answer = stripped.split(":", 1)[1].strip()

    return {
        "reasoning": reasoning,
        "equation": equation,
        "solve_for": solve_for,
        "known_values": known_values,
        "final_answer": final_answer
    }