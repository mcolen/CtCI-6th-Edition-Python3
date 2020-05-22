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
    """Replace all spaces in chars with `%20`.

    :param chars: Mutable sequence of characters to be urlified. Assumed
        to have sufficient space at the end to hold the additional
        caracters.
    :param length: The "true" length of chars not including additional
        space at the end.
    """
    num_spaces = sum(char == ' ' for char in itertools.islice(chars, length))
    j = length - 1 + 2 * num_spaces  # last index of urlified chars
    for char in itertools.islice(reversed(chars), len(chars) - length, None):
        if char == ' ':
            chars[j - 2:j + 1] = '%20'
            j -= 3
        else:
            chars[j] = char
            j -= 1
