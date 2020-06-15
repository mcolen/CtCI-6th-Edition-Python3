"""Solution to 2.2 Return Kth to Last.

Implement an algorithm to find the kth to last element of a singly
linked list.
"""

from typing import Optional, TypeVar

from chapter02 import llist

T = TypeVar('T')


def kth_to_last(head: llist.LinkedList[T], k: int) -> Optional[llist.Node[T]]:
    """Returns kth to last node of the linked list.

    Returns the last node if k is 1. k may not be 0.
    """
    runner = head
    for _ in range(k):
        if not runner:
            raise ValueError('fewer than k nodes in list')
        runner = runner.next
    while runner:
        assert head
        head, runner = head.next, runner.next
    return head
