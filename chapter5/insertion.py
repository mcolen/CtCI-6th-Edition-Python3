"""Solution to 5.1 Insertion.

You are given two 32-bit numbers, `N` and `M`, and two bit positions,
`i` and `j`. Write a method to insert `M` into `N` such that `M` starts
at bit `j` and ends at bit `i`. You can assume that the bits `j` through
`i` have enough space to fit all of `M`. That is, if `M` = 10011, you
can assume that there are at least 5 bits between `j` and `i`. You would
not, for example have `j` = 3 and `i` = 2, because `M` could not fully
fit between bit 3 and bit 2.

EXAMPLE
Input:  `N` = 10000000000, `M` = 10011, `i` = 2, `j` = 6
Output: `N` = 10001001100
"""


def insert_bits(N: int, M: int, i: int, j: int) -> int:
    """Inserts M into N such that M starts at bit j and ends at bit i.

    Args:
        N: 32-bit number.
        M: 32-bit number.
        i: Bit position at which to end insertion of M. There must be
            enough space between i and j to fit all of M.
        j: Bit position at which to start insertio of M. There must be
            enough space between i and j to fit all of M.

    Returns:
        Integer formed by inserting M into N, starting at bit j and
        ending at bit i.
    """
    # First, clear bits j through i with a mask e.g. 111000111.
    left = ~0 << (j + 1)
    right = (1 << i) - 1
    mask = left | right
    N &= mask
    # Now insert M into N.
    return N | (M << i)
