"""
simulation_processor.py
-----------------------
Defines the SimulationProcessor, which orchestrates simulation execution.
Reintegrates Sedaro's Rust query parser and faithfully reproduces the
original Simulator's semantics with a clean processor interface.
"""

from functools import reduce
from operator import __or__
from typing import Any, Dict, List, Mapping, Tuple
from app.utilities.structures.qrange_store import QRangeStore
from app.config.simulation_config import agents, default_data
from app.utilities.queries.query_parser import parse_query


class SimulationProcessor:
    """
    Simulation runtime for Sedaro Nano agent-based models.

    Attributes
    ----------
    agents : dict
        Agent configuration specifying consumed/produced variables and functions.
    default_data : dict
        Default initial state for all agents.
    """

    def __init__(self) -> None:
        """
        Initialize the processor with agent configuration and defaults.
        """
        self.agents: Mapping[str, Any] = agents
        self.default_data: Dict[str, Any] = default_data
        self.store: QRangeStore[Dict[str, Any]]
        self.init: Dict[str, Any]
        self.times: Dict[str, float]
        self.sim_graph: Dict[str, Any]

    def run(
        self, params: Dict[str, Any], iterations: int = 500
    ) -> List[Tuple[float, float, Dict[str, Any]]]:
        """
        Run the simulation with given parameters.

        Parameters
        ----------
        params : dict
            Dictionary containing initial conditions for each body.
        iterations : int, optional
            Number of iterations to run the simulation (default = 500).

        Returns
        -------
        list of tuple
            Simulation history as (low, high, state_dict) records.
        """
        # Initialize store and state
        self.store = QRangeStore()
        self.init = self._merge_params(params)

        # Save initial state
        self.store[-1e9, 0] = self.init

        # Track time for each agent
        self.times = {agent_id: state['time'] for agent_id, state in self.init.items()}

        # Build simulation graph (parse queries with Rust)
        self.sim_graph = {}
        for agent_id, sms in self.agents.items():
            agent = []
            for sm in sms:
                consumed = parse_query(sm['consumed'])['content']
                produced = parse_query(sm['produced'])
                func = sm['function']
                agent.append({'func': func, 'consumed': consumed, 'produced': produced})
            self.sim_graph[agent_id] = agent

        # Run simulation
        self.simulate(iterations=iterations)
        return self.store.dump()

    def read(self, t: float) -> Dict[str, Any]:
        """
        Read the universe state at time `t`.

        Parameters
        ----------
        t : float
            The time to read from the store.

        Returns
        -------
        dict
            Combined state of the universe at time `t`.
        """
        try:
            data = self.store[t]
        except IndexError:
            data = []
        return reduce(__or__, data, {})

    def step(self, agent_id: str, universe: Dict[str, Any]) -> Dict[str, Any]:
        """
        Run one agent for a single step.

        Parameters
        ----------
        agent_id : str
            Identifier of the agent to step.
        universe : dict
            Current universe state.

        Returns
        -------
        dict
            New state for the agent after one step.
        """
        state: Dict[str, Any] = {}
        sms = [(agent_id, sm) for sm in self.sim_graph[agent_id]]

        while sms:
            next_sms = []
            for agent, sm in sms:
                if self.run_sm(agent, sm, universe, state) is None:
                    next_sms.append((agent, sm))
            if len(sms) == len(next_sms):
                raise Exception(
                    f'No progress made while evaluating state managers for agent {agent_id}. '
                    f'Remaining: {[sm["func"].__name__ for (_, sm) in sms]}'
                )
            sms = next_sms
        return state

    def run_sm(self, agent_id: str, sm: Dict[str, Any], universe: Dict[str, Any], new_state: Dict[str, Any]) -> Any:
        """
        Run a single state manager.

        Parameters
        ----------
        agent_id : str
            Agent identifier.
        sm : dict
            State manager with func, consumed, produced.
        universe : dict
            Current universe state.
        new_state : dict
            State being built for this step.

        Returns
        -------
        Any
            Result of the state manager, or None if dependencies unresolved.
        """
        inputs = []
        for q in sm['consumed']:
            found = self.find(agent_id, q, universe, new_state)
            if found is None:
                return None
            inputs.append(found)
        res = sm['func'](*inputs)
        self.put(agent_id, sm['produced'], universe, new_state, res)
        return res

    def find(
        self, agent_id: str, query: Dict[str, Any], universe: Dict[str, Any], new_state: Dict[str, Any], prev: bool = False
    ) -> Any:
        """
        Resolve a query to fetch consumed data.

        Supports Base, Prev, Root, Agent, Access, Tuple.

        Parameters
        ----------
        agent_id : str
            Agent identifier.
        query : dict
            Parsed query AST.
        universe : dict
            Universe state.
        new_state : dict
            Current step's new state.
        prev : bool
            Whether to look at previous state.

        Returns
        -------
        Any
            The resolved data, or None if unavailable.
        """
        match query['kind']:
            case 'Base':
                if prev:
                    return universe[agent_id][query['content']]
                agent_state = new_state.get(agent_id)
                if agent_state is None:
                    return None
                return agent_state.get(query['content'])
            case 'Prev':
                return self.find(agent_id, query['content'], universe, new_state, prev=True)
            case 'Root':
                if prev:
                    return universe[agent_id]
                return new_state
            case 'Agent':
                return universe[query['content']]
            case 'Access':
                base = self.find(agent_id, query['content']['base'], universe, new_state, prev)
                if base is None:
                    return None
                return base.get(query['content']['field'])
            case 'Tuple':
                res = []
                for q in query['content']:
                    found = self.find(agent_id, q, universe, new_state, prev)
                    if found is None:
                        return None
                    res.append(found)
                return res
            case _:
                return None

    def put(
        self, agent_id: str, query: Dict[str, Any], universe: Dict[str, Any], new_state: Dict[str, Any], data: Any
    ) -> None:
        """
        Insert produced data into the new state.

        Supports Base, Access, Agent.

        Parameters
        ----------
        agent_id : str
            Agent identifier.
        query : dict
            Parsed query AST for the produced variable.
        universe : dict
            Current universe state.
        new_state : dict
            Current step's new state.
        data : Any
            Value to insert.
        """
        match query['kind']:
            case 'Base':
                agent_state = new_state.get(agent_id)
                if agent_state is None:
                    agent_state = {}
                    new_state[agent_id] = agent_state
                agent_state[query['content']] = data
            case 'Prev':
                raise Exception(f'Cannot produce prev query {query}')
            case 'Root':
                pass
            case 'Agent':
                res = universe[query['content']]
                if res is None:
                    res = {}
                    universe[query['content']] = res
                return res
            case 'Access':
                base_query = query['content']['base']
                base = self.find(agent_id, base_query, universe, new_state)
                if base is None:
                    base = {}
                    self.put(agent_id, base_query, universe, new_state, base)
                base[query['content']['field']] = data
            case 'Tuple':
                raise Exception(f'Tuple production not implemented')

    def simulate(self, iterations: int = 500) -> None:
        """
        Run the full simulation for the given number of iterations.

        Parameters
        ----------
        iterations : int
            Number of iterations.
        """
        for _ in range(iterations):
            for agent_id in self.init:
                t = self.times[agent_id]
                universe = self.read(t - 0.001)
                if set(universe) == set(self.init):
                    new_state = self.step(agent_id, universe)
                    self.store[t, new_state[agent_id]['time']] = new_state
                    self.times[agent_id] = new_state[agent_id]['time']

    def _merge_params(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Merge user-provided parameters with default simulation data.

        Parameters
        ----------
        params : dict
            User-specified initial conditions.

        Returns
        -------
        dict
            Full simulation state combining defaults and overrides.
        """
        merged: Dict[str, Any] = {**self.default_data}
        for body, overrides in params.items():
            if body in merged:
                merged[body].update(overrides)
            else:
                merged[body] = overrides
        return merged
