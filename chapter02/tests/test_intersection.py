"""Tests for chapter02.intersection."""

import unittest

from chapter02 import intersection, llist


class TestFindIntersection(unittest.TestCase):

    def test_0_1_2_3_4_5_6_7_8_and_12_14_4_5_6_7_8(self) -> None:
        head1 = llist.Node(0)
        head1.next = llist.Node(1)
        head1.next.next = llist.Node(2)
        head1.next.next.next = llist.Node(3)
        head1.next.next.next.next = llist.Node(4)
        head1.next.next.next.next.next = llist.Node(5)
        head1.next.next.next.next.next.next = llist.Node(6)
        head1.next.next.next.next.next.next.next = llist.Node(7)
        head1.next.next.next.next.next.next.next.next = llist.Node(8)

        head2 = llist.Node(12)
        head2.next = llist.Node(14)
        head2.next.next = head1.next.next.next.next

        self.assertIs(head1.next.next.next.next,
                      intersection.find_intersection(head1, head2))


if __name__ == '__main__':
    unittest.main()
