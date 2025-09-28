"""
qrange_store.py
---------------
Defines QRangeStore, a custom key-value data structure that maps 
left-inclusive, right-exclusive numeric ranges [low, high) to values.

Used in simulation to store and query agent states efficiently by time ranges.
"""

from __future__ import annotations
from typing import Generic, List, Tuple, TypeVar

T = TypeVar('T')


class QRangeStore(Generic[T]):
    """
    QRangeStore
    -----------
    A key-value store mapping numeric ranges [low, high) to values.

    Querying the store returns all values whose ranges contain the given key.

    Examples
    --------
    ```
    0  1  2  3  4  5  6  7  8  9
    [A      )[B)            [E)
    [C   )[D   )
           ^       ^        ^  ^
    ```
    >>> store = QRangeStore[str]()
    >>> store[0, 3] = 'Record A'
    >>> store[3, 4] = 'Record B'
    >>> store[0, 2] = 'Record C'
    >>> store[2, 4] = 'Record D'
    >>> store[8, 9] = 'Record E'
    >>> store[2, 0] = 'Record F'
    Traceback (most recent call last):
    IndexError: Invalid Range.
    >>> store[2.1]
    ['Record A', 'Record D']
    >>> store[8]
    ['Record E']
    >>> store[5]
    Traceback (most recent call last):
    IndexError: Not found.
    >>> store[9]
    Traceback (most recent call last):
    IndexError: Not found.
    """

    def __init__(self) -> None:
        """Initialize an empty QRangeStore."""
        self._store: List[Tuple[float, float, T]] = []

    def __setitem__(self, rng: Tuple[float, float], value: T) -> None:
        """
        Insert a value for a given range.

        Parameters
        ----------
        rng : tuple of (float, float)
            The range [low, high) for which the value is valid.
        value : T
            The value to associate with the range.

        Raises
        ------
        IndexError
            If the provided range is invalid.
        """
        try:
            low, high = rng
        except (TypeError, ValueError):
            raise IndexError('Invalid Range: must provide a (low, high) tuple.')
        if not low < high:
            raise IndexError('Invalid Range: low must be < high.')
        self._store.append((low, high, value))

    def __getitem__(self, key: float) -> List[T]:
        """
        Retrieve all values valid at the given key.

        Parameters
        ----------
        key : float
            The point in time or index to query.

        Returns
        -------
        list of T
            List of values whose ranges contain the key.

        Raises
        ------
        IndexError
            If no values are found at the key.
        """
        ret: List[T] = [v for (l, h, v) in self._store if l <= key < h]
        if not ret:
            raise IndexError('Not found.')
        return ret

    def __len__(self) -> int:
        """
        Return the number of stored ranges.

        Returns
        -------
        int
            The count of ranges stored in QRangeStore.
        """
        return len(self._store)

    def dump(self) -> List[Tuple[float, float, T]]:
        """
        Return a shallow copy of all stored ranges and values.

        Returns
        -------
        list of tuple
            A list of (low, high, value) tuples representing stored ranges.
        """
        return self._store.copy()
