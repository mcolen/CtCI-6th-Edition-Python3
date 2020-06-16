"""Tests for chapter05.binary_to_string."""

import unittest

from chapter05 import binary_to_string


class TestPrintFractionInBinary(unittest.TestCase):

    def test_0_125(self) -> None:
        self.assertEqual(
            '.001', binary_to_string.fraction_to_binary_string(0.125))


if __name__ == "__main__":
    unittest.main()
