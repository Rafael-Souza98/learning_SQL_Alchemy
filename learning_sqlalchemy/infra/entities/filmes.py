from infra.configs.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Filmes(Base):
    __tablename__ = 'filmes'
    
    titulo = Column(String(20), primary_key=True)
    genero = Column(String(20), nullable=False)
    ano = Column(Integer, nullable=False)
    atores = relationship("Atores", backref="atores", lazy="subquery")