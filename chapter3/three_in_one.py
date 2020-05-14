"""Solution to 3.1 Three in One.

Describe how you could use a single array to implement three stacks.
"""

from typing import Any


class Error(Exception):
    """Base class for exceptions in this module."""


class EmptyStackError(Error):
    """Raised when attempting to peek at or pop from an empty stack."""


class FullStackError(Error):
    """Raised when attempting to write to push to a full stack."""


class FixedMultiStack:
    """Multiple stacks implemented with one array."""

    def __init__(self, num_stacks: int, stack_capacity: int) -> None:
        """Both num_stacks and stack_capacity must be positive."""
        if num_stacks <= 0:
            raise ValueError('num_stacks must be positive')
        if stack_capacity <= 0:
            raise ValueError('stack_capacity must be positive')
        self.num_stacks, self.stack_capacity = num_stacks, stack_capacity
        self.array = [None] * (num_stacks * stack_capacity)
        self.lengths = [0] * num_stacks

    def _in_bounds(self, stack_num: int) -> bool:
        return 0 <= stack_num < self.num_stacks

    def _tail(self, stack_num: int) -> int:
        return stack_num * self.stack_capacity + self.lengths[stack_num] - 1

    def pop(self, stack_num: int) -> Any:
        """Removes and returns the top item from the given stack."""
        if not self._in_bounds(stack_num):
            raise ValueError('stack_num out of bounds')
        if self.is_empty(stack_num):
            raise EmptyStackError
        item = self.array[self._tail(stack_num)]
        self.array[self._tail(stack_num)] = None
        self.lengths[stack_num] -= 1
        return item

    def push(self, stack_num: int, item: Any) -> None:
        """Adds given item to the top of given stack."""
        if not self._in_bounds(stack_num):
            raise ValueError('stack_num out of bounds')
        if self.lengths[stack_num] >= self.stack_capacity:
            raise FullStackError
        self.array[self._tail(stack_num) + 1] = item
        self.lengths[stack_num] += 1

    def peek(self, stack_num: int) -> Any:
        """Returns the top of the given stack."""
        if not self._in_bounds(stack_num):
            raise ValueError('stack_num out of bounds')
        if self.is_empty(stack_num):
            raise EmptyStackError
        return self.array[self._tail(stack_num)]

    def is_empty(self, stack_num: int) -> bool:
        """Returns True if the given stack is empty."""
        if not self._in_bounds(stack_num):
            raise ValueError('stack_num out of bounds')
        return self.lengths[stack_num] == 0
