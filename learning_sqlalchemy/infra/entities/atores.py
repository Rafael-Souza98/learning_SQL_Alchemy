from infra.configs.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Atores(Base):
    __tablename__ = 'atores'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(20))
    titulo_filme = Column(String(20), ForeignKey("filmes.titulo"))
    
    
    
    
    def __repr__(self):
        return f"Atores [nome={self.nome}, filme={self.titulo_filme}]"
    