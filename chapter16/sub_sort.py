"""Solution to 16.16 Sub Sort.

Given an array of integers, write a method to find indices `m` and `n`
such that if you sorted elements `m` through `n`, the entire array would
be sorted. Minimize `n - m` (that is, find the smallest such sequence).

EXAMPLE
Input: 1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19
Output: (3, 9)
"""

from typing import Optional, Sequence, Tuple


def indices(nums: Sequence[int]) -> Optional[Tuple[int, int]]:
    """Finds smallest sub sort that would make nums sorted.

    Args:
        nums: A sequence of integers.

    Returns:
        The closest indices (m, n) such that all of nums would be sorted
        if the elments in range [m, n] were sorted. Returns None if nums
        is already sorted.
    """
    # It is the job of _start() to return None if nums is fully sorted.
    m = _start(nums)
    return None if m is None else (m, _end(nums))


def _start(nums: Sequence[int]) -> Optional[int]:
    res, running_min = None, float('inf')
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] > running_min:
            res = i
        else:
            running_min = nums[i]
    return res


def _end(nums: Sequence[int]) -> int:
    # Assumes nums is not empty or fully sorted.
    res, running_max = 0, nums[0]
    for i, num in enumerate(nums):
        if num < running_max:
            res = i
        else:
            running_max = num
    return res
