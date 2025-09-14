from fastapi import APIRouter
import requests, math
from app.helper_functions.fetch_details import fetch_all_animals
from app.helper_functions.transform_details import transform_fields
from typing import List
from app.schema.schema import PipelineResponse

router = APIRouter()

BASE_URL = "http://127.0.0.1:3123"  

def post_animals_in_batches(animals: List[dict], batch_size: int = 100) -> int:
    total_batches = math.ceil(len(animals) / batch_size)
    posted = 0

    for i in range(0, len(animals), batch_size):
        batch = animals[i:i+batch_size]
        resp = requests.post(f"{BASE_URL}/animals/v1/home", json=batch)
        if resp.status_code == 200:
            posted += len(batch)
    return posted

@router.post("/pipeline/run", response_model=PipelineResponse)
def run_pipeline():
    raw_animals_file = fetch_all_animals()
    cleaned_animals = transform_fields(raw_animals_file)
    posted_count = post_animals_in_batches(cleaned_animals)

    return PipelineResponse(
        status="done",
        fetched_file=raw_animals_file,
        fetched=len(cleaned_animals),
        posted=posted_count
    )