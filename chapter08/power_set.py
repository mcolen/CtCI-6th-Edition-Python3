"""Solution to 8.4 Power Set.

Write a method to return all subsets of a set.
"""

from typing import AbstractSet, FrozenSet, Set, TypeVar

T = TypeVar('T')


def power_set(set_: AbstractSet[T]) -> Set[FrozenSet[T]]:
    """Returns the set of all subsets of given set_."""
    list_ = list(set_)  # Get a stable iteration order.
    subsets = set()
    for i in range(1 << len(set_)):
        subset = set()
        for j, item in enumerate(list_):
            if (1 << j) & i:
                subset.add(item)
        subsets.add(frozenset(subset))
    return subsets
