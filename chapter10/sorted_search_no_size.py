"""Solution to 10.4 Sorted Search, No Size.

You are given an array-like data structure `Listy` which lacks a size
method. It does, however, have an `elementAt(i)` method that returns the
element at index `i` in `O(1)` time. If `i` is byeond the bounds of the
data structure, it returns -1. (For this reason, the data structure only
supports positive integers.) Given a `Listy` which contains sorted,
positive integers, find the index at which an element `x` occurs. If `x`
occurs multiple times, you may return any index.
"""

from typing import Optional, Sequence


class Listy:  # pylint: disable=too-few-public-methods
    """Array-like data strcuture which lacks a size method."""

    def __init__(self, seq: Sequence[int]) -> None:
        self._seq = seq

    def __getitem__(self, i: int) -> int:
        return self._seq[i] if i < len(self._seq) else -1


def index(listy: Listy, target: int) -> Optional[int]:
    """Finds index of target in sorted Listy.

    Args:
        listy: A Listy of sorted, positive integers.
        target: An integer for which to search in argument listy.

    Returns:
        An index at which target can be found in listy, or None if no
        such index exists.
    """
    lo, hi = 0, _bound_size(listy) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if listy[mid] > target or listy[mid] == -1:
            hi = mid - 1
        elif listy[mid] < target:
            lo = mid + 1
        else:  # listy[mid] == target
            return mid
    return None


def _bound_size(listy: Listy) -> int:
    bound = 1
    while listy[bound] != -1:
        bound *= 2
    return bound
