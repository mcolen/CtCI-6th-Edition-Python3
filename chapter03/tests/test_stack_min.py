"""Tests for chapter03.stack_min."""

import unittest

import chapter03.stack
from chapter03 import stack_min

IntStack = stack_min.Stack[int]


class TestStack(unittest.TestCase):

    def test_2_1_3_1(self) -> None:
        stack = IntStack()
        stack.push(2)
        stack.push(1)
        stack.push(3)
        stack.push(1)

        self.assertEqual(1, stack.pop())
        self.assertEqual(1, stack.min())
        self.assertEqual(3, stack.pop())
        self.assertEqual(1, stack.min())
        self.assertEqual(1, stack.pop())
        self.assertEqual(2, stack.min())
        self.assertEqual(2, stack.pop())
        with self.assertRaises(chapter03.stack.EmptyStackError):
            stack.min()


if __name__ == '__main__':
    unittest.main()
