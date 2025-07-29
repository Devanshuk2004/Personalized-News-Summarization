from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

# Adjust paths to import Phase 1 and Phase 2
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../Phase1")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../Phase2")))

from model import summarize  # Phase 1 summarization
from bias_model import detect_bias  # Phase 2 bias detection

# Initialize FastAPI
app = FastAPI(title="Integrated News Analysis API")

# ✅ Enable CORS for Chrome Extension
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # (Optional: Restrict to chrome-extension://<your-id>)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request body model
class AnalyzeNewsRequest(BaseModel):
    text: str
    max_length: int = 150
    min_length: int = 30

# Response model
class AnalyzeNewsResponse(BaseModel):
    summary: str
    bias_scores: dict

# API endpoint
@app.post("/analyze_news", response_model=AnalyzeNewsResponse)
async def analyze_news(req: AnalyzeNewsRequest):
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
    
    try:
        # Run summarization
        summary = summarize(
            req.text,
            max_length=req.max_length,
            min_length=req.min_length
        )
        
        # Run bias detection
        bias_scores = detect_bias(req.text)
        
        return AnalyzeNewsResponse(summary=summary, bias_scores=bias_scores)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Integrated API is running on port 8002!"}
