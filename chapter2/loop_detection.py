"""Solution to 2.8 Loop Detection.

Given a linked list which might contain a loop, implemente an algorithm
that returns the node at the beginning of the loop (if one exists).

EXAMPLE
Input:  A -> B -> C -> D -> E -> C [the same C as earlier]
Output: C
"""

from typing import Optional

from chapter2.node import LinkedList, Node


def loop_detection(head: LinkedList) -> Optional[Node]:
    """Returns first node in loop of linked list."""
    slow = fast = head
    while fast and fast.next:
        assert slow
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            break
    else:
        return None
    while head is not slow:
        assert head and slow
        head, slow = head.next, slow.next
    return head
