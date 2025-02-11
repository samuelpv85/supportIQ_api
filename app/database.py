from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import DATABASE_URL

# Crear el motor de conexión
engine = create_engine(DATABASE_URL)

# Crear la sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos ORM
Base = declarative_base()


# create_engine(DATABASE_URL) → Crea el motor de PostgreSQL.
# SessionLocal → Manejador de sesiones de SQLAlchemy.
# Base → Se usará para definir modelos ORM.