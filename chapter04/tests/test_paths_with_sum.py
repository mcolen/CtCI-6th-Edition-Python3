"""Tests for chapter04.paths_with_sum."""

import unittest

from chapter04 import paths_with_sum
from chapter04 import tree


class TestPathsWithSum(unittest.TestCase):

    def test_sum_to_zero(self) -> None:
        root = tree.Node(value=5,
                         left=tree.Node(value=3,
                                        left=tree.Node(-8),
                                        right=tree.Node(9)),
                         right=tree.Node(value=1,
                                         left=tree.Node(2),
                                         right=tree.Node(6)))
        self.assertEqual(1, paths_with_sum.paths_with_sum(root, sum_=0))

    def test_sum_to_negative(self) -> None:
        root = tree.Node(
            value=-7,
            left=tree.Node(value=-7,
                           left=None,
                           right=tree.Node(value=1,
                                           left=tree.Node(2),
                                           right=None)),
            right=tree.Node(value=7,
                            left=tree.Node(value=3),
                            right=tree.Node(
                                value=20,
                                left=tree.Node(value=0,
                                               left=tree.Node(
                                                   value=-3,
                                                   left=None,
                                                   right=tree.Node(
                                                       value=2,
                                                       left=tree.Node(value=1),
                                                       right=None))))))
        self.assertEqual(1, paths_with_sum.paths_with_sum(root, sum_=-14))

    def test_all_values_zero(self) -> None:
        root = tree.Node(value=0,
                         left=tree.Node(0),
                         right=tree.Node(value=0,
                                         left=tree.Node(value=0,
                                                        left=None,
                                                        right=tree.Node(0)),
                                         right=tree.Node(0)))
        self.assertEqual(9, paths_with_sum.paths_with_sum(root, sum_=0))


if __name__ == '__main__':
    unittest.main()
