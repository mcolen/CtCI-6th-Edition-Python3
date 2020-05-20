"""Tests for chapter4.bst_sequences."""

import unittest

from chapter4.bst_sequences import bst_sequences
from chapter4.minimal_tree import minimal_bst


class TestBSTSequences(unittest.TestCase):

    def test_three_nodes_balanced(self) -> None:
        sequences = bst_sequences(minimal_bst(range(3)))
        self.assertEqual({(1, 0, 2), (1, 2, 0)}, set(map(tuple, sequences)))


if __name__ == '__main__':
    unittest.main()
