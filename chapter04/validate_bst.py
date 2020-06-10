"""Solution to 4.5 Validate BST.

Implement a function to check if a binary tree is a binary search tree.
"""

import itertools
from typing import Any

from chapter04 import tree


def is_bst(root: tree.Tree[Any]) -> bool:
    """Checks if a binary tree is a binary search tree.

    Args:
        root: The root node of a binary tree (or None). All the data in
            the tree must be orderable.

    Returns:
        True if the given tree is a binary search tree. Duplicate values
            are not allowed in our definition of a binary search tree.
    """
    if not root:
        return True
    back_iter = tree.in_order_traversal(root)
    front_iter = itertools.islice(tree.in_order_traversal(root), 1, None)
    return all(t1.value < t2.value for t1, t2 in zip(back_iter, front_iter))
