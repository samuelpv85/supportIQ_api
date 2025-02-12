from fastapi import APIRouter
from app.tasks import process_data

router = APIRouter()

@router.post("/tasks/")
async def create_task(data: dict):
    """Recibe datos y ejecuta la tarea en segundo plano."""
    task = process_data.apply_async(args=[data])
    return {"task_id": task.id, "status": "Task started"}

@router.get("/tasks/{task_id}")
async def get_task_status(task_id: str):
    """Consulta el estado de una tarea específica."""
    from app.cel import celery_app
    task_result = celery_app.AsyncResult(task_id)
    return {"task_id": task_id, "status": task_result.status, "result": task_result.result}


# POST /tasks/ → Inicia una tarea en segundo plano.
# GET /tasks/{task_id} → Consulta el estado de una tarea en ejecución.