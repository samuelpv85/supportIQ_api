# import subprocess
# import os

# def run_playbook(playbook_path):
#     try:
#         ansible_bin = "venv/bin/ansible-playbook"
#         inventory_path = f"app/ansible/inventory.yml"  # O .ini según el caso
#         command = [ansible_bin, "-i", inventory_path, playbook_path]
        
#         result = subprocess.run(command, capture_output=True, text=True)
#         return result.stdout if result.returncode == 0 else result.stderr
#     except Exception as e:
#         return str(e)
    
from app.cel import celery_app
import subprocess
import os
from datetime import datetime
from app.mongodb import logs_collection

@celery_app.task(name="run_ansible_playbook")
def run_playbook(playbook_path):
    try:
        ansible_bin = "venv/bin/ansible-playbook"
        inventory_path = f"app/ansible/inventory.yml"
        command = [ansible_bin, "-i", inventory_path, playbook_path]

        result = subprocess.run(command, capture_output=True, text=True)
        output = result.stdout if result.returncode == 0 else result.stderr

        # Guardar en MongoDB
        task_result = {
            "task_id": run_playbook.request.id,
            "playbook_name": os.path.basename(playbook_path),
            "output": output,
            "status": "SUCCESS" if result.returncode == 0 else "FAILURE",
            "timestamp": datetime.utcnow()
        }
        logs_collection.insert_one(task_result)

        return output
    except Exception as e:
        logs_collection.insert_one({
            "task_id": run_playbook.request.id,
            "playbook_name": os.path.basename(playbook_path),
            "output": str(e),
            "status": "FAILURE",
            "timestamp": datetime.utcnow()
        })
        return str(e)