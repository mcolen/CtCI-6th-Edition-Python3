"""Solution to 16.17 Contiguous Sequence.

You are given an array of integers (both positive and negative). Find
the contiguous sequence with the largest sum. Return the sum.

EXAMPLE
Input: 2, -8, 3, -2, 4, -10
Output: 5 (i.e. {3, -2, 4})
"""

from typing import Sequence


def max_sum(nums: Sequence[int]) -> int:
    """Finds the contiguous sequence with the largest sum.

    A sequence is allowed to be empty.

    Args:
        nums: A sequence of integers (can be positive or negative).

    Returns:
        The sum of the contiguous sequence with the largest sum.
    """
    running_sum = res = 0
    for num in nums:
        running_sum = max(running_sum + num, 0)
        res = max(res, running_sum)
    return res
