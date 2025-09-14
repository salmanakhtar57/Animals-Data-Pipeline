from fastapi import APIRouter
from app.apis.animals_endpoints import router as animal_router

api_router = APIRouter()

api_router.include_router(animal_router, tags=["Animal Routers"])