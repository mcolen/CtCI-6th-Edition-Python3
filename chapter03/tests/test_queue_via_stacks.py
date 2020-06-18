"""Tests for chapter03.queue_via_stacks."""

import unittest

from chapter03 import queue_via_stacks

IntQueue = queue_via_stacks.MyQueue[int]


class TestMyQueue(unittest.TestCase):

    def test_alternating_three_add_two_remove(self) -> None:
        queue = IntQueue()
        queue.add(0)
        queue.add(1)
        queue.add(2)

        self.assertEqual(0, queue.remove())
        self.assertEqual(1, queue.remove())

        queue.add(3)
        queue.add(4)
        queue.add(5)

        self.assertEqual(2, queue.remove())
        self.assertEqual(3, queue.remove())
        self.assertEqual(4, queue.peek())


if __name__ == '__main__':
    unittest.main()
