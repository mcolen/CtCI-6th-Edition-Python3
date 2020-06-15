"""Tests for chapter10.group_anagrams."""

import unittest

from chapter10 import group_anagrams


class TestSort(unittest.TestCase):

    def test_apple_ele_papel_eel_lee_elppa(self) -> None:
        strings = ['apple', 'ele', 'papel', 'eel', 'lee', 'elppa']
        group_anagrams.sort(strings)
        self.assertEqual(6, len(strings))
        self.assertCountEqual(
            [{'apple', 'papel', 'elppa'}, {'ele', 'eel', 'lee'}],
            [set(strings[:3]), set(strings[3:])])


if __name__ == '__main__':
    unittest.main()
