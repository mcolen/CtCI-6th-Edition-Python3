"""Tests for chapter8.recursive_multiply."""

import unittest

from chapter8 import recursive_multiply


class TestRecursiveMultiply(unittest.TestCase):

    def test_37_101(self) -> None:
        self.assertEqual(3737, recursive_multiply.recursive_multiply(37, 101))


if __name__ == '__main__':
    unittest.main()
