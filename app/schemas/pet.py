from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.db import Base


class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    breed_id = Column(Integer, ForeignKey("breeds.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    created_ip = Column(String(255), nullable=False)

    user = relationship("User", back_populates="pets")


class Breed(Base):
    __tablename__ = "breeds"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    species_id = Column(Integer, ForeignKey("species.id"))

    species = relationship("Species", back_populates="breed")


class Species(Base):
    __tablename__ = "species"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)

    breed = relationship("Breed", back_populates="species")
