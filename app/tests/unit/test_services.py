"""
test_services.py
----------------
Unit tests for simulation services.
"""

from app.services.simulation_service import SimulationService
from app.utilities.messages.error_messages import ErrorMessages


class TestSimulationService:
    """
    TestSimulationService
    ---------------------
    Unit tests for SimulationService methods.
    """

    def test_fetch_invalid_hash_returns_error(self):
        """
        test_fetch_invalid_hash_returns_error
        -------------------------------------
        Verify that fetching a simulation with an unknown params_hash
        returns the expected error response.

        Raises
        ------
        AssertionError
            If the returned detail does not match the expected error message.
        """
        service = SimulationService()
        result = service._fetch('non_existent_hash')
        assert result == [], ErrorMessages.LATEST_FAILED
