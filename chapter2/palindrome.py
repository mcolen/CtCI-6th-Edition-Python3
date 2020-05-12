"""Solution to 2.6 Palindrome.

Implement a function to check if a linked list is a palindrome.
"""

from chapter2.node import Node


def is_palindrome(head: Node) -> bool:
    """Returns True if linked list with given head is a palindrome."""
    data = []
    while head:
        data.append(head.data)
        head = head.next
    return all(data1 == data2 for data1, data2 in zip(data, reversed(data)))
