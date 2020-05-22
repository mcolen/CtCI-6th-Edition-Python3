"""Tests for chapter4.bst_sequences."""

import unittest

from chapter4.bst_sequences import bst_sequences
from chapter4.tree import TreeNode


class TestBSTSequences(unittest.TestCase):

    def test_2_1_3(self) -> None:
        tree = TreeNode(
            value=2,
            left=TreeNode(1),
            right=TreeNode(3)
        )
        sequences = bst_sequences(tree)
        self.assertEqual({(2, 1, 3), (2, 3, 1)}, set(map(tuple, sequences)))


if __name__ == '__main__':
    unittest.main()
