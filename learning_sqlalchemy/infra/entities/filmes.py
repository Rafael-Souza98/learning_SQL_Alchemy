from infra.configs.base import Base
from sqlalchemy import Column, Integer, String

class Filmes(Base):
    __tablename__ = 'Filmes'
    
    titulo = Column(String(20), primary_key=True)
    genero = Column(String(20), nullable=False)
    ano = Column(Integer, nullable=False)
    