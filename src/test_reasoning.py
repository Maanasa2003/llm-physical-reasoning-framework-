from src.models.llm_interface import LLMInterface
from src.core.reasoning_engine import ReasoningEngine
import os
HF_API_TOKEN = os.getenv("HF_API_TOKEN")

llm = LLMInterface(
    model_name="meta-llama/Llama-3.2-1B-Instruct",
    api_token=HF_API_TOKEN
)

engine = ReasoningEngine(llm)

scenario = {
    "description": "A ball is dropped from a height of 10 meters.",
    "expected": "It falls to the ground.",
    "key_concept": "gravity"
}

result = engine.run(scenario)
print(result)