from fastapi import APIRouter, Body, Depends
from typing import Annotated
from sqlmodel import Session

from app.dependencies import SessionDeps
from app import crud, models, schemas


medico_router = APIRouter(prefix='/medico', tags=['Medico'])



@medico_router.post('/search')
def encontra_medico_com_paginacao(
    body: Annotated[schemas.PaginacaoRequest[schemas.FiltroMedico], Body()],
    session: SessionDeps,
                            ) -> schemas.PaginacaoResponse[models.Medico]:

    retorno = crud.procura_medicos_paginado(session, body.pagina, body.limite, body.filtro)
    
    return retorno


@medico_router.post('/')
def inclui_novo_medico(body: Annotated[models.Medico, Body()],
                       session: SessionDeps):
    ...