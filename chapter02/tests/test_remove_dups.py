"""Tests for chapter02.remove_dups."""

import unittest

from chapter02 import llist, remove_dups


class TestRemoveDups1(unittest.TestCase):

    def test_01010101(self) -> None:
        head = _linked_list_01010101()
        remove_dups.remove_dups1(head)
        self.assertEqual(_linked_list_01(), head)


class TestRemoveDups2(unittest.TestCase):

    def test_01010101(self) -> None:
        head = _linked_list_01010101()
        remove_dups.remove_dups2(head)
        self.assertEqual(_linked_list_01(), head)


def _linked_list_01010101() -> llist.Node:
    head = llist.Node(0)
    head.next = llist.Node(1)
    head.next.next = llist.Node(0)
    head.next.next.next = llist.Node(1)
    head.next.next.next.next = llist.Node(0)
    head.next.next.next.next.next = llist.Node(1)
    head.next.next.next.next.next.next = llist.Node(0)
    head.next.next.next.next.next.next.next = llist.Node(1)
    return head


def _linked_list_01() -> llist.Node:
    head = llist.Node(0)
    head.next = llist.Node(1)
    return head


if __name__ == '__main__':
    unittest.main()
