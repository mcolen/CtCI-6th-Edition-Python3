"""Solution to 16.21 Sum Swap.

Given two arrays of integers, find a pair of values (one value from each
array) that you can swap to give the two arrays the same sum.

EXAMPLE
Input: {4, 1, 2, 1, 1, 2} and {3, 6, 3, 3}
Output: {1, 3}
"""

from typing import Optional, Sequence, Tuple


def pair(nums1: Sequence[int],
         nums2: Sequence[int]) -> Optional[Tuple[int, int]]:
    """Finds pair of values to swap to give sum(nums1) == sum(nums2).

    Args:
        nums1: Sequence of integers.
        nums2: Sequence of integers.

    Returns:
        (num1, num2) where num1 is an element of nums1 and num2 is an
        element of nums2 and sum(nums1) - sum(nums2) == 2 * (num1 -
        num2). Returns None if no such pair of integers exists.
    """
    if len(nums1) > len(nums2):
        reversed_pair = pair(nums1=nums2, nums2=nums1)
        return (reversed_pair[1], reversed_pair[0]) if reversed_pair else None
    sum_diff = sum(nums1) - sum(nums2)
    if sum_diff % 2 == 1:
        return None
    set_nums1 = set(nums1)
    for num2 in nums2:
        num1 = sum_diff // 2 + num2
        if num1 in set_nums1:
            return (num1, num2)
    return None
