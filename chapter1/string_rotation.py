"""Solve 1.9 String Rotation.

Assume you have a method `isSubstring` which checks if one word is a
substring of another. Given two strings, `s1` and `s2`, write code to
check if `s2` is a rotation of `s1` using only one call to `isSubstring`
(e.g. "waterbottle" is a rotation of "erbottlewat").
"""


def _is_substring(s1: str, s2: str) -> bool:
    """Return True if s2 is a substring of s1."""
    return s2 in s1


def is_rotation(s1: str, s2: str) -> bool:
    """Return True if s2 is a rotation of s1."""
    return len(s1) == len(s2) and _is_substring(s1 + s1, s2)
