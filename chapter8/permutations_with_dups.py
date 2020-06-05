"""Solution to 8.8 Permutations with Dups.

Write a method to compute all permutations of a string whose characters
are not necessarily unique. The list of permutations should not have
duplicates.
"""

import collections
from typing import Counter, Set


def permutations(s: str) -> Set[str]:
    """Computes all permutations of a string.

    Args:
        s: A string which may or may not have all unique characters.

    Returns:
        Set of all permutations of argument s.
    """
    return _permutations_internal(collections.Counter(s))


def _permutations_internal(char_counts: Counter[str]) -> Set[str]:
    if not char_counts:
        return {''}
    ans: Set[str] = set()
    for c in char_counts:
        ans.update(c + perm for perm in
                   _permutations_internal(char_counts - Counter(c)))
    return ans
