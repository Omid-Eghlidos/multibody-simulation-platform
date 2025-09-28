"""
warning_messages.py
-------------------
Centralized warning message definitions for the Sedaro Nano backend.
"""

class WarningMessages:
    # Simulation warnings
    DEPRECATED_METHOD = 'WARNING: This simulation method is deprecated and may be removed in future versions.'
    PERFORMANCE = 'WARNING: Simulation may take longer than expected due to large input size.'

    # Database warnings
    DB_SLOW_QUERY = 'WARNING: Database query took longer than expected.'
    DB_FALLBACK = 'WARNING: Falling back to default database configuration.'
