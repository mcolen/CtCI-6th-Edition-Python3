"""Tests for chapter4.successor."""

import unittest

from chapter4 import minimal_tree, successor


class TestSuccessorInMinimalBST7(unittest.TestCase):
    """Test `successor` using a minimal BST with 7 nodes .

    Use 7 nodes because there is only one minimal BST with 7 nodes.
    """

    def test_0(self) -> None:
        root = minimal_tree.minimal_bst(range(7))
        assert root and root.left and root.left.left
        assert root.left.left.value == 0 and root.left.value == 1
        self.assertIs(root.left, successor.successor(root.left.left))

    def test_1(self) -> None:
        root = minimal_tree.minimal_bst(range(7))
        assert root and root.left and root.left.right
        assert root.left.value == 1 and root.left.right.value == 2
        self.assertIs(root.left.right, successor.successor(root.left))

    def test_2(self) -> None:
        root = minimal_tree.minimal_bst(range(7))
        assert root and root.left and root.left.right
        assert root.left.right.value == 2 and root.value == 3
        self.assertIs(root, successor.successor(root.left.right))

    def test_3(self) -> None:
        root = minimal_tree.minimal_bst(range(7))
        assert root and root.right and root.right.left
        assert root.value == 3 and root.right.left.value == 4
        self.assertIs(root.right.left, successor.successor(root))

    def test_4(self) -> None:
        root = minimal_tree.minimal_bst(range(7))
        assert root and root.right and root.right.left
        assert root.right.left.value == 4 and root.right.value == 5
        self.assertIs(root.right, successor.successor(root.right.left))

    def test_5(self) -> None:
        root = minimal_tree.minimal_bst(range(7))
        assert root and root.right and root.right.right
        assert root.right.value == 5 and root.right.right.value == 6
        self.assertIs(root.right.right, successor.successor(root.right))

    def test_6(self) -> None:
        root = minimal_tree.minimal_bst(range(7))
        assert root and root.right and root.right.right
        assert root.right.right.value == 6
        self.assertIsNone(successor.successor(root.right.right))


if __name__ == '__main__':
    unittest.main()
