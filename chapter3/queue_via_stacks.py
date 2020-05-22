"""Solution to 3.4 Queue via Stacks.

Implement a `MyQueue` class which implements a queue using two stacks.
"""

from typing import Any

import chapter3.stack


class EmptyQueueError(Exception):
    """Raised when attempting to access an item from an empty queue."""


class MyQueue:
    """Queue implemented using two stacks."""

    def __init__(self) -> None:
        self._new_items = chapter3.stack.Stack()
        self._old_items = chapter3.stack.Stack()

    def __len__(self) -> int:
        return len(self._new_items) + len(self._old_items)

    def _shift_stacks(self) -> None:
        # Pops everything off self._new_items onto self._old_items.
        while self._new_items:
            self._old_items.push(self._new_items.pop())

    def add(self, item: Any) -> None:
        """Adds item to end of the queue."""
        self._new_items.push(item)

    def remove(self) -> Any:
        """Removes and returns the first item in the queue.

        Raises:
            EmptyQueueError: The queue was empty.
        """
        if not self._old_items:
            self._shift_stacks()
        try:
            return self._old_items.pop()
        except IndexError as e:
            raise EmptyQueueError() from e

    def peek(self) -> Any:
        """Returns (but does not remove) the first item in the queue.

        Raises:
            EmptyQueueError: The queue was empty.
        """
        if not self._old_items:
            self._shift_stacks()
        try:
            return self._old_items.peek()
        except IndexError as e:
            raise EmptyQueueError() from e
