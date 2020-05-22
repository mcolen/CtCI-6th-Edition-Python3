"""Tests for chapter2.partition."""

import unittest

from chapter2.node import Node
from chapter2.partition import partition


class TestPartition(unittest.TestCase):

    def test_partition_3_5_8_10_2_1_around_5(self) -> None:
        head = Node(3)
        head.next = Node(5)
        head.next.next = Node(8)
        head.next.next.next = Node(10)
        head.next.next.next.next = Node(2)
        head.next.next.next.next.next = Node(1)

        partition(head, x=5)
        self.assertEqual({1, 2, 3},
                         {head.data, head.next.data, head.next.next.data})
        self.assertEqual({5, 8, 10}, {
            head.next.next.next.data, head.next.next.next.next.data,
            head.next.next.next.next.next.data
        })


if __name__ == '__main__':
    unittest.main()
