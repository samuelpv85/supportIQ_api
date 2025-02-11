from fastapi import APIRouter, HTTPException
from app.models.ssh_model import SSHRequest
from services.ssh_client import SSHClient

router = APIRouter()

@router.post("/execute")
def execute_command(request: SSHRequest):
    ssh = SSHClient(request.server_ip, request.username, request.password, request.key_file)

    if not ssh.connect():
        raise HTTPException(status_code=400, detail="❌ Error al conectar vía SSH")

    output = ssh.execute_command(request.command)
    ssh.close()

    return {"server": request.server_ip, "output": output}



# @router.post("/execute") → Endpoint para recibir y ejecutar comandos.
# SSHRequest → Modelo de datos que define los parámetros requeridos.
# ssh.connect() → Establece conexión SSH con el servidor remoto.
# ssh.execute_command(request.command) → Ejecuta el comando enviado.
# return {"server": request.server_ip, "output": output} → Devuelve la salida del comando.