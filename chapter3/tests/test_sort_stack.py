"""Tests for chapter3.short_stack"""

import unittest

import chapter3.stack
from chapter3 import sort_stack


class TestSortStack(unittest.TestCase):

    def test_2_6_1_7_4_3_10_8_9_5(self) -> None:
        stack = chapter3.stack.Stack()
        stack.push(2)
        stack.push(6)
        stack.push(1)
        stack.push(7)
        stack.push(4)
        stack.push(3)
        stack.push(10)
        stack.push(8)
        stack.push(9)
        stack.push(5)

        sort_stack.sort_stack(stack)

        self.assertEqual(1, stack.pop())
        self.assertEqual(2, stack.pop())
        self.assertEqual(3, stack.pop())
        self.assertEqual(4, stack.pop())
        self.assertEqual(5, stack.pop())
        self.assertEqual(6, stack.pop())
        self.assertEqual(7, stack.pop())
        self.assertEqual(8, stack.pop())
        self.assertEqual(9, stack.pop())
        self.assertEqual(10, stack.pop())
        self.assertRaises(chapter3.stack.EmptyStackError, stack.pop)


if __name__ == '__main__':
    unittest.main()
