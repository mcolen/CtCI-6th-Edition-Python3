"""Solution to 8.4 Power Set.

Write a method to return all subsets of a set.
"""

import itertools
from typing import FrozenSet, Set, TypeVar

T = TypeVar('T')


def power_set(set_: Set[T]) -> Set[FrozenSet[T]]:
    """Returns the set of all subsets of given set_."""
    subsets = itertools.chain.from_iterable(itertools.combinations(set_, size)
                                            for size in range(len(set_) + 1))
    return {frozenset(subset) for subset in subsets}
