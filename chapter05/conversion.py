"""Solution to 5.6 Conversion.

Write a function to determine the number of bits you would need to flip
to convert integer `A` to integer `B`.

EXAMPLE
Input:  29 (or: 11101), 15 (or: 01111)
Output: 2
"""

from typing import Iterator


def num_bits_different(A: int, B: int) -> int:
    """Returns number of bits that are different between A and B."""
    return sum(_bits(A ^ B))


def _bits(n: int) -> Iterator[int]:
    while n:
        yield n & 1
        n >>= 1
