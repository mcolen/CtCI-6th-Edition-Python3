"""Solution to 16.1 Number Swapper.

Write a function to swap swap [sic] two numbers in place (that is,
without temporary variables.)
"""

import dataclasses


@dataclasses.dataclass
class Int:
    """Wrapper for an int."""
    val: int


def swap(num1: Int, num2: Int) -> None:
    """Swaps num1 and num2 in place."""
    num1.val ^= num2.val
    num2.val ^= num1.val
    num1.val ^= num2.val
