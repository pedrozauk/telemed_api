from sqlmodel import select, Session
from app import models



def procura_medicos(session: Session)->list[models.Medico]:
    stmt = select(models.Medico)
    return session.exec(stmt).all()
