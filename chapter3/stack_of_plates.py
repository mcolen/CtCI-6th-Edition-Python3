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

from typing import Any, List

from chapter3.stack import EmptyStackError, Stack


class SetOfStacks:
    """Stack implemented as a set of stacks."""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self._stacks: List[Stack] = []

    def _pop_empty(self):
        while self._stacks and not self._stacks[-1]:
            self._stacks.pop()

    def push(self, item: Any) -> None:
        """Adds given item to the top of the stack."""
        if not self._stacks or len(self._stacks[-1]) > self.capacity:
            self._stacks.append(Stack())
        self._stacks[-1].push(item)

    def pop(self) -> Any:
        """Removes and returns the top item from the stack."""
        try:
            item = self._stacks[-1].pop()
        except IndexError:
            raise EmptyStackError
        self._pop_empty()
        return item

    def peek(self) -> Any:
        """Returns the top item of the stack."""
        try:
            return self._stacks[-1].peek()
        except IndexError:
            raise EmptyStackError

    def is_empty(self) -> bool:
        """Returns True if the stack is empty."""
        return not self._stacks

    def pop_at(self, index: int) -> Any:
        """Removes and returns top item from stack at given index."""
        item = self._stacks[index].pop()
        self._pop_empty()
        return item
