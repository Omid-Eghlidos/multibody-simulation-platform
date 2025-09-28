"""
base_test.py
------------
Abstract base test class providing reusable FastAPI TestClient.

Purpose
-------
- Defines a shared TestClient instance for all test cases.
- Centralizes setup logic for consistent API testing.
"""

from fastapi.testclient import TestClient
from app.app import app


class BaseTestCase:
    """
    BaseTestCase
    ------------
    Sets up a reusable FastAPI TestClient for all tests inheriting from this class.
    """

    @classmethod
    def setup_class(cls):
        """
        Initialize a shared FastAPI TestClient for all tests extending this class.
        """
        cls.client = TestClient(app)
