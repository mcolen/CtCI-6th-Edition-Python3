"""Implementation of a basic node class for use in chapter 2 solutions."""

from __future__ import annotations


class Node:
    """Node in a singly linked list."""

    def __init__(self, data=None, next_=None) -> None:
        self.data = data
        self.next = next_

    def __repr__(self) -> str:
        return repr(self.data) + '->' + repr(self.next)

    def __eq__(self, other) -> bool:
        if isinstance(other, Node):
            return self.data == other.data and self.next == other.next
        return NotImplemented
