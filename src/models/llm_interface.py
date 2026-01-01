import requests
from typing import List

class LLMInterface:
    """
    Core interface for querying a large language model using
    the Hugging Face Inference API (free tier supported).
    """
    def __init__(self, model_name: str, api_token: str):
        self.model_name = model_name
        self.api_token = api_token
        self.api_url = f"https://api-inference.huggingface.co/models/{model_name}"
        self.headers = {"Authorization": f"Bearer {api_token}"}
    def generate(self, prompt: str, max_tokens: int = 256) -> str:
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": max_tokens,
                "temperature": 0.2,
                "return_full_text": False
            }
        }
        response = requests.post(self.api_url, headers=self.headers, json=payload)
        if response.status_code != 200:
            raise RuntimeError(
                f"Hugging Face API error {response.status_code}: {response.text}"
            )
        data = response.json()

        try:
            return data[0]["generated_text"]
        except Exception:
            raise RuntimeError(f"Unexpected HF response format: {data}")
    def batch_generate(self, prompts: List[str], max_tokens: int = 256) -> List[str]:
        return [self.generate(p, max_tokens=max_tokens) for p in prompts]
