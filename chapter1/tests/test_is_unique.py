"""Tests for chapter1.is_unique."""

import unittest

from chapter1.is_unique import is_unique1, is_unique2


def make_test_case(impl):
    """Returns a test case for provided impl to be tested."""
    class TestIsUnique(unittest.TestCase):

        def test_abcde(self):
            self.assertTrue(impl('abcde'))

        def test_hello(self):
            self.assertFalse(impl('hello'))

        def test_apple(self):
            self.assertFalse(impl('apple'))

        def test_kite(self):
            self.assertTrue(impl('kite'))

        def test_padle(self):
            self.assertTrue(impl('padle'))

    return TestIsUnique


class TestIsUnique1(make_test_case(is_unique1)):
    pass


class TestIsUnique2(make_test_case(is_unique2)):
    pass


if __name__ == '__main__':
    unittest.main()
