from sqlalchemy import Column, Integer, String
from zdatabase import Base


class Perro(Base):
    __tablename__ = "perro"

    id_perro = Column(Integer, primary_key=True, index=True)
    name_perro = Column(String, index=True)
    owner = Column(String, unique=True, index=True)
