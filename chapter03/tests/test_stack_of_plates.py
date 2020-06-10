"""Tests for chapter03.stack_of_plates."""

import unittest

import chapter03.stack
from chapter03 import stack_of_plates

IntStack = stack_of_plates.Stack[int]


class TestStackOfPlates(unittest.TestCase):

    def test_7_items_3_capacity(self) -> None:
        stack = IntStack(capacity=3)
        stack.push(0)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        stack.push(6)
        self.assertEqual(6, stack.pop())
        self.assertEqual(5, stack.pop())
        self.assertEqual(4, stack.pop())
        self.assertEqual(3, stack.pop())
        self.assertEqual(2, stack.pop())
        self.assertEqual(1, stack.pop())
        self.assertEqual(0, stack.pop())
        with self.assertRaises(chapter03.stack.EmptyStackError):
            stack.pop()


if __name__ == '__main__':
    unittest.main()
