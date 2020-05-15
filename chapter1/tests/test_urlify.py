"""Tests for chapter1.urlify."""

import unittest

from chapter1.urlify import urlify


class TestURLify(unittest.TestCase):

    def test_mr_john_smith(self):
        s = list('mr john smith    ')
        urlify(s, length=13)
        self.assertEqual('mr%20john%20smith', ''.join(s))


if __name__ == '__main__':
    unittest.main()
