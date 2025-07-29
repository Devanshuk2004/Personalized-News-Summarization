from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import os

# Absolute path to Phase1 directory
BASE_DIR = os.path.dirname(__file__)

# Path to your fine‑tuned checkpoint
MODEL_DIR = os.path.join(BASE_DIR, "checkpoints", "checkpoint-215337")

# Load tokenizer (base model tokenizer)
tokenizer = AutoTokenizer.from_pretrained("t5-small")

# Load fine‑tuned model weights
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_DIR)

def summarize(text: str, max_length: int = 150, min_length: int = 30) -> str:
    """
    Generate a summary for the given text using fine‑tuned model.
    Repetition is controlled using no_repeat_ngram_size and repetition_penalty.
    """
    inputs = tokenizer.encode(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=1024
    )
    summary_ids = model.generate(
        inputs,
        max_length=max_length,
        min_length=min_length,
        length_penalty=1.8,
        num_beams=5,               # More beams for better structure
        num_beam_groups=5,
        no_repeat_ngram_size=8,    # Prevent repeated phrases
        repetition_penalty=4.0,    # Penalize repeated tokens
        diversity_penalty=0.5,
        early_stopping=True
    )
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)
