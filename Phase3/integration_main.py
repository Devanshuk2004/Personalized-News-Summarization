# Phase3/integration_main.py
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from Phase1.download import download_model

download_model()

# ---- Import summarization model ----
from Phase1.model import summarize

# ---- Import bias detection model ----
from Phase2.bias_model import detect_bias

app = FastAPI()

# Request body format
class NewsInput(BaseModel):
    text: str
    max_length: int = 150
    min_length: int = 30

@app.post("/analyze_news")
def analyze_news(news: NewsInput):
    try:
        # Summarization
        summary = summarize(news.text, max_length=news.max_length, min_length=news.min_length)

        # Bias Detection
        bias_scores = detect_bias(news.text)

        return {
            "summary": summary,
            "bias_scores": bias_scores
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
