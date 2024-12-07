from sqlmodel import select, Session
from sqlalchemy import func
from math import ceil

from app import models, schemas



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

    medicos = session.exec(stmt).all()

    return schemas.PaginacaoResponse[models.Medico](
        pagina=pagina,
        limite=limite,
        qtd_itens=total,
        qtd_paginas=paginas,
        conteudo=medicos
    )

