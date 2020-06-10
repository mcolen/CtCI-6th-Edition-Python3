"""Tests for chapter04.successor."""

import unittest

from chapter04 import successor


class TestSuccessorInMinimalBST7(unittest.TestCase):
    """Tests `successor` using a minimal BST with 7 nodes."""

    def test_0(self) -> None:
        root = _minimal_bst7()
        assert root and root.left and root.left.left
        self.assertIs(root.left, successor.successor(root.left.left))

    def test_1(self) -> None:
        root = _minimal_bst7()
        assert root and root.left and root.left.right
        self.assertIs(root.left.right, successor.successor(root.left))

    def test_2(self) -> None:
        root = _minimal_bst7()
        assert root and root.left and root.left.right
        self.assertIs(root, successor.successor(root.left.right))

    def test_3(self) -> None:
        root = _minimal_bst7()
        assert root and root.right and root.right.left
        self.assertIs(root.right.left, successor.successor(root))

    def test_4(self) -> None:
        root = _minimal_bst7()
        assert root and root.right and root.right.left
        self.assertIs(root.right, successor.successor(root.right.left))

    def test_5(self) -> None:
        root = _minimal_bst7()
        assert root and root.right and root.right.right
        self.assertIs(root.right.right, successor.successor(root.right))

    def test_6(self) -> None:
        root = _minimal_bst7()
        assert root and root.right and root.right.right
        self.assertIsNone(successor.successor(root.right.right))


def _minimal_bst7() -> successor.NodeWithParent:
    root = successor.NodeWithParent(parent=None)
    root.left = successor.NodeWithParent(parent=root)
    root.left.left = successor.NodeWithParent(parent=root.left)
    root.left.right = successor.NodeWithParent(parent=root.left)
    root.right = successor.NodeWithParent(parent=root)
    root.right.left = successor.NodeWithParent(parent=root.right)
    root.right.right = successor.NodeWithParent(parent=root.right)
    return root


if __name__ == '__main__':
    unittest.main()
