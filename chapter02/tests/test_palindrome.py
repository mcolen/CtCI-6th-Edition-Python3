"""Tests for chapter02.palindrome."""

import unittest

from chapter02 import palindrome, llist


class TestPalindrome(unittest.TestCase):

    def test_1_2_3_4_5_4_3_2_1(self) -> None:
        head = llist.Node(1)
        head.next = llist.Node(2)
        head.next.next = llist.Node(3)
        head.next.next.next = llist.Node(4)
        head.next.next.next.next = llist.Node(5)
        head.next.next.next.next.next = llist.Node(4)
        head.next.next.next.next.next.next = llist.Node(3)
        head.next.next.next.next.next.next.next = llist.Node(2)
        head.next.next.next.next.next.next.next.next = llist.Node(1)
        self.assertTrue(palindrome.is_palindrome(head))

    def test_1_2_3_4_5_6_7_8_9(self) -> None:
        head = llist.Node(1)
        head.next = llist.Node(2)
        head.next.next = llist.Node(3)
        head.next.next.next = llist.Node(4)
        head.next.next.next.next = llist.Node(5)
        head.next.next.next.next.next = llist.Node(6)
        head.next.next.next.next.next.next = llist.Node(7)
        head.next.next.next.next.next.next.next = llist.Node(8)
        head.next.next.next.next.next.next.next.next = llist.Node(9)
        self.assertFalse(palindrome.is_palindrome(head))


if __name__ == '__main__':
    unittest.main()
