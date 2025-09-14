from fastapi import APIRouter
import requests, math
from app.helper_functions.fetch_details import fetch_all_animals
from app.helper_functions.transform_details import transform_fields

router = APIRouter()

BASE_URL = "http://127.0.0.1:3123"  

def post_animals_in_batches(animals: list, batch_size: int = 100):
    total_batches = math.ceil(len(animals) / batch_size)
    posted = 0

    for i in range(0, len(animals), batch_size):
        batch = animals[i:i+batch_size]
        resp = requests.post(f"{BASE_URL}/animals/v1/home", json=batch)
        if resp.status_code == 200:
            posted += len(batch)

    return posted

@router.post("/animals/v1/home")
def run_pipeline():
    raw_animals = fetch_all_animals()
    cleaned_animals = transform_fields(raw_animals)
    posted_count = post_animals_in_batches(cleaned_animals)

    return {
        "status": "done",
        "fetched": len(raw_animals),
        "posted": posted_count
    }