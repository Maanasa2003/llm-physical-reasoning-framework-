import os
from typing import List, Optional
import requests
from dotenv import load_dotenv

load_dotenv()

class LLMInterface:
    """
    Clean, stable interface for Hugging Face Router Chat Completions API.
    Adds raw-output debugging and safer extraction.
    """

    def __init__(self, model_name: str, api_token: Optional[str] = None):
        self.model_name = model_name

        if api_token is None:
            api_token = os.getenv("HF_API_TOKEN")

        if not api_token:
            raise RuntimeError("Missing HF_API_TOKEN. Add it to your .env or pass it explicitly.")

        self.api_token = api_token
        self.api_url = "https://router.huggingface.co/v1/chat/completions"

        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json",
        }

    def generate(self, prompt: str, max_tokens: int = 512) -> str:
        
        payload = {
            "model": self.model_name,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens,
            "temperature": 0.0,
            "top_p": 0.9,
        }

        response = requests.post(self.api_url, headers=self.headers, json=payload)

        if response.status_code != 200:
            raise RuntimeError(f"HF Router error {response.status_code}: {response.text}")

        data = response.json()

        # Extract content safely
        try:
            choices = data.get("choices")

            if not choices:
                print("WARNING: No 'choices' returned by model.")
                return ""

            # Case 1: choices is a list (normal)
            if isinstance(choices, list):
                content = choices[0]["message"]["content"]
                return content.strip() if content else ""

            # Case 2: choices is a dict with string keys
            if isinstance(choices, dict):
                first_key = sorted(choices.keys())[0]
                content = choices[first_key]["message"]["content"]
                return content.strip() if content else ""

            print("WARNING: Unknown choices format:", choices)
            return ""

        except Exception as e:
            print("ERROR extracting model output:", e)
            print("Full data:", data)
            return ""

    def batch_generate(self, prompts: List[str], max_tokens: int = 256) -> List[str]:
        return [self.generate(p, max_tokens=max_tokens) for p in prompts]