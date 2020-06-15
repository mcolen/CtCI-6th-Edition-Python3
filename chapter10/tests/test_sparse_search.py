"""Tests for chapter10.sparse_search."""

import unittest

from chapter10 import sparse_search


class TestIndex(unittest.TestCase):

    def test_find_apple_in_apple_banana_carrot_duck_eel_flower(self) -> None:
        self.assertEqual(0,
                         sparse_search.index(
                             ['apple', '', '', 'banana', '', '', '', 'carrot',
                              'duck', '', '', 'eel', '', 'flower'],
                             target='apple'))

    def test_find_banana_in_apple_banana_carrot_duck_eel_flower(self) -> None:
        self.assertEqual(3,
                         sparse_search.index(
                             ['apple', '', '', 'banana', '', '', '', 'carrot',
                              'duck', '', '', 'eel', '', 'flower'],
                             target='banana'))

    def test_find_carrot_in_apple_banana_carrot_duck_eel_flower(self) -> None:
        self.assertEqual(7,
                         sparse_search.index(
                             ['apple', '', '', 'banana', '', '', '', 'carrot',
                              'duck', '', '', 'eel', '', 'flower'],
                             target='carrot'))

    def test_find_duck_in_apple_banana_carrot_duck_eel_flower(self) -> None:
        self.assertEqual(8,
                         sparse_search.index(
                             ['apple', '', '', 'banana', '', '', '', 'carrot',
                              'duck', '', '', 'eel', '', 'flower'],
                             target='duck'))

    def test_find_eel_in_apple_banana_carrot_duck_eel_flower(self) -> None:
        self.assertEqual(11,
                         sparse_search.index(
                             ['apple', '', '', 'banana', '', '', '', 'carrot',
                              'duck', '', '', 'eel', '', 'flower'],
                             target='eel'))

    def test_find_flower_in_apple_banana_carrot_duck_eel_flower(self) -> None:
        self.assertEqual(13,
                         sparse_search.index(
                             ['apple', '', '', 'banana', '', '', '', 'carrot',
                              'duck', '', '', 'eel', '', 'flower'],
                             target='flower'))

    def test_find_ac_in_apple_banana_carrot_duck_eel_flower(self) -> None:
        self.assertIsNone(
            sparse_search.index(
                ['apple', '', '', 'banana', '', '', '', 'carrot',
                 'duck', '', '', 'eel', '', 'flower'],
                target='ac'))


if __name__ == '__main__':
    unittest.main()
