"""Solution for 2.2 Return Kth to Last.

Implement an algorithm to find the kth to last element of a singly
linked list.
"""

from typing import Optional

from chapter2 import llist


def kth_to_last(head: llist.LinkedList, k: int) -> Optional[llist.Node]:
    """Return kth to last node of the linked list.

    Return the last node if k is 1. k may not be 0.
    """
    runner = head
    for _ in range(k):
        if not runner:
            raise ValueError('Fewer than k nodes in list')
        runner = runner.next
    while runner:
        assert head
        head, runner = head.next, runner.next
    return head
