from sqlalchemy.orm import Session

from . import models, schemas


def get_informazione(db: Session, informazioni_id: int):
    return db.query(models.Informazioni).filter(models.Informazioni.id == informazioni_id).first()


def get_informazioni(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Informazioni).offset(skip).limit(limit).all()


def get_strutture(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Struttura).offset(skip).limit(limit).all()


def create_struttura_informazioni(db: Session, informazioni: schemas.InformazioniCreate, struttura_id: int):
    db_info = models.Informazioni(**informazioni.model_dump(), owner_id=struttura_id)
    db.add(db_info)
    db.commit()
    db.refresh(db_info)
    return db_info

def create_struttura(db: Session, struttura: schemas.StrutturaCreate):   
    db_struttura = models.Struttura(name=struttura.name)
    db.add(db_struttura)
    db.commit()
    db.refresh(db_struttura)
    return db_struttura
