"""Solution to 8.5 Recursive Multiply.

Write a recursive function to multiply two positive integers without
using the `*` operator. You can use addition, subtraction, and bit
shifting, but you should minimize the number of those operations.
"""


def recursive_multiply(m: int, n: int) -> int:
    """Returns product of m and n."""
    if m < n:
        m, n = n, m
    if n == 0:
        return 0
    return (m if n & 1 else 0) + (recursive_multiply(m, n >> 1) << 1)
