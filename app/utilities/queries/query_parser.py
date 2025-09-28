"""
query_parser.py
---------------
Provides a Python interface to the Sedaro Nano Rust query parser.

This module calls the compiled Rust binary to parse query expressions
into JSON-serializable abstract syntax trees (ASTs). It is used by the
SimulationProcessor to interpret agent update rules.
"""

import json
import subprocess
from typing import Any, Dict
from app.config.settings import Settings


def parse_query(query: str) -> Dict[str, Any]:
    """
    Parse a query expression using the Rust query parser binary.

    Parameters
    ----------
    query : str
        The query expression to parse, e.g., 'prev!(velocity)'.

    Returns
    -------
    dict
        Parsed query AST as a dictionary.

    Raises
    ------
    Exception
        If the Rust parser returns a non-zero exit code.
    """
    proc = subprocess.Popen(
        [Settings.QUERY_BIN_PATH],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    stdout, stderr = proc.communicate(query)
    if proc.returncode:
        raise Exception(f'Parsing query failed: {stderr}')
    return json.loads(stdout)
