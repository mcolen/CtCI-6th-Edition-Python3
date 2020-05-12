"""Solution to 1.3 URLify.

Write a method to replace all spaces in a string with `%20`. You may
assume that the string has sufficient space at the end to hold the
additional characters, and that you are given the "true" length of the
string. (Note: If implementing in Java, please use a character array so
that you can perform this operation in place.)

EXAMPLE
Input:  "Mr John Smith    ", 13
Output: "Mr%20John%20Smith"
"""

from itertools import islice
from typing import MutableSequence


def urlify(s: MutableSequence[str], length: int) -> None:
    """Replaces all spaces in s of given length with `%20`.

    s is assumed to have sufficient space at the end to hold the
    additional characters. length is the "true" length of s.
    """
    num_spaces = sum(1 for c in islice(s, length) if c == ' ')
    j = length - 1 + 2*num_spaces
    for i in range(length - 1, -1, -1):
        if s[i] == ' ':
            s[j-2:j+1] = '%20'
            j -= 3
        else:
            s[j] = s[i]
            j -= 1
