from fastapi import FastAPI, Request
from app.routers import users, logs, ssh
from datetime import datetime
from app.mongodb import logs_collection
from app.schemas import LogEntry
import json

app = FastAPI(title="API con FastAPI, PostgreSQL, Mongo, Streamlit - supportIQ")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    response = await call_next(request)
    
    log_data = LogEntry(
        timestamp=datetime.utcnow(),
        method=request.method,
        path=str(request.url.path),
        status_code=response.status_code,
        client_ip=request.client.host
    ).dict()

    await logs_collection.insert_one(log_data)  # Guardar log en MongoDB
    
    return response


app.include_router(users.router)
app.include_router(logs.router)
app.include_router(ssh.router, prefix="/ssh")


@app.get("/")
def root():
    return {"message": "Bienvenido a la API supportIQ"}



# FastAPI(title="API con FastAPI y PostgreSQL") → Define la app.
# app.include_router(users.router) → Agrega las rutas de usuarios.

# @app.middleware("http") → Intercepta cada petición.
# request.method → Captura el método HTTP.
# request.url.path → Obtiene la ruta accedida.
# request.client.host → Obtiene la IP del cliente.
# await logs_collection.insert_one(log_data) → Guarda el log en MongoDB.