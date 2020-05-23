"""Solution to 3.3 Stack of Plates.

Imagine a (literal) stack of plates. If the stack gets too high, it
might topple. Therefore, in real life, we would likely start a new stack
when the previous stack exceeds some threshold. Implement a data
structure `SetOfStacks` that mimics this. `SetOfStacks` should be
composed of several stacks and should create a new stack once the
previous one exceeds capacity. `SetOfStacks.push()` and
`SetOfStacks.pop()` should behave identically to a single stack (that
is, `pop()` should return the same values as it would if there were just
a single stack).

FOLLOW UP
Implement a function `popAt(int index)` which performs a `pop` operation
on a specific sub-stack.
"""

from typing import Generic, List, TypeVar

import chapter3.stack

T = TypeVar('T')


class Stack(Generic[T]):
    """Stack implemented as a set of stacks."""

    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._stacks: List[chapter3.stack.Stack[T]] = []

    def _pop_empty(self) -> None:
        # Pops empty stacks from self._stacks.
        while self._stacks and not self._stacks[-1]:
            self._stacks.pop()

    def push(self, item: T) -> None:
        """Adds given item to the top of the stack."""
        if not self._stacks or len(self._stacks[-1]) > self._capacity:
            self._stacks.append(chapter3.stack.Stack())
        self._stacks[-1].push(item)

    def pop(self) -> T:
        """Removes and returns the top item from the stack.

        Raises:
            EmptyStackError: The stack was empty.
        """
        try:
            item = self._stacks[-1].pop()
        except IndexError as e:
            raise chapter3.stack.EmptyStackError() from e
        self._pop_empty()
        return item

    def peek(self) -> T:
        """Returns (but does not remove) the top item of the stack.

        Raises:
            EmptyStackError: The stack was empty.
        """
        try:
            return self._stacks[-1].peek()
        except IndexError as e:
            raise chapter3.stack.EmptyStackError() from e

    def pop_at(self, index: int) -> T:
        """Removes and returns the top item from stack at given index.

        Raises:
            EmptyStackError: The stack at given index was empty.
        """
        item = self._stacks[index].pop()
        self._pop_empty()
        return item
