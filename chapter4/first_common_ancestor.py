"""Solve 4.8 First Common Ancestor.

Design an algorithm and write code to find the first common ancestor of
two nodes in a binary tree. Avoid storing additional nodes in a data
structure. NOTE: This is not necessarily a binary search tree.
"""

from typing import Optional

from chapter4.tree import TreeNode


def first_common_ancestor(node1: TreeNode,
                          node2: TreeNode) -> Optional[TreeNode]:
    """Return first common ancestor of node1 and node2."""
    depth1, depth2 = 0, 0
    float1, float2 = node1, node2
    while float1.parent:
        depth1, float1 = depth1 + 1, float1.parent
    while float2.parent:
        depth2, float2 = depth2 + 1, float2.parent
    if float1 is not float2:
        return None

    for _ in range(depth1 - depth2):
        assert node1.parent
        node1 = node1.parent
    for _ in range(depth2 - depth1):
        assert node2.parent
        node2 = node2.parent
    while node1 is not node2:
        assert node1.parent and node2.parent
        node1, node2 = node1.parent, node2.parent
    return node1
