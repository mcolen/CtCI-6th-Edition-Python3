"""Tests for chapter04.validate_bst."""

import unittest

from chapter04 import tree, validate_bst


class TestIsBST(unittest.TestCase):

    def test_bst_min_3_5_6_10_13_15_max(self) -> None:
        root = tree.Node(value=6,
                         left=tree.Node(value=3,
                                        left=tree.Node(float('-inf')),
                                        right=tree.Node(5)),
                         right=tree.Node(value=13,
                                         left=tree.Node(10),
                                         right=tree.Node(value=15,
                                                         left=None,
                                                         right=tree.Node(
                                                             float('inf')))))

        self.assertTrue(validate_bst.is_bst(root))

    def test_non_bst_min_6_5_6_10_13_15_max(self) -> None:
        root = tree.Node(value=6,
                         left=tree.Node(value=6,
                                        left=tree.Node(float('-inf')),
                                        right=tree.Node(5)),
                         right=tree.Node(value=13,
                                         left=tree.Node(10),
                                         right=tree.Node(value=15,
                                                         left=None,
                                                         right=tree.Node(
                                                             float('inf')))))

        self.assertFalse(validate_bst.is_bst(root))


if __name__ == '__main__':
    unittest.main()
