from sqlalchemy import Column, Integer, String
from database import Base


class Persona(Base):
    __tablename__ = "persona"

    id_persona = Column(Integer, primary_key=True, index=True)
    name_persona = Column(String, index=True)
    email_oficina = Column(String, unique=True, index=True)
