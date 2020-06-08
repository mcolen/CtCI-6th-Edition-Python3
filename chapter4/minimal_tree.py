"""Solution to 4.2 Minimal Tree.

Given a sorted (increasing order) array with unique integer elments,
write an algorithm to create a binary search tree with minimal height.
"""

from typing import Sequence

from chapter4 import tree


def minimal_bst(array: Sequence[int]) -> tree.Node[int]:
    """Creates a binary search tree with minimal height.

    Args:
        array: A sorted (inreasing order) sequence with unique integer
            elements. Cannot be empty.

    Returns:
        A binary search tree with minimal height containing the elements
            in the array argument.
    """
    if not array:
        raise ValueError('array is empty')
    mid = len(array) // 2
    node = tree.Node[int](array[mid])
    if len(array) > 1:
        node.left = minimal_bst(array[:mid])
    if len(array) > 2:
        node.right = minimal_bst(array[mid + 1:])
    return node
