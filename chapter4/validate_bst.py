"""Solution to 4.5 Validate BST.

Implement a function to check if a binary tree is a binary search tree.
"""

from typing import Any

from chapter4 import tree


def is_bst(root: tree.Tree, mini: Any = None, maxi: Any = None) -> bool:
    """Checks if a binary tree is a binary search tree.

    Args:
        root: The root node of a binary tree (or None).
        mini: The binary search tree is not allowed to have any values
            as small as mini.
        maxi: The binary search tree is not allowed to have any values
            as big as maxi.

    Returns:
        True if the given tree is a binary search tree. Duplicate values
            are not allowed in our definition of a binary search tree.
    """
    if not root:
        return True
    if mini is not None and root.value <= mini:
        return False
    if maxi is not None and root.value >= maxi:
        return False
    if not is_bst(root.left, mini, root.value):
        return False
    if not is_bst(root.right, root.value, maxi):
        return False
    return True
