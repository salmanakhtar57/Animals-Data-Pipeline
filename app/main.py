from fastapi import FastAPI
import uvicorn
from app.core.routing import api_router

app = FastAPI

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("app.main:QA_Agent_Application", host="0.0.0.0", port=5000, reload=True)