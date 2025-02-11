import configparser
import os

# Obtener la ruta absoluta del archivo config.ini
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "../config.ini")

# Cargar configuración desde config.ini
config = configparser.ConfigParser()
config.read(CONFIG_PATH)

# Construir la URL de conexión a PostgreSQL
DB_CONFIG = config["database"]
DATABASE_URL = f"postgresql://{DB_CONFIG['USER']}:{DB_CONFIG['PASSWORD']}@{DB_CONFIG['HOST']}:{DB_CONFIG['PORT']}/{DB_CONFIG['NAME']}"

# Construir la URL de conexión a MONGP
DB_CONFIG_MONGO = config["databaseMongo"]
MONGODB_URL = f"mongodb://{DB_CONFIG_MONGO['USER']}:{DB_CONFIG_MONGO['PASSWORD']}@{DB_CONFIG_MONGO['HOST']}:{DB_CONFIG_MONGO['PORT']}"
# MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://admin:password@localhost:27017")
MONGO_DB_NAME = "audit_logs"




# configparser.ConfigParser() → Carga el archivo .ini.
# config.read(CONFIG_PATH) → Lee las propiedades de la sección [database].
# DATABASE_URL → Se genera dinámicamente con los valores del archivo config.ini.

# MONGODB_URL → Obtiene la URL de MongoDB.
# MONGO_DB_NAME → Nombre de la base de datos de logs.