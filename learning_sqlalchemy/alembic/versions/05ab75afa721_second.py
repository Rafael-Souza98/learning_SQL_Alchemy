"""second

Revision ID: 05ab75afa721
Revises: 11b3ec7f7684
Create Date: 2022-09-12 12:01:28.203196

"""
from alembic import op
import sqlalchemy as sa
from infra.repository.filmes_repository import FilmesRepository



# revision identifiers, used by Alembic.
revision = '05ab75afa721'
down_revision = '11b3ec7f7684'
branch_labels = None
depends_on = None


def upgrade() -> None:
    filmes_repository = FilmesRepository()
    filmes_repository.insert('Filme title', 'aventura', 2015)


def downgrade() -> None:
   filmes_repository = FilmesRepository()
   filmes_repository.delete('Filme title')
