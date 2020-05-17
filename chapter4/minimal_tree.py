"""Solution to 4.2 Minimal Tree.

Given a sorted (increasing order) array with unique integer elments,
write an algorithm to create a binary search tree with minimal height.
"""

from typing import Optional, Sequence

from chapter4.tree_node import TreeNode


def minimal_bst(array: Sequence[int]) -> Optional[TreeNode]:
    """Returns bst with minimal height from given sorted array."""
    if not array:
        return None
    mid = len(array) // 2
    left_bst = minimal_bst(array[:mid])
    right_bst = minimal_bst(array[mid + 1:])
    return TreeNode(value=array[mid], left=left_bst, right=right_bst)
