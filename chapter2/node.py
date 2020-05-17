"""Implementation of a basic node for use in chapter 2 solutions."""

from __future__ import annotations

from typing import Any, Optional


class Node:
    """Node in a singly linked list."""

    def __init__(self, data: Any, next_: Optional[Node] = None) -> None:
        self.data = data
        self.next = next_

    def __repr__(self) -> str:
        return repr(self.data) + '->' + repr(self.next)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Node):
            return self.data == other.data and self.next == other.next
        return NotImplemented


LinkedList = Optional[Node]
