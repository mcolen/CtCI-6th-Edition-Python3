"""Solution to 2.4 Parition

Write code to partition a linked list around a value `x`, such that all
nodes less than `x` come before all nodes greater than or equal to `x`.
(IMPORTANT: The partition elment `x` can appear anywhere in the "right
partition"; it does not need to appear between the left and right
partitions. The additional spacing the example below indicates the
partition.)

EXAMPLE
Input:  3->5->8->5->10->2->1 [partition = 5]
Output: 3->1->2    ->    10->5->5->8
"""

from typing import Any

from chapter2 import llist


def partition(head: llist.LinkedList, x: Any) -> None:
    """Partitions linked list around value x.

    All nodes less than x come before all nodes greater than or equal to
    x.

    Args:
        head: Head of linked list to partition.
        x: Value around which to partition. Must be comparable with all data
            in given linked list.
    """
    swap = head
    while head:
        if head.data < x:
            assert swap
            swap.data, head.data = head.data, swap.data
            swap = swap.next
        head = head.next
