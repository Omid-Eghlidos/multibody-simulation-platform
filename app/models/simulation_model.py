"""
simulation_model.py
-------------------
Defines the Object Relational Mapping (ORM) schema for storing simulation runs in the database.
"""

from datetime import datetime
from sqlalchemy import String, Text, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from app.clients.database import Base


class Simulation(Base):
    """
    Simulation
    ----------
    ORM model representing a simulation run.
    Stores parameters, their hash for caching, results, and timestamp.
    """

    __tablename__ = 'simulations'
    # Primary key
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    # Input parameters (as JSON string)
    params_json: Mapped[str] = mapped_column(Text, nullable=False)
    # Deterministic hash of parameters for caching
    params_hash: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    # Simulation results (as JSON string)
    results_json: Mapped[str] = mapped_column(Text, nullable=False)
    # Timestamp for creation
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    def __repr__(self) -> str:
        """
        Returns a string representation of the Simulation object for debugging.
        """
        return (
            f'<Simulation(id={self.id}, '
            f'params_hash={self.params_hash!r}, '
            f'created_at={self.created_at})>'
        )
