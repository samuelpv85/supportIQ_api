from fastapi import APIRouter, HTTPException
from app.ansible.ansible_runner import run_playbook

router = APIRouter()

@router.post("/run-playbook/{playbook_name}")
def execute_playbook(playbook_name: str):
    playbook_path = f"app/ansible/playbooks/{playbook_name}.yml"
    # inventory_path = f"app/ansible/inventory.yml"  # O .ini según el caso
    try:
        output = run_playbook(playbook_path)
        return {"playbook": playbook_name, "output": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



# @router.post("/run-playbook/{playbook_name}") → Recibe el nombre del playbook y lo ejecuta.
# run_playbook(playbook_path) → Llama a la función que ejecuta Ansible.