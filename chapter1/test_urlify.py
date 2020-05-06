"""Tests for solution to 1.3 URLify."""

import unittest

from urlify import urlify


class TestURLify(unittest.TestCase):
    """Simple tests of URLify."""
    def test_mr_john_smith(self):
        s = list('mr john smith    ')
        urlify(s, len(''.join(s).strip()))
        self.assertEqual(list('mr%20john%20smith'), s)


if __name__ == '__main__':
    unittest.main()
