from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from bias_model import detect_bias

app = FastAPI(title="Bias Detection API")

class BiasRequest(BaseModel):
    text: str

class BiasResponse(BaseModel):
    bias_scores: dict

@app.post("/detect_bias", response_model=BiasResponse)
async def detect_bias_endpoint(req: BiasRequest):
    if not req.text:
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
    
    try:
        scores = detect_bias(req.text)  # Get bias scores
        return BiasResponse(bias_scores=scores)  # Send in response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Bias Detection API is running!"}
