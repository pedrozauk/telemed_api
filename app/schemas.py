from pydantic import BaseModel, Field
from typing import TypeVar, Generic

T = TypeVar("T")


class ComumResponse(BaseModel, Generic[T]):
    status: int 
    mensagem: str = Field(default="")
    conteudo: T


class BasePaginacao(BaseModel):
    """
    Modelo base para rotas
    """

    pagina: int
    limite: int


class PaginacaoResponse(ComumResponse, BasePaginacao, Generic[T]):
    """
    Modelo de paginacao utilizado para retornos de rotas paginadas
    """
    
    qtd_itens: int
    qtd_paginas: int


class PaginacaoRequest(BasePaginacao, Generic[T]):
    filtro: T


class FiltroMedico(BaseModel):

    nome: str
    id: str
    conselho: str
    uf_conselho: str