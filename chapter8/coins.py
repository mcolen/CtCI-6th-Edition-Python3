"""Solution to 8.11 Coins.

Given an infinite number of quarters (25 cents), dimes (10 cents),
nickles (5 cents), and pennies (1 cent), write code to calculate the
number of ways of representing `n` cents.
"""

import functools
from typing import FrozenSet


def coin_combinations(n: int) -> int:
    """Returns the number of ways of representing n cents.

    Representations of cents can include any number of quarters (25
    cents), dimes (10 cents), nickles (5 cents), and pennies (1 cent).
    """
    if n < 0:
        return 0
    return _coin_combinations_internal(n, denoms=frozenset([1, 5, 10, 25]))


@functools.lru_cache(maxsize=None)
def _coin_combinations_internal(n: int, denoms: FrozenSet[int]) -> int:
    if n == 0 or len(denoms) == 1:
        return 1
    max_denom = max(denoms)
    remaining_denoms = frozenset(denoms - {max_denom})
    return sum(_coin_combinations_internal(n - i * max_denom, remaining_denoms)
               for i in range(n // max_denom + 1))
