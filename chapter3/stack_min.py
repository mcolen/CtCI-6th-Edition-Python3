"""Solution to 3.2 Stack Min.

How would you design a stack which, in addition to `push` and `pop`, has
a function `min` which returns the minimum element? `push`, `pop`, and
`min` should all operate in O(1) time.
"""

from typing import Generic, NamedTuple, TypeVar

import chapter3.stack

T = TypeVar('T')


class _Node(NamedTuple, Generic[T]):
    item: T
    mini: T


class Stack(Generic[T]):
    """Stack which gives access to minimum element in constant time."""

    def __init__(self) -> None:
        self.stack = chapter3.stack.Stack[_Node]()

    def push(self, item: T) -> None:
        """Adds given item to the top of the stack."""
        mini = min(item, self.min()) if self.stack else item
        self.stack.push(_Node(item, mini))

    def pop(self) -> T:
        """Removes and returns the top item from the stack.

        Raises:
            EmptyStackError: The stack was empty.
        """
        return self.stack.pop().item

    def peek(self) -> T:
        """Returns (but does not remove) the top item of the stack.

        Raises:
            EmptyStackError: The stack was empty.
        """
        return self.stack.peek().item

    def min(self) -> T:
        """Returns minimum item in the stack.

        Raises:
            EmptyStacError: The stack was empty.
        """
        return self.stack.peek().mini
