from fastapi import APIRouter

router = APIRouter()

@router.get("/animals/v1/animals")
def get_list_of_animals(animals):
    return animals

@router.get("/animals/v1/animals/<id>")
def get_animal_by_id():
    pass

@router.post("/animals/v1/home")
def tarnsorm_animal_data():
    pass