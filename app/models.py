
from sqlmodel import SQLModel, Field, Date
import datetime
from typing import Optional





class MedicoBase(SQLModel):


    nome_completo: str = Field(index=True)
    cpf: str
    data_nascimento: datetime.date = Field(allow_mutation=True)
    conselho: str = Field(index=True)
    numero_conselho: int
    uf_conselho: str
    status: str

class NovoMedico(MedicoBase):
    ...

class Medico(MedicoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)