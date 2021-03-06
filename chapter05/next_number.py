"""Solution to 5.4 Next Number.

Given a positive integer, print the next smallest and the next largest
number that have the same number of 1s in their binary representation.
"""


class NoValidSmallerNumberError(Exception):
    """Raised when there does not exist a valid smaller number."""


def smaller(n: int) -> int:
    """Calculates next smaller number with the same # of 1s in binary.

    Args:
        n: A positive integer.

    Raises:
        NoValidSmallerNumberError: There was no smaller number with the
        same # of 1s in binary representation.

    Returns:
        The next smaller number with the same # of 1s in binary.
    """
    # Catch cases like 0b00111 with no valid smaller number.
    if (n + 1) & n == 0:
        raise NoValidSmallerNumberError()

    zeros = ones = 0
    while _bit(n, i=ones):
        ones += 1
    while not _bit(n, i=ones + zeros):
        zeros += 1
    return n - (1 << ones) - (1 << zeros - 1) + 1


def larger(n: int) -> int:
    """Calculates next larger number with the same # of 1s in binary.

    Args:
        n: A positive integer.

    Returns:
        The next larger number with the same # of 1s in binary.
    """
    zeros = ones = 0
    while not _bit(n, i=zeros):
        zeros += 1
    while _bit(n, i=zeros + ones):
        ones += 1
    return n + (1 << zeros) + (1 << ones - 1) - 1


def _bit(n: int, i: int) -> int:
    return n & (1 << i)
