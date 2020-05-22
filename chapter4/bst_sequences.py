"""Solution to 4.9 BST Sequences.

A binary search tree was created by traversing through an array from
left to right and inserting each element. Given a binary search tree
with distinct elements, print all possible arrays that could have led to
this tree.

EXAMPLE:
Input: 1 <-- 2 --> 3
Output: {2, 1, 3}, {2, 3, 1}
"""

import itertools
from typing import Any, List, Sequence

from chapter4 import tree


def bst_sequences(root: tree.Tree) -> List[List[Any]]:
    """Return all possible sequences that could have led to given Tree.

    The Tree is assumed to be created by iterating through a sequence
    and inserting each element.
    """
    if not root:
        return [[]]

    sequences: List[List[Any]] = []
    for left in bst_sequences(root.left):
        for right in bst_sequences(root.right):
            sequences.extend(_permute(root.value, left, right))
    return sequences


def _permute(root_value: Any, left: Sequence[Any],
             right: Sequence[Any]) -> List[List[Any]]:
    # Return all possible weavings of left and right after root_value.
    sequences: List[List[Any]] = []
    for permutation in itertools.permutations([1] * len(left) +
                                              [0] * len(right)):
        sequence = [root_value]
        i = j = 0
        for bit in permutation:
            if bit:
                sequence.append(left[i])
                i += 1
            else:
                sequence.append(right[j])
                j += 1
        sequences.append(sequence)
    return sequences
