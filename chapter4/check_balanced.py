"""Solution to 4.4 Check Balanced.

Implement a function to check if a binary tree is balanced. For the
purposes of this question, a balanced tree is defined to be a tree such
that the heights of the two subtrees of any node never differ by more
than one.
"""

from typing import Tuple

from chapter4.tree_node import Tree


def is_balanced(root: Tree) -> bool:
    """Returns True if given tree is balanced.

    A balanced tree is defined to be a tree such that the heights of the
    two subtrees of any node never differ by more than one.
    """
    def helper(root: Tree) -> Tuple[bool, int]:
        # Returns whether balanced and tree height.
        if not root:
            return True, 0
        l_balanced, l_height = helper(root.left)
        r_balanced, r_height = helper(root.right)
        balanced = l_balanced and r_balanced and abs(l_height - r_height) <= 1
        height = max(l_height, r_height) + 1
        return balanced, height
    return helper(root)[0]
