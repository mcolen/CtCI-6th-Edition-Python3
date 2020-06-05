"""Basic linked list data structure for use in chapter 2 solutions."""

from __future__ import annotations

from typing import Any, Generic, Iterator, Optional, TypeVar

T = TypeVar('T')


class Node(Generic[T]):
    """Node in a singly linked list.

    Attributes:
        data: Value stored in this node.
        next: The following node in the linked list.
    """

    def __init__(self, data: T, next_: Optional[Node[T]] = None) -> None:
        self.data = data
        self.next = next_

    def __iter__(self) -> Iterator[Node[T]]:
        def traversal(node: Optional[Node[T]]) -> Iterator[Node[T]]:
            while node:
                yield node
                node = node.next
        return traversal(self)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Node):
            return self.data == other.data and self.next == other.next
        return NotImplemented


LinkedList = Optional[Node[T]]
