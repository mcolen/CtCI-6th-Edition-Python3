"""Tests for chapter08.magic_index."""

import unittest

from chapter08 import magic_index


class TestMagicIndexDistinct(unittest.TestCase):

    def test_one_magic_index(self) -> None:
        self.assertEqual(5, magic_index.magic_index_distinct(
            [-14, -12, 0, 1, 2, 5, 9, 10, 23, 25]))


class TestMagicIndex(unittest.TestCase):

    def test_one_magic_index(self) -> None:
        self.assertEqual(5, magic_index.magic_index(
            [-14, -12, 0, 5, 5, 5, 5, 5, 23, 25]))


if __name__ == '__main__':
    unittest.main()
