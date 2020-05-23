"""Implementation of a basic node for use in chapter 2 solutions."""

from __future__ import annotations

from typing import Any, Generic, Optional, TypeVar

T = TypeVar('T')


class Node(Generic[T]):
    """Node in a singly linked list.

    Attributes:
        data: A value stored in this node (could be any type).
        next: The following node in the linked list.
    """

    def __init__(self, data: T, next_: Optional[Node[T]] = None) -> None:
        self.data = data
        self.next = next_

    def __repr__(self) -> str:
        return repr(self.data) + '->' + repr(self.next)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Node):
            return self.data == other.data and self.next == other.next
        return NotImplemented


LinkedList = Optional[Node[T]]
