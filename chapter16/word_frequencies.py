"""Solution to 16.2 Word Frequencies.

Design a method to find the frequency of occurences of any given word in
a book. What if we were running this algorithm multiple times?
"""

import collections
from typing import Counter


def count(book: str, word: str) -> int:
    """Finds the frequency of occurences of any given word in a book.

    Parses book into words by splitting on whitespace.

    Args:
        book: The book in which to find frequency of occurences.
        word: The word for which to find frequency of occurences.

    Returns:
        The number of times argument word appears in argument book.
    """
    return book.split().count(word)


class BookIndexer:
    """Indexes a book for fast computations of word frequencies."""

    def __init__(self) -> None:
        self.word_counts: Counter[str] = collections.Counter()

    def index_book(self, book: str) -> None:
        """Indexes book for future computed word frequencies."""
        self.word_counts += collections.Counter(book.split())

    def count(self, word: str) -> int:
        """Returns the number of times word apperas in indexed books."""
        return self.word_counts.get(word, 0)
