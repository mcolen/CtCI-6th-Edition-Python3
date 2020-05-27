"""Solution to 1.4 Palindrome Permutation.

Given a string, write a function to check if it is a permutation of a
palindrome. A palindrome is a word or phrase that is the same forwards
and backwards. A permutation is a rearrangement of letters. The
palindrome does not need to be limited to just dictionary words. You
can ignore casing and non-letter characters.

EXAMPLE
Input:  Tact Coa
Output: True (permutations: "taco cat", "atco cta", etc.)
"""

import collections


def is_palindrome_permutation(s: str) -> bool:
    """Returns True if s is a permutaton of a palindrome.

    Case insensitive. Ignores non-letter characters.
    """
    counts = collections.Counter(c.lower() for c in s if c.isalpha())
    return sum(count % 2 for count in counts.values()) <= 1
