"""
error_messages.py
-----------------
Centralized error message definitions for the Sedaro Nano backend.
"""

class ErrorMessages:
    # Simulation errors
    INVALID_PARAMS = 'ERROR: Invalid simulation parameters!'
    RUN_FAILED = 'ERROR: Simulation run failed!'
    FETCH_FAILED = 'ERROR: Simulation fetch failed!'
    LATEST_FAILED = 'ERROR: Could not retrieve latest simulation results!'

    # Database errors
    DB_CONNECTION = 'ERROR: Could not connect to database!'
