"""Solution to 1.2 Check Permutation.

Given two strings, write a method to decide if one is a permutation of
the other.
"""

from collections import Counter


def are_permutations(s1: str, s2: str) -> bool:
    """Return True if s1 is a permutation of s2."""
    return Counter(s1) == Counter(s2)
