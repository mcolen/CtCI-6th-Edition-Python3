"""Solution to 3.4 Queue via Stacks.

Implement a `MyQueue` class which implements a queue using two stacks.
"""

from typing import Any

from chapter3.stack import Stack


class EmptyQueueError(Exception):
    """Raised when attempting to access an item from an empty queue."""


class MyQueue:
    """Queue implemented using two stacks."""

    def __init__(self):
        self._new_items = Stack()
        self._old_items = Stack()

    def __len__(self):
        return len(self._new_items) + len(self._old_items)

    def _shift_stacks(self):
        """Pops everything off self._new_items onto self._old_items.

        This can be done when self._old_items is empty to put the oldest
        items in the queue on top of self._old_items.
        """
        while self._new_items:
            self._old_items.push(self._new_items.pop())

    def add(self, item: Any):
        """Adds item to end of the queue."""
        self._new_items.push(item)

    def remove(self):
        """Removes and returns the first item in the queue."""
        if not self._old_items:
            self._shift_stacks()
        try:
            return self._old_items.pop()
        except IndexError:
            raise EmptyQueueError

    def peek(self):
        """Returns the first item in the queue."""
        if not self._old_items:
            self._shift_stacks()
        try:
            return self._old_items.peek()
        except IndexError:
            raise EmptyQueueError
