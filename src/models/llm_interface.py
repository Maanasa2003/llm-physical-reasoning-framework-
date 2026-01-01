import requests
from typing import List

class LLMInterface:
    """
    Interface for querying a large language model using
    the Hugging Face Router Chat Completions API.
    """

    def __init__(self, model_name: str, api_token: str):
        self.model_name = model_name
        self.api_token = api_token
        self.api_url = "https://router.huggingface.co/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }

    def generate(self, prompt: str, max_tokens: int = 256) -> str:
        payload = {
            "model": self.model_name,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": max_tokens,
            "temperature": 0.2
        }

        response = requests.post(self.api_url, headers=self.headers, json=payload)

        if response.status_code != 200:
            raise RuntimeError(
                f"Hugging Face API error {response.status_code}: {response.text}"
            )

        data = response.json()

        # Chat Completions format
        try:
            return data["choices"][0]["message"]["content"]
        except Exception:
            raise RuntimeError(f"Unexpected HF response format: {data}")

    def batch_generate(self, prompts: List[str], max_tokens: int = 256) -> List[str]:
        return [self.generate(p, max_tokens=max_tokens) for p in prompts]