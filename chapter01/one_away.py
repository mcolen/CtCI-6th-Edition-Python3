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


def are_one_away(s1: str, s2: str) -> bool:
    """Returns True if s1 and s2 are one edit (or zero edits) away."""
    if abs(len(s1) - len(s2)) > 1:
        return False
    if len(s1) == len(s2):
        return sum(c1 != c2 for c1, c2 in zip(s1, s2)) <= 1

    # Make s1 the longer string.
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    # Calculate index of first difference.
    idx = next((i for i, (c1, c2) in enumerate(zip(s1, s2)) if c1 != c2),
               len(s2))
    # Compare rest of strings.
    return all(s1[i + 1] == s2[i] for i in range(idx, len(s2)))
