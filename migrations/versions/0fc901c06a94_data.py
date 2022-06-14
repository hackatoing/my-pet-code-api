"""data

Revision ID: 0fc901c06a94
Revises: e9d15175f9ed
Create Date: 2022-06-14 20:00:29.136815

"""
from alembic import op
from sqlalchemy.orm.session import Session

from app.schemas.pet import Breed, Species

# revision identifiers, used by Alembic.
revision = "0fc901c06a94"
down_revision = "e9d15175f9ed"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Attach a sqlalchemy Session to the env connection
    session = Session(bind=op.get_bind())

    # Adding Species
    cat = Species(name="Cat")
    dog = Species(name="Dog")
    session.add(cat)
    session.add(dog)
    session.flush()

    # Cat breeds
    session.add(Breed(name="Persian", species_id=cat.id))
    session.add(Breed(name="Siamese", species_id=cat.id))

    # Dog breeds
    session.add(Breed(name="Poodle", species_id=dog.id))
    session.add(Breed(name="Bulldog", species_id=dog.id))
    session.add(Breed(name="German Shepherd", species_id=dog.id))

    session.commit()


def downgrade() -> None:
    # Attach a sqlalchemy Session to the env connection
    session = Session(bind=op.get_bind())

    # Delete all records
    session.query(Breed).delete()
    session.query(Species).delete()

    session.commit()
