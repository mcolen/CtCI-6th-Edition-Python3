"""Solution to 4.5 Successor.

Write an algorithm to find the "next" node (i.e., in-order successor) of
a given node in a binary search tree. You may assume that each node has
a link to its parent.
"""

from typing import Optional

from chapter4.tree import TreeNode


def successor(node: TreeNode) -> Optional[TreeNode]:
    """Return the in-order successor of given node in a BST."""
    def leftmost_child(node: TreeNode) -> TreeNode:
        # Return leftmost child of given node.
        while node.left:
            node = node.left
        return node
    if node.right:
        return leftmost_child(node.right)

    parent = node.parent
    while parent is not None and node is not parent.left:
        node, parent = parent, parent.parent
    return parent
