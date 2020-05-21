"""Solution to 3.2 Stack Min.

How would you design a stack which, in addition to `push` and `pop`, has
a function `min` which returns the minimum element? `push`, `pop`, and
`min` should all operate in O(1) time.
"""

from collections import namedtuple
from typing import Any

from chapter3.stack import Stack


class StackWithMin(Stack):
    """Stack which gives access to minimum element in constant time."""

    Node = namedtuple('Node', ['item', 'min'])

    def push(self, item: Any) -> None:
        """Extend method to push min as well as item."""
        min_ = min(item, self._items[-1].min) if self else item
        super().push(self.Node(item, min_))

    def pop(self) -> Any:
        """Extend method to unpack popped tuple."""
        return super().pop().item

    def peek(self) -> Any:
        """Extend method to unpack popped tuple."""
        return super().peek().item

    def min(self) -> Any:
        """Return minimum item in the stack."""
        return super().peek().min
