"""Definition of a basic tree node for use in chapter 4 solutions."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class TreeNode:
    """A node in a binary tree."""
    value: Any
    left: Optional[TreeNode] = None
    right: Optional[TreeNode] = None

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, TreeNode):
            return (self.value == other.value
                    and self.left == other.left and self.right == other.right)
        return NotImplemented


Tree = Optional[TreeNode]


@dataclass
class TreeNodeWithParent(TreeNode):
    """A node in a binary tree with a link to its parent."""
    parent: Optional[TreeNodeWithParent] = None
    left: Optional[TreeNodeWithParent] = None
    right: Optional[TreeNodeWithParent] = None
