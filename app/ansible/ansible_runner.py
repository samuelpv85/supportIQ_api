# import ansible_runner

# def run_playbook(playbook_path):
#     try:
#         result = ansible_runner.run(private_data_dir="app/ansible", playbook=playbook_path)
#         return result.stdout
#     except Exception as e:
#         return str(e)

# ansible_runner.run() → Ejecuta un playbook de Ansible.
# private_data_dir="ansible" → Define la carpeta donde está el inventario.
import subprocess
import os

def run_playbook(playbook_path):
    try:
        ansible_bin = "venv/bin/ansible-playbook"
        inventory_path = f"app/ansible/inventory.yml"  # O .ini según el caso
        command = [ansible_bin, "-i", inventory_path, playbook_path]
        
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return str(e)








# import ansible_runner
# import os

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Directorio del script
# ANSIBLE_DIR = os.path.join(BASE_DIR, "..", "ansible")  # Ajusta la ruta

# def run_playbook(playbook_name):
#     playbook_path = os.path.join(ANSIBLE_DIR, "playbooks", f"{playbook_name}.yml")

#     if not os.path.exists(playbook_path):
#         return f"Playbook {playbook_name}.yml no encontrado en {ANSIBLE_DIR}/playbooks"

#     try:
#         result = ansible_runner.run(private_data_dir=ANSIBLE_DIR, playbook=playbook_path)
#         return result.stdout
#     except Exception as e:
#         return str(e)





