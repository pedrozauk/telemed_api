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
                            ) -> schemas.PaginacaoResponse[list[models.Medico]]:

    retorno = crud.procura_medicos_paginado(session, body.pagina, body.limite, body.filtro)
    
    return retorno


@medico_router.post('/')
def inclui_novo_medico(payload: models.NovoMedico,
                       session: SessionDeps
                       ) -> schemas.ComumResponse[models.Medico]:
    
    novo_medico = models.Medico.model_validate(payload)
    session.add(novo_medico)
    session.commit()
    session.refresh(novo_medico)

    return schemas.ComumResponse[models.Medico](
        status=1,
        mensagem="Médico incluido com sucesso",
        conteudo=novo_medico
    )
    