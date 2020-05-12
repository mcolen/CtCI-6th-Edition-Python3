"""Tests for 2.5 Sum Lists."""

import unittest

from chapter2.node import Node
from chapter2.sum_lists import sum_reverse_lists, sum_forward_lists


class TestSumReverseLists(unittest.TestCase):
    def test_999_plus_001(self):
        head_999 = Node(9)
        head_999.next = Node(9)
        head_999.next.next = Node(9)

        head_001 = Node(1)
        head_001.next = Node(0)
        head_001.next.next = Node(0)

        head_1000 = Node(0)
        head_1000.next = Node(0)
        head_1000.next.next = Node(0)
        head_1000.next.next.next = Node(1)

        self.assertEqual(head_1000, sum_reverse_lists(head_999, head_001))


class TestSumForwardLists(unittest.TestCase):
    def test_31_plus_591(self):
        head_31 = Node(3)
        head_31.next = Node(1)

        head_591 = Node(5)
        head_591.next = Node(9)
        head_591.next.next = Node(1)

        head_622 = Node(6)
        head_622.next = Node(2)
        head_622.next.next = Node(2)

        self.assertEqual(head_622, sum_forward_lists(head_31, head_591))
