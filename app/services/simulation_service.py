"""
simulation_service.py
--------------------
Handles simulation execution, retrieval, and caching.

Components
----------
- SimulationProcessor : Runs the core simulation logic.
- Simulation (DB model) : Persists parameters, results, and hashes.
"""

import json
import hashlib
from typing import List, Tuple, Dict, Any, Optional
from app.utilities.messages.error_messages import ErrorMessages
from app.processors.simulation_processor import SimulationProcessor
from app.models.simulation_model import Simulation
from app.clients.database import SessionLocal


class SimulationService:
    """
    Service responsible for handling simulation lifecycle:
    execution, persistence, and retrieval.

    Attributes
    ----------
    processor : SimulationProcessor
        Processor used to run simulations with given parameters.
    """

    def __init__(self) -> None:
        """
        Initialize the service with the simulator processor.
        """
        self.processor: SimulationProcessor = SimulationProcessor()

    def run(self, params: Dict[str, Any]) -> List[Tuple[float, float, Dict[str, Any]]]:
        """
        Run a simulation with caching.

        This method first validates the parameters and computes their hash.
        It then attempts to retrieve cached results using `_fetch`. If a cached
        result is found, it is returned immediately. Otherwise, a new simulation
        is executed with `SimulationProcessor`, the results are persisted, and
        then returned.

        Parameters
        ----------
        params : dict
            Dictionary containing initial conditions for the simulation.

        Returns
        -------
        list of tuple
            Simulation history as (low, high, state_dict) records.
        """
        self._validate_params(params)
        params_hash: str = self._compute_hash(params)

        results: Optional[List[Tuple[float, float, Dict[str, Any]]]] = self._fetch(params_hash)
        if results:
            return results
        else:
            # If not found, run a new simulation
            results = self.processor.run(params)
            self._save_to_db(params, params_hash, results)
        return results

    def get_latest(self) -> List[Tuple[float, float, Dict[str, Any]]]:
        """
        Retrieve the most recent simulation result.

        Returns
        -------
        list of tuple
            Simulation history as (low, high, state_dict) records.
            Returns an empty list if no simulation exists.
        """
        with SessionLocal() as session:
            sim: Optional[Simulation] = session.query(Simulation).order_by(Simulation.id.desc()).first()
            if sim:
                return json.loads(sim.results_json)
            return []

    def _fetch(self, params_hash: str) -> List[Tuple[float, float, Dict[str, Any]]]:
        """
        Retrieve cached simulation results for the given parameters hash.

        Parameters
        ----------
        params_hash : str
            SHA256 hash of the simulation parameters.

        Returns
        -------
        list of tuple
            Cached simulation history as (low, high, state_dict) records
            if found, otherwise an empty list.
        """
        with SessionLocal() as session:
            sim: Optional[Simulation] = (
                session.query(Simulation).filter(Simulation.params_hash == params_hash).first()
            )
            if sim:
                return json.loads(sim.results_json)
            return []

    def _validate_params(self, params: Dict[str, Any]) -> None:
        """
        Validate simulation parameters for correctness.

        Parameters
        ----------
        params : dict
            Simulation parameters to validate.

        Raises
        ------
        ValueError
            If parameters are invalid.
        """
        if not isinstance(params, dict) or not params:
            raise ValueError(ErrorMessages.INVALID_PARAMS)

    def _compute_hash(self, params: Dict[str, Any]) -> str:
        """
        Compute a deterministic hash of parameters for caching.

        Parameters
        ----------
        params : dict

        Returns
        -------
        str
            SHA256 hash of parameters JSON.
        """
        params_json: str = json.dumps(params, sort_keys=True)
        return hashlib.sha256(params_json.encode('utf-8')).hexdigest()

    def _save_to_db(self, params: Dict[str, Any], params_hash: str, results: List[Tuple[float, float, Dict[str, Any]]]) -> None:
        """
        Save simulation run to the database.

        Parameters
        ----------
        params : dict
        params_hash : str
        results : list of tuple
            Simulation history as (low, high, state_dict) records.
        """
        with SessionLocal() as session:
            sim = Simulation(
                params_json=json.dumps(params),
                params_hash=params_hash,
                results_json=json.dumps(results),
            )
            session.add(sim)
            session.commit()
