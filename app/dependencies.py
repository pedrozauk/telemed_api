from typing import Annotated
from fastapi import Depends

from app.infra.db import engine, Session



def get_session():
    with Session(engine) as session:
        yield session

SessionDeps = Annotated[Session, Depends(get_session)]