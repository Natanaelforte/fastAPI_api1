from fastapi import APIRouter

from typing import List
from _decimal import Decimal
from pydantic import BaseModel

router = APIRouter(prefix='/contas-a-pagar-e-receber')


class ContasPagarReceberResponse(BaseModel):
    id: int
    descricao: str
    valor: Decimal
    tipo: str  # pagar ou receber


class ContasPagarReceberRequest(BaseModel):
    descricao: str
    valor: Decimal
    tipo: str  # pagar ou receber


@router.get('/', response_model=List[ContasPagarReceberResponse])
def listar_contas():
    return [
        ContasPagarReceberResponse(
            id=1,
            descricao='aluguel',
            valor=1000.50,
            tipo='pagar'
        ),
        ContasPagarReceberResponse(
            id=2,
            descricao='salario',
            valor=5000,
            tipo='receber'
        ),
        ContasPagarReceberResponse(
            id=3,
            descricao='energia',
            valor=200,
            tipo='pagar'
        ),
        ContasPagarReceberResponse(
            id=4,
            descricao='agua',
            valor=150,
            tipo='pagar'
        )
    ]


@router.post('/', response_model=ContasPagarReceberResponse, status_code=201)
def criar_conta(conta:ContasPagarReceberRequest):
    return ContasPagarReceberResponse(
            id=5,
            descricao=conta.descricao,
            valor=conta.valor,
            tipo=conta.tipo
        )
