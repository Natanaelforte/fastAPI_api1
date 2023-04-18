from fastapi import APIRouter

from typing import List
from _decimal import Decimal
from pydantic import BaseModel
from sqlalchemy.orm import Session

from contas_a_pagar_e_receber.models.contas_a_pagar_receber_model import ContaPagarReceber

router = APIRouter(prefix='/contas-a-pagar-e-receber')


class ContasPagarReceberResponse(BaseModel):
    id: int
    descricao: str
    valor: Decimal
    tipo: str  # pagar ou receber

    class Config:
        orm_mode = True


class ContasPagarReceberRequest(BaseModel):
    descricao: str
    valor: Decimal
    tipo: str  # pagar ou receber


@router.get('/', response_model=List[ContasPagarReceberResponse])
def listar_contas(db: Session = Depends(Get_db)):
    return db.query(ContaPagarReceber).all()



@router.post('/', response_model=ContasPagarReceberResponse, status_code=201)
def criar_conta(conta:ContasPagarReceberRequest, db: Session = Depends(Get_db)):

    contas_a_pagar_e_receber = ContaPagarReceber(

        **conta_a_pagar_e_receber_request.dict()

    )

    db.add(contas_a_pagar_e_receber)
    db.commit()
    db.refresh(contas_a_pagar_e_receber)

    return contas_a_pagar_e_receber
