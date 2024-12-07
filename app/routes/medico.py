from fastapi import APIRouter, Body, Depends
from typing import Annotated
from sqlmodel import Session

from app.dependencies import get_session
from app import crud, models, schemas


medico_router = APIRouter(prefix='/medico', tags=['Medico'])

@medico_router.post('/')
def encontra_medico(
    session: Session = Depends(get_session)
                    )-> list[models.Medico]:
    """
    Realize a consulta de médicos cadastrados na plataforma
    """
    medicos = crud.procura_medicos(session)    

    return medicos

@medico_router.post('/search')
def encontra_medico_com_paginacao(
    body: Annotated[schemas.PaginacaoRequest[schemas.FiltroMedico], Body()],
    session: Session = Depends(get_session),
                            ) -> schemas.PaginacaoResponse[models.Medico]:

    retorno = crud.procura_medicos_paginado(session, body.pagina, body.limite, body.filtro)
    
    return retorno
