from infra.configs.connection import DBConnetionHandler
from infra.entities.atores import Atores
from infra.entities.filmes import Filmes
from sqlalchemy import delete, update

class AtoresRepository:
    def select(self):
        with DBConnetionHandler() as db:
            data = db.session\
            .query(Atores, Filmes)\
            .with_entities(
                Atores.nome,
                Filmes.titulo,
                Filmes.ano)\
                .all()   
            
            return data
        
    