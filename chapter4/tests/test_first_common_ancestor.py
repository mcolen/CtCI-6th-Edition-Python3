"""Tests for chapter4.first_common_ancestor."""

import unittest

from chapter4 import first_common_ancestor, minimal_tree


class TestFirstCommonAncestor(unittest.TestCase):

    def test_no_common_ancestor(self) -> None:
        bst1 = minimal_tree.minimal_bst(range(7))
        bst2 = minimal_tree.minimal_bst(range(7))
        assert bst1.left and bst2.right
        self.assertIsNone(
            first_common_ancestor.first_common_ancestor(bst1.left, bst2.right))

    def test_same_depth(self) -> None:
        bst = minimal_tree.minimal_bst(range(7))
        assert bst.left and bst.left.left and bst.left.right
        self.assertIs(
            bst.left,
            first_common_ancestor.first_common_ancestor(
                bst.left.left, bst.left.right))

    def test_different_depth(self) -> None:
        bst = minimal_tree.minimal_bst(range(7))
        assert bst.left and bst.right and bst.right.right
        self.assertIs(
            bst,
            first_common_ancestor.first_common_ancestor(
                bst.left, bst.right.right))


if __name__ == '__main__':
    unittest.main()
