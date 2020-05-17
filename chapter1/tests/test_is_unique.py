"""Tests for chapter1.is_unique."""

import unittest

from chapter1.is_unique import is_unique1, is_unique2


class TestIsUnique1(unittest.TestCase):
    def test_abcde(self) -> None:
        self.assertTrue(is_unique1('abcde'))

    def test_hello(self) -> None:
        self.assertFalse(is_unique1('hello'))

    def test_apple(self) -> None:
        self.assertFalse(is_unique1('apple'))

    def test_kite(self) -> None:
        self.assertTrue(is_unique1('kite'))

    def test_padle(self) -> None:
        self.assertTrue(is_unique1('padle'))


class TestIsUnique2(unittest.TestCase):
    def test_abcde(self) -> None:
        self.assertTrue(is_unique2('abcde'))

    def test_hello(self) -> None:
        self.assertFalse(is_unique2('hello'))

    def test_apple(self) -> None:
        self.assertFalse(is_unique2('apple'))

    def test_kite(self) -> None:
        self.assertTrue(is_unique2('kite'))

    def test_padle(self) -> None:
        self.assertTrue(is_unique2('padle'))


if __name__ == '__main__':
    unittest.main()
