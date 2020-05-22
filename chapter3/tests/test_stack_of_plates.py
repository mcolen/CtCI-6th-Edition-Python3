"""Tests for chapter3.stack_of_plates."""

import unittest

import chapter3.stack
from chapter3 import stack_of_plates


class TestSetOfStacks(unittest.TestCase):

    def test_34_items_5_capacity(self) -> None:
        stack = stack_of_plates.Stack(capacity=5)
        for i in range(34):
            stack.push(i)
        for i in reversed(range(34)):
            self.assertEqual(i, stack.pop())
        self.assertRaises(chapter3.stack.EmptyStackError, stack.pop)


if __name__ == '__main__':
    unittest.main()
