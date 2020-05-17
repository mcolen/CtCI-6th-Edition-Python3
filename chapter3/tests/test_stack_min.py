"""Tests for chapter3.stack_min."""

import unittest

from chapter3.stack import EmptyStackError
from chapter3.stack_min import StackWithMin


class TestStackWithMin(unittest.TestCase):

    def test_2_1_3_1(self) -> None:
        stack = StackWithMin()
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
        self.assertRaises(EmptyStackError, stack.min)


if __name__ == '__main__':
    unittest.main()
