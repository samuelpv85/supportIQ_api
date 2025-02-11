from sqlalchemy import create_engine, inspect

DATABASE_URL = "postgresql://supportIQ:supportIQ@172.20.0.2:5432/supportIQ"
engine = create_engine(DATABASE_URL)

inspector = inspect(engine)
print(inspector.get_table_names(schema= "app"))  # Esto imprimirá todas las tablas en la BD