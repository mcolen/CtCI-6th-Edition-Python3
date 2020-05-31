"""Tests for chapter3.three_in_one."""

import unittest

import chapter3.stack
from chapter3 import three_in_one

IntStacks = three_in_one.Stacks[int]


class TestFixedMultiStack(unittest.TestCase):

    def test_all_operations(self) -> None:
        stacks = IntStacks(num_stacks=3, stack_capacity=4)
        stacks.push(0, 10)
        stacks.push(1, 20)
        stacks.push(2, 30)
        stacks.push(1, 21)
        stacks.push(0, 11)
        stacks.push(0, 12)
        self.assertEqual(12, stacks.pop(stack_num=0))
        stacks.push(2, 31)
        stacks.push(0, 13)
        stacks.push(1, 22)
        stacks.push(2, 31)
        stacks.push(2, 32)

        self.assertEqual(13, stacks.pop(stack_num=0))
        self.assertEqual(11, stacks.pop(stack_num=0))
        self.assertEqual(10, stacks.pop(stack_num=0))
        with self.assertRaises(chapter3.stack.EmptyStackError):
            stacks.pop(stack_num=0)

        self.assertEqual(22, stacks.pop(stack_num=1))
        self.assertEqual(21, stacks.pop(stack_num=1))
        self.assertEqual(20, stacks.pop(stack_num=1))
        with self.assertRaises(chapter3.stack.EmptyStackError):
            stacks.pop(stack_num=1)

        self.assertEqual(32, stacks.pop(stack_num=2))
        self.assertEqual(31, stacks.pop(stack_num=2))
        self.assertEqual(31, stacks.pop(stack_num=2))
        self.assertEqual(30, stacks.pop(stack_num=2))
        with self.assertRaises(chapter3.stack.EmptyStackError):
            stacks.pop(stack_num=2)


if __name__ == '__main__':
    unittest.main()
