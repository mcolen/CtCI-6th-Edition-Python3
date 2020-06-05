"""Solution to 3.5 Sort Stack.

Write a program to sort a stack such that the smallest items are on the
top. You can use an additional temporary stack, but you may not copy the
elements into any other data structure (such as an array). The stack
supports the following operations: `push`, `pop`, `peek`, and `isEmpty`.
"""

from typing import Any

import chapter3.stack

AnyStack = chapter3.stack.Stack[Any]


def sort_stack(stack: AnyStack) -> None:
    """Sorts stack such that the smallest items are on the top.

    Data in stack must be orderable.
    """
    sorted_stack = AnyStack()
    while stack:
        curr = stack.pop()
        while sorted_stack and curr < sorted_stack.peek():
            stack.push(sorted_stack.pop())
        sorted_stack.push(curr)
    while sorted_stack:
        stack.push(sorted_stack.pop())
