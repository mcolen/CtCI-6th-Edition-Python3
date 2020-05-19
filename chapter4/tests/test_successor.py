"""Tests for chapter4.successor."""

from typing import Optional
import unittest

from chapter4.minimal_tree import minimal_bst
from chapter4.successor import successor
from chapter4.tree_node import Tree, TreeNode


def _find_or_die(root: Tree, value: int) -> TreeNode:
    def find(root: Tree, value: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.value == value:
            return root
        return find(root.left if root.value > value else root.right, value)

    node = find(root, value)
    assert node
    return node


class TestSuccessor(unittest.TestCase):

    def setUp(self) -> None:
        self.bst_10 = minimal_bst(range(10))

    def test_0(self) -> None:
        node = _find_or_die(self.bst_10, 0)
        res = successor(node)
        self.assertIsNotNone(res)
        # https://github.com/python/mypy/issues/4063
        self.assertEqual(1, res.value)  # type: ignore[union-attr]

    def test_1(self) -> None:
        node = _find_or_die(self.bst_10, 1)
        res = successor(node)
        self.assertIsNotNone(res)
        # https://github.com/python/mypy/issues/4063
        self.assertEqual(2, res.value)  # type: ignore[union-attr]

    def test_2(self) -> None:
        node = _find_or_die(self.bst_10, 2)
        res = successor(node)
        self.assertIsNotNone(res)
        # https://github.com/python/mypy/issues/4063
        self.assertEqual(3, res.value)  # type: ignore[union-attr]

    def test_3(self) -> None:
        node = _find_or_die(self.bst_10, 3)
        res = successor(node)
        self.assertIsNotNone(res)
        # https://github.com/python/mypy/issues/4063
        self.assertEqual(4, res.value)  # type: ignore[union-attr]

    def test_4(self) -> None:
        node = _find_or_die(self.bst_10, 4)
        res = successor(node)
        self.assertIsNotNone(res)
        # https://github.com/python/mypy/issues/4063
        self.assertEqual(5, res.value)  # type: ignore[union-attr]

    def test_5(self) -> None:
        node = _find_or_die(self.bst_10, 5)
        res = successor(node)
        self.assertIsNotNone(res)
        # https://github.com/python/mypy/issues/4063
        self.assertEqual(6, res.value)  # type: ignore[union-attr]

    def test_6(self) -> None:
        node = _find_or_die(self.bst_10, 6)
        res = successor(node)
        self.assertIsNotNone(res)
        # https://github.com/python/mypy/issues/4063
        self.assertEqual(7, res.value)  # type: ignore[union-attr]

    def test_7(self) -> None:
        node = _find_or_die(self.bst_10, 7)
        res = successor(node)
        self.assertIsNotNone(res)
        # https://github.com/python/mypy/issues/4063
        self.assertEqual(8, res.value)  # type: ignore[union-attr]

    def test_8(self) -> None:
        node = _find_or_die(self.bst_10, 8)
        res = successor(node)
        self.assertIsNotNone(res)
        # https://github.com/python/mypy/issues/4063
        self.assertEqual(9, res.value)  # type: ignore[union-attr]

    def test_9(self) -> None:
        node = _find_or_die(self.bst_10, 9)
        res = successor(node)
        self.assertIsNone(res)


if __name__ == '__main__':
    unittest.main()
