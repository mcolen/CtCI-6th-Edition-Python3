"""Solution to 2.1 Remove Dups.

Write code to remove duplicates from an unsorted linked list.

FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""

from chapter2.node import Node


def remove_dups1(head: Node) -> None:
    """Reomves dulicates from the linked list with given head node."""
    if not head:
        return
    seen = {head.data}
    while head.next:
        if head.next.data in seen:
            head.next = head.next.next
        else:
            head = head.next
            seen.add(head.data)


def remove_dups2(head: Node) -> None:
    """Reomves dulicates from the linked list with given head node.

    Does not use a temporary buffer."""
    while head:
        runner = head
        while runner.next:
            if runner.next.data == head.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        head = head.next
