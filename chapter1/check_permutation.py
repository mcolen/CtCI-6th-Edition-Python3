"""Solution to 1.2 Check Permutation.

Given two strings, write a method to decide if one is a permutation of
the other.
"""

import collections


def are_permutations(s1: str, s2: str) -> bool:
    """Returns True if s1 is a permutation of s2."""
    return collections.Counter(s1) == collections.Counter(s2)
