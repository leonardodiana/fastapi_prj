from pydantic import BaseModel


class InformazioniBase(BaseModel):
    regioni: str
    anno: int | None = None
    partenze: int | None = None
    arrivi: int | None = None


class InformazioniCreate(InformazioniBase):
    pass


class Informazioni(InformazioniBase):
    id: int
    struttura_id: int

    class Config:
        orm_mode = True


class StrutturaBase(BaseModel):
    nome: str



class Struttura(StrutturaBase):
    id: int
    informazioni: list[Informazioni] = []

    class Config:
        orm_mode = True
