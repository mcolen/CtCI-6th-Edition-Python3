"""Tests for chapter16.word_frequencies."""

import unittest

from chapter16 import word_frequencies


class TestCount(unittest.TestCase):

    def test_count_lara_in_the_lara_and_outcropping_career_it(self) -> None:
        self.assertEqual(1, word_frequencies.count(
            book='the Lara and outcropping career it', word='Lara'))


class TestBookIndexer(unittest.TestCase):

    def test_count_lara_in_the_lara_and_outcropping_career_it(self) -> None:
        book_indexer = word_frequencies.BookIndexer()
        book_indexer.index_book('the Lara and outcropping career it')
        self.assertEqual(1, book_indexer.count(word='Lara'))


if __name__ == '__main__':
    unittest.main()
