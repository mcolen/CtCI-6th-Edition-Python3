"""Tests for 2.6 Palindrome."""

import unittest

from chapter2.node import Node
from chapter2.palindrome import is_palindrome


class TestPalindrome(unittest.TestCase):

    def test_1_2_3_4_5_4_3_2_1(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        head.next.next.next.next.next = Node(4)
        head.next.next.next.next.next.next = Node(3)
        head.next.next.next.next.next.next.next = Node(2)
        head.next.next.next.next.next.next.next.next = Node(1)
        self.assertTrue(is_palindrome(head))

    def test_1_2_3_4_5_6_7_8_9(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        head.next.next.next.next.next = Node(6)
        head.next.next.next.next.next.next = Node(7)
        head.next.next.next.next.next.next.next = Node(8)
        head.next.next.next.next.next.next.next.next = Node(9)
        self.assertFalse(is_palindrome(head))


if __name__ == '__main__':
    unittest.main()
