"""Tests for chapter05.next_number."""

import unittest

from chapter05 import next_number


class TestSmaller(unittest.TestCase):

    def test_0b10110(self) -> None:
        self.assertEqual(0b10101, next_number.smaller(0b10110))


class TestLarger(unittest.TestCase):

    def test_0b10110(self) -> None:
        self.assertEqual(0b11001, next_number.larger(0b10110))


if __name__ == "__main__":
    unittest.main()
