from sqlmodel import select, Session, update
from sqlalchemy import func
from math import ceil

from app import models, schemas
import app.exceptions as excp


def procura_medicos(session: Session,
                    filtro: schemas.FiltroMedico|None = None,

                    )->list[models.Medico]:
    """
    Função para consulta de médicos no banco de dados
    """

    # Inicializa stmt para realizar os filtros e paginaççao posterior 
    # caso necessário

    stmt = select(models.Medico)

    if filtro:
        if filtro.conselho:
            stmt = stmt.where(models.Medico.conselho == filtro.conselho)

        if filtro.uf_conselho:
            stmt = stmt.where(models.Medico.uf_conselho == filtro.uf_conselho)

        if filtro.nome:
            stmt = stmt.where(models.Medico.nome_completo == filtro.nome)

    return session.exec(stmt).all()


def procura_medicos_paginado(session: Session,
                    pagina: int,
                    limite: int,
                    filtro: schemas.FiltroMedico|None = None,

                    )->schemas.PaginacaoResponse[list[models.Medico]]:
    """
    Função para consulta de médicos no banco de dados
    """
    
    offset = (pagina - 1) * limite

    # Inicializa stmt para realizar os filtros e paginaççao posterior 
    # caso necessário

    stmt = select(models.Medico)



    if filtro:
        if filtro.conselho:
            stmt = stmt.where(models.Medico.conselho == filtro.conselho)

        if filtro.uf_conselho:
            stmt = stmt.where(models.Medico.uf_conselho == filtro.uf_conselho)

        if filtro.nome:
            stmt = stmt.where(models.Medico.nome_completo == filtro.nome)

    total = session.exec(select(func.count()).select_from(stmt.subquery())).one()

    paginas = 0

    if total:
        paginas = ceil(total/limite)

    stmt = stmt.offset(offset).limit(limite)

    medicos = session.exec(stmt).all()

    return schemas.PaginacaoResponse[list[models.Medico]](
        status=1,
        pagina=pagina,
        limite=limite,
        qtd_itens=total,
        qtd_paginas=paginas,
        conteudo=medicos
    )



def inativa_medico(id_medico: int, session: Session) -> bool:
    """
    Função para inativar medicos
    """

    stmt = (
        select(models.Medico)
        .filter_by(id=id_medico))
    
    medico = session.exec(stmt).first()
    if not medico or medico.status == 'I':
        return False

    medico.status = 'I'
    session.commit()

    return True

def inclui_novo_medico(novo_medico: models.NovoMedico, session: Session)->models.Medico:
    """
    Função para incluir novos medicos
    """
    medico_db = models.Medico.model_validate(novo_medico)
    session.add(medico_db)
    session.commit()
    session.refresh(medico_db)

    return medico_db

def altera_medico(id_medico: int, 
                  dados: models.MedicoBase, 
                  session: Session
                  )->models.Medico:
    """
    Função para alterar medicos
    Utiliza exclude_unset para remover atributos não enviados no parametro "dados".
    """
    dados_a_atualizar = dados.model_dump(exclude_unset=True)
    stmt = (
            update(models.Medico)
            .where(models.Medico.id == id_medico)
            .values(**dados_a_atualizar)
            .returning(models.Medico)
        )
    medico_atualizado = session.exec(stmt).scalar()
    
    session.commit()
    session.refresh(medico_atualizado)

    if not medico_atualizado:
        raise excp.NenhumRegistroRetornado()
    
    return medico_atualizado
