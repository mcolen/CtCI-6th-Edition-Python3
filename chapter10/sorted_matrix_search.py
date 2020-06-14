"""Solution to 10.9 Sorted Matrix Search.

Given an `M x N` matrix in which each row and each column is sorted in
ascending order, write a method to find an element.
"""

import bisect
from typing import Any, Sequence, Tuple


def index(matrix: Sequence[Sequence[Any]], target: Any) -> Tuple[int, int]:
    """Finds an element in a sorted matrix.

    Args:
        matrix: A rectangular matrix in which each row and column is
            sorted in ascending order.
        target: Element to find in matrix.

    Returns:
        (row, column) of target.

    Raises:
        ValueError: target was not in matrix.
    """
    # First find candidate row with binary search.
    lo, hi = 0, len(matrix) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if matrix[mid][0] < target:
            lo = mid + 1
        else:
            hi = mid
    row = lo
    col = bisect.bisect_left(matrix[row], target)
    if col == len(matrix[row]) or matrix[row][col] != target:
        raise ValueError
    return (row, col)
