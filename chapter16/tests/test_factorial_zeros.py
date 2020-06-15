"""Tests for chapter16.factorial_zeros."""

import math
import unittest

from chapter16 import factorial_zeros


class TestZeros(unittest.TestCase):

    def test_11(self) -> None:
        assert math.factorial(11) == 39916800
        self.assertEqual(2, factorial_zeros.zeros(11))

    def test_26(self) -> None:
        assert math.factorial(26) == 403291461126605635584000000
        self.assertEqual(6, factorial_zeros.zeros(26))


if __name__ == '__main__':
    unittest.main()
