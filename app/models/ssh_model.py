from pydantic import BaseModel, Optional

class SSHRequest(BaseModel):
    server_ip: str
    username: str
    password: Optional[str] = None
    key_file: Optional[str] = None
    command: str

# BaseModel → Valida los datos de entrada.
# Optional[str] → Permite que password y key_file sean opcionales.