"""Basic stack for use in chapter 3 solutions."""

from typing import Generic, List, TypeVar


class EmptyStackError(Exception):
    """Raised when attempting to access an item from an empty stack."""


T = TypeVar('T')


class Stack(Generic[T]):
    """A minimal stack implementation."""

    def __init__(self) -> None:
        self._items: List[T] = []

    def __len__(self) -> int:
        return len(self._items)

    def push(self, item: T) -> None:
        """Adds given item to the top of the stack."""
        self._items.append(item)

    def pop(self) -> T:
        """Removes and returns the top item from the stack.

        Raises:
            EmptyStackError: The stack was empty.
        """
        try:
            return self._items.pop()
        except IndexError as e:
            raise EmptyStackError() from e

    def peek(self) -> T:
        """Returns (but does not remove) the top item of the stack.

        Raises:
            EmptyStackError: The stack was empty.
        """
        try:
            return self._items[-1]
        except IndexError as e:
            raise EmptyStackError() from e
