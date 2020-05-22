"""Solution to 4.2 Minimal Tree.

Given a sorted (increasing order) array with unique integer elments,
write an algorithm to create a binary search tree with minimal height.
"""

from typing import Optional, Sequence

from chapter4 import tree


def minimal_bst(
        array: Sequence[int],
        parent: Optional[tree.NodeWithParent] = None) -> tree.NodeWithParent:
    """Return bst with minimal height from given sorted array.

    Raise ValueError if array is empty.
    """
    if not array:
        raise ValueError('array is empty')
    mid = len(array) // 2
    node = tree.NodeWithParent(value=array[mid], parent=parent)
    if len(array) > 1:
        node.left = minimal_bst(array[:mid], parent=node)
    if len(array) > 2:
        node.right = minimal_bst(array[mid + 1:], parent=node)
    return node
