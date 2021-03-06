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

import itertools
from typing import MutableSequence


def urlify(chars: MutableSequence[str], length: int) -> None:
    """Replaces all spaces in chars with '%20'.

    Args:
        chars: Mutable sequence of characters to be urlified. Must have
            sufficient space at the end to hold the additional
            characters.
        length: The "true" length of 'chars' not including additional
            space at the end.
    """
    num_spaces = sum(char == ' ' for char in itertools.islice(chars, length))
    j = length - 1 + 2 * num_spaces  # last index of urlified chars
    for i in range(length - 1, -1, -1):
        char = chars[i]
        if char == ' ':
            chars[j - 2:j + 1] = '%20'
            j -= 3
        else:
            chars[j] = char
            j -= 1
