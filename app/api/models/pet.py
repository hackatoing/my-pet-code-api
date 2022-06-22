from pydantic import BaseModel


class Species(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class Breed(BaseModel):
    id: int
    name: str
    species: Species

    class Config:
        orm_mode = True
