"""Tests for chapter16.operations."""

import unittest

from chapter16 import operations


class TestMultiply(unittest.TestCase):

    def test_3_times_11(self) -> None:
        self.assertEqual(33, operations.multiply(3, 11))


class TestSubtract(unittest.TestCase):

    def test_2_minus_4(self) -> None:
        self.assertEqual(-2, operations.subtract(2, 4))


class TestDivide(unittest.TestCase):

    def test_20_divided_by_negative_5(self) -> None:
        self.assertEqual(-4, operations.divide(20, -5))


if __name__ == '__main__':
    unittest.main()
