from typing import List, Dict, Any
class LLMInterface:
    """
    Core interface for querying a large language model.
    This is backend-agnostic: you can plug in OpenAI, local models, etc.
    """
    def __init__(self, model_name: str):
        """
        Initialize the LLM interface.
        Args:
            model_name: Identifier for the underlying model/backend.
        """
        self.model_name = model_name
    def generate(self, prompt: str, max_tokens: int = 256) -> str:
        """
        Generate a single completion for a given prompt.
        Args:
            prompt: Input text prompt.
            max_tokens: Maximum number of tokens in the output.
        Returns:
            Model-generated text.
        """
        raise NotImplementedError("LLM generate() not implemented yet.")
    def batch_generate(self, prompts: List[str], max_tokens: int = 256) -> List[str]:
        """
        Generate outputs for a batch of prompts.
        Args:
            prompts: List of input prompts.
            max_tokens: Maximum tokens for each output.
        Returns:
            List of model-generated texts.
        """
        return [self.generate(p, max_tokens=max_tokens) for p in prompts]
