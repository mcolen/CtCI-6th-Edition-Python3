"""Tests for chapter4.bst_sequences."""

import unittest

from chapter4 import bst_sequences, tree


class TestBSTSequences(unittest.TestCase):

    def test_2_1_3(self) -> None:
        root = tree.Node(value=2, left=tree.Node(1), right=tree.Node(3))
        sequences = bst_sequences.bst_sequences(root)
        self.assertEqual({(2, 1, 3), (2, 3, 1)}, set(map(tuple, sequences)))


if __name__ == '__main__':
    unittest.main()
