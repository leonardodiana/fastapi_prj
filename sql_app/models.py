from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Struttura(Base):
    __tablename__ = "struttura"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    informazioni = relationship("Informazioni", back_populates="owner")


class Informazioni(Base):
    __tablename__ = "informazioni"

    id = Column(Integer, primary_key=True, index=True)
    regione = Column(String, index=True)
    anno = Column(Integer, index=True)
    presenze = Column(Integer, index=True)
    arrivi = Column(Integer, index=True)
    owner_id = Column(Integer, ForeignKey("struttura.id"))

    owner = relationship("Struttura", back_populates="informazioni")
