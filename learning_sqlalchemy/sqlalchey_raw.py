from sqlalchemy import create_engine, update, delete




    
class Filmes(Base):
    __tablename__ = "filmes"
    
    
session = Session(engine)
stmt = delete(Filmes).where(Filmes.titulo == 'Viva la vida')
session.execute(stmt)
session.commit()

