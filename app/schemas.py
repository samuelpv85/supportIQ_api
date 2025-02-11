from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# UserBase → Define los campos compartidos.
# UserCreate → Se usa para recibir datos de creación de usuarios.
# UserResponse → Se usa para devolver datos en la API.


class LogEntry(BaseModel):
    timestamp: datetime
    method: str
    path: str
    status_code: int
    client_ip: str




# timestamp: datetime → Fecha y hora de la petición.
# method: str → Método HTTP (GET, POST, etc.).
# path: str → Ruta de la API.
# status_code: int → Código de respuesta HTTP.
# client_ip: str → IP del cliente.