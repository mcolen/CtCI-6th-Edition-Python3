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
    idx_merged = len(A) - 1  # index of next merged item
    idx_a = len(A) - 1 - len(B)  # index of next item in A
    idx_b = len(B) - 1  # index of next item in B
    # Just need to finish B. Last items in A are already merged.
    while idx_b >= 0:
        if idx_a >= 0 and A[idx_a] > B[idx_b]:
            A[idx_merged] = A[idx_a]
            idx_a -= 1
        else:
            A[idx_merged] = B[idx_b]
            idx_b -= 1
        idx_merged -= 1
