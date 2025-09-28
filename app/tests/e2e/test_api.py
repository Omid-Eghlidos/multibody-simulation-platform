"""
test_api.py
-----------
End-to-end tests for the FastAPI simulation API endpoints.
"""

from app.tests.abstract.base_test import BaseTestCase


class TestAPI(BaseTestCase):
    """
    TestAPI
    -------
    Tests the FastAPI endpoints exposed by the simulation controller.
    Validates health check, simulation run, and retrieval of latest results.
    """

    def test_health_endpoint(self):
        """
        test_health_endpoint
        --------------------
        Verify that the health check endpoint responds successfully.

        Raises
        ------
        AssertionError
            If the endpoint does not return status 200 or expected response.
        """
        response = self.client.get('/api/v1/simulation/')
        assert response.status_code == 200
        assert response.json() == {'message': 'Sedaro Nano API is running!'}

    def test_run_simulation_endpoint(self):
        """
        test_run_simulation_endpoint
        ----------------------------
        Verify that the run simulation endpoint executes and returns a response.

        Raises
        ------
        AssertionError
            If the endpoint does not return status 200 or expected keys.
        """
        # Sample input
        payload = {'param1': 1.0, 'param2': 2.0}
        response = self.client.post('/api/v1/simulation/run', json=payload)
        assert response.status_code == 200
        assert 'content' in response.json()

    def test_latest_simulation_endpoint(self):
        """
        test_latest_simulation_endpoint
        -------------------------------
        Verify that the latest simulation endpoint retrieves the most recent run.

        Raises
        ------
        AssertionError
            If the endpoint does not return status 200 or expected keys.
        """
        response = self.client.get('/api/v1/simulation/latest')
        assert response.status_code == 200
        assert 'content' in response.json()
