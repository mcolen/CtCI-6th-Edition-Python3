"""Tests for chapter1.string_compression."""

import unittest

from chapter1.string_compression import compressed


class TestStringCompression(unittest.TestCase):
    """Simple tests of string compression."""

    def test_aaaaabbbbaaaabbddc(self):
        self.assertEqual('a5b4a4b2d2c1', compressed('aaaaabbbbaaaabbddc'))


if __name__ == '__main__':
    unittest.main()
