"""Solution to 10.12 Peaks and Valleys.

In an arary of integers, a "peak" is an element which is greater than or
equal to the adjacent integers and a "valley" is an element which is
less than or equal to the adjacent integers. For example, in the array
`{5, 8, 6, 2, 3, 4, 6}`, `{8, 6}` are peaks and `{5, 2}` are valleys.
Given an array of integers, sort the array into an alternating sequence
of peaks and valleys.

EXAMPLE
Input: {5, 3, 1, 2, 3}
Output: {5, 1, 3, 2, 3}
"""

from typing import MutableSequence


def sort(ints: MutableSequence[int]) -> None:
    """Sorts sequence into alternating peaks and valleys."""
    peaking = True
    for i in range(len(ints) - 1):
        if ((peaking and ints[i] < ints[i + 1]) or
                (not peaking and ints[i] > ints[i + 1])):
            ints[i], ints[i + 1] = ints[i + 1], ints[i]
        peaking = not peaking
