"""Solution to 2.7 Intersection.

Given two (singly) linked lists, determine if the two lists intersect.
Return the intersecting node. Note that the intersection is defined
based on reference, not value. That is, if the kth node of the first
linked list is the exact same node (by reference) as the jth node of
the second linked list, then they are intersecting.
"""

from typing import Optional

from chapter2.node import Node


def intersection(head1: Node, head2: Node) -> Optional[Node]:
    """Returns first node of intersection between given linked lists.

    If there is no intersecting node, returns None.
    """
    length1, length2 = 1, 1
    tail1, tail2 = head1, head2
    while tail1.next:
        tail1, length1 = tail1.next, length1 + 1
    while tail2.next:
        tail2, length2 = tail2.next, length2 + 1
    if tail1 is not tail2:
        return None

    for _ in range(length1 - length2):
        head1 = head1.next
    for _ in range(length2 - length1):
        head2 = head2.next
    while head1 is not head2:
        head1, head2 = head1.next, head2.next
    return head1
