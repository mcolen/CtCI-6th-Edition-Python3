"""Solution to 3.4 Queue via Stacks.

Implement a `MyQueue` class which implements a queue using two stacks.
"""

from typing import Any, List


class EmptyQueueError(Exception):
    """Raised when attempting to access an item from an empty queue."""


class MyQueue:
    """Queue implemented using two stacks."""

    def __init__(self):
        self.push_stack: List[Any] = []
        self.pop_stack: List[Any] = []

    def _shift_stacks(self):
        """Pops everything off self.push_stack onto self.pop_stack.

        This can be done when self.pop_stack is empty to put the oldest
        items in the queue on top of self.pop_stack.
        """
        while self.push_stack:
            self.pop_stack.append(self.push_stack.pop())

    def add(self, item: Any):
        """Adds item to end of the queue."""
        self.push_stack.append(item)

    def remove(self):
        """Removes and returns the first item in the queue."""
        if not self.pop_stack:
            self._shift_stacks()
        try:
            return self.pop_stack.pop()
        except IndexError:
            raise EmptyQueueError

    def peek(self):
        """Returns the first item in the queue."""
        if not self.pop_stack:
            self._shift_stacks()
        try:
            return self.pop_stack[-1]
        except IndexError:
            raise EmptyQueueError

    def is_empty(self):
        """Returns True if the queue is empty."""
        return len(self.push_stack) == len(self.pop_stack) == 0
