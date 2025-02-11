from motor.motor_asyncio import AsyncIOMotorClient
from app.config import MONGODB_URL, MONGO_DB_NAME

client = AsyncIOMotorClient(MONGODB_URL)
db = client[MONGO_DB_NAME]
logs_collection = db["logs"]



# AsyncIOMotorClient(MONGODB_URL) → Conexión asíncrona a MongoDB.
# db["logs"] → Crea una colección logs en la base de datos.