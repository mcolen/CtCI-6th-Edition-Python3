"""Solution to 1.5 One Away.

There are three types of edits that can be performed on strings: insert
a character, remove a character, or replace a character. Given two
strings, write a function to check if they are one edit (or zero edits)
away.

EXAMPLE
pale,  ple  -> true
pales, pale -> true
pale,  bale -> true
pale,  bake -> false
"""

from itertools import islice


def are_one_away(s1: str, s2: str) -> bool:
    """Returns True if s1 and s2 are one edit (or zero edits) away."""
    if len(s1) == len(s2):
        return sum(char1 != char2 for char1, char2 in zip(s1, s2)) <= 1
    # Make s1 the longer string.
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    # Calculate index of first difference.
    i = next((i for i, (char1, char2) in enumerate(
        zip(s1, s2)) if char1 != char2), len(s2))
    return all(char1 == char2 for char1, char2 in zip(
        islice(s1, i + 1, None), islice(s2, i, None)))
