# database/dependencies.py
from app.database.session import SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends

def get_db():
    """
    Dependency that provides a new database session per request.
    Closes the session once the request is complete.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
