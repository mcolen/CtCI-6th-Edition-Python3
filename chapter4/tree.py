"""Basic tree data structure for use in chapter 4 solutions."""

from __future__ import annotations

from typing import Any, Generic, Iterator, TypeVar, Optional

T = TypeVar('T')


class Node(Generic[T]):
    """A node in a binary tree."""

    def __init__(self, value: T,
                 left: Optional[Node] = None,
                 right: Optional[Node] = None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __iter__(self) -> Iterator[Node[T]]:
        return in_order_traversal(self)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Node):
            return (self.value == other.value and self.left == other.left
                    and self.right == other.right)
        return NotImplemented


Tree = Optional[Node[T]]


class NodeWithParent(Node[T]):  # pylint: disable=too-few-public-methods
    """A node in a binary tree with a link to its parent."""

    def __init__(self, value: T,
                 left: Optional[Node] = None,
                 right: Optional[Node] = None,
                 parent: Optional[Node] = None) -> None:
        super().__init__(value, left, right)
        self.parent = parent


def in_order_traversal(node: Node[T]) -> Iterator[Node[T]]:
    """Returns successive nodes of in-order traversal."""
    if node.left:
        yield from node.left
    yield node
    if node.right:
        yield from node.right
