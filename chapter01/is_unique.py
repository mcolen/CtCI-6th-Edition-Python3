"""Solution to 1.1 Is Unique.

Implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?
"""

from typing import MutableSet


def is_unique1(s: str) -> bool:
    """Returns True if s has all unique characters."""
    seen: MutableSet[str] = set()
    # Make sure not to loop over all of s, because there are a finite
    # number of possible unique characters which puts a cap on the
    # run-time of this function, regardless of how massively long s
    # might be.
    for c in s:
        if c in seen:
            return False
        seen.add(c)
    return True


def is_unique2(s: str) -> bool:
    """Returns True if s has all unique characters.

    Does not use any additional data structures.
    """
    sorted_s = sorted(s)
    return not any(sorted_s[i] == sorted_s[i + 1] for i in range(len(s) - 1))
