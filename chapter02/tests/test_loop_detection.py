"""Tests for chapter02.loop_detection."""

import unittest

from chapter02 import llist, loop_detection


class TestFindLoopStart(unittest.TestCase):

    def test_a_b_c_d_e_c(self) -> None:
        head = llist.Node('a')
        head.next = llist.Node('b')
        head.next.next = llist.Node('c')
        head.next.next.next = llist.Node('d')
        head.next.next.next.next = llist.Node('e')
        head.next.next.next.next.next = head.next.next

        res = loop_detection.find_loop_start(head)

        self.assertIs(head.next.next, res)


if __name__ == '__main__':
    unittest.main()
