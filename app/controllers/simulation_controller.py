"""
simulator_controller.py
-----------------------
Defines the FastAPI routes for simulation tasks.
Handles simulation requests from the frontend and delegates processing
to the SimulatorService.
"""

from typing import Dict, Any
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.utilities.messages.error_messages import ErrorMessages
from app.services.simulation_service import SimulationService

# Create router and service instance
simulation_router = APIRouter()
simulation_service = SimulationService()


@simulation_router.get('/')
async def health_check() -> JSONResponse:
    """
    Health check endpoint.

    Returns
    -------
    JSONResponse
        A simple message to confirm the server is running.
    """
    return JSONResponse(
        content={'message': 'Sedaro Nano API is running!'},
        status_code=200
    )


@simulation_router.post('/run')
async def run_simulation(params: Dict[str, Any]) -> JSONResponse:
    """
    Run a simulation with caching.

    If identical parameters exist in the database, the cached results
    are returned. Otherwise, a new simulation is executed, persisted,
    and the results are returned.

    Parameters
    ----------
    params : dict
        Dictionary containing initial conditions for the simulation.

    Returns
    -------
    JSONResponse
        Simulation results as JSON data.
    """
    try:
        result: Dict[str, Any] = simulation_service.run(params)
        return JSONResponse(content=result, status_code=200)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail=ErrorMessages.RUN_FAILED)


@simulation_router.get('/latest')
async def get_latest_simulation() -> JSONResponse:
    """
    Retrieve the most recent simulation result.

    Returns
    -------
    JSONResponse
        JSON data of the most recent simulation, or empty dict if none exists.
    """
    try:
        result: Dict[str, Any] = simulation_service.get_latest()
        return JSONResponse(content=result, status_code=200)
    except Exception:
        raise HTTPException(status_code=500, detail=ErrorMessages.LATEST_FAILED)

