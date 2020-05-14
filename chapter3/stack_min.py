"""Solution to 3.2 Stack Min.

How would you design a stack which, in addition to `push` and `pop`, has
a function `min` which returns the minimum element? `push`, `pop`, and
`min` should all operate in O(1) time.
"""

import collections
from typing import Any, List


class Error(Exception):
    """Base class for exceptions in this module."""


class EmptyStackError(Exception):
    """Raised when attempting to access an item from an empty stack."""


class StackWithMin:
    """Stack which gives access to minimum element in constant time."""

    Node = collections.namedtuple('Node', ['item', 'min'])

    def __init__(self) -> None:
        self.stack: List[Any] = []

    def push(self, item: Any) -> None:
        """Adds given item to the top of the stack."""
        min_ = min(item, self.stack[-1].min) if self.stack else item
        self.stack.append(StackWithMin.Node(item, min_))

    def pop(self) -> Any:
        """Removes and returns the top item from the stack."""
        if not self.stack:
            raise EmptyStackError
        item = self.stack[-1].item
        del self.stack[-1]
        return item

    def min(self) -> Any:
        """Returns minimum item in the stack."""
        if not self.stack:
            raise EmptyStackError
        return self.stack[-1].min
