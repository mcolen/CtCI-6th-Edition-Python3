"""Tests for chapter 01.string_rotation."""

import unittest

from chapter01 import string_rotation


class TestStringRotation(unittest.TestCase):

    def test_pleap_apple(self) -> None:
        self.assertTrue(string_rotation.is_rotation('pleap', 'apple'))

    def test_erbottlewat_waterbottle(self) -> None:
        self.assertTrue(
            string_rotation.is_rotation('erbottlewat', 'waterbottle'))

    def test_macera_camera(self) -> None:
        self.assertFalse(string_rotation.is_rotation('macera', 'camera'))


if __name__ == '__main__':
    unittest.main()
