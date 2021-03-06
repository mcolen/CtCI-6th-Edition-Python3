"""Solution to 2.1 Remove Dups.

Write code to remove duplicates from an unsorted linked list.

FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""

from typing import Any

from chapter02 import llist


def remove_dups1(head: llist.LinkedList[Any]) -> None:
    """Removes duplicates from the linked list.

    Uniqueness is determined by the __hash__ of the node data.
    """
    if not head:
        return
    seen = {head.data}
    while head.next:
        if head.next.data in seen:
            head.next = head.next.next
        else:
            head = head.next
            seen.add(head.data)


def remove_dups2(head: llist.LinkedList[Any]) -> None:
    """Removes duplicates from the linked list.

    Uniqueness is determined by the __eq__ of the node data.

    Does not use a temporary buffer.
    """
    if not head:
        return
    while head:
        runner = head
        while runner.next:
            if runner.next.data == head.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        head = head.next
