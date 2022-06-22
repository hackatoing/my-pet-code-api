from typing import List

from fastapi import APIRouter, Depends
from pytest import Session

from app.api.exceptions.exceptions import EmptyList, ItemNotFound
from app.api.models.pet import Breed, Species
from app.core.db import get_db
from app.services.pet import BreedService, SpeciesService

router = APIRouter()


@router.get("/breeds/{id}", response_model=Breed)
def get_breed_by_id(id: int, db: Session = Depends(get_db)):
    breed_service = BreedService()
    breed = breed_service.get_by_id(db, id)
    if breed is None:
        raise ItemNotFound(name="breed")

    return breed


@router.get("/breeds", response_model=List[Breed])
def get_breeds(db: Session = Depends(get_db)):
    breed_service = BreedService()
    breeds = breed_service.get_all(db)
    if len(breeds) == 0:
        raise EmptyList(name="breed")

    return breeds


@router.get("/species/{id}", response_model=Species)
def get_species_by_id(id: int, db: Session = Depends(get_db)):
    species_service = SpeciesService()
    species = species_service.get_by_id(db, id)
    if species is None:
        raise ItemNotFound(name="species")

    return species


@router.get("/species", response_model=List[Species])
def get_species(db: Session = Depends(get_db)):
    species_service = SpeciesService()
    species = species_service.get_all(db)
    if len(species) == 0:
        raise EmptyList(name="species")

    return species
