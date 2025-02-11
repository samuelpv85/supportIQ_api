from fastapi import APIRouter
from app.mongodb import logs_collection
from app.schemas import LogEntry
from typing import List

router = APIRouter(prefix="/logs", tags=["Logs"])

@router.get("/", response_model=List[LogEntry])
async def get_logs():
    logs = await logs_collection.find().to_list(100)
    return logs



# @router.get("/") → Endpoint para obtener los logs.
# logs_collection.find().to_list(100) → Recupera hasta 100 registros de MongoDB.