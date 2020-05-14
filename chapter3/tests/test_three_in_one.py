"""Tests for chapter3.three_in_one."""

import unittest

from chapter3.three_in_one import FixedMultiStack


class TestFixedMultiStack(unittest.TestCase):

    def test_all_operations(self):
        stacks = FixedMultiStack(num_stacks=3, stack_capacity=4)
        stacks.push(0, 10)
        stacks.push(1, 20)
        stacks.push(2, 30)
        stacks.push(1, 21)
        stacks.push(0, 11)
        stacks.push(0, 12)
        self.assertEqual(12, stacks.pop(0))
        stacks.push(2, 31)
        stacks.push(0, 13)
        stacks.push(1, 22)
        stacks.push(2, 31)
        stacks.push(2, 32)
        self.assertEqual([10, 11, 13, None, 20, 21, 22, None, 30, 31, 31, 32],
                         stacks.array)


if __name__ == '__main__':
    unittest.main()
