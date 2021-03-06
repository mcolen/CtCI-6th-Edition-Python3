"""Solution to 4.5 Successor.

Write an algorithm to find the "next" node (i.e., in-order successor) of
a given node in a binary search tree. You may assume that each node has
a link to its parent.
"""

from __future__ import annotations

import dataclasses
from typing import Optional


@dataclasses.dataclass
class NodeWithParent:
    """A node in a binary tree with a link to its parent."""
    parent: Optional[NodeWithParent]
    left: Optional[NodeWithParent] = None
    right: Optional[NodeWithParent] = None


def successor(node: NodeWithParent) -> Optional[NodeWithParent]:
    """Returns the in-order successor of given node in a BST."""
    if node.right:
        return _leftmost_child(node.right)
    parent = node.parent
    while parent is not None and node is not parent.left:
        node, parent = parent, parent.parent
    return parent


def _leftmost_child(node: NodeWithParent) -> NodeWithParent:
    while node.left:
        node = node.left
    return node
