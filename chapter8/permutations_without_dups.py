"""Solution to 8.7 Permutations without Dups.

Write a method to compute all permutations of a string of unique
characters.
"""

from typing import Set


def permutations(s: str) -> Set[str]:
    """Computes all permutations of a string of unique characters.

    Args:
        s: A string of unique characters.

    Returns:
        Set of all permutations of argument s.
    """
    res = {''}
    for c in s:
        next_res = set()
        for perm in res:
            for i in range(len(perm) + 1):
                next_res.add(perm[:i] + c + perm[i:])
        res = next_res
    return res
