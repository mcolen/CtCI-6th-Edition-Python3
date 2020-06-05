"""Solution to 2.6 Palindrome.

Implement a function to check if a linked list is a palindrome.
"""

from typing import Any

from chapter2 import llist


def is_palindrome(linked_list: llist.LinkedList[Any]) -> bool:
    """Return True if given linked list is a palindrome."""
    if not linked_list:
        return True
    data = [node.data for node in linked_list]
    return all(data1 == data2 for data1, data2 in zip(data, reversed(data)))
