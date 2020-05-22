"""Solution to 3.2 Stack Min.

How would you design a stack which, in addition to `push` and `pop`, has
a function `min` which returns the minimum element? `push`, `pop`, and
`min` should all operate in O(1) time.
"""

from typing import Any, NamedTuple

import chapter3.stack


class Stack(chapter3.stack.Stack):
    """Stack which gives access to minimum element in constant time."""

    class _Node(NamedTuple):
        item: Any
        mini: Any

    def push(self, item: Any) -> None:
        """See base class."""
        mini = min(item, self._items[-1].mini) if self else item
        super().push(self._Node(item, mini))

    def pop(self) -> Any:
        """See base class."""
        return super().pop().item

    def peek(self) -> Any:
        """See base class."""
        return super().peek().item

    def min(self) -> Any:
        """Returns minimum item in the stack."""
        return super().peek().mini
