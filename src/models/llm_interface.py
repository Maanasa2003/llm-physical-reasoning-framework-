import os
from typing import List, Optional

import requests
from dotenv import load_dotenv
# Load environment variables from .env at project root
load_dotenv()

class LLMInterface:
    """
    Interface for querying a large language model using
    the Hugging Face Router Chat Completions API.
    """
    def __init__(self, model_name: str, api_token: Optional[str] = None):
        self.model_name = model_name

        # Allow passing token explicitly or loading from .env
        if api_token is None:
            api_token = os.getenv("HF_API_TOKEN")

        if not api_token:
            raise RuntimeError(
                "Hugging Face API token is missing. "
                "Set HF_API_TOKEN in your .env or pass api_token to LLMInterface."
            )

        self.api_token = api_token
        self.api_url = "https://router.huggingface.co/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json",
        }

    def generate(self, prompt: str, max_tokens: int = 256) -> str:
        """
        Send a single prompt to the HF Router and return the model's text response.
        """
        payload = {
            "model": self.model_name,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": max_tokens,
            "temperature": 0.2,
        }

        response = requests.post(self.api_url, headers=self.headers, json=payload)

        if response.status_code != 200:
            raise RuntimeError(
                f"Hugging Face API error {response.status_code}: {response.text}"
            )

        data = response.json()

        # Chat Completions format
        try:
            return data["choices"]["0"]["message"]["content"]
        except Exception:
            # Fallback for usual list-based format
            try:
                return data["choices"][0]["message"]["content"]
            except Exception:
                raise RuntimeError(f"Unexpected HF response format: {data}")

    def batch_generate(self, prompts: List[str], max_tokens: int = 256) -> List[str]:
        """
        Convenience method to generate outputs for a list of prompts.
        """
        return [self.generate(p, max_tokens=max_tokens) for p in prompts]