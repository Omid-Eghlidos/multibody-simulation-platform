"""
simulation_math.py
------------------
Defines core mathematical functions for agent simulation.

These functions are pure (stateless) and can be tested independently.
They implement physics propagation such as position, velocity,
and time updates under simple Newtonian dynamics.
"""

from typing import Dict
import numpy as np


def propagate_velocity(
    time_step: float,
    position: Dict[str, float],
    velocity: Dict[str, float],
    other_position: Dict[str, float],
    m_other: float
) -> Dict[str, float]:
    """
    Propagate the velocity of a body using Newton's law of gravitation.

    Parameters
    ----------
    time_step : float
        Time increment for propagation.
    position : dict
        Current position {'x', 'y', 'z'} of this body.
    velocity : dict
        Current velocity {'x', 'y', 'z'} of this body.
    other_position : dict
        Position {'x', 'y', 'z'} of the other interacting body.
    m_other : float
        Mass of the other body.

    Returns
    -------
    dict
        Updated velocity vector {'x', 'y', 'z'}.
    """
    r_self = np.array([position['x'], position['y'], position['z']])
    v_self = np.array([velocity['x'], velocity['y'], velocity['z']])
    r_other = np.array([other_position['x'], other_position['y'], other_position['z']])

    r = r_self - r_other
    dvdt = -m_other * r / np.linalg.norm(r) ** 3
    v_self = v_self + dvdt * time_step

    return {'x': float(v_self[0]), 'y': float(v_self[1]), 'z': float(v_self[2])}


def propagate_position(time_step: float, position: Dict[str, float], velocity: Dict[str, float]) -> Dict[str, float]:
    """
    Propagate the position of a body using its velocity.

    Parameters
    ----------
    time_step : float
        Time increment for propagation.
    position : dict
        Current position {'x', 'y', 'z'}.
    velocity : dict
        Current velocity {'x', 'y', 'z'}.

    Returns
    -------
    dict
        Updated position vector {'x', 'y', 'z'}.
    """
    r_self = np.array([position['x'], position['y'], position['z']])
    v_self = np.array([velocity['x'], velocity['y'], velocity['z']])

    r_self = r_self + v_self * time_step

    return {'x': float(r_self[0]), 'y': float(r_self[1]), 'z': float(r_self[2])}


def propagate_mass(mass: float) -> float:
    """
    Propagate the mass of a body (identity function).

    Parameters
    ----------
    mass : float
        Current mass.

    Returns
    -------
    float
        Unchanged mass.
    """
    return mass


def identity(arg: float) -> float:
    """
    Identity function that returns its input unchanged.

    Parameters
    ----------
    arg : float
        Input value.

    Returns
    -------
    float
        The same input value.
    """
    return arg


def timestep_manager(velocity: Dict[str, float]) -> float:
    """
    Compute the next time step for a body.
    Currently returns a fixed value (stub).

    Parameters
    ----------
    velocity : dict
        Current velocity vector.

    Returns
    -------
    float
        Length of the next time step.
    """
    return 100.0


def time_manager(time: float, time_step: float) -> float:
    """
    Compute the next simulation time for a body.

    Parameters
    ----------
    time : float
        Current time.
    time_step : float
        Time increment.

    Returns
    -------
    float
        Updated time value.
    """
    return time + time_step
