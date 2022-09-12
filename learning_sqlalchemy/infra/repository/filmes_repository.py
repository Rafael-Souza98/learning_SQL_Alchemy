from infra.configs.connection import DBConnetionHandler
from infra.entities.filmes import Filmes
from sqlalchemy import delete, update
from sqlalchemy.orm.exc import NoResultFound

class FilmesRepository:
    def select(self):
        with DBConnetionHandler() as db:
           try:
                data = db.session.query(Filmes).all()
                return data
           except Exception as exception:
               return None
           except Exception as exception:
                 db.session.rollback()
                 raise exception
           
    def insert(self, titulo, genero, ano):
        with DBConnetionHandler() as db:
            try:
                insert_filme = Filmes(titulo=titulo, genero=genero, ano=ano)
                db.session.add(insert_filme)
                db.session.commit()
            except Exception as exception:
                 db.session.rollback()
                 raise exception
        
    def update (self, titulo, ano):
        try:
            with DBConnetionHandler() as db:
                update(Filmes).where(Filmes.titulo == titulo).values(ano = ano)
                db.session.commit()
        except Exception as exception:
                 db.session.rollback()
                 raise exception
        
    def delete (self, titulo):
        try:
            with DBConnetionHandler() as db:
                delete_filme = delete(Filmes).where(Filmes.titulo == titulo)
                db.session.execute(delete_filme)
                db.session.commit()
        except Exception as exception:
                 db.session.rollback()
                 raise exception
            
            
            
                
        