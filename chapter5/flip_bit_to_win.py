"""Solution to 5.3 Flip Bit to Win.

You have an integer and you can flip exactly one bit from a 0 to a 1.
Write code to find the length of the longest sequence of 1s you could
create.

EXAMPLE
Input:  1775 (or: 11011101111)
Output: 8
"""

from typing import Iterator


def max_length(n: int) -> int:
    """Flips a bit in n to create maximal sequence of 1s.

    Exactly one bit in n is allowed to be flipped from a 0 to a 1.

    Args:
        n: An integer.

    Returns
        The length of the longest sequence of 1s that can be created.
    """
    ret = curr_unflipped = curr_flipped = 0
    for bit in _bits(n):
        if bit:
            curr_unflipped += 1
            curr_flipped += 1
        else:
            ret = max(ret, curr_flipped)
            curr_flipped = curr_unflipped + 1
            curr_unflipped = 0
    return max(ret, curr_flipped)


def _bits(n: int) -> Iterator[int]:
    while n:
        yield n & 1
        n >>= 1
