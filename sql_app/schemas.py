from pydantic import BaseModel


class InformazioniBase(BaseModel):
    regione: str
    anno: int | None = None
    presenze: int | None = None
    arrivi: int | None = None


class InformazioniCreate(InformazioniBase):
    pass


class Informazioni(InformazioniBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class StrutturaBase(BaseModel):
    name: str

class StrutturaCreate(StrutturaBase):
    pass

class Struttura(StrutturaBase):
    id: int
    informazioni: list[Informazioni] = []

    class Config:
        orm_mode = True
