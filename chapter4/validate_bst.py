"""Solution to 4.5 Validate BST.

Implement a function to check if a binary tree is a binary search tree.
"""

from typing import Any

from chapter4.tree import Tree


def is_bst(root: Tree, mini: Any = None, maxi: Any = None) -> bool:
    """Return true if given binary tree is a binary search tree.

    Duplicates are not allowed.
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
