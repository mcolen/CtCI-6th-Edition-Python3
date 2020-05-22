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
    """Returns all possible sequences that could have led to given tree.

    Args:
        root: Top node in a binary search tree (or None). The tree is
            assumed to have been created by traversing through an array
            from left to right and inserting each element. All elements
            must be distinct.

    Returns:
        List of all possible lists that could have led to given tree.
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
    """Weaves together given sequences in all possible orderings.

    Args:
        root_value: The first value of every returned sequence.
        left: Sequence to weave together with the argument right.
        right: Sequence to weave together with the argument left.

    Returns:
        List of all possible weavings of root_value, left, and right. A
            weaving must contain root_value as the first element. Then
            come all items in left and right maintaining their ordering
            within left and right. For example given root_value=0,
            left=[1, 2], and right=[-1]:

            [
                [0, 1, 2, -1],
                [0, 1, -1, 2],
                [0, -1, 1, 2],
            ]
    """
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
