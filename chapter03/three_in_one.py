"""Solution to 3.1 Three in One.

Describe how you could use a single array to implement three stacks.
"""

from typing import Generic, List, Optional, TypeVar

import chapter03.stack


class FullStackError(Exception):
    """Raised when attempting to add an item to a full stack."""


T = TypeVar('T')


class Stacks(Generic[T]):
    """Multiple stacks implemented with one array."""

    def __init__(self, num_stacks: int, stack_capacity: int) -> None:
        """Both num_stacks and stack_capacity must be positive."""
        if num_stacks <= 0:
            raise ValueError('num_stacks must be positive')
        if stack_capacity <= 0:
            raise ValueError('stack_capacity must be positive')
        self._num_stacks, self._stack_capacity = num_stacks, stack_capacity
        self._array: List[Optional[T]] = [None] * (num_stacks * stack_capacity)
        self._lengths = [0] * num_stacks

    def _tail(self, stack_num: int) -> int:
        """Returns index of last item in stack numbered stack_num."""
        return stack_num * self._stack_capacity + self._lengths[stack_num] - 1

    def pop(self, stack_num: int) -> T:
        """Removes and returns the top item from the given stack.

        Raises:
            EmptyStackError: The given stack was empty.
        """
        if self.is_empty(stack_num):
            raise chapter03.stack.EmptyStackError()
        item = self._array[self._tail(stack_num)]
        assert item is not None
        self._array[self._tail(stack_num)] = None
        self._lengths[stack_num] -= 1
        return item

    def push(self, stack_num: int, item: T) -> None:
        """Adds given item to the top of given stack.

        Raises:
            FullStackError: There was no room in array for new item.
        """
        if self._lengths[stack_num] >= self._stack_capacity:
            raise FullStackError()
        self._array[self._tail(stack_num) + 1] = item
        self._lengths[stack_num] += 1

    def peek(self, stack_num: int) -> T:
        """Returns (but does not remove) the top of the given stack.

        Raises:
            EmptyStackError: The given stack was empty.
        """
        if self.is_empty(stack_num):
            raise chapter03.stack.EmptyStackError()
        item = self._array[self._tail(stack_num)]
        assert item is not None
        return item

    def is_empty(self, stack_num: int) -> bool:
        """Returns True if the given stack is empty."""
        return self._lengths[stack_num] == 0
