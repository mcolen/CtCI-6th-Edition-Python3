"""Definition of a basic tree node for use in chapter 4 solutions."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class TreeNode:
    """A node in a binary tree with links to its children and parent."""
    value: Any
    left: Optional[TreeNode] = None
    right: Optional[TreeNode] = None
    parent: Optional[TreeNode] = None


Tree = Optional[TreeNode]
