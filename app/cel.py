from celery import Celery

# Configuración de Celery con Redis como broker
celery_app = Celery(
    "supportIQ_tasks",
    broker="redis://redis_broker:6379/0",
    backend="redis://redis_broker:6379/0",
    include=["app.tasks"]
)

# Configuración opcional para evitar pérdida de tareas
celery_app.conf.task_acks_late = True
celery_app.conf.worker_prefetch_multiplier = 1
celery_app.conf.result_expires = 3600  # Expiración de resultados en 1 hora



# Celery("supportIQ_tasks") → Define la aplicación Celery.
# broker="redis://redis_broker:6379/0" → Usa Redis como cola de mensajes.
# backend="redis://redis_broker:6379/0" → Guarda los resultados en Redis.
# include=["app.tasks"] → Importa las tareas desde el archivo tasks.py.