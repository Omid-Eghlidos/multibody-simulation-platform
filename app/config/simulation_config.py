"""
simulation_config.py
--------------------
Defines agent configurations and default initial conditions
for Sedaro Nano simulations.
"""

from typing import Callable, Dict, List, Union, TypedDict
from app.utilities.physics.simulation_math import (
    propagate_velocity,
    propagate_position,
    propagate_mass,
    identity,
    timestep_manager,
    time_manager,
)


class AgentConfig(TypedDict):
    """
    Defines the configuration for a single agent state update step.

    Attributes
    ----------
    consumed : str
        Query expression for values consumed by this step.
    produced : str
        Name of the value produced by this step.
    function : Callable
        Function used to compute the produced value.
    """
    consumed: str
    produced: str
    function: Callable[..., Union[Dict[str, float], float]]


class BodyState(TypedDict, total=False):
    """
    Defines the structure of a body's simulation state.

    Attributes
    ----------
    timeStep : float
        Length of the timestep for this body.
    time : float
        Current simulation time for this body.
    position : dict
        Dictionary {'x', 'y', 'z'} representing position.
    velocity : dict
        Dictionary {'x', 'y', 'z'} representing velocity.
    mass : float
        Mass of the body.
    """
    timeStep: float
    time: float
    position: Dict[str, float]
    velocity: Dict[str, float]
    mass: float


# Agent configuration
agents: Dict[str, List[AgentConfig]] = {
    'Body1': [
        {'consumed': '( prev!(velocity), )', 'produced': 'velocity', 'function': identity},
        {'consumed': '( prev!(timeStep), prev!(position), velocity, )', 'produced': 'position', 'function': propagate_position},
        {'consumed': '( prev!(mass), )', 'produced': 'mass', 'function': propagate_mass},
        {'consumed': '( prev!(time), timeStep )', 'produced': 'time', 'function': time_manager},
        {'consumed': '( velocity, )', 'produced': 'timeStep', 'function': timestep_manager},
    ],
    'Body2': [
        {'consumed': '( prev!(timeStep), prev!(position), prev!(velocity), agent!(Body1).position, agent!(Body1).mass, )', 'produced': 'velocity', 'function': propagate_velocity},
        {'consumed': '( prev!(timeStep), prev!(position), velocity, )', 'produced': 'position', 'function': propagate_position},
        {'consumed': '( prev!(mass), )', 'produced': 'mass', 'function': propagate_mass},
        {'consumed': '( prev!(time), timeStep )', 'produced': 'time', 'function': time_manager},
        {'consumed': '( velocity, )', 'produced': 'timeStep', 'function': timestep_manager},
    ],
}

# Default initial conditions
default_data: Dict[str, BodyState] = {
    'Body1': {
        'timeStep': 0.01,
        'time': 0.0,
        'position': {'x': -0.73, 'y': 0.0, 'z': 0.0},
        'velocity': {'x': 0.0, 'y': -0.0015, 'z': 0.0},
        'mass': 1.0,
    },
    'Body2': {
        'timeStep': 0.01,
        'time': 0.0,
        'position': {'x': 60.34, 'y': 0.0, 'z': 0.0},
        'velocity': {'x': 0.0, 'y': 0.13, 'z': 0.0},
        'mass': 0.123,
    },
}
