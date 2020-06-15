"""Solution to 5.7 Pairwise Swap.

Write a program to swap odd and even bits in an integer with as few
instructions as possible (e.g. bit 0 and bit 1 are swapped, bit 2 and bit
3 are swapped, and so on).
"""


def swap_bits(n: int) -> int:
    """Swaps odd and even bits in n and returns the result.

    Bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on.
    """
    even_mask = 1
    while even_mask < n:
        even_mask <<= 2
        even_mask |= 1
    odd_mask = even_mask << 1
    return ((n & even_mask) << 1) | ((n & odd_mask) >> 1)
