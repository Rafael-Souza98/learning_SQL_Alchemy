from infra.configs.connection import DBConnetionHandler
from infra.entities.filmes import Filmes
from sqlalchemy import delete, update

class FilmesRepository:
    def select(self):
        with DBConnetionHandler() as db:
            data = db.session.query(Filmes).all()
            return data
        
    def insert(self, titulo, genero, ano):
        with DBConnetionHandler() as db:
            insert_filme = Filmes(titulo=titulo, genero=genero, ano=ano)
            db.session.add(insert_filme)
            db.session.commit()
    
    def update (self, titulo, ano):
        with DBConnetionHandler() as db:
            update(Filmes).where(Filmes.titulo == titulo).values(ano = ano)
            db.session.commit()
        
    def delete (self, titulo):
        with DBConnetionHandler() as db:
            delete_filme = delete(Filmes).where(Filmes.titulo == titulo)
            db.session.execute(delete_filme)
            db.session.commit()
            
            
            
                
        