"""Tests for chapter1.string_rotation."""

import unittest

from chapter1.string_rotation import is_rotation


class TestStringRotation(unittest.TestCase):

    def test_apple_is_rotation_of_pleap(self):
        self.assertTrue(is_rotation('pleap', 'apple'))

    def test_waterbottle_is_rotation_of_erbottlewat(self):
        self.assertTrue(is_rotation('erbottlewat', 'waterbottle'))

    def test_camera_is_not_rotation_of_macera(self):
        self.assertFalse(is_rotation('macera', 'camera'))


if __name__ == '__main__':
    unittest.main()
