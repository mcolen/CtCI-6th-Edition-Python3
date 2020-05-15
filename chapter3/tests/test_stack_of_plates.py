"""Tests for chapter3.stack_of_plates."""

import unittest

from chapter3.stack_of_plates import EmptyStackError, SetOfStacks


class TestSetOfStacks(unittest.TestCase):

    def test_34_items_5_capacity(self):
        stack = SetOfStacks(capacity=5)
        for i in range(34):
            stack.push(i)
        for i in reversed(range(34)):
            self.assertEqual(i, stack.pop())
        self.assertRaises(EmptyStackError, stack.pop)


if __name__ == '__main__':
    unittest.main()
