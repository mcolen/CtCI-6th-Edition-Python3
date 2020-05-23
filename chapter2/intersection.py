"""Solution to 2.7 Intersection.

Given two (singly) linked lists, determine if the two lists intersect.
Return the intersecting node. Note that the intersection is defined
based on reference, not value. That is, if the kth node of the first
linked list is the exact same node (by reference) as the jth node of
the second linked list, then they are intersecting.
"""

from typing import Optional, TypeVar

from chapter2 import llist

T = TypeVar('T')


def find_intersection(head1: llist.LinkedList[T],
                      head2: llist.LinkedList[T]) -> Optional[llist.Node[T]]:
    """Determines if and where two linked lists intersect.

    Args:
        head1: First linked list.
        head2: Second linked list.

    Returns:
        The first node of intersection. If there is no intersecting
        node, returns None.
    """
    if not head1 or not head2:
        return None
    length1, length2 = 1, 1
    tail1, tail2 = head1, head2
    while tail1.next:
        tail1, length1 = tail1.next, length1 + 1
    while tail2.next:
        tail2, length2 = tail2.next, length2 + 1
    if tail1 is not tail2:
        return None

    for _ in range(length1 - length2):
        assert head1
        head1 = head1.next
    for _ in range(length2 - length1):
        assert head2
        head2 = head2.next
    while head1 is not head2:
        assert head1 and head2
        head1, head2 = head1.next, head2.next
    return head1
