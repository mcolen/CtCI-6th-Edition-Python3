"""Solution to 16.5 Factorial Zeros.

Write an algorithm which computes the number of trailing zeros in `n`
factorial.
"""


def zeros(n: int) -> int:
    """Returns the number of trailing zeros in n!."""
    if n < 0:
        raise ValueError('factorial is not defined for negative values')
    res, factor = 0, 5
    while factor <= n:
        res, factor = res + n // factor, factor * 5
    return res
