# verify_connection.py
from sqlalchemy import create_engine, text
from app.core.config import config
from app.database.base import Base

engine = create_engine(config.DATABASE_URL, connect_args={"check_same_thread": False})
print("Engine created.")
Base.metadata.create_all(bind=engine)
print("Database and tables created.")

with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print(result.fetchone())