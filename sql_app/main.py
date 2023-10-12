from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/struttura/{struttura_id}/informazioni/", response_model=schemas.Informazioni)
def create_informazioni_for_struttura(
    struttura_id: int, informazioni: schemas.InformazioniCreate, db: Session = Depends(get_db)
):
    return crud.create_struttura_informazioni(db=db, informazioni=informazioni, struttura_id=struttura_id)


@app.post("/struttura/", response_model=schemas.Struttura)
def create_struttura(struttura: schemas.Struttura, db: Session = Depends(get_db)):
    return crud.create_struttura(db=db, struttura=struttura)


@app.get("/informazioni/", response_model=list[schemas.Informazioni])
def read_informazioni(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    informazioni = crud.get_informazioni(db, skip=skip, limit=limit)
    return informazioni



@app.get("/strutture/", response_model=list[schemas.Struttura])
def read_strutture(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    strutture = crud.get_strutture(db, skip=skip, limit=limit)
    return strutture
