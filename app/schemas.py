from pydantic import BaseModel
from typing import TypeVar, Generic

T = TypeVar("T")


class BasePaginacao(BaseModel):
    """
    Modelo base para rotas
    """

    pagina: int
    limite: int


class PaginacaoResponse(BasePaginacao, Generic[T]):
    """
    Modelo de paginacao utilizado para retornos de rotas paginadas
    """
    
    conteudo: list[T]
    qtd_itens: int
    qtd_paginas: int


class PaginacaoRequest(BasePaginacao, Generic[T]):
    filtro: T


class FiltroMedico(BaseModel):

    nome: str
    id: str
    conselho: str
    uf_conselho: str