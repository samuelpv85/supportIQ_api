# from fastapi import APIRouter, HTTPException
# from app.ansible.ansible_runner import run_playbook

# router = APIRouter()

# @router.post("/run-playbook/{playbook_name}")
# def execute_playbook(playbook_name: str):
#     playbook_path = f"app/ansible/playbooks/{playbook_name}.yml"
#     try:
#         output = run_playbook(playbook_path)
#         return {"playbook": playbook_name, "output": output}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @router.post("/run-playbook/{playbook_name}") → Recibe el nombre del playbook y lo ejecuta.
# run_playbook(playbook_path) → Llama a la función que ejecuta Ansible.

# app/routers/ansible.py
from fastapi import APIRouter, HTTPException
from app.ansible.ansible_runner import run_playbook
from app.cel import celery_app

router = APIRouter()

@router.post("/run-playbook/{playbook_name}")
def execute_playbook(playbook_name: str):
    playbook_path = f"app/ansible/playbooks/{playbook_name}.yml"
    try:
        task = run_playbook.apply_async(args=[playbook_path])
        return {"task_id": task.id, "status": "Task started"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))