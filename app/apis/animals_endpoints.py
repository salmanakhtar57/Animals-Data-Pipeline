from fastapi import APIRouter
import json

router = APIRouter()

with open(r"D:\Backend\Tech Companies Tasks\Funsol Technologies Task\Animals-Data-Pipeline\app\apis\animal_details.json", "r") as file:
    content = json.load(file)



for animal in content:
    print(animal)

    # Function to fetch Animal Details 
def fetch_animal_details():
    pass
# @router.get("/animals/v1/animals")
# def get_list_of_animals(animals):
#     return animals

@router.get("/animals/v1/animals/<id>")
def get_animal_by_id():
    pass

@router.post("/animals/v1/home")
def tarnsorm_animal_data():
    pass