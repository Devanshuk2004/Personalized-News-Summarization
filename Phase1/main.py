from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import summarize, MODEL_NAME

app = FastAPI(title="News Summarization API")

class SummarizeRequest(BaseModel):
    text: str
    max_length: int = 150
    min_length: int = 30

class SummarizeResponse(BaseModel):
    model_used: str
    summary: str

@app.post("/summarize", response_model=SummarizeResponse)
async def summarize_endpoint(req: SummarizeRequest):
    if not req.text:
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
    
    try:
        summary = summarize(
            req.text,
            max_length=req.max_length,
            min_length=req.min_length
        )
        return SummarizeResponse(
            model_used=MODEL_NAME,
            summary=summary
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Summarization API is running!", "model": MODEL_NAME}
