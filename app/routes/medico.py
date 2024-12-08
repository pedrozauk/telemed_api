from fastapi import APIRouter, Body, Path, Depends
from typing import Annotated
from sqlmodel import Session

from app.dependencies import SessionDeps
from app import crud, models, schemas
import app.exceptions as excp

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
    
    novo_medico = crud.inclui_novo_medico(payload, session)

    return schemas.ComumResponse[models.Medico](
        status=1,
        mensagem="Médico incluido com sucesso",
        conteudo=novo_medico
    )

@medico_router.delete('/{id_medico}')
def deleta_medico(id_medico: int,
                  session: SessionDeps
                  )->schemas.ComumResponse[None]:
    deletado = crud.inativa_medico(id_medico, session)

    if not deletado:
        return schemas.ComumResponse[None](
            status=0,
            mensagem="Não foi possível deletar o médico, registro não encontrado",
            conteudo=None
        )
    
    return schemas.ComumResponse[None](
            status=1,
            mensagem="Medico deletado com sucesso",
            conteudo=None
        )    


@medico_router.patch('/{id_medico}')
def altera_medico(id_medico: int, 
                  payload: models.AtualizacaoMedico,
                  session: SessionDeps
                  )-> schemas.ComumResponse[models.Medico|None]:
    
    """
    Altera um médico no banco de dados

    Serão somente atualizados os campos que forem passados no payload
    
    """
    if id_medico == 0:
        return schemas.ComumResponse[None](
            status=0,
            mensagem="Id inválido",
            conteudo=None
        ) 
    try:
        medico_atualizado = crud.altera_medico(id_medico, payload, session)
    except excp.NenhumRegistroRetornado:

        return schemas.ComumResponse[None](
            status=0,
            mensagem="Medico não encontrado",
            conteudo=None
        )

    return schemas.ComumResponse[models.Medico](
        status=1,
        mensagem="Médico alterado com sucesso",
        conteudo=medico_atualizado
    ) 


