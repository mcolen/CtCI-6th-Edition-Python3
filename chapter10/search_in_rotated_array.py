"""Solution to 10.3 Search in Rotated Array.

Given a sorted array of `n` integers that has been rotated an unknown
number of times, write code to find an element in the array. You may
assume that the array was originally sorted in increasing order.

EXAMPLE
Input: find `5` in `{15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}`
Output: `8` (the index of `5` in the array)
"""

from typing import Optional, Sequence


def index(nums: Sequence[int], target: int) -> Optional[int]:
    """Finds target in sequence of integers.

    Args:
        nums: Sequence of sorted (ascending) integers that may have been
            rotated by some amount.
        target: Element to find in argument nums.

    Returns:
        An index at which target can be found in nums, or None if no
        such index exists.
    """
    if not nums:
        return None
    # We cannot guarantee better than O(n) if there are duplicates.
    if nums[0] == nums[-1]:
        try:
            return nums.index(target)
        except ValueError:
            return None

    target_left_of_wraparound = target >= nums[0]
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_left_of_wraparound = nums[mid] >= nums[0]
        if mid_left_of_wraparound and not target_left_of_wraparound:
            lo = mid + 1
        elif not mid_left_of_wraparound and target_left_of_wraparound:
            hi = mid - 1
        elif nums[mid] < target:
            lo = mid + 1
        elif nums[mid] > target:
            hi = mid - 1
        else:
            assert nums[mid] == target
            return mid
    return None
