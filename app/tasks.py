from time import sleep
from app.cel import celery_app

@celery_app.task(name="process_data_task")
def process_data(data: dict):
    """Simula una tarea de procesamiento pesado."""
    sleep(5)  # Simula un proceso que tarda 5 segundos
    return {"status": "completed", "processed_data": data}



# @celery_app.task → Define una tarea que Celery ejecutará en segundo plano.
# sleep(5) → Simula un proceso largo.
# Retorna el estado "completed" cuando termina.
