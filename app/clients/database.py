"""
database.py
-----------
Defines the database engine, session factory, and declarative base for ORM models.
This module acts as the database client, providing connectivity to the SQLite database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session
from sqlalchemy.engine import Engine
from app.config.settings import Settings


class Base(DeclarativeBase):
    """
    Base
    ----
    Declarative base class for all ORM models.
    Ensures compatibility with SQLAlchemy 2.0 typing (Mapped, mapped_column).
    """
    pass


# Create the SQLAlchemy engine
engine: Engine = create_engine(
    Settings.BACKEND_DATABASE_URL,
    connect_args={'check_same_thread': False} if Settings.BACKEND_DATABASE_URL.startswith('sqlite') else {}
)

# Session factory bound to the engine
SessionLocal: sessionmaker[Session] = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
