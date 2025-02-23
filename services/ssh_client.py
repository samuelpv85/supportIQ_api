import paramiko

class SSHClient:
    def __init__(self, hostname, username, password=None, key_file=None):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.key_file = key_file
        self.client = None

    def connect(self):
        try:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            if self.key_file:
                self.client.connect(self.hostname, username=self.username, key_filename=self.key_file)
            else:
                self.client.connect(self.hostname, username=self.username, password=self.password)

            return True
        except Exception as e:
            print(f"Error al conectar: {e}")
            return False

    def execute_command(self, command):
        if self.client is None:
            return "❌ No conectado"

        stdin, stdout, stderr = self.client.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()

        return output if output else error

    def close(self):
        if self.client:
            self.client.close()



# paramiko.SSHClient() → Crea un cliente SSH.
# set_missing_host_key_policy() → Permite conexiones a hosts desconocidos.
# connect() → Se conecta usando contraseña o clave SSH.
# exec_command() → Ejecuta un comando en el servidor remoto.
# close() → Cierra la conexión SSH.