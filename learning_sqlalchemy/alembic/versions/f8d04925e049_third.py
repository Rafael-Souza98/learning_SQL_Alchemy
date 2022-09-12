"""third

Revision ID: f8d04925e049
Revises: 05ab75afa721
Create Date: 2022-09-12 12:15:38.754986

"""
from alembic import op
import sqlalchemy as sa
from infra.repository.filmes_repository import FilmesRepository
from infra.configs.connection import DBConnetionHandler


# revision identifiers, used by Alembic.
revision = 'f8d04925e049'
down_revision = '05ab75afa721'
branch_labels = None
depends_on = None


def upgrade() -> None:
    db_connection_handler = DBConnetionHandler()
    engine = db_connection_handler.get_engine()
    engine.execute(   ''' 
        INSERT INTO filmes (titulo, genero, ano)
        VALUES('Kung fu Panda', 'Desenho', 2012);
        ''')
    
    
   
   


def downgrade() -> None:
        db_connection_handler = DBConnetionHandler()
        engine = db_connection_handler.get_engine()
        engine.execute(
        ''' 
        DELETE FROM filmes
        WHERE titulo='Kung fu Panda';
        '''
    )