"""Solution to 1.1 Is Unique.

Implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?
"""

def is_unique1(s: str) -> bool:
    """Returns True if s has all unique characters."""
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True


def is_unique2(s: str) -> bool:
    """Returns True if s has all unique characters.

    Does not use any additional data structures.
    """
    s = sorted(s)
    return not any(s[i] == s[i + 1] for i in range(len(s) - 1))
