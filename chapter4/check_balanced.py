"""Solution to 4.4 Check Balanced.

Implement a function to check if a binary tree is balanced. For the
purposes of this question, a balanced tree is defined to be a tree such
that the heights of the two subtrees of any node never differ by more
than one.
"""

from typing import Tuple

from chapter4 import tree


def is_balanced(root: tree.Tree) -> bool:
    """Return True if given tree is balanced.

    A balanced tree is defined to be a tree such that the heights of the
    two subtrees of any node never differ by more than one.
    """
    return _helper(root)[0]


def _helper(root: tree.Tree) -> Tuple[bool, int]:
    # Return whether balanced and tree height.
    if not root:
        return True, 0
    l_balanced, l_height = _helper(root.left)
    r_balanced, r_height = _helper(root.right)
    balanced = l_balanced and r_balanced and abs(l_height - r_height) <= 1
    height = max(l_height, r_height) + 1
    return balanced, height
