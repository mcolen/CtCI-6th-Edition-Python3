"""Solution to 2.8 Loop Detection.

Given a linked list which might contain a loop, implement an algorithm
that returns the node at the beginning of the loop (if one exists).

EXAMPLE
Input:  A -> B -> C -> D -> E -> C [the same C as earlier]
Output: C
"""

from typing import Optional

from chapter2 import llist


def find_loop_start(head: llist.LinkedList) -> Optional[llist.Node]:
    """Detects loop in a linked list.

    Args:
        head: First node of a linked list (or None).

    Returns:
        First node in the loop of given linked list. Or None if there is
        no loop in given linked list.
    """
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
