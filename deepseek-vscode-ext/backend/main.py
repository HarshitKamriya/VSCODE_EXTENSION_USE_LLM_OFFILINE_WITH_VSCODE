"""
Ollama Model Server - FastAPI Backend Proxy
Proxies requests from the DeepSeek VS Code extension to a local Ollama instance.
"""

import os
import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(title="Ollama AI Model Server Proxy", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
MODEL_NAME = os.getenv("MODEL_NAME", "deepseek-r1:1.5b")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
TOP_P = float(os.getenv("TOP_P", "0.95"))

current_model_name = MODEL_NAME

class CompletionRequest(BaseModel):
    prompt: str
    max_tokens: int = 256
    temperature: float = TEMPERATURE
    top_p: float = TOP_P

class CodeReviewRequest(BaseModel):
    code: str
    language: str = "python"

class CompletionResponse(BaseModel):
    completion: str
    prompt: str
    model: str
    tokens_used: int

class CodeReviewResponse(BaseModel):
    review: str
    issues: list
    suggestions: list

@app.on_event("startup")
async def startup_event():
    logger.info(f"Starting Ollama Proxy Server")
    logger.info(f"Target Ollama URL: {OLLAMA_BASE_URL}")
    logger.info(f"Target Model: {current_model_name}")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=5.0)
            response.raise_for_status()
            
            # Check if our model is available in Ollama
            models = response.json().get("models", [])
            model_loaded = any(m.get("name") == current_model_name for m in models)
            
            return {
                "status": "healthy",
                "model": current_model_name,
                "device": "ollama",
                "model_loaded": model_loaded,
                "8bit_enabled": False
            }
    except Exception as e:
        logger.warning(f"Ollama health check failed: {e}")
        return {
            "status": "unhealthy",
            "model": current_model_name,
            "device": "ollama",
            "model_loaded": False,
            "error": str(e)
        }

@app.get("/api/models")
async def list_models():
    """List available models in Ollama"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=5.0)
            response.raise_for_status()
            models = response.json().get("models", [])
            
            suggested_models = []
            for m in models:
                suggested_models.append({
                    "name": m.get("name"),
                    "description": f"Ollama model ({m.get('details', {}).get('parameter_size', 'unknown')})",
                    "size": m.get('details', {}).get('parameter_size', 'unknown')
                })
                
            return {
                "current_model": current_model_name,
                "device": "ollama",
                "model_loaded": True,
                "suggested_models": suggested_models
            }
    except Exception as e:
        logger.error(f"Failed to list Ollama models: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/models/load")
async def load_different_model(request: dict):
    """Change the active model"""
    global current_model_name
    
    if "model_name" not in request:
        raise HTTPException(status_code=400, detail="model_name is required")
    
    new_model_name = request["model_name"]
    current_model_name = new_model_name
    logger.info(f"Switched target model to: {current_model_name}")
    
    return {
        "success": True,
        "model": current_model_name,
        "device": "ollama"
    }

@app.post("/api/complete", response_model=CompletionResponse)
async def code_completion(request: CompletionRequest):
    """
    Generate code completion by forwarding to Ollama
    """
    try:
        payload = {
            "model": current_model_name,
            "prompt": request.prompt,
            "stream": False,
            "options": {
                "temperature": request.temperature,
                "top_p": request.top_p,
                "num_predict": request.max_tokens
            }
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{OLLAMA_BASE_URL}/api/generate",
                json=payload,
                timeout=60.0
            )
            response.raise_for_status()
            result = response.json()
            
            return CompletionResponse(
                completion=result.get("response", "").strip(),
                prompt=request.prompt,
                model=current_model_name,
                tokens_used=result.get("eval_count", 0)
            )
            
    except Exception as e:
        logger.error(f"Error during completion via Ollama: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/review", response_model=CodeReviewResponse)
async def code_review(request: CodeReviewRequest):
    """
    Perform code review by forwarding to Ollama
    """
    try:
        review_prompt = f"Review the following {request.language} code and provide:\n1. Issues found\n2. Suggestions for improvement\n\nCode:\n```{request.language}\n{request.code}\n```\n\nReview:"
        
        payload = {
            "model": current_model_name,
            "prompt": review_prompt,
            "stream": False,
            "options": {
                "temperature": 0.5,
                "top_p": TOP_P,
                "num_predict": 512
            }
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{OLLAMA_BASE_URL}/api/generate",
                json=payload,
                timeout=120.0
            )
            response.raise_for_status()
            result = response.json()
            
            return CodeReviewResponse(
                review=result.get("response", "").strip(),
                issues=[],
                suggestions=[]
            )
            
    except Exception as e:
        logger.error(f"Error during review via Ollama: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )
