"""Tests for chapter 01.string_compression."""

import unittest

from chapter01 import string_compression


class TestStringCompression(unittest.TestCase):

    def test_aaaaabbbbaaaabbddc(self) -> None:
        self.assertEqual('a5b4a4b2d2c1',
                         string_compression.compressed('aaaaabbbbaaaabbddc'))


if __name__ == '__main__':
    unittest.main()
