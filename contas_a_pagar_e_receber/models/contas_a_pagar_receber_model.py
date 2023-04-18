from sqlalchemy import column, Integer, String, Numeric

from shared.database import Base


class ContaPagarReceber(Base):
    __tablename__ = 'contas_a_pagar_e_receber'

    id = column(Integer, primary_key=True, autoincrement=True)
    inscricao = column(String(38))
    valor = column(Numeric)
    tipo = column(String(38))
