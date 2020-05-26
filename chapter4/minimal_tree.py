"""Solution to 4.2 Minimal Tree.

Given a sorted (increasing order) array with unique integer elments,
write an algorithm to create a binary search tree with minimal height.
"""

from typing import Optional, Sequence

from chapter4 import tree

IntNodeWithParent = tree.NodeWithParent[int]


def minimal_bst(
        array: Sequence[int],
        parent: Optional[IntNodeWithParent] = None) -> IntNodeWithParent:
    """Creates a binary search tree with minimal height.

    Args:
        array: A sorted (inreasing order) sequence with unique integer
            elements. Cannot be empty.
        parent: The parent of the root of the created tree.

    Returns:
        A binary search tree with minimal height containing the elements
            in the array argument. The parent of the root is set to the
            parent argument.
    """
    if not array:
        raise ValueError('array is empty')
    mid = len(array) // 2
    node = IntNodeWithParent(value=array[mid], parent=parent)
    if len(array) > 1:
        node.left = minimal_bst(array[:mid], parent=node)
    if len(array) > 2:
        node.right = minimal_bst(array[mid + 1:], parent=node)
    return node
