"""
settings.py
-----------
Application configuration settings.
Loads environment variables and provides defaults for local development.
"""

import os
from dotenv import load_dotenv


class Settings:
    """
    Settings
    --------
    Centralized configuration class for application settings.
    Loads values from environment variables with sensible defaults.
    """
    # Load environment variables from .env file (if present)
    load_dotenv()

    # Application settings
    APP_NAME: str = os.getenv('APP_NAME', 'Sedaro Nano')
    DEBUG: bool = os.getenv('DEBUG', 'true').lower() == 'true'

    # Backend configuration
    BACKEND_DATABASE_URL: str = os.getenv('BACKEND_DATABASE_URL', 'sqlite:///database.db')
    QUERY_BIN_PATH = os.getenv(
        'QUERY_BIN_PATH',
        os.path.abspath(os.path.join(os.path.dirname(__file__), '../../queries/target/release/sedaro-nano-queries'))
    )

    # Frontend configuration
    FRONTEND_URL: str = os.getenv('FRONTEND_URL', 'http://localhost:3030')

