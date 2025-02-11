from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from app.database import Base

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