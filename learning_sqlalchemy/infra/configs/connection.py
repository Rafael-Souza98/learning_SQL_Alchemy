from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


class DBConnetionHandler:
    
    def __init__(self) -> None:
        self.__connection_string = 'mysql+pymysql://root:28285456@localhost:3306/cinema'
        self.__engine = self.__create_database_engine()
        self.session = None
        
    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine
    
    def get_engine(self):
        self._engine 
        
        
    def __enter__(self):
        session = Session(self.__engine)
        self.session = session
        return self
    
    def __exit__(self, type, value, traceback):
        self.session.close()

    