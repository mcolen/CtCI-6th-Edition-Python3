"""Tests for chapter02.return_kth_to_last."""

import unittest

from chapter02 import return_kth_to_last, llist


class TestKthToLast(unittest.TestCase):

    def test_last(self) -> None:
        head = llist.Node(0)
        head.next = llist.Node(1)
        head.next.next = llist.Node(2)
        head.next.next.next = llist.Node(3)

        res = return_kth_to_last.kth_to_last(head, k=1)

        self.assertIs(head.next.next.next, res)

    def test_2nd_to_last(self) -> None:
        head = llist.Node(0)
        head.next = llist.Node(1)
        head.next.next = llist.Node(2)
        head.next.next.next = llist.Node(3)

        res = return_kth_to_last.kth_to_last(head, k=2)

        self.assertIs(head.next.next, res)

    def test_3rd_to_last(self) -> None:
        head = llist.Node(0)
        head.next = llist.Node(1)
        head.next.next = llist.Node(2)
        head.next.next.next = llist.Node(3)

        res = return_kth_to_last.kth_to_last(head, k=3)

        self.assertIs(head.next, res)

    def test_4th_to_last(self) -> None:
        head = llist.Node(0)
        head.next = llist.Node(1)
        head.next.next = llist.Node(2)
        head.next.next.next = llist.Node(3)

        res = return_kth_to_last.kth_to_last(head, k=4)

        self.assertIs(head, res)


if __name__ == '__main__':
    unittest.main()
