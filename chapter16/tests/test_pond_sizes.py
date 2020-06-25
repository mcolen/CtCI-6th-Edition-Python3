"""Tests for chapter16.pond_sizes."""

import unittest

from chapter16 import pond_sizes


class TestPondSizes(unittest.TestCase):

    def test_three_ponds(self) -> None:
        self.assertCountEqual([2, 4, 1], pond_sizes.pond_sizes([
            [0, 2, 1, 0],
            [0, 1, 0, 1],
            [1, 1, 0, 1],
            [0, 1, 0, 1],
        ]))


if __name__ == '__main__':
    unittest.main()
