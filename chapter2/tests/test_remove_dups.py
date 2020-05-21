"""Tests for chapter2.remove_dups."""

import unittest

from chapter2.node import Node
from chapter2.remove_dups import remove_dups1, remove_dups2


def _make_list_01010101() -> Node:
    # Construct and return linked list 0->1->0->1->0->1->0->1.
    head = Node(0)
    head.next = Node(1)
    head.next.next = Node(0)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(0)
    head.next.next.next.next.next = Node(1)
    head.next.next.next.next.next.next = Node(0)
    head.next.next.next.next.next.next.next = Node(1)
    return head


def _make_list_01() -> Node:
    # Construct and return linked list 0>1.
    head = Node(0)
    head.next = Node(1)
    return head


class TestRemoveDups1(unittest.TestCase):

    def test_01010101(self) -> None:
        head = _make_list_01010101()
        remove_dups1(head)
        self.assertEqual(_make_list_01(), head)


class TestRemoveDups2(unittest.TestCase):

    def test_01010101(self) -> None:
        head = _make_list_01010101()
        remove_dups2(head)
        self.assertEqual(_make_list_01(), head)


if __name__ == '__main__':
    unittest.main()
