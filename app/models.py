
from sqlmodel import SQLModel, Field, Date
import datetime
from typing import Optional





class MedicoBase(SQLModel):


    nome_completo: str = Field(index=True)
    cpf: str
    data_nascimento: datetime.date = Field()
    conselho: str = Field(index=True)
    numero_conselho: int
    uf_conselho: str
    status: str = Field(default='A')

class NovoMedico(MedicoBase):
    ...

class AtualizacaoMedico(SQLModel):
    nome_completo: Optional[str] = None 
    cpf: Optional[str] = None
    data_nascimento: Optional[datetime.date] = None
    conselho: Optional[str] = None
    numero_conselho: Optional[int] = None
    uf_conselho: Optional[str] = None
    status: Optional[str] = None

class Medico(MedicoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)