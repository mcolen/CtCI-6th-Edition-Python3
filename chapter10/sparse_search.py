"""Solution to 10.5 Sparse Search.

Given a sorted array of strings that is interspresed with empty strings,
write a method to find the location of a given string.

EXAMPLE
Input:
`ball, {"at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""}`
Output: 4
"""

from typing import Optional, Sequence


def index(sorted_strings: Sequence[str], target: str) -> Optional[int]:
    """Finds target in sorted_strings.

    Args:
        sorted_strings: Sequence of strings in which all the non-empty
            strings are sorted in ascending order.
        target: String to find in sorted_strings. May not be empty.

    Returns:
        An index at which target can be found in sorted_strings, or None
        if no such index exists.
    """
    lo, hi = 0, len(sorted_strings) - 1
    while lo <= hi:
        left = right = (lo + hi) // 2
        # Find middlemost non-empty string.
        while not sorted_strings[left] and not sorted_strings[right]:
            if left == lo and right == hi:
                return None
            if left > lo:
                left -= 1
            if right < hi:
                right += 1
        if sorted_strings[right]:
            if sorted_strings[right] < target:
                lo = right + 1
            elif sorted_strings[right] > target:
                hi = left if left < right else right - 1
            else:
                assert sorted_strings[right] == target
                return right
        else:
            if sorted_strings[left] < target:
                lo = right + 1
            elif sorted_strings[left] > target:
                hi = left - 1
            else:
                assert sorted_strings[left] == target
                return left
    return None
