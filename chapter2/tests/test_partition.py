"""Tests for chapter2.partition."""

import itertools
import unittest

from chapter2 import llist, partition


class TestPartition(unittest.TestCase):

    def test_partition_3_5_8_10_2_1_around_5(self) -> None:
        head = llist.Node(3)
        head.next = llist.Node(5)
        head.next.next = llist.Node(8)
        head.next.next.next = llist.Node(10)
        head.next.next.next.next = llist.Node(2)
        head.next.next.next.next.next = llist.Node(1)

        partition.partition(head, x=5)
        self.assertEqual({1, 2, 3},
                         {node.data for node in
                          itertools.islice(iter(head), 3)})
        self.assertEqual({5, 8, 10},
                         {node.data for node in
                          itertools.islice(iter(head), 3, None)})


if __name__ == '__main__':
    unittest.main()
