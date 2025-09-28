"""
app.py
------
Main entry point to initialize the FastAPI application and register routes
for simulation tasks.
"""

import warnings
from typing import Any
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.__version__ import __version__
from app.config.settings import Settings
from app.controllers.simulation_controller import simulation_router
from app.clients.database import Base, engine

# Suppress unnecessary warnings
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=UserWarning)
# Load environment variables from .env file
load_dotenv()
# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('uvicorn')


# Define lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI) -> Any:
    """
    Lifespan context manager for FastAPI.
    Runs once on startup and once on shutdown.
    """
    # --- Startup tasks ---
    Base.metadata.create_all(bind=engine)
    logger.info('Database is initialized and ready!')
    yield
    # --- Shutdown tasks ---
    logger.info('Shutting down application...')

# Create the FastAPI app instance
app: FastAPI = FastAPI(title=Settings.APP_NAME, version=__version__, lifespan=lifespan)

# Enable CORS to connect the backend to the local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[Settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Register simulation routes
app.include_router(simulation_router, prefix='/api/v1/simulation', tags=['simulation'])
