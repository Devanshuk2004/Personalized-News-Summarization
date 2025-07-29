from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Using a locally cached model
MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"

# Load tokenizer & model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

LABELS = ["negative", "positive"]  # This is for sentiment — we’ll interpret bias later

def detect_bias(text: str) -> dict:
    """
    Detect bias (simulated via sentiment classification for now).
    Positive sentiment -> possible favorable bias
    Negative sentiment -> possible unfavorable bias
    """
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    
    with torch.no_grad():
        logits = model(**inputs).logits
    
    probs = torch.nn.functional.softmax(logits, dim=-1)[0]
    
    # Map sentiment to bias scores (just example)
    bias_result = {
        "unfavorable_bias": round(float(probs[0]), 4),  # negative
        "favorable_bias": round(float(probs[1]), 4)     # positive
    }
    return bias_result

if __name__ == "__main__":
    sample = "The government’s new policy is a major win for workers."
    print("Bias scores:", detect_bias(sample))
