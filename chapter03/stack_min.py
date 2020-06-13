"""Solution to 3.2 Stack Min.

How would you design a stack which, in addition to `push` and `pop`, has
a function `min` which returns the minimum element? `push`, `pop`, and
`min` should all operate in O(1) time.
"""

import dataclasses
from typing import Generic, TypeVar

import chapter03.stack

T = TypeVar('T')


@dataclasses.dataclass
class _Node(Generic[T]):
    item: T
    mini: T


class Stack(Generic[T]):
    """Stack which gives access to minimum element in constant time."""

    def __init__(self) -> None:
        self._stack = chapter03.stack.Stack[_Node]()

    def push(self, item: T) -> None:
        """Adds given item to the top of the stack."""
        mini = min(item, self.min()) if self._stack else item
        self._stack.push(_Node(item, mini))

    def pop(self) -> T:
        """Removes and returns the top item from the stack.

        Raises:
            EmptyStackError: The stack was empty.
        """
        return self._stack.pop().item

    def peek(self) -> T:
        """Returns (but does not remove) the top item of the stack.

        Raises:
            EmptyStackError: The stack was empty.
        """
        return self._stack.peek().item

    def min(self) -> T:
        """Returns minimum item in the stack.

        Raises:
            EmptyStackError: The stack was empty.
        """
        return self._stack.peek().mini
