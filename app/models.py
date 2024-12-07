
from sqlmodel import SQLModel, Field
from datetime import date
from typing import Optional


class Medico(SQLModel, table=True):

    id: Optional[int] = Field(primary_key=True)
    nome_completo: str = Field(default=None, index=True)
    cpf: str
    data_nascimento: date
    conselho: str = Field(index=True)
    numero_conselho: int
    uf_conselho: str
    status: str

