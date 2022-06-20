from sqlalchemy.orm import Session

from app.schemas.pet import Breed, Species


class BreedService:
    def get_by_id(self, db: Session, id: int) -> Breed:
        return db.query(Breed).filter(Breed.id == id).first()

    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(Breed).offset(skip).limit(limit).all()


class SpeciesService:
    def get_by_id(self, db: Session, id: int) -> Species:
        return db.query(Species).filter(Species.id == id).first()

    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(Species).offset(skip).limit(limit).all()
