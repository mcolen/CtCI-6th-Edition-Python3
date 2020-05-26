"""Tests for chapter3.stack_min."""

import unittest

import chapter3.stack
from chapter3 import stack_min

IntStack = stack_min.Stack[int]


class TestStackWithMin(unittest.TestCase):

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
        with self.assertRaises(chapter3.stack.EmptyStackError):
            stack.min()


if __name__ == '__main__':
    unittest.main()
