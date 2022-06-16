from fastapi import APIRouter, Depends, HTTPException
from pytest import Session

from app.api.exceptions.exceptions import ItemNotFound
from app.api.models.pet import Breed
from app.core.db import get_db
from app.services.pet import BreedService

router = APIRouter()


@router.get("/breeds/{id}", response_model=Breed)
def get_breed_by_id(id: int, db: Session = Depends(get_db)):

    breed_service = BreedService()
    breed = breed_service.get_by_id(db, id)
    if breed is None:
        raise ItemNotFound(name="breed")

    return breed
