"""Solution to 16.6 Smallest Difference.

Given two arrays of integers, compute the pair of values (one value in
each array) with the smallest (non-negative) difference. Return the
difference.

EXAMPLE
Input: {1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
Output: 3. That is, the pair (11, 8).
"""

import bisect
from typing import Sequence


def smallest_difference(nums1: Sequence[int], nums2: Sequence[int]) -> int:
    """Computes the pair of values with the smallest difference.

    The difference must be non-negative and the pair must include one
    value in each sequence argument.

    Args:
        nums1: A non-empty sequence of integers.
        nums2: A non-empty sequence of integers.

    Returns:
        The smallest difference.
    """
    if not nums1 or not nums2:
        raise ValueError('sequences must not be empty')
    if len(nums1) > len(nums2):
        return smallest_difference(nums1=nums2, nums2=nums1)
    res, sorted1 = float('inf'), sorted(nums1)  # Sort the smaller list.
    for num2 in nums2:
        idx = bisect.bisect(sorted1, num2)
        if idx < len(sorted1):
            res = min(res, abs(num2 - sorted1[idx]))
        if idx > 0:
            res = min(res, abs(num2 - sorted1[idx - 1]))
        if res == 0:
            return 0
    assert isinstance(res, int)
    return res
