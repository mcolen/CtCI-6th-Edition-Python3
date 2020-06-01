"""Basic tree data structure for use in chapter 4 solutions."""

from __future__ import annotations

import dataclasses
from typing import Any, Generic, TypeVar, Optional

T = TypeVar('T')


@dataclasses.dataclass
class Node(Generic[T]):
    """A node in a binary tree."""
    value: T
    left: Optional[Node] = None
    right: Optional[Node] = None

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Node):
            return (self.value == other.value and self.left == other.left
                    and self.right == other.right)
        return NotImplemented


Tree = Optional[Node[T]]


@dataclasses.dataclass
class NodeWithParent(Node[T]):
    """A node in a binary tree with a link to its parent."""
    parent: Optional[NodeWithParent] = None
    left: Optional[NodeWithParent] = None
    right: Optional[NodeWithParent] = None
