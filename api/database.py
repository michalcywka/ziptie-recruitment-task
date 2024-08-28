from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL')

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db_session():
    """
    Provides a database session for dependency injection.

    This function is a generator that yields a new SQLAlchemy session and ensures
    the session is properly closed after use. It is typically used with FastAPI's
    dependency injection system to provide a database session to route handlers.

    Yields:
        Session: An SQLAlchemy `Session` instance for database operations.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()