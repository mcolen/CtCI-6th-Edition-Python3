"""Solution to 2.3 Delete Middle Node.

Implement an algorithm to delete a node in the middle (i.e. any node
but the first and last node, not necessarily the exact middle) of a
singly linked list, given only access to that node.

EXAMPLE
Input: The node `c` from the linked list a->b->c->d->e->f
Result: Nothing is returned, but the new list looks like a->b->d->e->f
"""

from chapter2.node import Node


def delete_middle_node(node: Node) -> None:
    """Delete given middle node from its linked list."""
    if not node.next:
        raise ValueError('node not in middle of list')
    node.data, node.next = node.next.data, node.next.next
