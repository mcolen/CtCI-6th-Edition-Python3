"""Solution to 10.8 Find Duplicates.

You have an array with all the numbers from 1 to `N`, where `N` is at
most 32,000. The array may have duplicate entries and you do not know
what `N` is. With only 4 kilobytes of memory available, how would you
print all duplicate elements in the array?
"""

from typing import Sequence


def print_duplicates(nums: Sequence[int]) -> None:
    """Prints all duplicate elements in an array.

    Uses only 4 kilobytes of memory.

    Args:
        nums: A sequence with all the numbers from 1 to `N`, where `N`
            is at most 32,000. May or may not have duplicate entries.
    """
    min_num, max_num = 1, 32_000
    seen = _BitSet(size=max_num - min_num + 1)
    for num in nums:
        key = num - min_num
        if seen[key]:
            print(num)
        else:
            seen[key] = True


class _BitSet:
    def __init__(self, size: int) -> None:
        bits_in_byte = 8
        self.bytes = bytearray(size // bits_in_byte)

    def __getitem__(self, key: int) -> bool:
        return self.bytes[key // 8] & (1 << (key % 8)) != 0

    def __setitem__(self, key: int, value: bool) -> None:
        mask = 1 << (key % 8)
        if value:
            self.bytes[key // 8] |= mask
        else:
            self.bytes[key // 8] &= ~mask
