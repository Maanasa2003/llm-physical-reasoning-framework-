from utils.config import HF_API_TOKEN
from models.llm_interface import LLMInterface
model = LLMInterface(
    model_name="google/gemma-2-2b-it",
    api_token=HF_API_TOKEN
)
response = model.generate("Explain gravity in one sentence.")
print(response)