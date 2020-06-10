"""Solution to 10.1 Sorted Merge.

You are given two sorted arrays, `A` and `B`, where `A` has a large
enough buffer at the end to hold `B`. Write a method to merge `B` into
`A` in sorted order.
"""

from typing import Any, MutableSequence, Sequence


def merge(A: MutableSequence[Any], B: Sequence[Any]) -> None:
    """Merges B into A in sorted order.

    Args:
        A: Sorted sequence in which all items must be orderable with the
            items in argument B. Must contain exactly enough buffer at
            the end to hold all the items in B.
        B: Sorted sequence in which all the items must be orderable with
            the items in argument A.
    """
    index_merged = len(A) - 1  # index of next merged item
    index_a = len(A) - 1 - len(B)  # index of next item in A
    index_b = len(B) - 1  # index of next item in B
    # Just need to finish B. Last items in A are already merged.
    while index_b >= 0:
        if index_a >= 0 and A[index_a] > B[index_b]:
            A[index_merged] = A[index_a]
            index_a -= 1
        else:
            A[index_merged] = B[index_b]
            index_b -= 1
        index_merged -= 1
