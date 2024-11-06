# database/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import config
from app.database.base import Base

SQLALCHEMY_DATABASE_URL = config.DATABASE_URL
print(f"SQLALCHEMY_DATABASE_URL: {SQLALCHEMY_DATABASE_URL}")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    # Ensure tables are created
    Base.metadata.create_all(bind=engine)
    print("Database and tables created.")


