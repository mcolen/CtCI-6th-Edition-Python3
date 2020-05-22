"""Tests for 2.5 Sum Lists."""

import unittest

from chapter2 import llist, sum_lists


class TestSumReverseLists(unittest.TestCase):

    def test_999_plus_001(self) -> None:
        head_999 = llist.Node(9)
        head_999.next = llist.Node(9)
        head_999.next.next = llist.Node(9)

        head_001 = llist.Node(1)
        head_001.next = llist.Node(0)
        head_001.next.next = llist.Node(0)

        head_1000 = llist.Node(0)
        head_1000.next = llist.Node(0)
        head_1000.next.next = llist.Node(0)
        head_1000.next.next.next = llist.Node(1)

        self.assertEqual(head_1000,
                         sum_lists.sum_reverse_lists(head_999, head_001))


class TestSumForwardLists(unittest.TestCase):

    def test_31_plus_591(self) -> None:
        head_31 = llist.Node(3)
        head_31.next = llist.Node(1)

        head_591 = llist.Node(5)
        head_591.next = llist.Node(9)
        head_591.next.next = llist.Node(1)

        head_622 = llist.Node(6)
        head_622.next = llist.Node(2)
        head_622.next.next = llist.Node(2)

        self.assertEqual(head_622,
                         sum_lists.sum_forward_lists(head_31, head_591))


if __name__ == '__main__':
    unittest.main()
