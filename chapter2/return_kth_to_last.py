"""Solution for 2.2 Return Kth to Last.

Implement an algorithm to find the kth to last element of a singly
linked list.
"""

from chapter2.node import Node


def kth_to_last(head: Node, k: int) -> Node:
    """Returns kth to last node of linked list with given head.

    We will return the last node if k is 1. k may not be 0."""
    runner = head
    for _ in range(k):
        runner = runner.next
    while runner:
        head, runner = head.next, runner.next
    return head
