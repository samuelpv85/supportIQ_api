from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Column, Integer, String
from app.database import Base  # Asegúrate de que 'Base' esté correctamente importado


class SSHRequest(BaseModel):
    server_ip: str
    username: str
    password: Optional[str] = None
    key_file: Optional[str] = None
    command: str

# BaseModel → Valida los datos de entrada.
# Optional[str] → Permite que password y key_file sean opcionales.



class SSHModel(Base):
    __tablename__ = "ssh_connections"

    id = Column(Integer, primary_key=True, index=True)
    host = Column(String, nullable=False)
    user = Column(String, nullable=False)
    password = Column(String, nullable=False)  # ⚠️ No se recomienda guardar contraseñas en texto plano