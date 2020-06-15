"""Tests for chapter04.check_subtree."""

import unittest

from chapter04 import check_subtree, tree


class TestIsSubtree(unittest.TestCase):

    def test_is_2_3_1_subtree_of_1_2_1_3_1_1_5(self) -> None:
        tree_2_3_1 = tree.Node(value=2, left=tree.Node(3), right=tree.Node(1))
        self.assertTrue(
            check_subtree.is_subtree(_tree_1_2_1_3_1_1_5(), tree_2_3_1))

    def test_is_1_2_3_subtree_of_1_2_1_3_1_1_5(self) -> None:
        tree_1_2_3 = tree.Node(value=1, left=tree.Node(2), right=tree.Node(3))
        self.assertFalse(
            check_subtree.is_subtree(_tree_1_2_1_3_1_1_5(), tree_1_2_3))


def _tree_1_2_1_3_1_1_5() -> tree.Node:
    return tree.Node(value=1,
                     left=tree.Node(value=2,
                                    left=tree.Node(3),
                                    right=tree.Node(1)),
                     right=tree.Node(value=1,
                                     left=tree.Node(1),
                                     right=tree.Node(5)))


if __name__ == '__main__':
    unittest.main()
