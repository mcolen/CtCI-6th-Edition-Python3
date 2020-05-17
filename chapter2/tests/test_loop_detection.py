"""Tests for 2.8 Loop Detection."""

import unittest

from chapter2.loop_detection import loop_detection
from chapter2.node import Node


class TestLoopDetection(unittest.TestCase):

    def test_a_b_c_d_e_c(self) -> None:
        head = Node('a')
        head.next = Node('b')
        head.next.next = Node('c')
        head.next.next.next = Node('d')
        head.next.next.next.next = Node('e')
        head.next.next.next.next.next = head.next.next
        self.assertIs(head.next.next, loop_detection(head))


if __name__ == '__main__':
    unittest.main()
