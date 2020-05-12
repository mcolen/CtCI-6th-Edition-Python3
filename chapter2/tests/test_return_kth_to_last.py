"""Tests for chapter2.return_kth_to_last."""

import unittest

from chapter2.node import Node
from chapter2.return_kth_to_last import kth_to_last


class TestReturnKthToLast(unittest.TestCase):
    def test_0th_to_last(self):
        head = Node(0)
        head.next = Node(1)
        head.next.next = Node(2)
        head.next.next.next = Node(3)
        self.assertIsNone(kth_to_last(head, k=0))

    def test_last(self):
        head = Node(0)
        head.next = Node(1)
        head.next.next = Node(2)
        head.next.next.next = Node(3)
        self.assertEqual(head.next.next.next, kth_to_last(head, k=1))

    def test_2nd_to_last(self):
        head = Node(0)
        head.next = Node(1)
        head.next.next = Node(2)
        head.next.next.next = Node(3)
        self.assertEqual(head.next.next, kth_to_last(head, k=2))

    def test_3rd_to_last(self):
        head = Node(0)
        head.next = Node(1)
        head.next.next = Node(2)
        head.next.next.next = Node(3)
        self.assertEqual(head.next, kth_to_last(head, k=3))

    def test_4th_to_last(self):
        head = Node(0)
        head.next = Node(1)
        head.next.next = Node(2)
        head.next.next.next = Node(3)
        self.assertEqual(head, kth_to_last(head, k=4))


if __name__ == '__main__':
    unittest.main()
