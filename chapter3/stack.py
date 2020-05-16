"""Implementation of a basic stack for use in chapter 3 solutions."""

from typing import Any, List


class EmptyStackError(Exception):
    """Raised when attempting to access an item from an empty stack."""


class Stack:
    """A minimal stack implementation."""

    def __init__(self):
        self._items: List[Any] = []

    def __len__(self):
        return len(self._items)

    def push(self, item: Any) -> None:
        """Adds given item to the top of the stack."""
        self._items.append(item)

    def pop(self) -> Any:
        """Removes and returns the top item from the stack."""
        try:
            return self._items.pop()
        except IndexError:
            raise EmptyStackError

    def peek(self) -> Any:
        """Returns the top item of the stack."""
        try:
            return self._items[-1]
        except IndexError:
            raise EmptyStackError

    def is_empty(self) -> bool:
        """Returns True if the stack is empty."""
        return not self
