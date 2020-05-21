"""Solution to 4.9 BST Sequences.

A binary search tree was created by traversing through an array from
left to right and inserting each element. Given a binary search tree
with distinct elements, print all possible arrays that could have led to
this tree.

EXAMPLE:
Input: 1 <-- 2 --> 3
Output: {2, 1, 3}, {2, 3, 1}
"""

from itertools import permutations
from typing import Any, List, Sequence

from chapter4.tree import Tree


def bst_sequences(root: Tree) -> List[List[Any]]:
    """Return all possible sequences that could have led to given Tree.

    The Tree is assumed to be created by iterating through a sequence
    and inserting each element.
    """
    if not root:
        return [[]]

    def permute(left: Sequence[Any], right: Sequence[Any]) -> List[List[Any]]:
        # Return all possible weavings of left and right.
        assert root
        sequences: List[List[Any]] = []
        for permutation in permutations([1] * len(left) + [0] * len(right)):
            sequence = [root.value]
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

    sequences: List[List[Any]] = []
    for left in bst_sequences(root.left):
        for right in bst_sequences(root.right):
            sequences.extend(permute(left, right))
    return sequences
