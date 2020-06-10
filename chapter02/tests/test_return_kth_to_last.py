"""Tests for chapter02.return_kth_to_last."""

import unittest

from chapter02 import return_kth_to_last, llist


class TestReturnKthToLast(unittest.TestCase):

    def test_last(self) -> None:
        head = llist.Node(0)
        head.next = llist.Node(1)
        head.next.next = llist.Node(2)
        head.next.next.next = llist.Node(3)
        self.assertIs(head.next.next.next,
                      return_kth_to_last.kth_to_last(head, k=1))

    def test_2nd_to_last(self) -> None:
        head = llist.Node(0)
        head.next = llist.Node(1)
        head.next.next = llist.Node(2)
        head.next.next.next = llist.Node(3)
        self.assertIs(head.next.next,
                      return_kth_to_last.kth_to_last(head, k=2))

    def test_3rd_to_last(self) -> None:
        head = llist.Node(0)
        head.next = llist.Node(1)
        head.next.next = llist.Node(2)
        head.next.next.next = llist.Node(3)
        self.assertIs(head.next, return_kth_to_last.kth_to_last(head, k=3))

    def test_4th_to_last(self) -> None:
        head = llist.Node(0)
        head.next = llist.Node(1)
        head.next.next = llist.Node(2)
        head.next.next.next = llist.Node(3)
        self.assertIs(head, return_kth_to_last.kth_to_last(head, k=4))


if __name__ == '__main__':
    unittest.main()
