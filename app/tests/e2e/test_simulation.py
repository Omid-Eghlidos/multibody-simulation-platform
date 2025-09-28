"""
test_simulation.py
------------------
End-to-end smoke test for the simulation pipeline.
"""

from app.tests.abstract.base_test import BaseTestCase
from app.processors.simulation_processor import SimulationProcessor
from app.config import simulation_config


class TestSimulation(BaseTestCase):
    """
    TestSimulation
    --------------
    End-to-end tests for the SimulationProcessor.
    Ensures that a simulation can be executed and results are produced.
    """

    def test_simulation_runs(self):
        """
        test_simulation_runs
        --------------------
        Run a basic simulation and assert that results are produced.

        Raises
        ------
        AssertionError
            If the simulation results are empty after running.
        """
        processor = SimulationProcessor()
        results = processor.run(simulation_config.default_data, iterations=10)
        assert len(results) > 0, 'Simulation should produce results'
