from datasets import load_dataset
def load_piqa():
    """Load PIQA dataset using streaming."""
    return load_dataset("facebook/piqa", split="train", streaming=True)
