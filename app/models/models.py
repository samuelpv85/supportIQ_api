from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from app.database import Base
from pydantic import BaseModel
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "app"}  # <--- Definir el esquema aquí

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

# __tablename__ = "users" → Define la tabla en PostgreSQL.
# Column(Integer, primary_key=True, index=True) → Clave primaria.
# Column(String(50), unique=True, nullable=False) → Nombre de usuario único.
# Column(TIMESTAMP, server_default=func.now()) → Marca de tiempo automática.


# app/models/models.py
class AnsibleTaskResult(BaseModel):
    task_id: str
    playbook_name: str
    output: str
    status: str
    timestamp: datetime