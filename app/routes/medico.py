from fastapi import APIRouter, Body, Depends
from typing import Annotated
from sqlmodel import Session

from app.dependencies import get_session
from app import crud, models

medico_router = APIRouter(prefix='/medico', tags=['Medico'])

@medico_router.post('/search')
def encontra_medico(
    session: Session = Depends(get_session)
                    )-> list[models.Medico]:
    """
    Realize a consulta de médicos cadastrados na plataforma
    """
    medicos = crud.procura_medicos(session)    

    return medicos

