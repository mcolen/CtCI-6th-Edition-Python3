"""Solution to 8.3 Magic Index.

A magic index in an Array `A[0...n-1]` is defined to be an index such
that `A[i] = i`. Given a sorted array of distinct integers, write a
method to find a magic index, if one exists, in array `A`.

FOLLOW UP
What if the values are not distinct?
"""

from typing import Optional, Sequence


def magic_index_distinct(A: Sequence[int]) -> Optional[int]:
    """Looks for a magic index in given sequence.

    Args:
        A: Sequence of sorted, distinct integers.

    Returns:
        A magic index in argument A, or None if there is no magic index.
    """
    lo, hi = 0, len(A) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if A[mid] < mid:
            lo = mid + 1
        else:
            hi = mid
    return lo if A[lo] == lo else None


def magic_index(A: Sequence[int]) -> Optional[int]:
    """Looks for a magic index in given sequence.

    Args:
        A: Sequence of sorted integers.

    Returns:
        A magic index in argument A, or None if there is no magic index.
    """
    return next((i for i, a in enumerate(A) if i == a), None)
