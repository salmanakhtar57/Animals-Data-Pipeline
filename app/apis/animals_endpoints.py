from fastapi import APIRouter
import json
from datetime import datetime, timezone

router = APIRouter()


# Function to Transform Variable 
def transform_fields(file_path: str):
    with open(file_path, "r") as file:
        animals = json.load(file)

    transformed = []

    for animal in animals:
        if "friends" in animal:
            if animal["friends"] and type(animal["friends"]) is str:
                seperated = animal["friends"].split(",")
                cleaned = []
                for f in seperated:
                    f = f.strip()
                    if f:
                        cleaned.append(f)
                animal["friends"] = cleaned
            elif not animal["friends"]:
                animal["friends"] = []

        # Handle born_at
        if "born_at" in animal and animal["born_at"]:
            ts = int(animal["born_at"]) / 1000
            dt = datetime.fromtimestamp(ts, tz=timezone.utc)
            animal["born_at"] = dt.isoformat()

        transformed.append(animal)

    return transformed

animals = transform_fields(r"D:\Backend\Tech Companies Tasks\Funsol Technologies Task\Animals-Data-Pipeline\app\apis\animal_details.json")
print(animals)


# @router.get("/animals/v1/animals")
# def get_list_of_animals(animals):
#     return animals

@router.get("/animals/v1/animals/<id>")
def get_animal_by_id():
    pass

@router.post("/animals/v1/home")
def tarnsorm_animal_data():
    pass