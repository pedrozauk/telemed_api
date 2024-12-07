from fastapi import FastAPI


from app.routes.auth import auth_router
from app.routes.medico import medico_router
from app.infra.db import create_all_tables


def app_lifespan(app: FastAPI):
    #Ao iniciar
    
    #Inicializa tabelas
    create_all_tables()
    yield

    #Ao encerrar


app = FastAPI(lifespan=app_lifespan)

app.include_router(auth_router)
app.include_router(medico_router)



@app.get('/hello')
def hello():
    return {"msg":"hello world"}