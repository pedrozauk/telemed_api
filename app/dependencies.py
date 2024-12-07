from app.infra.db import engine, Session



def get_session():
    with Session(engine) as session:
        yield session