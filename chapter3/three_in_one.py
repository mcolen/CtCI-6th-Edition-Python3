"""Solution to 3.1 Three in One.

Describe how you could use a single array to implement three stacks.
"""

from typing import Any

import chapter3.stack


class FullStackError(Exception):
    """Raised when attempting to add an item to a full stack."""


class Stack:
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

    def _tail(self, stack_num: int) -> int:
        # Return index of last item in stack numbered stack_num..
        return stack_num * self.stack_capacity + self.lengths[stack_num] - 1

    def pop(self, stack_num: int) -> Any:
        """Remove and return the top item from the given stack."""
        if self.is_empty(stack_num):
            raise chapter3.stack.EmptyStackError()
        item = self.array[self._tail(stack_num)]
        self.array[self._tail(stack_num)] = None
        self.lengths[stack_num] -= 1
        return item

    def push(self, stack_num: int, item: Any) -> None:
        """Adds given item to the top of given stack."""
        if self.lengths[stack_num] >= self.stack_capacity:
            raise FullStackError()
        self.array[self._tail(stack_num) + 1] = item
        self.lengths[stack_num] += 1

    def peek(self, stack_num: int) -> Any:
        """Return the top of the given stack."""
        if self.is_empty(stack_num):
            raise chapter3.stack.EmptyStackError()
        return self.array[self._tail(stack_num)]

    def is_empty(self, stack_num: int) -> bool:
        """Return True if the given stack is empty."""
        return self.lengths[stack_num] == 0
