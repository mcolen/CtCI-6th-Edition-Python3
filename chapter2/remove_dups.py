"""Solution to 2.1 Remove Dups.

Write code to remove duplicates from an unsorted linked list.

FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""

from chapter2.node import LinkedList


def remove_dups1(head: LinkedList) -> None:
    """Remove duplicates from the linked list."""
    if not head:
        return
    seen = {head.data}
    while head.next:
        if head.next.data in seen:
            head.next = head.next.next
        else:
            head = head.next
            seen.add(head.data)


def remove_dups2(head: LinkedList) -> None:
    """Remove duplicates from the linked list.

    Do not use a temporary buffer.
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
