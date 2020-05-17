"""Tests for 2.7 Intersection."""

import unittest

from chapter2.intersection import intersection
from chapter2.node import Node


class TestIntersection(unittest.TestCase):

    def test_0_1_2_3_4_5_6_7_8_and_12_14_4_5_6_7_8(self) -> None:
        head1 = Node(0)
        head1.next = Node(1)
        head1.next.next = Node(2)
        head1.next.next.next = Node(3)
        head1.next.next.next.next = Node(4)
        head1.next.next.next.next.next = Node(5)
        head1.next.next.next.next.next.next = Node(6)
        head1.next.next.next.next.next.next.next = Node(7)
        head1.next.next.next.next.next.next.next.next = Node(8)

        head2 = Node(12)
        head2.next = Node(14)
        head2.next.next = head1.next.next.next.next

        self.assertIs(head1.next.next.next.next, intersection(head1, head2))


if __name__ == '__main__':
    unittest.main()
