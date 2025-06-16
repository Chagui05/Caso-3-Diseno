from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel #Se usan para las validaciones
from typing import List
from Encryption import generar_tripleta_deks
from QueuePublisher import email_notifications


# El body para las llamadas a Generate
class Group(BaseModel):
    admin: str
    representantes: List[str]

app = FastAPI()
@app.get("/")
def read_root():
    return {"mensaje": "Hola desde FastAPI"}

@app.post("/generate-keys")
def generate(grupo: Group):

    # Se genera Tripleta
    tripleta = generar_tripleta_deks(grupo.representantes, grupo.admin)

    email_notifications(tripleta['representantes'])
    return JSONResponse(content=tripleta, status_code=200)
