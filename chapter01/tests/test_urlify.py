"""Tests for chapter01.urlify."""

import unittest

from chapter01 import urlify


class TestURLify(unittest.TestCase):

    def test_mr_john_smith(self) -> None:
        s = list('mr john smith    ')
        urlify.urlify(s, length=13)
        self.assertEqual(list('mr%20john%20smith'), s)


if __name__ == '__main__':
    unittest.main()
