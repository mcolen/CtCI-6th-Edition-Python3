"""Tests for chapter1.is_unique."""

import unittest

from chapter1.is_unique import is_unique1, is_unique2


def make_test_case(impl):
    """Returns a test case for provided impl to be tested."""
    class TestIsUnique(unittest.TestCase):
        """Simple tests of uniqueness."""

        def test_abcde_is_unique(self):
            self.assertTrue(impl('abcde'))

        def test_hello_is_not_unique(self):
            self.assertFalse(impl('hello'))

        def test_apple_is_not_unique(self):
            self.assertFalse(impl('apple'))

        def test_kite_is_unique(self):
            self.assertTrue(impl('kite'))

        def test_padle_is_unique(self):
            self.assertTrue(impl('padle'))

    return TestIsUnique


class TestIsUnique1(make_test_case(is_unique1)):
    """Simple tests of uniqueness for is_unique1 implementation."""


class TestIsUnique2(make_test_case(is_unique2)):
    """Simple tests of uniqueness for is_unique2 implementation."""


if __name__ == '__main__':
    unittest.main()
