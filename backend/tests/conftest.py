# tests/conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database.base import Base
from app.database import init_db, SessionLocal

# Set up an SQLite in-memory database for testing
SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Initialize the database and create tables
# @pytest.fixture(scope="module")
# def test_db():
#     # Create all tables
#     Base.metadata.create_all(bind=engine)
#     yield
#     # Drop all tables after the test run
#     Base.metadata.drop_all(bind=engine)

# Dependency to provide a new session for each test
@pytest.fixture(scope="function")
def db_session():
    # Create tables
    Base.metadata.create_all(bind=engine)  # This initializes tables without calling init_db directly
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)
        session.close()
